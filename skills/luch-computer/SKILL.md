---
name: luch-computer
description: 'Operate a connected, permitted user computer: screen, pointing/click, keyboard and native apps only
  when the particular device is online and capability is verified. RU: работа с разрешённым компьютером, экраном,
  мышью и приложениями.'
---

**Public Core 0.1.5 availability gate:** This skill is guidance only. Before invoking an operation, verify that the **currently authenticated Claude host** exposes the exact LUCH tool and that the user has the required scoped grant. If absent or unverified, report `NOT_AVAILABLE` or `NOT_RUN` instead of implying access. No private OWNER LUCH fallback is permitted.

# LUCH Computer — optional local device control
Use when the user needs action inside a *paired, currently online* Mac or another permitted desktop. Distinguish remote server-browser actions from native computer mouse/keyboard/desktop automation.

1. Discover device-list, device identity and tool schemas first. Do **not** assume screen, computer-click, hotkey or keyboard operations exist just because this skill is installed.
2. Require specific device pairing, user authorization, and visible session/OS permission; don't bypass TCC/accessibility or system prompts. If several machines are online, ask/resolve the exact target; do not silently switch devices.
3. If native computer tools are exposed, prefer screenshot/observation, then bounded single action, then screenshot verification. For element clicks prefer semantic/coordinate grounding and correct display scaling; don't assume a screenshot coordinate always maps to OS coordinates.
4. For logins, payments, confidential messages, publishing and destructive modifications require explicit confirmation and preserve the human's ability to pause/revoke.
5. If mouse/keyboard APIs are unavailable in the host or device is offline, say **HOST_SURFACE_LIMIT / DEVICE_OFFLINE / NOT_VERIFIED** as appropriate; do not pretend the action happened. Native desktop and iPhone control are not generally guaranteed by first-release Core.
