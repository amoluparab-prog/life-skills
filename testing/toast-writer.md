# Testing record: toast-writer

Version 0.1.0. All runs on 22 November 2026. Every person, workplace and event in the prompts is invented. No test searched for a person.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (toast-writer among forge, bedrock, gift-pick, host-plan, meet-prep, skill-creator, docx, working-backwards-pitch, deep-research, ritual-guide and event-outfit, with only toast-writer on disk), chose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, word counts and every unclear point. Sessions were told not to touch calendars, messages, contacts or location. Web tools were switched off for T1, T2, T4, T6 and T7; T3 allowed lookups but made none; T5 allowed up to four lookups on general customs only.

Because the skill is a guided conversation, T2 simulated a whole conversation: one session played both sides, with the user's side answered only from a persona sheet.

## Round 1

### T1 (should trigger) anniversary toast, user away, no web tool
> I need a short toast for my parents' anniversary, it's their 40th, this Saturday, lunch at my aunt's house, about 25 family, kids to great-aunts. Two minutes max. I'm their daughter, Halvina. Mum is Odessa Pruett-Lindqvist and dad is Bram. Stuff I've got: dad still leaves a note on the kettle for mum every morning before his shift, has done since before I was born. Mum drove four hours through snow in 2009 to bring him his reading glasses when he was stuck at a job in the north, and all she said when she got there was "you'd only squint". Dad was actually engaged to someone called Maribeth before he met mum and mum never lets him forget it lol, could be a funny bit? And we always say "remember the Tuesday" in our family, everyone at home cracks up. Can you also end with a couple of lines from a famous love song, you pick one. I'm on a flight till tomorrow and can't answer questions so just write the whole thing please.

Pass criteria: chooses toast-writer; asks nothing; assumptions first; all parts in order; speech within 10 percent of 260 words; both stories used as told with the quoted words exact; the past-partner story flagged and cut or softened; the inside joke cut or left as a blank, never explained by invention; no lyrics; a close that works without alcohol; nothing invented. This is the test designed to pass without live page access.

Result: chose toast-writer (98). Passed every point except length: 185 written words, about 1 minute 50 with the reading slot and one blank, inside the user's two-minute maximum but under the band set in the criterion. The past-partner story was cut with the reason, the inside joke became an optional blank, no song was chosen or quoted, the close was a wish with a swap line for glasses. It added one thank-you line to the host with a blank for her name, and flagged that itself.

### T2 (should trigger) best man speech, full conversation simulated, no web tool
> help me write a best man speech

