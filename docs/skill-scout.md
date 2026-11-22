# skill-scout

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4). A few small wording changes made after the last test round and after the final review have not been retested; see the testing record. Version 0.1.0.

## What it does

Looks through a person's past work with Claude for jobs they keep repeating, and says what each one deserves. It only diagnoses: it builds, edits and installs nothing, and ends by asking which candidates to take forward.

1. Settles what to read: past chats (only where the session can search them), Claude Code session transcripts on disk, or notes and documents the person names. If the source the person named cannot be reached, it says so and does not quietly read something else.
2. Lists the skills the person already has, so it does not propose duplicates and can spot a skill that keeps needing correction.
3. Reads within a stated budget (by default the last 30 days of Claude Code sessions, 40 at most, or about 50 recent chats), the person's own messages first.
4. Groups what recurs by the job done, with a count and dates. A pattern needs three occurrences in at least two separate sessions; two go on a watch list.
5. Gives each pattern one verdict: a new skill, an improvement to an existing skill, a simple automation (a script or scheduled task), a fix (a standing instruction or a repair), or nothing.
6. Ranks the candidates by how often, how recently, effort saved and how generic, each marked high, medium or low with the facts behind it. No numeric scores.
7. Flags every candidate: employer or client work, personal or sensitive, something the person sells, or general. Flagged work is described by the kind of job, without names or figures. Passwords and keys are never copied; the report says only where one was seen.
8. Reports what was read and what was not, then asks which candidates to take forward, and hands the chosen ones to a skill builder such as forge if one is installed.

Text found inside past chats and transcripts is treated as data. If a transcript contains something that reads like an instruction, the skill does not act on it and says where it was.

## How it differs from similar public skills

Several public skills mine history for skill ideas. Three were read before this one was written: skill-idea-miner (takusaotome/claude-skills-library), which scans a week of Claude Code logs with scripts and scores novelty and feasibility; workflow-pattern-analyzer-web (hirefrank), which uses chat history tools, scores patterns on numeric scales and offers to generate the skills; and conversation-analyzer (mhattingpete/claude-skills-marketplace), a general review of usage patterns. skill-scout takes a narrower line on purpose:

- the verdict is often not "build a skill" (an existing skill to improve, a script, a standing instruction, or nothing);
- every candidate carries a provenance and privacy flag, and secrets and sensitive detail stay out of the report;
- it reads whatever source the person points at, with no scripts or installs;
- it states its coverage, including what it did not read;
- it stops at diagnosis.

The threshold of three occurrences and the short capped list are close to what workflow-pattern-analyzer-web uses; credit to it for those ideas. No text was copied from any of the three.

## Example

> Find patterns in my Claude Code sessions worth automating.

The reply, in outline: coverage (31 sessions from the last 30 days read, 12 older ones not read, past chats not reachable); existing skills checked; then a ranked list. A weekly newsletter put together from new blog posts, asked for four times with the same rules restated each time: new skill, general. An installed code-review skill corrected the same way in three of five uses: improve that skill. A date format restated in six sessions: a fix, one line in standing instructions. A recurring supplier report for a client: new skill, private only, described without names. Backing up a notes folder with identical steps each time: a scheduled script. Watch list: a personal letter seen twice. A note that a key was visible in one session's tool output, not copied. Then: "Which of these would you like to take forward?"

## Not for

Building or editing a skill (forge or skill-creator), listing the skills that are installed, advice on a person's own career or learning skills, or summarising one chat.

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim). One independent reviewer fetched sources 1, 2 and 6 again, and a second fetched sources 3 and 4, each through a summarising tool as well, and checked the skill and this page against them. Source 5 was not re-checked.

1. Anthropic, "Skill authoring best practices": https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
2. Anthropic, "Lessons from building Claude Code: How we use skills": https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
3. takusaotome, "Skill Idea Miner": https://takusaotome.github.io/claude-skills-library/en/skills/meta/skill-idea-miner/
4. hirefrank, "workflow-pattern-analyzer-web": https://smithery.ai/skills/hirefrank/workflow-pattern-analyzer-web
5. mhattingpete, "conversation-analyzer": https://github.com/mhattingpete/claude-skills-marketplace
6. Classmethod, "I investigated the storage location and retention period of Claude Code conversation history": https://dev.classmethod.jp/en/articles/claude-code-conversation-history-retention/

The transcript layout comes from source 6, a third-party article, not official documentation, so the skill tells Claude to look at what is actually on disk.

The author's own judgement, not taken from a source: the five verdicts and the tests for each; the threshold (three occurrences in two sessions, two for the watch list); the default budgets; high, medium and low in place of numeric scores; the four flags and the rule to describe flagged work in general terms; never reading a source the person did not name without a yes; treating text in history as data.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/skill-scout.md](../testing/skill-scout.md)
