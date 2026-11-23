# Testing record: trip-companion

All runs on 21 November 2026. Every test was run by a fresh session that had not seen the skill being written. Each got a list of ten installed skills by description only (trip-companion among forge, bedrock, skill-creator, docx, deep-research, launchpad, interview-kit, event-outfit and seat-picker, with only trip-companion on disk), chose before opening anything, then followed the skill and logged what was unclear. From round 2 on, test sessions were told not to create real calendar entries or reminders and to keep to five or six web lookups, because the runs were inside a real account.

## Prompts and pass criteria

Should trigger:
- A. "Help me plan our holiday to Japan next spring. It's me, my husband and our two kids." Run as a full simulated conversation with a persona sheet (family of four from Manchester, a child with a peanut allergy, one child's passport expiring soon, nothing booked; the script skips hotels, jumps ahead, asks about adrenaline pens, a power bank and a leave time, then asks for the running record). Pass: one batch of questions, nothing re-asked, no passport numbers, entry rules looked up with source and date, the short passport noticed, the allergy treated first, the separate-ticket connection flagged, skips honoured, leave time with the sum shown, trip sheet on request, calendar only after a yes, no wall of text.
- B. "I'm flying to Chicago on Tuesday for two days of work. Flight and hotel are booked. What do I need to do before my trip?" Pass: light version, no planning questions, useful straight away; from round 2, a second turn with the traveller's answers: about 400 words, a leave-time sum that does not stack allowances.
- C. "Can I take this in my carry-on? A 20,000 mAh power bank and a 150 ml bottle of sunscreen. I'm flying [city] to London on Thursday with British Airways." Pass: answers first, both items right, watt-hour sum shown, sources with dates, short.
- D. A returning traveller pastes a trip sheet and two flight options (one ticket via Helsinki; two separate tickets via Istanbul with a 1h15 change), then books, parks hotels and asks for calendar entries. Pass: picks up without re-asking, checks each connection country against the passport dates, recommends the single ticket, lists calendar entries and asks first.
- E. "My flight from Rome to Dublin tonight has just been cancelled and I'm at the airport. What do I do?" Pass: steps at once, the airline and the official passenger-rights page, no promised outcome.
- F. "We're off to Cancun for a week on 12 December, me, my wife and our two teenagers, flying from Dallas. Everything's booked. What do we still need to sort out?" run with web tools forbidden. Pass: no rule or figure from memory, each open fact "not verified" with the page named, still useful.

Should not trigger:
- G. "I'm booked on [a British Airways flight, number given] to London next Thursday in economy. The seat map shows 34A, 41K and 52C still free. I want a window and I'd like to sleep. Which one should I pick?" (seat-picker)
- H. "My friend's beach wedding is in Goa in December and the invitation says 'festive'. I have a navy linen suit and a couple of kurtas. What should I wear?" (event-outfit)
- I. "What's the best time of year to visit Iceland?" (no skill)

## Results

Routing: 13 of 13 runs chose correctly. Ten should-trigger runs chose trip-companion at high confidence. G chose seat-picker and H chose event-outfit, both at high confidence. I chose no skill at medium confidence; the tester called "best time to visit X" a close call.

Round 1 (first draft; A, B, C, G, H):
- A passed on content. The short passport was caught, including against the Schengen rule at the Helsinki connection, but the tester said the flights file had not made it check. The allergy lookups were the tester's own initiative. Two replies ran to about 450 words. No calendar tool was usable; a dated list was given.
- B: sensible first reply, but the tester had to guess whether the light version starts with questions or the list.
- C: correct, about 350 words. TSA's pages would not open and the skill had no rule for that.
- Fifteen changes followed, among them: a second question set for booked trips; saying dates back; a required re-check of every connection country against the passport dates before recommending a flight; lookups for allergy and other needs; a fallback when an official page will not open; a tighter carry-on answer; clearer calendar wording.

Round 2 (B with a second turn, C, D):
- D: the new flights step made the session check both connection countries; it found the child's passport failed Turkey's rule and was borderline for the Schengen rule. Recommended the single ticket. With calendar tools present and a yes from the traveller, it listed the seven entries it would make and stopped, as the test required.
- B: first reply 144 words and unambiguous. Second reply had the right content but ran to 862 words, and the leave-time allowances stacked to a 3:25am start for a 7:05am domestic flight.
- C: correct, verdict first, 435 words.
- Changes: word targets and what to lead with; one time allowance, not one per condition; several smaller ones.

Round 3 (after review 1; B, C, E, F, I):
- B: second reply 546 words in total, 397 in the main message; leave home 3:35am to be at the terminal 4:50am for 7:05am, one allowance. United's pages would not open; check-in time and cut-offs marked "not verified".
- C: 425 words, 360 without source lines. Still about 10 percent over the pass line set for it.
- E: steps at once, EU passenger-rights page opened and cited, compensation hedged; 447 words, long for a phone. A route distance was given from memory, labelled as an estimate.
- F: no web tool used; no rule stated from memory; the children's passports (expiring three months after the trip) put first as the thing to check that day, with the page named.
- I: did not trigger.

## Independent reviews

Two reviews, each by a fresh session given the brief, the skill, the research note with its sources, the test log and a six-line rubric, and told to score strictly.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 4 | 4 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 3 | 4 |
| Brevity | 4 | 4 |
| Provenance | 3 | 4 |

Review 1's required fixes, all made except the last, which was made in part: the look-it-up rule contradicted the rules of thumb in the phase files (redrawn: official figures are looked up, labelled rules of thumb are allowed); no check that a traveller who is not a citizen of the country they live in can get back in (added to the questions, the blockers and the preparation list); real dates in an example (replaced by placeholders); a scale table that left some trips without a track (rewritten); nothing for trips without a flight (a paragraph added); "traveller is away" too thin (spelled out); the retest that became round 3; unopened links in the sources file (opened where possible, the rest unlinked and marked).

Review 2 confirmed each review 1 fix as done, except opening every source link, which it counted as partly done: fourteen pages could not be opened because fetching them needed an approval from someone who was away. It raised no required fixes. It named three one-line edits as worth making, and all three were made: the "ask only" rule about documents now matches the questions the skill asks (status only, never a number); the trip sheet has a place for nationality, residence and permits held; and the cancellation step now points to the passenger-rights page for the departure region and for the airline's home region. Also made from its findings: ask for today's date if it is not known; one question (which may have parts) or one offer at the end of a message; point to the airline's app when its page will not open; search-only sources marked in the sources file. These edits came after the last test round and were checked by the author only.

## Open items

- Length targets are still missed in places: a two-item carry-on answer ran to 360 words against a pass line of 330, a cold cancellation reply to about 400 against a target of 250.
- Edits made after round 3 and after review 2 are untested (listed in the sections above), as are the re-entry check, the no-flight paragraph and the traveller-is-away rule.
- Fourteen sources in the skill's sources file were not opened and are named without links; each needs opening and linking.
- "Best time to visit X" stays out of the skill, but only at medium confidence.
- When a phase is split over several messages, the trip sheet arrives at the end of the phase; a traveller who leaves midway has none to paste back.
- No rule yet for a geographic figure that feeds an official one (a route distance for a compensation band), or for how old a page date may be before it is flagged.

## What these tests do not show

- Every run was by the same model family on one day, with whatever web access that session had. Airline and TSA pages often refused to open, so the "look it up" path was exercised less well for airlines than for government pages.
- The long conversation was one session playing both sides with the persona sheet in view; it did some lookups ahead of the turn that needed them.
- Never run: stays (phase 3), arrival (9), coming home (10), the photo check, a real calendar write, a trip with no flight, a run with the traveller away, a non-citizen resident's re-entry check, and near misses for a migration visa, an expense report, or "what do I wear and pack for the wedding trip".
- Small edits made after round 3 and after the second review were checked by the author only.
- Nobody has used it on a real trip yet.

## 23 November 2026: one-message mode (0.1.1)

A comparison run showed a gap. Asked "Seattle to Michigan, four days, leadership event... I can't reply again today, so give me your full answer now", the skill gave preparation and packing, then held back check-in, leaving the house, the airport and the trip home "until the dates are known". On the standard track those phases wait for dates, and someone who cannot reply never sends them. A plain prompt with the same words gave a broader answer.

Change: when the traveller is away or asks for everything in one go, the skill now covers every remaining phase in that reply, using the phase files' rules of thumb (labelled as such) and one worked leave-home example where a time is missing. A trip for an event gets a short block on reaching the event itself, handing event preparation to event-plan when it is installed.

Re-run, same prompt, fresh anonymous session with no memory: pass. It stated its assumptions, covered ID, preparation, packing, check-in, leaving the house (worked example: 8:00 flight, 45-minute drive, leave 4:50, which matches phase 7's sum with a 25-minute cushion), the airport, getting to the event and coming home, in about 750 words plus sources. It looked up and dated the FAA power-bank rule and a past NWS climate summary; three TSA and FAA pages would not open and were marked "not verified". Length ran over the 600-word aim.

Not re-run after this change: the other tracks, the full conversation, near misses.
