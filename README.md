# LUCH for Claude — public client package (0.1.6)

LUCH connects AI agents to explicitly authorized tools and devices through a user-scoped remote MCP endpoint. This client-side plugin contains skills and connection metadata. It contains **no server implementation, user credentials, or device access tokens**.

## Availability

LUCH is an operating service with access limited to enabled accounts. Independent new-user OAuth onboarding and device-pairing end-to-end verification is not yet complete. Installing this package alone does **not** grant access to computers, browsers, files or accounts. Features depend on your account, grants, and connected devices. Do not assume public self-service access or an independently verified multi-user release.

## Included components

- 12 Claude skills under `skills/`, for choosing tools and permission-aware use. These are instructions, not extra APIs.
- `.mcp.json` connecting to the isolated public LUCH MCP endpoint.
- `.claude-plugin/plugin.json` with publisher metadata and Apache-2.0 client license.

## Connection and safe use

If your LUCH account has been enabled, connect through an officially supported MCP/OAuth flow, inspect granted tools, start with bounded read-only work, and revoke access when finished. Do not share credentials in chat. LUCH never grants private owner tools simply by installing this package.

## Public information

- Home: https://luch.lenarsalimov.ru/
- Getting started: https://luch.lenarsalimov.ru/docs/get-started/
- Privacy Policy (effective 31 October 2026): https://luch.lenarsalimov.ru/privacy/
- Terms of Use (effective 31 October 2026): https://luch.lenarsalimov.ru/terms/
- Support: https://luch.lenarsalimov.ru/support/

Technical questions: https://github.com/lenar2/luch-claude-plugin/issues/new (public). Confidential security or privacy reports: https://github.com/lenar2/luch-claude-plugin/security/advisories/new (private GitHub channel). No guarantees of independently verified public onboarding are made.

## License and scope

The files **in this repository** are licensed under Apache-2.0. This license does not include or open-source the separate, hosted LUCH server implementation, third-party services, user data, or trademarks. See `LICENSE`.
