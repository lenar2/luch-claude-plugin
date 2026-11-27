---
name: luch-services
description: 'Operate an explicitly linked and supported user service only through verified available MCP APIs or
  authorized browser workflows; never invent integrations. RU: сервисы, аккаунты, приложения и безопасная автоматизация.'
---


**LUCH task-level autonomy:** The user's concrete request and existing account/device/session grant authorize the routine steps needed to complete it. Continue through clicks, typing, saves, form submissions and result verification; never invent a second LUCH human-last-click confirmation. Do not bypass Claude/OS/provider checks, OAuth, pairing, revocation, protected contexts or the limits of the requested task. Missing permission or unrelated high-impact action is a real boundary, not a reason to interrupt every ordinary click.

**Live capability gate:** This skill does not itself grant access. Discover the exact tool exposed in the authenticated Claude host and the intended device/account scope. If absent, report `NOT_AVAILABLE` rather than claiming success or switching to an unrelated device; do not bypass host permissions.
# LUCH Services / Сервисы
Use only when a user asks to operate their own service, SaaS app or existing authorized account.
- Prefer a verified native service tool with tenant-scoped OAuth, then an isolated browser for public data, then a paired authorized local-browser session only if their login is required.
- Distinguish **provider present** from **tested end-to-end**. Integration roadmaps like Tilda/GetCourse do not prove live service access.
- Never ask for a raw password/token in chat and don't exfiltrate cookies, secrets or account recovery codes.
- For already requested service work, use available API and browser tools to complete actions, including clicks and form submission, without a repeated LUCH approval prompt. Ground target and consequences for publication, billing, purchases, deletion, invitations or account changes and obey actual host/provider approvals; never add unrelated effects.
- If the account is not connected or tool absent, say so; no unsupported guesses or cross-user operations.
