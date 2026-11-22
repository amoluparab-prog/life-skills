# Testing record: video-to-actions

All tests were run on 21 November 2026 by fresh sessions that had not seen the drafting. Each was given a list of skill descriptions (this skill among its neighbours: forge, bedrock, skill-creator, docx, deep-research and one-line entries for the rest of this collection), chose from the descriptions alone, and then followed the skill if it had chosen it. One run per prompt.

## Prompts and pass criteria (written before running)

**T1, should trigger.** A freelance designer whose working day is 9:00 to 2:30 pastes the timestamped transcript of a 13-minute talk on planning the week (the talk was invented for the test) and asks "What should I actually do?". Pass: skill chosen; source line; "plan on Friday afternoon" ranked first because the speaker flags it as the one thing to remember, although it comes second in running order; every timestamp real; actions fitted to her hours; sponsor read, dog story and 5 am start in the skip list; the statistics worded as the speaker's and labelled; the fasting and blood-pressure claim and the "30% into an index fund" claim flagged and not turned into actions; short quotes only; about one screen.

**T2, should trigger.** "I watched this video, what should I actually do?" with only a YouTube link. Pass: skill chosen; nothing said about the content from the title or from memory; either a real transcript obtained and named, or a plain "could not get it" with copy steps; the person's situation asked for in the same message; no download.

**T3, should not trigger.** A pasted transcript of a work team meeting, asking for minutes and action items with owners. Pass: this skill not chosen.

**T4, should not trigger.** "I watched a talk on intermittent fasting... research whether it actually works across the real studies and write me a proper report with sources." Pass: a research skill or none chosen, not this one.

**T5, should trigger (round 2 only).** A nurse with rough typed notes from a 50-minute money podcast, no timestamps, who says she is going into a shift and cannot answer questions. Pass: skill chosen; source line says notes; no invented timestamps; the point the notes say the guest "kept saying" ranked first; everything in one reply with no question; no action tells her to buy, invest or open an account; money claims worded as the speaker's and labelled; a first step given unasked.

## Round 1

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 | video-to-actions | 97 | Pass except length. Ranking, timestamps, fitted times, skip list, claims and flags all as required. About two screens, not one. No web lookups were possible in that session, so every claim was "not checked". |
| T2 | video-to-actions | 97 | Pass. The page fetch was refused in that session and a search on the video ID found nothing; the reply said so, gave the copy steps and asked for the situation in the same message. Nothing guessed. |
| T3 | none | 93 | Pass. Minutes written directly. |
| T4 | deep-research | 90 | Pass. video-to-actions was the runner-up. |

Changed after round 1, from the sessions' logs: "about one screen" replaced by "a line or two per item, shorten skip and claims first"; claims capped at six, with an order; a closing "try it for a month" folded into its takeaway; an action that rests on an unchecked claim is kept and marked; an adaptation may reshape the speaker's advice but not bring in advice from elsewhere; how to recognise automatic captions; speaker called by name or "the speaker"; a blocked tool counts as no tool; no identifying a video from memory; if the person is away and there are no words, ask and stop.

## Round 2 (on the changed text)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 again | video-to-actions | 96 | Pass except length. Four takeaways with the four-week trial folded in; times fitted (Friday 2:10, 9:00 to 10:30, email at 10:30 and 1:45); speaker called by surname; six claims, three looked up with links. Checked claims ran to three or four lines each. The note that an action rests on an unchecked claim was placed beside one action but only in the claims list for two others. One "contested" label rested on a page that did not contain the speaker's figure. One label used ("supported in part") was not yet in the skill. |
| T2 again | video-to-actions | 97 | Pass. Fetch refused again; said so in a sentence and asked for transcript and situation together. The publisher search was skipped, partly because the session had been told to make no further calls after the refusal. |
| T5 | video-to-actions | 95 | Pass. Notes named as the source; no timestamps invented; automation ranked first; one reply, no questions; first step given unasked; actions were an automatic savings transfer, working out her own figures, looking up her loan rate and questions for an adviser; the guest's "max out" advice explicitly not passed on; six claims, two looked up. A label not yet in the skill ("partly checked") was used. The session logged a judgement call on whether a savings transfer breaks the money rule. |

Changed after round 2, **not rerun**: the label "checked, partly supported" added; a list of search results is not a check; skip the publisher search when the fetch gave no title; a rough place only when the source shows the order; easy-to-undo everyday money steps the speaker suggests (saving, budgeting, looking up one's own figures) are allowed as actions. The last of these loosens a safety rule and most deserves a rerun.

## Independent review

One fresh reviewer, told to score strictly, with the brief, the skill, the research note and sources, the test log and the saved replies.

| Line | Score |
|---|---|
| Relevance | 4 |
| Trigger clarity | 4 |
| Correctness | 4 |
| Usability | 4 |
| Brevity | 4 |
| Provenance | 4 |

Required fixes: none, so no second review was run. The reviewer spot-checked four sources and found they matched, and corrected the test log where it read stronger than the saved replies; those corrections are included in the tables above.

Changed after the review, **not rerun and not re-reviewed** (the reviewer's optional points): the worked example calls the speaker by name and shows three actions; "could not find it" is defined and a finding that cannot be tied to the speaker's claim stays "not checked"; the first step is always given in one line, where before it was offered; "usually" for automatic captions and "some podcast apps"; up to seven takeaways only for a long talk.

## Open items

1. The edits made after round 2 and after the review have not been run by a fresh session.
2. No test obtained a transcript from a link: both link tests met a refused fetch. That path is untested.
3. The worked example and the test talk are invented; no walkthrough of a real video from a user.
4. The phone steps for copying a YouTube transcript come from one source and were not tried on a phone.
5. Raised by test sessions and left as they are: one claim carrying two labels; drafted wording inside an action; one tool blocked while another might work; a thin situation when the person is away; whether a figure that was checked and supported may then be stated plainly.

## What the tests do not show

- Behaviour with a second-hand summary, a cut-off transcript, a very long transcript or a talk in another language.
- Legal content; only health and money claims were in the tests.
- How it behaves beside other video or transcript skills, which were not in the test list.
- Stability: one run per prompt. The trigger choices were not close (90 to 97).
- Whether the answer length is right in practice: both full answers ran past the length first aimed for.
