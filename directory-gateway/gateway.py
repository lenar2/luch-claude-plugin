#!/usr/bin/env python3
"""LUCH Claude Directory: fail-closed, GitHub-specific MCP transport gateway.

This is a candidate for an isolated deployment, NOT the unrestricted LUCH core.
It does not grant authorization. It forwards each caller's bearer credential to
the core and checks every requested tool at the gateway boundary.
"""
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

PUBLIC_RESOURCE = os.getenv(
    "LUCH_DIRECTORY_RESOURCE",
    "https://luch.lenarsalimov.ru/luch/directory/mcp",
)
UPSTREAM = os.getenv(
    "LUCH_CORE_MCP_URL",
    "https://luch.lenarsalimov.ru/luch/core/mcp",
)
ISSUER = os.getenv(
    "LUCH_DIRECTORY_OAUTH_ISSUER",
    "https://axeudbiyabdqtdvjjhns.supabase.co/auth/v1",
)
MAX_BODY = 4 * 1024 * 1024
ALLOWED_TOOLS = frozenset({
    "github_repo_info", "github_repo_head", "github_branch_list",
    "github_tree", "github_file_get", "github_commit_log",
    "github_commit_get", "github_search_code", "github_compare",
    "github_issue", "github_pr", "github_apply_changes",
})
PASSTHROUGH_METHODS = frozenset({
    "initialize", "notifications/initialized", "ping",
    "tools/list", "tools/call",
})

def metadata_url():
    u = urlsplit(PUBLIC_RESOURCE)
    return u.scheme + "://" + u.netloc + "/.well-known/oauth-protected-resource" + u.path

def limit_tool_list(doc):
    if not isinstance(doc, dict):
        raise ValueError("Invalid MCP response")
    if "result" in doc and isinstance(doc["result"], dict):
        result = doc["result"]
        if not isinstance(result.get("tools"), list):
            raise ValueError("Unexpected MCP tool list")
        doc = dict(doc)
        result = dict(result)
        result["tools"] = [
            t for t in result["tools"]
            if isinstance(t, dict) and t.get("name") in ALLOWED_TOOLS
        ]
        doc["result"] = result
        return doc
    if "error" in doc:
        return doc
    raise ValueError("MCP tool list missing")

def filter_body(content_type, body):
    """Filter tool discovery in both JSON and SSE; malformed data fails closed."""
    if len(body) > MAX_BODY:
        raise ValueError("Oversized response")
    if "text/event-stream" in content_type:
        text = body.decode("utf-8")
        chunks = []
        matched = False
        for line in text.splitlines(keepends=True):
            if line.startswith("data:"):
                value = line[5:].strip()
                doc = json.loads(value)
                if "result" in doc or "error" in doc:
                    doc = limit_tool_list(doc)
                    matched = True
                line = "data: " + json.dumps(doc, separators=(",", ":")) + "\n"
            chunks.append(line)
        if not matched:
            raise ValueError("No tool-list result in SSE response")
        return "".join(chunks).encode("utf-8")
    doc = json.loads(body)
    return json.dumps(limit_tool_list(doc), separators=(",", ":")).encode("utf-8")

class Handler(BaseHTTPRequestHandler):
    server_version = "LUCHDirectoryGateway/0.1"
    def log_message(self, fmt, *args):
        # Never log Authorization headers, payloads or user source content.
        pass

    def send(self, code, body=b"", content_type="application/json", headers=None):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if body:
            self.wfile.write(body)

    def json_reply(self, code, doc, headers=None):
        self.send(code, json.dumps(doc, separators=(",", ":")).encode(), headers=headers)

    def do_GET(self):
        if self.path == urlsplit(metadata_url()).path:
            self.json_reply(200, {
                "resource": PUBLIC_RESOURCE,
                "authorization_servers": [ISSUER],
                "scopes_supported": ["openid", "email", "profile"],
                "bearer_methods_supported": ["header"],
            })
            return
        if self.path == urlsplit(PUBLIC_RESOURCE).path:
            self.send(405, b"", headers={"Allow": "POST"})
            return
        self.json_reply(404, {"error": "Not found"})

    def do_POST(self):
        if self.path != urlsplit(PUBLIC_RESOURCE).path:
            self.json_reply(404, {"error": "Not found"})
            return
        auth = self.headers.get("Authorization", "")
        if not auth.startswith("Bearer ") or not auth[7:].strip():
            self.json_reply(401, {"error": "OAuth bearer required"}, headers={
                "WWW-Authenticate": 'Bearer resource_metadata="' + metadata_url() + '"'
            })
            return
        try:
            n = int(self.headers.get("Content-Length", "0"))
            if n < 1 or n > MAX_BODY:
                raise ValueError("Request body size invalid")
            if "application/json" not in self.headers.get("Content-Type", ""):
                raise ValueError("JSON request required")
            incoming = json.loads(self.rfile.read(n))
            if not isinstance(incoming, dict):
                raise ValueError("Batched MCP requests are not supported")
            method = incoming.get("method")
            if method not in PASSTHROUGH_METHODS:
                self.json_reply(403, {"error": "MCP method not in directory scope"})
                return
            if method == "tools/call":
                params = incoming.get("params")
                if not isinstance(params, dict) or params.get("name") not in ALLOWED_TOOLS:
                    self.json_reply(403, {"error": "Tool not in directory scope"})
                    return
            if method == "tools/list" and not isinstance(incoming.get("params", {}), dict):
                raise ValueError("Invalid tools/list parameters")
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            self.json_reply(400, {"error": "Malformed MCP request"})
            return

        forwarded = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": auth,
        }
        for key in ("Mcp-Protocol-Version", "Mcp-Session-Id", "Last-Event-Id"):
            if self.headers.get(key):
                forwarded[key] = self.headers[key]
        request = Request(
            UPSTREAM,
            data=json.dumps(incoming, separators=(",", ":")).encode("utf-8"),
            headers=forwarded,
            method="POST",
        )
        try:
            try:
                response = urlopen(request, timeout=18)
            except HTTPError as exc:
                response = exc
            with response:
                status = response.status
                data = response.read(MAX_BODY + 1)
                content_type = response.headers.get("Content-Type", "application/json")
                safe_headers = {}
                for key in ("Mcp-Session-Id", "Mcp-Protocol-Version"):
                    if response.headers.get(key):
                        safe_headers[key] = response.headers[key]
                if status == 401:
                    safe_headers["WWW-Authenticate"] = (
                        'Bearer resource_metadata="' + metadata_url() + '"'
                    )
                if len(data) > MAX_BODY:
                    raise ValueError("Upstream MCP response too large")
                if status == 200 and method == "tools/list":
                    data = filter_body(content_type, data)
                self.send(status, data, content_type, safe_headers)
        except (URLError, TimeoutError, ValueError, UnicodeError, json.JSONDecodeError):
            self.json_reply(502, {"error": "Directory MCP upstream unavailable or malformed"})

def main():
    if not PUBLIC_RESOURCE.startswith("https://"):
        raise ValueError("Public resource must use HTTPS")
    if not UPSTREAM.startswith("https://") and os.getenv("LUCH_TEST_ALLOW_HTTP") != "1":
        raise ValueError("Upstream must use HTTPS")
    port = int(os.getenv("LUCH_DIRECTORY_PORT", "8739"))
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()

if __name__ == "__main__":
    main()
