---
name: luch-capabilities
description: 'Find what LUCH can actually do now across authorized browsers, tabs, screenshots, local computers,
  terminal, files and services; distinguish live tools from optional/unavailable features. RU: обнаружить реальные
  возможности браузера, вкладок, терминала, компьютера и файлов.'
---
# Discover LUCH capabilities / Возможности ЛУЧ
Use when the user asks whether LUCH can handle a page, tab, a native app, computer mouse, screenshot, file or folder, SSH/server, connected service, browser extension, or third-party agent.

## Discovery order
1. Enumerate installed MCP tools from the **current host session**. A skill only instructs; it does not install missing tools.
2. Get account-scoped device/server availability and permissions. Resolve the exact target and host; don't infer device online from historical inventory.
3. Classify each requested capability **LIVE_AND_AUTHORIZED**, **LIVE_NEEDS_PAIRING**, **HOST_SURFACE_LIMIT**, **OFFLINE**, **SOURCE_PREVIEW_ONLY**, **UNVERIFIED** or **NOT_AVAILABLE**. Never label an untested integration 'working'.
4. For public pages use isolated `server_browser_*`; for own signed-in browser only on a consented local tab; for native desktop require paired computer tools and actual OS access grants; for terminal require named server; for files require scoped file provider.
5. The browser extension developer preview currently has no agent relay. Physical OS mouse is a different capability from DOM click or Chrome tab-pointer events.

## User-facing bilingual shorthand
EN: “I can inspect the tools available in this Claude session and ask to connect a supported device if necessary.”
RU: «Я проверю реально доступные инструменты в этом чате и нужное разрешение. Наличие скилла не означает, что устройство уже подключено».

Basic LUCH tools are free. Do not offer plans, prices or paid services in replies.
