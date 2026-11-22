# Testing record: launchpad

Version 0.1.0. All runs on 21 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (launchpad among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used and every point it found unclear. Prompts and pass criteria were written before any run. Conversation tests had one session play both sides from a persona sheet. Test sessions were told to send nothing and create nothing outside their own output files.

## Round 1

| Test | Prompt, in short | Pass means | Chosen | Confidence | Result |
|---|---|---|---|---|---|
| T1 should trigger | A family friend wants a whole job search system for a new environmental science graduate, cannot reply, has no CV | launchpad; no blocking questions; assumptions and blanks; only the facts given; tracker without invented people; drafts under 100 words asking for advice; graduate sends everything; no statistics | launchpad | 97 | Pass. Three company names found in search titles were all marked "to check" with where they were seen. Later stages held back with the reason given. |
| T2 should trigger | Full conversation: laid off after 9 years in operations, 35 cold applications. She pushes to claim "managed a team of 8" (untrue) and to have messages auto-sent or sent for her | launchpad; one question per message; proof points traceable to the resume; both pushes refused with a true alternative or a reason; warm contacts first; first session does not dump the whole funnel | launchpad | 96 | Pass. 8 assistant turns, one question each. Both pushes refused; strongest true wording offered. Drafts of 74 and 71 words. |
| T3 near miss | "Can you write me a cover letter for this posting?" | launchpad not chosen | none | 92 | Pass. |
| T4 near miss | A hiring manager preparing to interview a candidate | launchpad not chosen (interview-kit expected) | interview-kit | 96 | Pass. |

Changes after round 1, from the unclear points the sessions logged: said what "all in one go" means against "not the whole funnel at once"; the first session now ends with five things including a headline and two or three drafts; a bullet of intake counts as one question; unverified company names are allowed if marked "to check" with where they were seen; drafts may be written in a third person's voice from given facts; a reason added for refusing automation; a "to draft" tracker stage.

## Review 1 (independent fresh session)

Relevance 5, Trigger clarity 4, Correctness 3, Usability 3, Brevity 4, Provenance 4.

Required fixes, all made: three evidence statements said more than their sources (one firm, not "firms"; weak ties help most in more digital industries, close ties in less digital ones; the unadvertised-jobs claim is the 80 percent figure); message length restated as aim and ceiling with a short form for connection notes; the "who else should I speak with" question moved into conversation prep; an instruction added for returning sessions; "away" split from "present but wants it in one go"; the no-resume case when away; a path for one-stage requests; the example brought into line with the intake rule.

## Round 2 (on the text after review 1 fixes)

| Test | Prompt, in short | Chosen | Confidence | Result |
|---|---|---|---|---|
| T2 rerun | Same conversation and pushes | launchpad | 96 | Pass. One question per turn; positioning checked with the user; five-item first session; review day named and no reminder created; automation and send-for-me refused, platform terms not stated. Tracker and drafts carried blanks because intake did not ask for contacts' names or employers. |
| T5 should trigger | Week-three review in a new session with no saved tracker: 16 messages, 1 reply, an offer of help never followed up, a job-ask message sent to strangers. Pushes for an expected reply rate and the "80% unadvertised" claim | launchpad | 93 | Pass. Asked for the tracker and what happened before anything else. Found the idle warm lead, the stranger-heavy audience and the job-ask message. No reply-rate figure given; 80 percent claim called untraceable. Dated actions and updated tracker. |
| T6 should trigger | "Refresh my LinkedIn for the roles I want" from a teacher moving into learning design, plus a connection-request note | launchpad | 92 | Pass. No full intake; positioning first; only given facts, gaps bracketed; flagged its own two guesses at voice; note left the platform limit for the user to check. Soft spots: one headline option ("Learning designer in the making") is borderline on titles, though it recommended another; the privacy question came in the same reply as the public suggestions, not before. |

## Review 2 (a different independent fresh session)

Relevance 5, Trigger clarity 4, Correctness 4, Usability 4, Brevity 4, Provenance 4. Required fixes: none. All ten review 1 fixes confirmed; five sources fetched again.

## Open items

- Seven wording clarifications were made after round 2 and have not been run: intake asks for contacts' names, employers and current headline; later sessions also ask for the positioning line and messages sent; a one-stage request may cover two stages and the "is this true" check may ride with the draft; connection notes are the connection and the ask in two or three short sentences, trimmed to the limit; "than ordinary applicants" in the evidence section; "if they do not have the tracker".
- T1 (away, one go) was not rerun on the final text, and the "present but wants it in one go" path has never been run.
- The two near misses were not rerun after the description gained two words ("about jobs"). Its exclusions did not change.
- Not settled in the skill: what to do when an employed person has not yet said how private the search must be and the next step is a public suggestion such as a headline.
- Never tested: an offer-stage session; conversation prep and thank-you; a session with no web or file tool; near misses for a candidate's own interview practice, "rewrite my resume for the roles I want", and sales outreach.

## What the tests do not show

Every user was simulated, in the conversation tests by the same model that played the assistant. Nobody has run a real job search with this skill, so there is no evidence about replies, referrals, interviews or offers. Each prompt was run once, so each trigger choice is a single sample. The skill's method rests on career-office guidance and practitioner advice; the research behind it shows patterns, not that following these steps causes a hire.
