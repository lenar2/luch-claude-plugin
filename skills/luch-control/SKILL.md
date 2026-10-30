---
name: luch-control
description: 'Choose and operate authorized LUCH tools based on actual availability and user permissions. RU: подключение
  устройств, выбор нужных инструментов и контроль прав.'
---

Use LUCH only when the user requests interaction with their own connected devices, services, browser sessions, or servers.

1. Discover the authorized LUCH resources and current capabilities before promising a result. A tool name appearing in a plugin does not grant access to its target.
2. Select a specific paired target. If multiple devices appear, do not guess. Never reroute to another device or account after a denial or failure.
3. For public web tasks choose an isolated **server browser** when that capability is available; user-local browser, file, credential, or native UI tasks need the specific user's connected device and matching permission.
4. Prefer read-only inspection first. Before writes or externally consequential operations, follow host confirmations and LUCH's own explicit authorization policy. Both layers apply.
5. Read current tool schemas and use the tools actually exposed. Never invent tool names, states, success receipts, or capabilities.
6. Keep sensitive content minimal. Never put passwords, API keys, cookies, authorization tokens, or unrelated personal data in prompts, arguments, reports, or logs.
7. Report completed action, observable result, and remaining uncertainty separately. A successful command submission is not necessarily a successful external side effect.

**Scope:** only the LUCH tools listed for the current account in this session are available. Local computer, browser, file and service tools depend on device pairing and authorization. iPhone control and service-specific actions are **not general LUCH guarantees**.
