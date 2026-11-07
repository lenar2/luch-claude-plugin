#!/usr/bin/env python3
"""Build the public LUCH ChatGPT/Codex preview ZIP; no credentials or hooks."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[2]
src = root / "integrations" / "chatgpt"
out = root / "dist" / "luch-chatgpt-0.1.6-preview.zip"
plugin = json.loads((src / "plugin.json").read_text(encoding="utf-8"))
mcp = json.loads((src / "mcp.json").read_text(encoding="utf-8"))

assert plugin["name"] == "luch"
assert plugin["$schema"].startswith("https://agent-plugins.org/")
assert plugin["extensions"]["com.openai"]["interface"]["displayName"] == "LUCH"
assert mcp["mcpServers"]["luch"]["type"] == "streamable-http"
assert mcp["mcpServers"]["luch"]["url"] == "https://luch.lenarsalimov.ru/luch/mcp"
assert set(mcp["mcpServers"]["luch"].keys()) == {"type", "url"}  # strict Agent Plugins portability
skills = sorted((root / "skills").glob("*/SKILL.md"))
assert len(skills) == 12, f"expected 12 portable skills, found {len(skills)}"
for path in skills:
    assert path.read_text(encoding="utf-8").startswith("---\n"), path

entries = {
    "plugin.json": src / "plugin.json",
    "mcp.json": src / "mcp.json",
    "README.md": src / "README.md",
    "README.ru.md": src / "README.ru.md",
    "CHATGPT_WORKFLOW.md": src / "CHATGPT_WORKFLOW.md",
    "CHATGPT_WORKFLOW.ru.md": src / "CHATGPT_WORKFLOW.ru.md",
    "assets/chatgpt-workflow.svg": src / "assets" / "chatgpt-workflow.svg",
    "LICENSE": root / "LICENSE",
}
for item in skills:
    entries[item.relative_to(root).as_posix()] = item

out.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for name, path in sorted(entries.items()):
        z.write(path, arcname=name)
with zipfile.ZipFile(out) as z:
    assert sorted(z.namelist()) == sorted(entries)
    forbidden = ("ghp_", "sk-proj-", "-----BEGIN PRIVATE KEY-----")
    for name in z.namelist():
        if name.endswith((".md", ".json")):
            data = z.read(name).decode("utf-8")
            assert not any(secret in data for secret in forbidden), name

print(json.dumps({
    "status": "STATIC_PACKAGE_PASS",
    "path": str(out),
    "files": len(entries),
    "skills": len(skills),
    "size_bytes": out.stat().st_size,
    "sha256": hashlib.sha256(out.read_bytes()).hexdigest()
}, indent=2))
print("Note: static validation does not prove OAuth, runtime tools or public review.")
