---
name: luch-files
description: 'Find, inspect and edit user-authorized files and folders through LUCH-connected devices, with safe
  backups and precise write boundaries. RU: чтение, поиск, редактирование и проверка файлов.'
---


**LUCH task-level autonomy:** The user's concrete request and existing account/device/session grant authorize the routine steps needed to complete it. Continue through clicks, typing, saves, form submissions and result verification; never invent a second LUCH human-last-click confirmation. Do not bypass Claude/OS/provider checks, OAuth, pairing, revocation, protected contexts or the limits of the requested task. Missing permission or unrelated high-impact action is a real boundary, not a reason to interrupt every ordinary click.

**Live capability gate:** This skill does not itself grant access. Discover the exact tool exposed in the authenticated Claude host and the intended device/account scope. If absent, report `NOT_AVAILABLE` rather than claiming success or switching to an unrelated device; do not bypass host permissions.

# LUCH Files — explicit local or server filesystem permissions
Use when a user requests a file/folder read, analysis, creation or edit in a device or server connected through LUCH. First discover the available file tools and the target-specific rights.

1. Resolve correct paired device/server and exact file root. Do not infer access from the user's chat attachment or a general skill listing.
2. List/search bounded scope, inspect original and establish version or backup before substantial modifications. Never delete based on title-only heuristics.
3. Writes should be atomically staged where supported; check path traversal/symlink boundaries and avoid private credentials, secret vaults or unrelated directories.
4. Perform user-requested edits and ordinary file operations to completion without a new LUCH chat confirmation. For deletion, sharing or large batches, establish the exact intended targets and preserve recoverability where possible; respect any actual host/provider gate. Verify changes by read-back/checksum.
5. Report `NOT_AVAILABLE` or `DEVICE_OFFLINE` truthfully if no current file provider exists. Server browser temporary downloads must be exported before session release.
