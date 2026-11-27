---
name: luch-github-workflows
description: Use LUCH for source-grounded GitHub project maintenance, issues, and pull requests in repositories authorized by the user.
---

# LUCH GitHub Workflows for Claude

Use these workflows only for GitHub repositories available under the user's authenticated LUCH account. LUCH Projects is an explicitly scoped GitHub integration, not the general LUCH browser/computer/phone agent.

## Read and investigate

Use github_repo_info or github_repo_head to ground the exact repo and branch. Use github_tree, github_file_get, github_commit_log, github_commit_get, github_search_code and github_compare when available. Read the actual source before proposing a change. Do not imply that an empty search result is proof of absence.

## Execute authorized project work

Use github_issue for concrete issue workflows and github_apply_changes for bounded file edits. Use github_pr for a pull request and explain the result with the exact repository and commit/PR evidence. For an ordinary requested change within the user's authorized repository, carry it through to the API write instead of stopping at a hypothetical final button. Verify the resulting state using a read-back tool. Do not invent successful writes.

Never use these tools to send commands to a computer, operate arbitrary web pages, control a signed-in browser session, transfer funds, or change account credentials. Do not invoke hidden or unrelated tools. A client or external service may still enforce authorization, consent or high-impact checks; do not promise to bypass those.

## Good requests

- Compare changes between two commits and create a source-backed issue for the gaps.
- Fix a documentation error on a branch and open a pull request with exact evidence.
- Review an issue, inspect matching files and write a precise plan back to the authorized GitHub issue.
