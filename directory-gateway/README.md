# LUCH Claude Directory MCP gateway — isolated candidate

This service is a **separate product boundary**, not a cosmetic tool filter or a new name for unrestricted LUCH Core.

The directory variant serves GitHub project operations only. The gateway filters tools/list and blocks disallowed tools/call and MCP methods before the request reaches Core. Ordinary GitHub writes can be executed by the assistant end-to-end, subject to the user's authorized GitHub scopes and any host-enforced controls. It does not expose a generic browser, user sessions, computer/phone automation, shell, or financial transactions.

## Run tests

From directory-gateway: python3 -m unittest -v test_gateway.py

## Deploy conditions (NOT SATISFIED)

1. Deploy on a separate route with valid HTTPS and an isolated process; never replace the production /luch/core/mcp endpoint.
2. Prove OAuth resource indicator/audience, issuer discovery, user separation and revocation for the new route. Do not rely solely on UI filtering or a full-Core OAuth token.
3. Independently validate the exact exposed upstream tool schemas, especially github_issue, github_pr and github_apply_changes, against fixed GitHub-only provider operations.
4. Test tools/list in JSON and SSE with a real permitted account; perform a synthetic GitHub issue + file change and verify receipt.
5. Check prompt injection, oversized responses, pagination, missing scopes, error handling and directory policy; collect test-user onboarding evidence.
6. Only then change the directory package's MCP URL to the independently verified deployed route and submit its scoped folder.

The gateway is a tested staging prototype. The URL shown in directory/.mcp.json is reserved but **not an assertion that the endpoint has been deployed**. This branch is not publishable until the conditions above pass.
