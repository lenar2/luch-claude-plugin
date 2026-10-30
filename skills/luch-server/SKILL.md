---
name: luch-server
description: 'Inspect an authorized server and execute bounded low-risk diagnostic commands through LUCH. RU: команды
  сервера, SSH и терминальные задачи.'
---

**Public Core 0.1.5 availability gate:** This skill is guidance only. Before invoking an operation, verify that the **currently authenticated Claude host** exposes the exact LUCH tool and that the user has the required scoped grant. If absent or unverified, report `NOT_AVAILABLE` or `NOT_RUN` instead of implying access. No private OWNER LUCH fallback is permitted.

Use server operations only for a server explicitly owned or authorized by the requesting user.

- Identify the exact paired server using the current device/server list. Do not assume the LUCH internal control server is the user's server.
- Read status and health before an operation. Start with harmless bounded diagnostics, such as an `echo` or listing a known test directory.
- If tool schemas expose safe argv execution, pass structured arguments, fixed working directory and timeout; do not include secrets or run pasted remote commands blindly.
- Never restart production, change firewalls, install services, alter DNS, shut down a node, or attempt failover from an ambiguous user instruction. Such changes require exact scope and a rollback plan.
- For ambiguous acknowledgment, use job receipts/status if supported; never replay a potentially state-changing operation blindly.
- A visible service response does **not** prove high availability or failover. Report availability claims only after independent tests.
