---
name: luch-tabs
description: 'Control user-authorized browser tabs and window state: list, open, activate and close only session-owned
  tabs with verification. RU: вкладки, переходы, история страниц, скриншоты и клики.'
---

**Public Core 0.1.5 availability gate:** This skill is guidance only. Before invoking an operation, verify that the **currently authenticated Claude host** exposes the exact LUCH tool and that the user has the required scoped grant. If absent or unverified, report `NOT_AVAILABLE` or `NOT_RUN` instead of implying access. No private OWNER LUCH fallback is permitted.
# LUCH Browser Tabs / Вкладки
For tabs/windows, prefer the host's exact exposed browser tool and the user's active authorized session.
- When using a local Browser Companion, require installation, pairing, and visible per-tab grant. Extension local preview does not yet enable remote agents.
- List only current granted scope and avoid showing unrelated tab URLs to an untrusted context.
- Open tabs for the execution; mark ownership, preserve human tabs and browsing history. Close only tabs created for this execution.
- Verify target after navigating, handle redirects and log-in state without reading credentials or cookies.
- Browser-level pointer clicks inside a tab are not OS-wide mouse control. Use current capability metadata and permission checks; Chrome Debugger access has a visible separate warning.
- If needed API is not in tool inventory, do not invent one: report the host limitation.
