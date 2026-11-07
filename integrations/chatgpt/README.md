<p><img src="https://raw.githubusercontent.com/lenar2/luch/main/website/assets/luch-ray.svg" width="36" alt=""></p>

# LUCH for ChatGPT
### From a request in chat to work in permitted tools.

[**A verified founder-environment case**](https://github.com/lenar2/luch/blob/main/docs/REAL_WORK.md) · [**Choose a connection path**](https://github.com/lenar2/luch/blob/main/docs/START_HERE.md) · [LUCH home](https://github.com/lenar2/luch) · [Русский](README.ru.md)

**Status: submission candidate — NOT an approved or published OpenAI Directory listing.** Installing this public source does not enable a new LUCH account.

## What a useful result looks like

The founder asked to redesign LUCH's own site, without touching the Mac. The assistant used authorized server and GitHub resources to inspect, revise, verify and publish the site. [Exact commit](https://github.com/lenar2/luch/commit/06daa8d6b89a3dfd65e74628b895879e79a0c931) · [release evidence](https://github.com/lenar2/ai-factory-evidence/issues/4009#issuecomment-6692683064).

This is **not** a fresh-user ChatGPT integration test; it is a real founder-environment LUCH workflow. The [later human-experience audit](https://github.com/lenar2/ai-factory-evidence/issues/4009#issuecomment-6705944671) did not mark the published design as finished.

## If you want to connect

**Using an existing enabled account?** Use the supported, host-managed OAuth connection for this portable candidate and inspect actual available tools before trying a read-only request. Do not copy tokens from another account.

**Not already enabled?** A public directory install and self-service signup path are **not verified**. Check [availability](https://luch.lenarsalimov.ru/en/status/) before assuming access.

**First safe task:** “Read this public page and summarize it with a source link.” Follow only permissions visible for your current account and client.

<details><summary>For OpenAI integration reviewers — package, endpoints and release gates</summary>

- **Public candidate v0.1.6:** portable `plugin.json` and `mcp.json`, twelve public skills and Apache-2.0 license. From the parent repository root run `python3 integrations/chatgpt/build_package.py` to create `dist/luch-chatgpt-0.1.6-preview.zip`.
- **Separate private installation:** the founder has a separate LUCH 0.3.51 personal plugin. **Do not modify or replace that installation** while preparing this public candidate; the public source is not its entry point.
- The portable client declares the public HTTPS MCP service; it embeds no credentials. An anonymous HTTP 401/OAuth metadata challenge is **not** evidence of successful consent or independent account access.
- **Before submission:** publisher identity/domain, new non-owner ChatGPT OAuth, actual tool discovery and risk annotations, independently authorized test devices, read-only browser task, unpaired-device denial, revocation, explicit approval for consequences, genuine walkthrough recording, automated scan, then owner-approved submission.
- The public candidate is **not** an iPhone installer, a standalone application or a route into the founder's private devices.

[Detailed guidance](https://developers.openai.com/plugins/build/plugins) · [Submission docs](https://developers.openai.com/plugins/deploy/submission) · [Privacy](https://luch.lenarsalimov.ru/privacy/) · [Terms](https://luch.lenarsalimov.ru/terms/)

</details>
