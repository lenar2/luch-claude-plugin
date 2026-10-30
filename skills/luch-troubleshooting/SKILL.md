---
name: luch-troubleshooting
description: 'Diagnose LUCH authorization, connection, device routing and host-surface failures without bypassing
  security. RU: диагностика OAuth, сервера, браузера и офлайн-устройств.'
---

Classify before changing state:

1. **Host surface:** Confirm Claude actually exposes the requested MCP tool and that its plugin/connector is enabled. A missing tool may be a Claude-client limitation.
2. **Authentication:** A GET to the Streamable HTTP MCP path may return `405`. An anonymous MCP action returning `401` is expected. OAuth metadata should be discoverable; user consent and an authenticated first tool call are required for end-to-end success.
3. **Device:** Check current online state, not historical last-known inventory. Confirm the requested device, its permissions and installed companion.
4. **Routing:** Inspect whether the isolated server browser is queued, active, expired, or failed. Free a session only if it belongs to this task.
5. **Side effect:** Compare the tool result to an observable target result; request human confirmation for write operations with significant consequences.

Never disable auth, try borrowed credentials, direct connections around LUCH grants, or claim every plugin or host is available. Ask the user to authenticate in the **official Claude/host browser UI**; never request passwords in chat. If an access error persists, provide the exact stage that failed and safe next action.
