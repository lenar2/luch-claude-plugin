# LUCH for Cursor — release candidate (0.1.6)

This repository contains a **Cursor Plugin** manifest under `.cursor-plugin/plugin.json`, 12 portable skills under `skills/`, and an OAuth-protected remote MCP entry in `mcp.json`. The original Claude package remains available and unchanged in `.claude-plugin/` and `.mcp.json`.

## What works, what does not

The client only describes and connects to a separately hosted LUCH service. LUCH currently limits access to approved test accounts, and installation does **not** create an account or pair a device automatically. The package provides **no** privileged access to the publisher's devices. Public self-service onboarding and independent Cursor-host OAuth and tools end-to-end testing are **not yet verified**.

## How to test locally (authorized reviewer only)

1. Clone this repository at a pinned commit. Copy it to `~/.cursor/plugins/local/luch` with the `.cursor-plugin/plugin.json`, `skills/` and `mcp.json` files intact.
2. Restart Cursor or run **Developer: Reload Window**. In **Customize**, check that the plugin shows 12 skills and one MCP server.
3. Connect the LUCH MCP server using the supported OAuth flow with an **authorized reviewer test account**. Confirm scoped `tools/list` only shows tools the reviewer is allowed to use. Never sign in with the publisher's owner account for testing.
4. Test only on an isolated synthetic reviewer fixture: discover paired demo device; read an explicitly authorized demo file; rename only the reviewer's demo device. Then verify that an unpaired owner's device and a forbidden file path are denied.
5. Record reproducible **Cursor-host**, not Inspector, evidence. Revoke reviewer access and verify the effect. Capture a private test log without access tokens or private data.

Do **not** submit to the Cursor marketplace or claim availability before successful validation, logged Cursor-host tests, an approved logo, and verified publisher terms.

## Security and publisher scope

- Public MCP: `https://api.lenarsalimov.ru/luch/core/mcp` (OAuth; permissions enforced server-side).
- Never connect public clients to the legacy private owner endpoint.
- No credentials, browser cookies, bearer tokens, reviewer passwords, or paired-device tokens are contained in this repository.
- Client files are Apache-2.0, but the hosted LUCH service is proprietary.
- Privacy: https://luch.lenarsalimov.ru/privacy/
- Terms: https://luch.lenarsalimov.ru/terms/
- Support: https://luch.lenarsalimov.ru/support/
