# A Claude workflow: make a decision from the material you already have

[← LUCH for Claude](../README.md) · [Русский](CLAUDE_WORKFLOW.ru.md)

## The situation

You need to decide what to do next, but the answer is spread across a project brief, two internal documents and current public information.

## The work

**1. Set the question.** Tell Claude what decision you need to make and what a useful answer should contain.

**2. Select the sources.** Name the exact approved files or folder. Ask Claude to use public pages for external context. LUCH's file and browser tools are separate routes; Claude should use only what the current session exposes.

**3. Compare, don't just summarize.** Ask for:
- points on which the documents agree;
- differences and contradictions;
- facts that are supported by a source;
- assumptions and unanswered questions;
- the implications for your decision.

**4. Shape the deliverable.** Ask for a one-page decision note, a comparison table or a draft message. Inspect the sources and conclusions.

**5. Save only when you choose.** If you want a file created or changed, name the exact destination and authorize that action separately. Keep the original intact.

## A prompt to try

> Read the two documents in my approved project folder. Compare their recommendations with these public sources: [add URLs]. Separate facts from assumptions, show the source for each important claim, and finish with the three decisions I need to make. Do not edit or publish anything.

## What makes this a LUCH workflow

Claude provides the reasoning and synthesis. LUCH can provide access to the selected browser, files and other connected resources. The exact tools available depend on the account and host. The result should show what was read, what was inferred and what remains open.

This is a designed workflow based on the plugin's 12 skills, not a customer testimonial or a claim that this exact scenario has been independently run on every Claude account.
