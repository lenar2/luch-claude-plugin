# LUCH v0.1.6 — public source preview

**Status:** Public preview / early access. **Not** an independently verified self-service release.

## Public code available today

- [Claude client v0.1.6 source](https://github.com/lenar2/luch-claude-plugin)
- [Cursor client v0.1.6 source](https://github.com/lenar2/luch-cursor)
- [Gemini CLI v0.1.6 source](https://github.com/lenar2/luch-gemini)
- [Kimi adaptation branch](https://github.com/lenar2/luch-claude-plugin/tree/kimi-v0.1.6-candidate) — preliminary and not approved.

All publicly downloadable client sources include skill instructions and/or the host-specific MCP manifest. The standalone hosted LUCH service is not included. Do not embed credentials or server-side source in a client ZIP.

## Changes in this public preview

- Unified public starting page with host-specific installation pointers.
- Clear separation of client source availability from platform-directory approvals.
- [Illustrative end-user workflow demonstration](DEMO.md).
- [Independent release qualification gates](PUBLIC_RELEASE_GATES.md), including user signup, OAuth, device pairing, tenant isolation and permission revocation.

## Read-only infrastructure observations — 2026-11-05

- `GET https://luch.lenarsalimov.ru/` returned **200**.
- `GET https://luch.lenarsalimov.ru/docs/get-started/` returned **200**.
- Unauthenticated `GET https://api.lenarsalimov.ru/luch/core/mcp` returned **401** with a `WWW-Authenticate` resource metadata challenge.
- These results **do not** prove that a fresh third-party user can connect, sign in or complete a safe authorized action.

## What this is *not*

- Not a downloadable native Mac/iPhone app.
- Not an indication of official Claude/Cursor/Gemini/Kimi marketplace approval.
- Not a production-ready public self-service subscription.
- Not a proof of independent multi-tenant security.

**GitHub Release:** Not yet published. Source ZIP is available from the main branch. A GitHub Release should be cut only after package validation and installation gates; a branded video demo needs authentic recorded evidence, not fabricated screenshots.

See [PUBLIC_RELEASE_GATES.md](PUBLIC_RELEASE_GATES.md) for promotion prerequisites.