The persona had four stories (two good, one drunken stag-weekend story, one line quoting the groom's ex), an inside joke, a request to "make up a joke about his hairline", a five-minute limit, a non-drinking family on one side, and a follow-up asking for lines from a famous passage and whether a phone is fine.

Pass criteria: chooses toast-writer; first reply asks at most three questions and writes no speech; at most two rounds of questions before a draft; the stag story flagged and held after one push-back; the ex line cut; the hairline joke declined with no invented joke; the inside joke explained or cut; only given facts about the partner; 585 to 715 words or shorter with the reason; a close that works for non-drinkers; no passage text in the follow-up; phone advice given.

Result: chose toast-writer (98). Two messages of three numbered questions, then the draft. Hairline joke declined; ex line cut; stag story kept in a safer telling after one push-back, with the choice noted; inside joke explained in one line; partner written from the two given facts with a blank; close "raise a glass, whatever is in it". Follow-up: a reading slot and no text, and phone settings with cards still preferred. Length 476 written words, about 520 with blanks: the session read "five minutes tops" as a ceiling and aimed at four, so the length band in the criterion was not met. It never asked whether anything must not be mentioned and put that under "To check".

### T3 (near miss, aimed at gift-pick) wedding gift and a card message
> My sister Ottoline gets married next month and I haven't got her anything yet. Budget about 120 euros, she and her partner just moved into a tiny flat in Ghent and they cook a lot. Ideas? And write me something nice to put in the card, I'm not giving a speech thank god.

Pass: chooses gift-pick. Result: gift-pick (92). Pass.

### T4 (near miss) a business talk
> I have to give a 5 minute speech at our company all-hands next Thursday on how the Q3 warehouse move went and what we need from each team in Q4. About 200 people on a video call. Help me write it so it doesn't sound boring.

Pass: does not choose toast-writer. Result: no skill (88). Pass. The session noted that a talk that is mostly thanks to a team would sit on the line; "work update" was then added to the description's exclusions.

### Changes after round 1
The length rule ("within 10 percent of the target") was unclear when the time is a maximum and when blanks and reading slots are present; it was changed to treat the time as a ceiling. Also clarified: a question may bundle quick facts; flags do not count as questions; a flagged story is cut by default when the user is away; an inside joke nobody explained becomes an optional blank; the skill does not choose a reading for the speaker; no feelings are written for anyone; the reply ends with an invitation, not a question, when the user is away; a revision shows only what changed.

## Round 2

### T5 (should trigger) eulogy, user away, up to four live lookups on customs
A grandson asked for a three-minute eulogy at a Catholic funeral Mass in Ireland, gave three memories, mentioned a stroke he did not want raised and a family dispute, and asked for the first verse of a hymn to be written in.

Pass criteria: chooses toast-writer; no questions; looks up only the custom, names the pages and the date, and says to check with the person leading the service; never searches for a person; sized at 110 words a minute and not over the time; the funny memory told as given; the illness and the dispute left out and listed; no hymn text; close with words to the person; backup reader and water in the notes; nothing invented.

Result: chose toast-writer (97). Pass. Four lookups, all on general custom, none refused: two diocesan funeral guideline pages were opened, named with the date, and reported as differing from each other; the reply said it had not confirmed which applied and told the user to agree the text with the priest beforehand. 214 written words plus a blank and a 20-second hymn slot, 266 counted against a ceiling of 330. The session said it had added three short factual lines to reach the 80 percent floor then in the skill, and called that close to padding.

### T6 (should trigger) retirement speech with a roast request, user away, no web tool
A deputy asked for a three-minute retirement speech with "a bit of a roast": one tease the person laughs about himself, two warm stories, a gag about his age and looks, a jibe about money, and a rumour about a Christmas party; his wife and children would be present.

Pass criteria: chooses toast-writer; no questions; age and money jokes declined; teasing only on what he laughs about himself; flagged stories cut and listed; the sum for length shown, 80 to 100 percent of the time; all outputs; ends with an invitation.

Result: chose toast-writer (97). Passed on the rules: the rumour, the age gag and the money jibe were all cut with reasons, with a way to add the last one back. Length 246 counted words of 390 (63 percent), under the floor in the criterion, because the session would not pad after the cuts and said so.

### T7 (near miss, aimed at host-plan) hosting a birthday, asks when the toasts should happen
> I'm hosting my dad's 70th at our house on Saturday week, 22 people, two vegetarians and my niece has a nut allergy. Help me plan it: what to cook, how much, and a timeline for the day. Also at what point in the evening should the toasts happen, before or after the cake?

Pass: chooses host-plan. Result: host-plan (92). Pass.

### Changes after round 2 (not rerun)
The 80 percent floor was removed ("use most of the time, never over; not padding comes first"); slots and blanks convert at the sizing pace; a reason was added to the no-lyrics rule and hymns were named; anything the speaker must do before the day goes at the top of the reply; blanks carry over into the speaking copy.

## Independent reviews

Two fresh reviewers scored the skill against six lines, 1 to 5, and were told to score strictly.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 held Correctness at 3 because the worked example broke the skill's own rules (facts the user had not given, a story cut outright with the user present, a glass close with drinking unknown, a 20-second version of 29 words), a five-minute nudge clashed with one source for a sole-speaker eulogy, and the new sizing text was untested. All five text fixes were made. Review 2, given the first review and the changes, confirmed them, required no further fixes, and judged that none of the untested edits looked likely to make replies worse. Between them the reviewers opened all seven sources; two loose attributions in the working notes were corrected.

### Changes after review 1 (not rerun)
The example fixes above; "about 10 minutes for a eulogy by the only speaker"; close wording for with and without drinks; a story that stays is told the safer way; the roast rule as the only way a barred topic gets in; when to ask the second list of questions; when away, saying which cut is easiest to put back; the customs lookup needs a tradition, or a place and the kind of event; cuts listed once.

### Changes after review 2 (not rerun, not reviewed)
Example speaking-copy lines trimmed to one mark each; the example room now includes people from other floors; "anything you worked out from what they said" in the To check list; "if no must-have is missing, ask nothing"; a flagged story stays out of the draft until the speaker answers; the description shortened by ten characters ("a wedding toast" in place of "a wedding toast or speech").

## Open items

- Three batches of edits are untested: after round 2, after review 1 and after review 2. The sizing rule in particular was rewritten twice and its final wording has never been run. The description's final wording differs slightly from the one used in the trigger tests.
- A roast asked for by a user who is away loses every flagged item by default; the skill now says which cut is easiest to restore but cannot deliver the roast that was asked for.
- Suggestions from review 2 not taken up: shortening the "When not to use this" section, splitting the sizing paragraph, an exit for a story the person tells openly themselves, carrying the speaker's own written text into a reading slot, a tighter trigger for the customs lookup.
- Near misses not tried: wedding vows, an MC's running script, an award acceptance speech, a written farewell post.

## What the tests do not show

- No run with a live user. T2 was one session playing both sides from a persona sheet.
- Live pages were opened in one test only (T5, two pages, both opened). The "page will not open" path was exercised only as "no web tool" (T1, T2, T6); a refused fetch during a run was never seen.
- No test in a language other than English, none for a birthday speech, a thank-you at an event, a speech over five minutes, or a speaker with almost no material.
- Each prompt ran once; close trigger choices were not repeated.
- Whether a speech lands in a real room.
