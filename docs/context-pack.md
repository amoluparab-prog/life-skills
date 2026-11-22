# context-pack

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Wording changes made after the second test round and after each review have not been retested, and several paths have never been run; see the testing record. Version 0.1.0.

## What it does

Gathers everything a person has said about one existing project, across past chats (where the session can search them), files, notes and pasted text, into one pack for whoever builds next: a developer or a coding agent. It reads only; it builds nothing.

The pack holds, in order:

1. What is being built and for whom, in one paragraph, from decided items and stated facts only.
2. A short note for the builder: decided items are the brief; suggested and open items are not instructions.
3. Specifications in the person's own words, each with its source and date.
4. A decision log. Every entry has a status: **Decided** (the person said it or accepted it in words), **Suggested, not confirmed** (an assistant or someone else proposed it), **Changed** (the person clearly replaced it; the old entry is kept and linked), or **Open**.
5. Conflicts, side by side. A later statement wins only when it clearly replaces the earlier one; when a date is missing the order is given as unknown.
6. Open questions for the person, including a fixed list of things a builder needs that nobody stated. Gaps stay gaps: no defaults are supplied.
7. Sources read, and what was not read or could not be reached.
8. Sharing flags: an employer's or client's material, other people's details, confidential items. Other people are referred to by role, and passwords and keys are never copied.
9. A check of the decision log against the sources, by a fresh session where one can be started, otherwise labelled a self-check.

An assistant's recap headed "what we decided" is treated as the assistant's words. Text inside the sources that reads like an instruction is treated as data and reported, not obeyed. With no chat search, it works from what is pasted and says so; with nothing to read, it asks for the material and stops.

## How it differs from similar public skills

Four were looked at before writing (listing pages only, through a summarising fetch tool): recall-conversations (gupsammy/claudest), which searches past Claude Code sessions with scripts and has a lens for extracting decisions; context-extract (yousufjoyian/claude-skills), which appends the current conversation to a running project history; project-kickoff (magi12345), which starts a new project with decision and progress files; and brief (davepoon/buildwithclaude), a session briefing from a status file and a memory service. context-pack takes a narrower line: it looks backwards across several kinds of source for one project, records who said each thing and when, keeps an assistant's suggestions apart from the person's decisions, shows conflicts instead of resolving them, states what it did not read, and checks itself against the sources. No text was copied from any of them.

## Example

> Pull together everything we discussed about the Plant Swap app before I brief a developer. Here are two chats and my notes.

The reply, in outline: a paragraph on what the app is and who it is for, noting that its reach is not settled; the person's own words as specifications ("No payments, ever. It's swaps only."); a decision log where swaps-only is Decided, sign-in by phone number is Suggested and not confirmed (the assistant's idea; the person moved on), web-first is Changed to Android-first ("scrap the web version, Android first"), and chat between neighbours is Open; one conflict, a 2 km radius in a dated chat against "whole city" in undated notes, order unknown; open questions (radius, sign-in, and deadline and budget not stated anywhere); sources read and not reachable; a flag that the notes name a neighbour and her address; and a self-check that corrected one entry.

## Not for

Summarising one chat or one document; writing a spec for a brand-new idea with no history; handing over something already built so someone can run it (handover-pack); finding repeated tasks to turn into skills (skill-scout); writing the code.

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim). Two independent reviewers fetched sources 1 to 5 again between them, the same way, and found the notes supported after two corrections.

1. Martin Fowler, "Architecture Decision Record": https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html (statuses; a changed decision is superseded and linked, not erased; keep records short)
2. Wikipedia, "Requirements traceability": https://en.wikipedia.org/wiki/Requirements_traceability (trace each requirement back to who wanted it)
3. Wikipedia, "Requirements elicitation": https://en.wikipedia.org/wiki/Requirements_elicitation (people leave out the obvious, conflict and change their minds; asking never yields everything)
4. Philipp Schmid, "Writing a good AGENTS.md": https://www.philschmid.de/writing-good-agents (context for a coding agent: short, what and why first, pointers over copies)
5. Chatlatanagulchai and others, "Agent READMEs: An Empirical Study of Context Files for Agentic Coding", arXiv 2511.12884: https://arxiv.org/html/2511.12884v1 (context files are long, hard to read and grow by addition; only the first part of the page was read)
6. The four skills named above: https://skills.sh/gupsammy/claudest/recall-conversations , https://skills.sh/yousufjoyian/claude-skills/context-extract , https://github.com/magi12345/project-kickoff , https://www.skills.sh/davepoon/buildwithclaude/brief

Two further pages could not be fetched and were not relied on: Anthropic's "Effective context engineering for AI agents" and the GitHub blog post on spec-driven development.

The author's own judgement, not taken from a source: the four statuses and the tests for each, including that silence is not acceptance; when a later statement counts as replacing an earlier one; exact quotes for the person and 25 words at most for anyone else; the gap checklist (informed by sources 3 and 5); the sharing flags; the sampling rule for the check and the "self-check" label; the reading budget; treating text in sources as data.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/context-pack.md](../testing/context-pack.md)
