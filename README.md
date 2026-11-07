<p><img src="https://raw.githubusercontent.com/lenar2/luch/main/website/assets/luch-ray.svg" width="36" alt=""></p>

# LUCH for Claude
### A useful answer is good. Work you can inspect is better.

Claude is where you explain what you need. **LUCH is the connection to websites, files and devices you choose to authorize**, when your account and host support them.

[**LUCH in action**](https://github.com/lenar2/luch/blob/main/docs/REAL_WORK.md) · [**Connection path**](#your-way-in) · [Русский](README.ru.md) · [LUCH home](https://github.com/lenar2/luch)

> **Current availability:** client source is public; a fresh customer's Claude sign-in, marketplace approval and device pairing are **not** independently verified. A published adapter does not grant service access.

## A real task, with receipts

A founder asked the assistant to turn the over-technical LUCH website into a human-facing product while leaving the Mac untouched. Through authorized server and GitHub tools, the site was inspected, revised and released. The [exact public commit](https://github.com/lenar2/luch/commit/06daa8d6b89a3dfd65e74628b895879e79a0c931) and [release QA](https://github.com/lenar2/ai-factory-evidence/issues/4009#issuecomment-6692683064) can be inspected.

**This is evidence for LUCH in the founder's environment, not proof that Claude performed that task or that a new Claude customer can connect today.** [Read the full case and the later critical review](https://github.com/lenar2/luch/blob/main/docs/REAL_WORK.md).

## What Claude could ask LUCH to do

| You ask Claude | LUCH's permitted route | What comes back |
| --- | --- | --- |
| “Compare these two public service pages.” | An isolated, temporary server browser | Sources and meaningful differences |
| “Find the document in my approved folder.” | A connected device or authorized file source | A located file and a reviewable summary |
| “Check the server I selected.” | An explicitly paired, permitted server | Actual diagnostic output, not a guess |

Each is a **possible task**. Availability depends on the selected account, client and grants. Offline devices do not silently switch to another machine.

## Your way in

**1 · Check access.** [See the current status](https://luch.lenarsalimov.ru/en/status/). The hosted service currently supports enabled accounts; there is no verified open self-service enrollment for arbitrary new users.

**2 · Connect through Claude only if eligible.** Inspect this repository's [Claude plugin manifest](.claude-plugin/plugin.json), follow the host-supported plugin connection/authorization path and approve only the required tools. This is source, **not a guarantee of marketplace publication**.

**3 · Start small.** Ask Claude to read one public page or report the exact list of authorized LUCH tools. Inspect its response before permitting writes.

If the account is not enabled, installing this client will not fix that. [Connection guidance](https://luch.lenarsalimov.ru/docs/get-started/) · [Support](https://luch.lenarsalimov.ru/support/).

<details><summary>For Claude plugin reviewers and developers</summary>

This is the **Claude adapter**, not the LUCH platform itself. The public package includes an authorized remote MCP integration and 12 agent skills. The client package version is v0.1.6; the hosted private service has a separate lifecycle. No private account, personal device or server source is included.

[Release gates](docs/PUBLIC_RELEASE_GATES.md) · [Original illustrative demo](docs/DEMO.md) · [Safety](SECURITY.md) · [Apache-2.0 license](LICENSE). Catalog approval and genuinely new-user OAuth E2E remain separate checks. A request receipt is not completed execution.

</details>
