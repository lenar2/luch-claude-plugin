# LUCH — Connect AI agents to the tools *you* authorize

**Public client preview v0.1.6 · Early-access service · Apache-2.0 client license**

[Website](https://luch.lenarsalimov.ru/) · [Getting started](https://luch.lenarsalimov.ru/docs/get-started/) · [Demo walkthrough](docs/DEMO.md) · [Release notes](docs/RELEASE_NOTES_v0.1.6-preview.md) · [Security](SECURITY.md)

> **RU:** LUCH — мост между ИИ-агентом и вашими разрешёнными устройствами, браузерами, файлами и сервисами. Пакеты можно скачать сейчас; самостоятельное подключение новых пользователей пока тестируется.

LUCH is a permission-aware bridge between AI assistants and user-approved browsers, files, connected services and devices. Public client packages contain instructions and connection metadata, **not** the hosted server, access tokens, device credentials, or private user data.

**Public code does not mean open access to someone else's computers.** Every real operation requires a supported host, an enabled LUCH account, OAuth authorization where supported, and the necessary device/tool permissions.

## Pick your AI assistant

| Client | Public package | How to start |
| --- | --- | --- |
| **Claude** | **[LUCH for Claude](https://github.com/lenar2/luch-claude-plugin)** (this repository) | Browse the 12 skills and `.mcp.json`. Install/connect using your Claude client's supported plugin/MCP flow; marketplace availability is separate. |
| **Cursor** | [LUCH for Cursor](https://github.com/lenar2/luch-cursor) | Follow the [Cursor installation steps](https://github.com/lenar2/luch-cursor#installation-and-local-verification). |
| **Gemini CLI** | [LUCH for Gemini](https://github.com/lenar2/luch-gemini) | `gemini extensions install https://github.com/lenar2/luch-gemini`, then follow the repo's OAuth instructions. |
| **Kimi** | [Kimi adapter candidate](https://github.com/lenar2/luch-claude-plugin/tree/kimi-v0.1.6-candidate) | **Preview only**. Not yet a verified Kimi install or approved directory listing. |

**Want to inspect the source?** [Download this Claude client package as ZIP](https://github.com/lenar2/luch-claude-plugin/archive/refs/heads/main.zip) or `git clone https://github.com/lenar2/luch-claude-plugin.git`. **The ZIP is source code, not a standalone Mac/iPhone installer.**

## What can LUCH help with?

- Discover tools and devices **explicitly linked to your account**.
- Read approved files and browser context, subject to actual per-tool and host permissions.
- Coordinate supported workflows across connected environments, only within granted scopes.
- Ask for explicit consent before permission-sensitive or destructive actions.

[Read a safe, illustrative demonstration](docs/DEMO.md). It distinguishes example prompts from actions verified in a live user account.

## Status — understand before installing

| Area | Status |
| --- | --- |
| Client source, skills and plugin metadata | **Public** |
| Hosted LUCH website and onboarding documentation | **Online (checked 2026-11-05)** |
| Unauthenticated request to public MCP | **401 expected (checked 2026-11-05)** |
| Independent new-user signup → OAuth → device pairing → permitted action | **NOT YET VERIFIED** |
| Multi-tenant isolation and revocation on an independent new-user E2E | **NOT YET VERIFIED** |
| App marketplace approvals or public self-service availability | **Do not infer from this GitHub page** |

**If you are not an enabled LUCH user, installing a client package alone will not grant operational access.** Public marketing remains in *early access* until the [release gates](docs/PUBLIC_RELEASE_GATES.md) are independently verified.

## Help improve LUCH

- **Star ⭐ this repository** if you want to follow the project. Stars measure developer interest, **not installs**.
- [Open an issue](https://github.com/lenar2/luch-claude-plugin/issues/new) with reproducible technical feedback (no secrets).
- See [documentation](https://luch.lenarsalimov.ru/docs/get-started/) and [support](https://luch.lenarsalimov.ru/support/).
- Report private vulnerabilities through [GitHub Security Advisories](https://github.com/lenar2/luch-claude-plugin/security/advisories/new), not public issues.

## What's inside this Claude client package

`skills/` contains 12 permission-aware skills; `.mcp.json` points to the HTTPS OAuth-protected remote MCP endpoint; `.claude-plugin/plugin.json` contains metadata for the Claude package. `LICENSE` applies only to files in this public client repo. The separately hosted LUCH backend, user data, accounts, connected devices, and trademarks are **not** open-sourced by this license.

[Privacy policy](https://luch.lenarsalimov.ru/privacy/) · [Terms](https://luch.lenarsalimov.ru/terms/) · [Support](https://luch.lenarsalimov.ru/support/)
