# LUCH for Kimi — submission candidate

This branch contains the **Kimi-native** adapter for LUCH v0.1.6 (12 public Skills + the OAuth-protected LUCH MCP endpoint). It is **not** an approved or published Kimi listing.

## Package and security
- Native manifest: `kimi.plugin.json`
- Skills: `skills/`
- Remote OAuth MCP: `https://api.lenarsalimov.ru/luch/core/mcp`
- Project site: https://luch.lenarsalimov.ru/
- License: Apache-2.0.
- No API keys, bearer tokens, or user credentials are shipped with this plugin.

Access to real devices and external systems requires explicit user authorization and supported hosts. Tools and scopes depend on the account and host. Do not infer grant of write/destructive permissions from installation.

## Validate
Kimi Code CLI can install the branch from its GitHub URL and report plugin diagnostics. If the remote MCP requires OAuth, use Kimi Code's documented `/mcp-config login luch` flow. Ensure authenticated runtime E2E before requesting a Kimi marketplace listing.

Kimi's official personal-plugin publication flow uses Kimi Work's Plugin Builder, then the plugin detail envelope → "Apply for official marketplace publication", with an email for reviewer contact. Kimi Work is supported on Apple silicon Macs and Windows; its Work mode is not supported on Intel Macs.

Docs:
- https://www.kimi.ai/help/plugins-and-skills/publish
- https://www.kimi.com/en/help/plugins-and-skills/create
- https://www.kimi.com/code/docs/en/kimi-code-cli/customization/plugins

## Status
- Native manifest and source paths: static candidate; not independently run on Kimi.
- Kimi authenticated OAuth, runtime integration tests, plugin Builder import, and official listing submission: **UNKNOWN / NOT YET VERIFIED**.
- Existing Claude `main` and separate Cursor release sources remain unchanged.
