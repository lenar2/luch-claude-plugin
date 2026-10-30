---
name: luch-local-browser
description: 'Work in the user-authorized, paired local browser tab or profile when local login/session/files are
  essential; support scoped clicks, typing and page interaction. RU: работа с локальной вкладкой браузера и активной
  пользовательской сессией.'
---

**Public Core 0.1.5 availability gate:** This skill is guidance only. Before invoking an operation, verify that the **currently authenticated Claude host** exposes the exact LUCH tool and that the user has the required scoped grant. If absent or unverified, report `NOT_AVAILABLE` or `NOT_RUN` instead of implying access. No private OWNER LUCH fallback is permitted.

# LUCH Local Browser — user's existing sessions (optional)
Use only when the user asks to work in their own browser's logged-in profile or open tabs. Public web navigation should default to LUCH's isolated server browser to minimize exposure.

- A local tab/profile must be discovered through a live authorized paired device or LUCH Browser Extension; the skill alone does not establish browser access.
- Obtain per-site/active-tab access, keep a visible running indicator, honor pause/end session. Do not extract session cookies, passwords or authentication tokens. Never bridge between private and unrelated profiles.
- Use current available browser capabilities to inspect target, click, type, scroll or screenshot only as needed, then verify outcome. Distinguish DOM element clicks from moving the operating-system mouse cursor; native mouse control requires a separate local companion/OS grant.
- No hidden indefinite access, no bypass of browser restrictions and no automation of other users' accounts. Ask for confirmation before purchases, publication, form submissions with external effects and sensitive changes.
- If extension/companion is not installed, online or authenticated, do not invent capabilities or claim automatic cross-browser coverage. Chrome-family first; Firefox requires its own compatibility QA.
