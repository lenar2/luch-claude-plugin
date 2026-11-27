---
name: luch-computer
description: 'Operate a connected, permitted user computer: screen, pointing/click, keyboard and native apps only
  when the particular device is online and capability is verified. RU: работа с разрешённым компьютером, экраном,
  мышью и приложениями.'
---


**LUCH task-level autonomy:** The user's concrete request and existing account/device/session grant authorize the routine steps needed to complete it. Continue through clicks, typing, saves, form submissions and result verification; never invent a second LUCH human-last-click confirmation. Do not bypass Claude/OS/provider checks, OAuth, pairing, revocation, protected contexts or the limits of the requested task. Missing permission or unrelated high-impact action is a real boundary, not a reason to interrupt every ordinary click.

**Live capability gate:** This skill does not itself grant access. Discover the exact tool exposed in the authenticated Claude host and the intended device/account scope. If absent, report `NOT_AVAILABLE` rather than claiming success or switching to an unrelated device; do not bypass host permissions.

# LUCH Computer — optional local device control
Use when the user needs action inside a *paired, currently online* Mac or another permitted desktop. Distinguish remote server-browser actions from native computer mouse/keyboard/desktop automation.

1. Discover device-list, device identity and tool schemas first. Do **not** assume screen, computer-click, hotkey or keyboard operations exist just because this skill is installed.
2. Require specific device pairing, user authorization, and visible session/OS permission; don't bypass TCC/accessibility or system prompts. If several machines are online, ask/resolve the exact target; do not silently switch devices.
3. If native computer tools are exposed, prefer screenshot/observation, then bounded single action, then screenshot verification. For element clicks prefer semantic/coordinate grounding and correct display scaling; don't assume a screenshot coordinate always maps to OS coordinates.
4. For an already authorized task and device, continue through normal UI actions including clicking, typing and saving without an extra LUCH confirmation. Preserve the person's ability to pause/revoke. Respect host, OS and service approval for credential, financial, destructive or otherwise high-impact operations; never silently exceed task scope.
5. If mouse/keyboard APIs are unavailable in the host or device is offline, say **HOST_SURFACE_LIMIT / DEVICE_OFFLINE / NOT_VERIFIED** as appropriate; do not pretend the action happened. Native desktop and iPhone control are not generally guaranteed by first-release Core.
