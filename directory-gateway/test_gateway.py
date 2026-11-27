"""Deterministic local tests. No network, tokens, production or paired Macs."""
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import gateway

class Upstream(BaseHTTPRequestHandler):
    calls = []
    mode = "json"
    def log_message(self, *_): pass
    def do_POST(self):
        n = int(self.headers["Content-Length"])
        doc = json.loads(self.rfile.read(n))
        Upstream.calls.append(doc)
        body = {
            "jsonrpc": "2.0", "id": doc.get("id"),
            "result": {"tools": [
                {"name": "github_issue"}, {"name": "github_apply_changes"},
                {"name": "browser_click"}, {"name": "computer_click"},
            ]} if doc.get("method") == "tools/list" else
            {"ok": True, "name": doc.get("params", {}).get("name")}
        }
        if Upstream.mode == "bad":
            data, kind = b"invalid json!", "application/json"
        elif Upstream.mode == "sse":
            data = ("event: message\ndata: " + json.dumps(body) + "\n\n").encode()
            kind = "text/event-stream"
        else:
            data, kind = json.dumps(body).encode(), "application/json"
        self.send_response(200)
        self.send_header("Content-Type", kind)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.upstream = ThreadingHTTPServer(("127.0.0.1", 0), Upstream)
        gateway.UPSTREAM = "http://127.0.0.1:" + str(cls.upstream.server_address[1])
        cls.gateway = ThreadingHTTPServer(("127.0.0.1", 0), gateway.Handler)
        cls.url = "http://127.0.0.1:" + str(cls.gateway.server_address[1])
        for app in (cls.upstream, cls.gateway):
            threading.Thread(target=app.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.gateway.shutdown()
        cls.upstream.shutdown()

    def setUp(self):
        Upstream.calls.clear()
        Upstream.mode = "json"

    def post(self, method, params=None, bearer=True):
        doc = {"jsonrpc": "2.0", "id": 7, "method": method}
        if params is not None:
            doc["params"] = params
        headers = {"Content-Type": "application/json"}
        if bearer:
            headers["Authorization"] = "Bearer synthetic-test-token"
        req = Request(
            self.url + "/luch/directory/mcp",
            json.dumps(doc).encode(), headers=headers, method="POST",
        )
        try:
            with urlopen(req, timeout=3) as resp:
                return resp.status, resp.read(), dict(resp.headers)
        except HTTPError as err:
            return err.code, err.read(), dict(err.headers)

    def test_metadata_uses_directory_resource(self):
        with urlopen(self.url + "/.well-known/oauth-protected-resource/luch/directory/mcp") as r:
            doc = json.load(r)
        self.assertEqual(doc["resource"], gateway.PUBLIC_RESOURCE)

    def test_missing_auth_does_not_reach_core(self):
        status, _, headers = self.post("tools/list", bearer=False)
        self.assertEqual(status, 401)
        self.assertIn("/luch/directory/mcp", headers["WWW-Authenticate"])
        self.assertEqual(Upstream.calls, [])

    def test_directory_filters_all_tools(self):
        status, body, _ = self.post("tools/list", {})
        self.assertEqual(status, 200)
        tools = json.loads(body)["result"]["tools"]
        self.assertEqual({t["name"] for t in tools}, {"github_issue", "github_apply_changes"})

    def test_sse_filters_all_tools(self):
        Upstream.mode = "sse"
        status, body, _ = self.post("tools/list", {})
        self.assertEqual(status, 200)
        self.assertIn(b"github_issue", body)
        self.assertNotIn(b"browser_click", body)
        self.assertNotIn(b"computer_click", body)

    def test_can_autonomously_commit_github_change(self):
        status, body, _ = self.post(
            "tools/call", {"name": "github_apply_changes", "arguments": {
                "repo": "synthetic/example", "changes": []
            }}
        )
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["result"]["name"], "github_apply_changes")
        self.assertEqual(len(Upstream.calls), 1)

    def test_rejects_browser_and_desktop_even_direct_call(self):
        for name in ("browser_click", "computer_click", "terminal_exec", "server_exec"):
            status, _, _ = self.post("tools/call", {"name": name, "arguments": {}})
            self.assertEqual(status, 403)
        self.assertEqual(Upstream.calls, [])

    def test_rejects_other_mcp_methods(self):
        status, _, _ = self.post("resources/list", {})
        self.assertEqual(status, 403)
        self.assertEqual(Upstream.calls, [])

    def test_rejects_malformed_list_before_core(self):
        status, _, _ = self.post("tools/list", ["bad"])
        self.assertEqual(status, 400)
        self.assertEqual(Upstream.calls, [])

    def test_fails_closed_if_core_returns_invalid_data(self):
        Upstream.mode = "bad"
        status, _, _ = self.post("tools/list", {})
        self.assertEqual(status, 502)

    def test_initialize_is_passed_through(self):
        status, _, _ = self.post("initialize", {"protocolVersion": "2025-03-26"})
        self.assertEqual(status, 200)
        self.assertEqual(Upstream.calls[0]["method"], "initialize")

if __name__ == "__main__":
    unittest.main()
