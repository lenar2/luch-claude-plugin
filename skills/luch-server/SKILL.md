---
name: luch-server
description: 'Inspect an authorized server and execute bounded low-risk diagnostic commands through LUCH. RU: команды
  сервера, SSH и терминальные задачи.'
---


**LUCH task-level autonomy:** The user's concrete request and existing account/device/session grant authorize the routine steps needed to complete it. Continue through clicks, typing, saves, form submissions and result verification; never invent a second LUCH human-last-click confirmation. Do not bypass Claude/OS/provider checks, OAuth, pairing, revocation, protected contexts or the limits of the requested task. Missing permission or unrelated high-impact action is a real boundary, not a reason to interrupt every ordinary click.

**Live capability gate:** This skill does not itself grant access. Discover the exact tool exposed in the authenticated Claude host and the intended device/account scope. If absent, report `NOT_AVAILABLE` rather than claiming success or switching to an unrelated device; do not bypass host permissions.

Use server operations only for a server explicitly owned or authorized by the requesting user.

- Identify the exact paired server using the current device/server list. Do not assume the LUCH internal control server is the user's server.
- Read status and health before an operation. Start with harmless bounded diagnostics, such as an `echo` or listing a known test directory.
- If tool schemas expose safe argv execution, pass structured arguments, fixed working directory and timeout; do not include secrets or run pasted remote commands blindly.
- Never restart production, change firewalls, install services, alter DNS, shut down a node, or attempt failover from an ambiguous user instruction. Such changes require exact scope and a rollback plan.
- For ambiguous acknowledgment, use job receipts/status if supported; never replay a potentially state-changing operation blindly.
- A visible service response does **not** prove high availability or failover. Report availability claims only after independent tests.
