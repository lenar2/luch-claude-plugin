# LUCH for ChatGPT and Codex — submission candidate

**Name:** LUCH (not “LUCH Claude Plugin” or “LUCH MCP”).  
**Product:** a permission-scoped AI action layer for authorized browsers, files, computers and paired servers.  
**State:** public package **candidate**, **not** an approved or published OpenAI Directory listing.

## Existing private installation

There is already a personal **LUCH 0.3.51** plugin in the owner's ChatGPT account. Its canonical production MCP origin is **https://luch.lenarsalimov.ru/luch/mcp**. Do **not** modify or replace the active private plugin as a side effect of preparing this public candidate.

The GitHub public client adapter release is 0.1.6. Its version does not imply that backend 0.3.51 is being redeployed.

## Packaging

This folder contains the OpenAI portable `plugin.json` and `mcp.json`. To build the candidate ZIP, run from the repository root:

```bash
python3 integrations/chatgpt/build_package.py
```

This stages the two manifests at the **archive root**, adds the twelve public `skills/*/SKILL.md` files and the Apache-2.0 client license, and creates `dist/luch-chatgpt-0.1.6-preview.zip`.

`mcp.json` declares OAuth by discovery with no embedded client secret. The host must independently verify OAuth interoperability; a 401 response proves rejection of anonymous access, **not** successful sign-in.

## What to test before OpenAI Directory submission

1. Complete verified publisher identity and domain ownership for the production MCP origin.
2. Confirm registration/discovery works from a **fresh non-owner ChatGPT account**.
3. Run the real authenticated MCP tool discovery and inspect read/write risk annotations.
4. Obtain an independent reviewer fixture and test account, perform authorized read-only browser test, paired server health check, and denial on an unpaired device.
5. Check revocation, error states, device isolation and user approval.
6. Record genuine walkthrough footage from the supported client and verify documentation, privacy, terms and support.
7. Complete OpenAI's automated scan and submit in the official portal; publish only after review and explicit owner approval.

**No standalone binary, no private server source, no access tokens and no agent auto-execution hooks** are included.

Docs: https://developers.openai.com/plugins/build/plugins and https://developers.openai.com/plugins/deploy/submission

This is a *preview candidate*. OpenAI plugin review requires operational completeness; do not submit an incomplete demo as a finished public product.
