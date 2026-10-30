---
name: luch-services
description: 'Operate an explicitly linked and supported user service only through verified available MCP APIs or
  authorized browser workflows; never invent integrations. RU: сервисы, аккаунты, приложения и безопасная автоматизация.'
---

**Public Core 0.1.5 availability gate:** This skill is guidance only. Before invoking an operation, verify that the **currently authenticated Claude host** exposes the exact LUCH tool and that the user has the required scoped grant. If absent or unverified, report `NOT_AVAILABLE` or `NOT_RUN` instead of implying access. No private OWNER LUCH fallback is permitted.
# LUCH Services / Сервисы
Use only when a user asks to operate their own service, SaaS app or existing authorized account.
- Prefer a verified native service tool with tenant-scoped OAuth, then an isolated browser for public data, then a paired authorized local-browser session only if their login is required.
- Distinguish **provider present** from **tested end-to-end**. Integration roadmaps like Tilda/GetCourse do not prove live service access.
- Never ask for a raw password/token in chat and don't exfiltrate cookies, secrets or account recovery codes.
- Publishing, billing, purchases, deletion, user invitations and account changes need exact target, consequences and explicit authorization.
- If the account is not connected or tool absent, say so; no unsupported guesses or cross-user operations.
