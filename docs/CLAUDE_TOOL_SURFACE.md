# LUCH Full for Claude — tool surface, permissions and review

**Full product, not a 12-tool GitHub-only edition.** The root .mcp.json still targets https://luch.lenarsalimov.ru/luch/core/mcp. There are 12 skill folders, which are guidance, not the number of tools.

## Live evidence vs snapshot

`tools/luch_connected_snapshot.json` records 166 tool *names* exposed by the linked ChatGPT LUCH connector on 2026-11-28. This is not a Claude OAuth tools/list receipt; exact Claude coverage, argument schemas and available paired devices must be independently tested.

| Family | Names observed | Typical operations |
| --- | ---: | --- |
| Paired local browser | 41 | Browse, click, type, screenshot, tabs and windows |
| Isolated server browser | 20 | Acquire a disposable context, navigate, click, type, release |
| GitHub | 23 | Search, compare, branch, issue, PR, write and inspect |
| Other server operations | 10 | Status, diagnostics and bounded command execution |
| Files, desktop, messaging, services and other | 72 | Files, native computer actions, services, pairing, etc. |

## Human autonomy model

Authorizing a task and account/device scope covers the ordinary steps to complete that *same* task. LUCH skills must not add another prompt at every click, Save or Submit button. Execute, read back and report actual results.

Auth, host permission gates, operating-system consent, external service protections, per-user tenant isolation, revocation and high-impact-use requirements remain enforceable. Never misrepresent a write as read-only, suppress an actual Claude approval, forge a grant or handle an unrelated target as part of the task.

## Correct MCP presentation

1. Define a narrow natural-language action for each tool with purpose, preconditions, arguments, side effects, errors and readback. Avoid `universal unrestricted agent` marketing claims that don't explain safeguards.
2. Apply truthful MCP `annotations.title`, `readOnlyHint`, `destructiveHint` and where supported `idempotentHint` and `openWorldHint` to *actual server tool definitions*. These are classification hints, not permission bypasses.
3. Keep distinct, well-described browser read, browser click, browser type, terminal and file-edit tools; avoid hiding all power behind a generic free-text `run_task` bypass.
4. Route local signed-in tabs only through real user-granted paired browser permissions; isolated web browsing remains separate. Never access a user's cookies or ungranted sessions.
5. Report only tools verified in the particular Claude host; fail closed for absent tools and scopes. Optimize tool discovery and search without inflating the public tool count.
6. The current Anthropic checker explicitly refuses arbitrary signed-in third-party browsing and open-ended desktop/phone automation **for Directory publication**. Merely renaming or rewriting descriptions does not eliminate those actual capabilities. Seek manual determination or distribute full LUCH as a custom connector.

## QA / publishing gates

- Run `python3 -m unittest -v tests/test_claude_autonomy.py` on exact HEAD.
- Obtain an authenticated Claude tools/list fixture with exact live tool annotations, verify no tool exceeds 64 characters and writes do not claim readOnlyHint=true.
- Conduct task-level E2E: allowed browser click, form submit, reversible file edit, and readback without an extra LUCH-made prompt. Honor real Claude/OS/provider permission gates.
- Audit browser companion and backend for additional interactive confirmation logic; the GitHub skill changes do not modify their runtime handlers.
- Obtain source-bound independent QA and actual publisher response before claiming approval.

Policy: https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy
MCP annotations: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
Submission: https://claude.ai/directory/manage
