# LUCH — 30-second illustrated walkthrough (NOT live test evidence)

**This is an example of the product flow, not a claim that a new customer successfully ran it.** The screenshots, user accounts, and receipts for an independent public-user E2E are still pending.

## 1. User chooses a supported AI client

Open [Claude source](../README.md), [Cursor plugin](https://github.com/lenar2/luch-cursor) or [Gemini CLI extension](https://github.com/lenar2/luch-gemini). Installation instructions differ by host. **Kimi** is currently a candidate, not a verified distribution channel.

## 2. The user authenticates and grants only needed scopes

The client discovers the LUCH MCP server over HTTPS. If the account is supported, the host must use its OAuth flow. **No copied access tokens, owner credentials or blanket device access.**

**Example prompt:** "Show only the tools and devices authorized for my account. Do not modify anything."

**Expected safe behavior:** The agent enumerates *only* devices granted to that user, or returns an authorization/onboarding error. No silent cross-tenant fallback.

## 3. First useful bounded action

**Example prompt:** "Read the README in the demo folder I allowed, and summarize the setup in three sentences. Do not edit files."

**Expected safe behavior:** Verify an allowed file path, honor read-only authorization, return the summary or a permission error. Do not simulate a successful read when it was not performed.

## 4. Permission-sensitive actions

**Example prompt:** "Rename my approved demo file to meeting-notes.txt."

**Expected safe behavior:** Check action scope, authorization, and target identity; require explicit action approval when applicable. A prohibited path, other person's account or unavailable device must fail closed.

## 5. User revokes permission

After revoking the relevant permission, the same capability should be unavailable on the next check. This must be independently tested before marketing it as a release guarantee.

## Suggested short-form video storyboard (to record only after E2E)

1. **0–4 s:** "What if your AI could work with *your* tools — only with your permission?"
2. **4–9 s:** Show real plugin selection and host-native OAuth.
3. **9–17 s:** Show an approved, **read-only** demo-folder task and its genuine result.
4. **17–23 s:** Show a forbidden-path refusal or permission-revocation check.
5. **23–30 s:** "LUCH — public client source on GitHub. Early access; independent onboarding still in validation."

Use actual test-session footage and avoid fake star counts, fake reviewers, fabricated results, and unverified platform approval badges.
