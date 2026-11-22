# Testing record: event-outfit

Version 0.1.0. All runs on 21 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (event-outfit among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used and every point it found unclear. Prompts and pass criteria were written before any run. Two rounds were run; the text that ships is the text round 2 tested.

## Prompts and pass criteria

### T1 (should trigger) dress code question, short
Prompt: "The invite to my cousin's wedding says 'cocktail attire'. What does that mean for me? It's in Austin on Saturday 5 December 2026, 5pm, at a ranch venue."
Pass: chooses event-outfit; explains cocktail attire in the first reply; asks the missing inputs in ONE short batch (no repeat of city, date, dress code); does not state Austin weather from memory (date is 14 days out: typical conditions labelled as typical or a looked-up source, plus a recheck); no gender assumed; mentions ground or shoes for a ranch; no comment on body.

### T2 (should trigger) multi-day, user away, one go
Prompt: "I can't reply after this, so give me the whole thing in one go. Three-day work event in [city], [three dates in early December], I'm an attendee and I present for 20 minutes on day 2. Agenda says 'business casual; dinner on day 2 is smart casual; day 3 afternoon is an outdoor team activity (easy walk)'. Hotel conference rooms, dinner at a restaurant downtown. I own: charcoal trousers, navy chinos, dark jeans, grey blazer, navy merino sweater, 3 oxford shirts (white, blue, pink stripe), 2 polos, black leather sneakers, brown derby shoes, a puffer jacket, a wool overcoat. I run warm indoors. Carry-on only. Not buying anything."
Pass: chooses event-outfit; asks no questions; assumptions listed; outfit per occasion (3 days, dinner, presentation, walk) from listed pieces only; weather looked up with source and date, or clearly flagged as not looked up; presenter adjustments; packing list with counts and reuse; care notes; backup; timeline as a plain checklist (no reminder tool claimed); no purchases suggested.

### T3 (should trigger) full conversation, both sides simulated
Persona sheet given to the session: guest at a friend's two-day Indian wedding in New Jersey, vague dress code ("Indian festive or formal"), wears a hijab, limited wardrobe, budget 80 dollars, dislikes heels, sends a "photo description" of wardrobe, answers briefly, gets impatient if asked more than one round of questions.
Pass: chooses event-outfit; one batch of questions then a plan (no second interrogation); cultural guidance labelled as commonly said and "check with the host or family"; hijab treated as fixed without questions or judgement; no body comments; flats respected; gaps with borrow or rent before buy and within 80 dollars; weather not from memory; reminders offered only if tools exist, else checklist; conversation ends within about 4 assistant turns.

### T4 (near miss, trip-companion)
Prompt: "Plan my 10-day trip to Japan in March end to end: flights from [city], where to stay, and a packing list."
Pass: does NOT choose event-outfit (trip-companion expected).

### T5 (near miss, one-item shopping)
Prompt: "I'm looking for a good navy blazer under $200. Any recommendations?"
Pass: does NOT choose event-outfit (no skill expected).

## Results

### Round 1 (run 21 November 2026, five fresh sessions)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 cocktail | event-outfit | 97 | Pass. Decoded in first reply, one batch of 4 questions (nothing re-asked), typical weather looked up and labelled with sources and a recheck date, no gender assumed (three routes), ranch shoes covered. Went further than needed: gave a prep timeline and reminder offer before knowing the wardrobe. |
| T2 offsite, one go | event-outfit | 92 | Pass. No questions, 8 tagged assumptions, outfit per occasion from listed pieces only, weather tool tried (reached only 28 Nov) then typical figures with source, presenter adjustments, packing list, care notes, backup, plain checklist, nothing to buy. Long. |
| T3 conversation | event-outfit | 95 | Pass. 3 assistant turns, 1 question round. Hijab treated as fixed, never questioned. Cultural colour advice labelled "commonly said", invitation put above guides, host message offered. Flats only. Gaps: none, but added an optional shawl (edges toward nice-to-have). No reminders (plain checklist). No body comments. |
| T4 Japan trip | trip-companion | 95 | Pass (event-outfit not chosen). |
| T5 navy blazer | none | 92 | Pass (event-outfit not chosen). |

Unclear points logged by the test sessions, and what changed in SKILL.md after round 1:
1. How much of the output belongs in a first reply before the wardrobe is known -> step 1 now says: decode, weather and venue effects first; hold outfits, gaps and timeline.
2. Typical-conditions case: hourly figures and "from memory" -> step 3 now says typical figures are looked up too, daily figures are enough, mix forecast and typical when the event straddles the horizon, units of the event's country.
3. "Avoid white, cream" versus a single cream piece or a head covering -> now "a look that is mostly white or cream"; one pale piece is fine; never applies to a religious head covering.
4. Invitation versus generic guides; culture-named codes versus the Festive row -> invitation outranks guides; culture-named codes are treated as ambiguous wording.
5. Religious garments: is picking a colour allowed -> yes, choosing among their own pieces is fine.
6. Away mode: reminders, question back, number of assumptions, unlisted small items -> plain checklist, no closing question, few assumptions, "check you have" line. Example no longer ends on a question.
7. Conflicting adjusters (5 p.m., ranch) -> keep the dressier reading, venue changes shoes and layers.
8. Grooming repeated per outfit -> once per plan. "Short" versus multi-day -> tight blocks, do not cut sections.
9. Timeline anchor -> first event day, or travel day.
10. Gaps: optional extras -> "none" means none, no nice-to-haves.
11. Travel mode and stay missing from intake -> added to question 5.
Not changed: colour and shade matching advice (out of scope, left to the model); T5's point about a shopping request that turns out to have an event behind it (the description already covers gaps for a named event).

Description unchanged after round 1, so T4 and T5 are not rerun.

## Round 2 (after review 1 fixes; text under test is the final SKILL.md)

Reruns T1 to T5 unchanged (the description changed by two phrases, so the near misses are rerun too). Extra pass points:
- T1: first reply stops at decode, weather, venue effects on shoes and layers, and the questions. No outfit blocks, gaps, timeline or reminder offer yet.
- T2: no closing question; short assumptions list; "check you have" line; plain checklist counted from the travel day, no reminder offer; one consistent care instruction for the blazer.
- T3: cream trousers and cream hijab handled per the new wording; gaps "none" with no optional extras; still one question round.

### T6 (should trigger; new) mixed forecast, no dress code, Celsius country, one go
Prompt: "One message only please, I'm about to board. I'm speaking at a developer conference in Toronto, Sat 28 to Mon 30 November 2026. My talk is Sunday 2pm, filmed. No dress code anywhere on the site. Speakers' dinner Saturday night at a brewery. I've got: black jeans, grey wool trousers, a navy unstructured blazer, a black crewneck sweater, white and black t-shirts, a light blue oxford shirt, a fine gingham check shirt, white leather sneakers, brown chelsea boots, a rain shell, a wool peacoat. Flying in Friday with a backpack only."
Pass: chooses event-outfit; no questions; missing dress code handled (most likely meaning stated, dressier reading with a removable piece, host or organiser check suggested without ending on a question); forecast used for the days it covers and typical figures, labelled, for the rest, in Celsius first; filmed talk keeps the gingham off stage; packing fits a backpack with reuse; timeline drops steps that have already passed.

### Round 2 results (run 21 November 2026, six fresh sessions, on the final SKILL.md)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 cocktail | event-outfit | 97 | Pass. First reply now stops at decode, typical weather (looked up, labelled, source, recheck date), ranch effects on shoes and layers, and four questions. No outfit blocks, gaps, timeline or reminder offer. Dressier reading kept for 5 p.m. on a ranch. |
| T2 offsite, one go | event-outfit | 93 | Pass. No questions and no closing question; five assumptions; outfits from listed pieces only; "check you have" line; checklist counted from the travel day; "No reminders have been set"; one consistent care instruction (shower steam, label decides); what could not be looked up is listed. |
| T3 conversation | event-outfit | 96 | Pass. 3 assistant turns, 1 question round. Hijab fixed and never questioned; cream hijab offered without caveat; cream trousers used as the one pale piece with a check-with-the-couple note; black kept to the party night and labelled as from guide lists; gaps "none", borrowing mentioned once as optional. Reminder offer skipped because the test forbade creating any (see limits). |
| T4 Japan trip | trip-companion | 96 | Pass (event-outfit not chosen). |
| T5 navy blazer | none | 92 | Pass (event-outfit not chosen). |
| T6 Toronto speaker, one go | event-outfit | 93 | Pass. No questions; missing dress code read as casual with a removable blazer for the talk and an optional one-line note to organisers; forecast for the days the tool reached and labelled typical figures for the rest, Celsius first; gingham kept off the filmed talk; backpack list with reuse (second shoes dropped); past timeline step dropped. |

Unclear points logged in round 2 and NOT fixed (the two-round test limit is used up, and the shipped text is the tested text). Carried as open items:
1. "Drop anything used only once if another piece can cover it" pulls against keeping a weather or spill backup and against the dressier reading; the skill does not say a backup role counts as a use. (T2, T3, T6)
2. Whether wardrobe-independent dated steps (cleaning deadline) belong in a first reply when the event is close. (T1)
3. The white and cream rule is written for Western weddings; at other weddings the commonly given reasons differ, and the skill does not say whether a commonly cited custom should demote an owned piece. (T3)
4. What stands in for rain chance and wind when only typical figures exist. (T2, T3, T6)
5. "Earlier date for a range" is written for reminders only, not the plain checklist. (T2, T6)
6. Two coats or "jacket" in "wear the bulkiest to travel". (T2, T6)

## What these tests do not show
- No real photo was used (T3 used a typed list described as a photo), so the photo privacy rule is untested.
- No session lacked a weather or web tool, so the paste-a-forecast branch is untested.
- No reminder was ever created; test sessions were told not to. The offer-then-create path is untested.
- Not tested: an interview, an invented dress code such as "mountain chic", an event tomorrow, a destination wedding with travel (the boundary with trip-companion on a mixed request).
- One run per prompt per round; trigger confidence was 92 to 97 but no repeat runs were made.
- The conversation test had one model playing both sides.
- Neighbour descriptions for the other collection skills were one-line placeholders, not their final text.

## Independent review

Two fresh reviewers, each given the brief, the skill, the research note with sources, the test log and a six-line rubric (1 to 5), and told to score strictly.

| Line | Review 1 | Review 2 (final) |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 required three fixes, all for Correctness: a care sentence that forbade steaming dry-clean-only items against the skill's own steam advice; wedding white and cream wording looser than the sources; no statement that the dress code meanings come from US and UK guides. All three were made, then round 2 was run on the result. Review 2 confirmed the fixes and required nothing further.

## Open items

From review 2 (optional points, not applied, because no test round was left and the shipped text was kept identical to the tested text):
1. Say that a weather or spill backup counts as a use in the "drop anything used only once" packing rule. The reviewer's top point.
2. Apply "the earlier date where a step gives a range" to the plain checklist as well as to reminders.
3. Say what stands in for rain chance and wind on days with only typical figures.
4. Scope the white rule to weddings where the bride traditionally wears white.
5. "Bulkiest shoes and coat" in place of "jacket".
6. Say that the timeline ends the full plan, not the first reply.
7. A request that mixes an event with full travel planning has not been tested against trip-companion.

Also open: the author has not yet walked through the skill against their own way of doing this job, and has not signed off the brief or the release.
