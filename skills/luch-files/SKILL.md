---
name: luch-files
description: 'Find, inspect and edit user-authorized files and folders through LUCH-connected devices, with safe
  backups and precise write boundaries. RU: чтение, поиск, редактирование и проверка файлов.'
---

**Public Core 0.1.5 availability gate:** This skill is guidance only. Before invoking an operation, verify that the **currently authenticated Claude host** exposes the exact LUCH tool and that the user has the required scoped grant. If absent or unverified, report `NOT_AVAILABLE` or `NOT_RUN` instead of implying access. No private OWNER LUCH fallback is permitted.

# LUCH Files — explicit local or server filesystem permissions
Use when a user requests a file/folder read, analysis, creation or edit in a device or server connected through LUCH. First discover the available file tools and the target-specific rights.

1. Resolve correct paired device/server and exact file root. Do not infer access from the user's chat attachment or a general skill listing.
2. List/search bounded scope, inspect original and establish version or backup before substantial modifications. Never delete based on title-only heuristics.
3. Writes should be atomically staged where supported; check path traversal/symlink boundaries and avoid private credentials, secret vaults or unrelated directories.
4. Ask confirmation for irreversible deletion, sharing/publication and large batches; verify exact modified file by read-back/checksum.
5. Report `NOT_AVAILABLE` or `DEVICE_OFFLINE` truthfully if no current file provider exists. Server browser temporary downloads must be exported before session release.
