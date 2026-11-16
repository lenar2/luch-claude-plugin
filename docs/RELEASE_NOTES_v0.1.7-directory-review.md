# LUCH for Claude v0.1.7 — directory review candidate

Status: review candidate, not yet approved or published by Anthropic.

Preserves the 12 original `skills/*/SKILL.md` workflows and protected MCP endpoint `https://api.lenarsalimov.ru/luch/core/mcp`, without production or OAuth permission changes.

## Changes after Anthropic's 8 Nov 2026 Needs changes
- Uses the exact founder-selected provisional R22.11.4 plugin icon B PNG from `lenar2/luch`, [draft PR #11](https://github.com/lenar2/luch/pull/11) at `3d74789168299daa7ce3cef91a68e949e319eeae`.
- Removes SVG assets and executable scripts disallowed by the current non-verified directory policy. The existing Claude workflow artwork is linked via a pinned read-only GitHub URL, not bundled as SVG.
- Removes unrelated ChatGPT plugin/build package files from the Claude submission repository root to avoid mixed-plugin review. Full prior source preserved on `archive/claude-before-policy-fix-20261116`.
- Does not change the hosted LUCH service, private owner connector, installed apps or public onboarding availability.

The plugin icon is provisional, not final brand approval; Anthropic catalog acceptance and external-user Claude E2E remain unverified.
