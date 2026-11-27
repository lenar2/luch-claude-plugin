---
name: luch-local-browser
description: 'Work in the user-authorized, paired local browser tab or profile when local login/session/files are
  essential; support scoped clicks, typing and page interaction. RU: работа с локальной вкладкой браузера и активной
  пользовательской сессией.'
---


**LUCH task-level autonomy:** The user's concrete request and existing account/device/session grant authorize the routine steps needed to complete it. Continue through clicks, typing, saves, form submissions and result verification; never invent a second LUCH human-last-click confirmation. Do not bypass Claude/OS/provider checks, OAuth, pairing, revocation, protected contexts or the limits of the requested task. Missing permission or unrelated high-impact action is a real boundary, not a reason to interrupt every ordinary click.

**Live capability gate:** This skill does not itself grant access. Discover the exact tool exposed in the authenticated Claude host and the intended device/account scope. If absent, report `NOT_AVAILABLE` rather than claiming success or switching to an unrelated device; do not bypass host permissions.

# LUCH Local Browser — user's existing sessions (optional)
Use only when the user asks to work in their own browser's logged-in profile or open tabs. Public web navigation should default to LUCH's isolated server browser to minimize exposure.

- A local tab/profile must be discovered through a live authorized paired device or LUCH Browser Extension; the skill alone does not establish browser access.
- Obtain per-site/active-tab access, keep a visible running indicator, honor pause/end session. Do not extract session cookies, passwords or authentication tokens. Never bridge between private and unrelated profiles.
- Use current available browser capabilities to inspect target, click, type, scroll or screenshot only as needed, then verify outcome. Distinguish DOM element clicks from moving the operating-system mouse cursor; native mouse control requires a separate local companion/OS grant.
- No hidden indefinite access, no bypass of browser restrictions or other users' accounts. Within an authorized session and explicit task, complete routine navigation, clicks, text entry and Submit without a separate LUCH prompt. For sensitive or unrequested high-impact outcomes, verify that the intended result is within the user's instruction and obey actual host/provider gates.
- If extension/companion is not installed, online or authenticated, do not invent capabilities or claim automatic cross-browser coverage. Chrome-family first; Firefox requires its own compatibility QA.
