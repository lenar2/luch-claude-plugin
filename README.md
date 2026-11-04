# LUCH for Claude — v0.1.6

**This repository is the Claude client adapter.** The independent, platform-neutral product and the main place to ⭐ Star the project is **[LUCH on GitHub](https://github.com/lenar2/luch)**. See [the global website](https://luch.lenarsalimov.ru/) for all supported clients.

**LUCH connects AI assistants to the browsers, computers, files and servers you authorize.**

[Website](https://luch.lenarsalimov.ru/) · [Getting started](https://luch.lenarsalimov.ru/docs/get-started/) · [Русский](README.ru.md) · [Security](https://luch.lenarsalimov.ru/security/)

> **Early access:** Public client packages are available, but independent new-user onboarding and end-to-end access are not yet verified.

## What can LUCH actually do?

| Your request | LUCH capability |
| --- | --- |
| “Open two websites and compare their details.” | Run an isolated, temporary server browser to read and interact with public web pages. |
| “Check my server and tell me whether it is healthy.” | Discover a permitted paired server and run a bounded diagnostic command. |
| “Find the project file I gave access to.” | Read allowed files through a paired device or connected service. |
| “Which of my devices are online?” | List account-authorized devices and their current availability. |
| “Use an application on my connected Mac.” | Use supported browser and computer actions when the device is online and access is granted. |

**One workflow, multiple execution surfaces:** An AI assistant can work through the remote MCP connection, a temporary server browser, or an authorized paired computer according to the task and available permissions.

## How to start

1. Pick a supported AI client.
2. Connect an enabled LUCH account through the host's supported authentication process.
3. Ask for a specific task and inspect the actual result.

Installation alone does not enroll a new user or connect their devices. The availability and permission scope vary by account and AI host.

## Choose an integration

| Client | Link | Status |
| --- | --- | --- |
| **ChatGPT and Codex** | [OpenAI client candidate](integrations/chatgpt/) | Existing private plugin; public review pending |
| **Claude** | [Claude client package](.claude-plugin/plugin.json) | Public source |
| **Cursor** | [Cursor plugin](https://github.com/lenar2/luch-cursor) | Public source |
| **Gemini CLI** | [Gemini extension](https://github.com/lenar2/luch-gemini) | Public source |
| **Kimi** | [Kimi candidate](https://github.com/lenar2/luch-claude-plugin/tree/kimi-v0.1.6-candidate) | Testing and submission not completed |

This repository contains the **Claude integration**. LUCH itself is a **platform-independent product**: [luch.lenarsalimov.ru](https://luch.lenarsalimov.ru/). The Claude repository name is kept for compatibility with existing installation and review links.

## Responsible release scope

Available for enabled accounts: selected cloud-browser, paired-server, local browser, file and computer capabilities. A complete new-user OAuth and device-pairing flow is **not yet independently verified**. iPhone control and live AI-agent coordination are separate tracks, not claims for the public Core release.

[Release gates](docs/PUBLIC_RELEASE_GATES.md) · [Illustrative demo](docs/DEMO.md) · [Support](https://luch.lenarsalimov.ru/support/)

**Follow LUCH:** Star this repository to bookmark the project. Stars are not a count of installed users.

Apache-2.0 covers these public client files only, not the hosted server or user data.
