---
name: luch-tabs
description: 'Control user-authorized browser tabs and window state: list, open, activate and close only session-owned
  tabs with verification. RU: вкладки, переходы, история страниц, скриншоты и клики.'
---


**LUCH task-level autonomy:** The user's concrete request and existing account/device/session grant authorize the routine steps needed to complete it. Continue through clicks, typing, saves, form submissions and result verification; never invent a second LUCH human-last-click confirmation. Do not bypass Claude/OS/provider checks, OAuth, pairing, revocation, protected contexts or the limits of the requested task. Missing permission or unrelated high-impact action is a real boundary, not a reason to interrupt every ordinary click.

**Live capability gate:** This skill does not itself grant access. Discover the exact tool exposed in the authenticated Claude host and the intended device/account scope. If absent, report `NOT_AVAILABLE` rather than claiming success or switching to an unrelated device; do not bypass host permissions.
# LUCH Browser Tabs / Вкладки
For tabs/windows, prefer the host's exact exposed browser tool and the user's active authorized session.
- When using a local Browser Companion, require installation, pairing, and visible per-tab grant. Extension local preview does not yet enable remote agents.
- List only current granted scope and avoid showing unrelated tab URLs to an untrusted context.
- Open tabs for the execution; mark ownership, preserve human tabs and browsing history. Close only tabs created for this execution.
- Verify target after navigating, handle redirects and log-in state without reading credentials or cookies.
- Browser-level pointer clicks inside a tab are not OS-wide mouse control. Use current capability metadata and permission checks; Chrome Debugger access has a visible separate warning.
- If needed API is not in tool inventory, do not invent one: report the host limitation.
