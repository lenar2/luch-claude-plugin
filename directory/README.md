# LUCH Projects for Claude — Directory candidate

LUCH Projects is the intentionally specialized GitHub project integration for Claude. It keeps an assistant autonomous through **actual authorized GitHub API actions**: inspect source, create issues, commit bounded changes and open pull requests. It does not instruct a user to click the last button for ordinary project changes. Authorization remains governed by the real provider and Claude host.

This is NOT a generic browser/desktop/phone executor. The approved GitHub tool names are enforced server-side by the isolated directory gateway. Requests for unknown tools cannot be forwarded. The full LUCH product is available separately through its direct integration, outside the Directory listing.

**Status:** source and gateway candidate only. Not a deployed connector and not an approved Directory listing. The endpoint in .mcp.json must be deployed and independently tested with OAuth before the package is submitted. See ../directory-gateway/README.md.

Typical tasks:
1. Inspect a repository and show which commit introduced a regression.
2. Read a project issue, change an authorized branch and open a pull request.
3. Review differences and create a structured follow-up issue.

Direct full LUCH remains unchanged at https://luch.lenarsalimov.ru/luch/core/mcp.
