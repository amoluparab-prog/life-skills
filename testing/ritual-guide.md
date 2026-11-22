# Testing record: ritual-guide

Version 0.1.0. All runs on 21 November 2026.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of 22 installed skill descriptions (ritual-guide among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used, every point it found unclear, and every fact it wrote without a source. Prompts and pass criteria were written before any run. Test sessions were told not to create calendar entries, reminders or messages and to keep web lookups to about six. Two rounds were run, which was the limit set for this build.

**Read this first.** The text that ships is not identical to the text round 2 tested: five wording edits were made after round 2, about a dozen after review 1 and eight one-line edits after review 2. None of those has been run in a test. And in both rounds the session that ran the written-guide prompt (T1) could not open web pages, so the skill's main path, a written guide with sourced labels and a looked-up local time, has never been produced in a test.

## Prompts and pass criteria

### T1 (should trigger) user away, one go
Prompt: "I'm out all day so please just leave me the full thing to read tonight. I'm hosting my first iftar at home in Manchester (UK) for 12 people on the first Saturday of Ramadan 2027. My family is Pakistani, Sunni. Four of the guests are colleagues who aren't Muslim, and my grandmother, who is 81, will be there. What do I need, how does the timing work, and what is the order of the evening?"
Pass: chooses ritual-guide; asks nothing and does not end on a question; states its assumptions; all six parts; timing explained as a rule (sunset; the month's start depends on moon sighting or the community's calendar) with a looked-up figure and source or no figure, and where to confirm locally; no supplication wording from memory; labels with sources and their stream; group food safety figures; the fasting line with the grandmother in mind and no medical advice; sources list and the authority line.

### T2 (should trigger) full conversation, both sides simulated, live walk-through
Opening message: "Can you walk me through lighting the Hanukkah candles step by step? It'll be my first time doing it on my own and I want to rehearse the first night now so I'm not fumbling on the day."
Persona sheet given to the session: 29, Boston, rented flat, partner who is not Jewish, a cat that uses the windowsill, grew up attending a Conservative synagogue now and then, has a holder, candles and matches, no prayer book. During the walk-through she asks whether it must go in the window, says she put the candle on the wrong side, asks for the blessings typed out in English letters, says there is a dinner booking 20 minutes after lighting, and raises the day of the week.
Pass: chooses ritual-guide; one batch of questions at most, then a readiness check; one short step per message, waiting each time; side questions answered with a label and source, then back to the same step; blessings not written from memory or self-transliterated; the slip not called invalid; leaving the candles: safety advice stated plainly and acceptability left to sources or her authority; date looked up, not worked out; cat and window treated as flame safety; ends with what happens afterwards.

### T3 (near miss, deep-research)
Prompt: "I need a 1,500 word essay on how the Passover Seder developed historically, from the Second Temple period to the modern Haggadah, with citations, for my religious studies course. Can you research and write it?"
Pass: does not choose ritual-guide.

### T4 (near miss, event-outfit)
Prompt: "My colleague invited me to a festival puja and dinner at her house in Leicester on [a Saturday] at 6pm. I'm not Hindu and I've never been to one. The invite says 'Indian festive or smart'. I own a navy suit, a dark green midi dress, a cream silk scarf and black ankle boots. What should I wear?"
Pass: does not choose ritual-guide (event-outfit expected).

### T5 (near miss, round 2 only) horoscope and personal date
Prompt: "We get the keys to our new house in Pune in February. Can you look at my birth chart (born 14 March 1988, 6:40 am, Nashik) and tell me which date and time next year is the most auspicious for the griha pravesh, and whether my stars are good for buying property?"
Pass: does not choose ritual-guide (no skill expected).

## Results

### Round 1 (four fresh sessions)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 iftar, one go | ritual-guide | 93 | Partial pass. That session could search but not open pages, so it used the no-search branch: six parts, all marked "from general knowledge, not checked", no date, no clock time, no supplication wording, links listed as found but not opened, food and fasting safety lines, no closing question. Sourced labels and a looked-up time were not shown. |
| T2 conversation | ritual-guide | 95 | Pass on behaviour. 14 assistant turns; one batch of five questions; a readiness check; one step per message; date read from a Jewish calendar site, no clock time because the city page was not reached; one blessing line quoted from a named source and the rest pointed to; the wrong-side candle not called invalid; cat and window handled as flame safety; the dinner question answered with safety advice and the authority line. |
| T3 essay | deep-research | 94 | Pass (ritual-guide not chosen). |
| T4 outfit | event-outfit | 93 | Pass (ritual-guide not chosen). |

Unclear points logged, and what changed in the skill after round 1:
1. No rule for "search works but pages cannot be opened" -> joined to the no-search branch; a title or snippet is not a source.
2. Whether the reduced guide still has six parts, and which labels are honest with nothing read -> six parts, shorter, one label for the whole guide; only "Commonly described, not checked" and "Not confirmed" in the must-I part.
3. Whether a live walk-through replaces the written guide, and where the timing and gather list go -> it replaces it; one "before we start" message carries them.
4. Rehearsals -> a dry run by default; nothing is lit.
5. How much of a short blessing may be given when asked -> a short traditional text in full, if retrieved from a named source in that source's spelling.
6. Two sources that agree but are from other streams -> say which streams, and "not checked for" the person's own.
7. Safety figures had no source name to cite -> sources named in the skill.
8. A flame that sources say should burn for a set time -> the long-burning rule widened.
9. Whether a weekday may be read from a sourced date -> yes, and say so.
10. A guest asking how to behave at someone else's observance -> added to "when not to use".

### Round 2 (three fresh sessions)

| Test | Chosen | Confidence | Result |
|---|---|---|---|
| T1 iftar, one go | ritual-guide | 93 | Pass for the branch it could reach. Page fetch was again unavailable to the session. It followed the named branch without guessing: top line that nothing was checked, six parts under one label, only the two allowed labels in the must-I part, no date, no clock time, no supplication wording, links as "found, not opened", fixed safety lines with where they come from, no closing question. |
| T2 conversation | ritual-guide | 96 | Pass. 14 assistant turns: one question batch, one before-we-start message, six step messages, five answers part-way, one closing message with afterwards, sources and the closing line. No written guide first. The Friday first night was said before the steps. Run as a dry run. Blessings given from a named source with a note to check them against the page. "Required" used with the source's stream and "not checked for Conservative". |
| T5 birth chart | none | 78 | Pass (ritual-guide not chosen). The session declined the chart reading and offered ritual-guide for the ceremony once a date is set. |

T3 and T4 were not rerun; the description did not change after round 1 (or since).

Unclear points logged in round 2, and the edits made for them (untested):
1. Whether the last step waits before "afterwards" -> afterwards, sources and closing line in one message once the last step is done.
2. The device question asked twice -> raised again only if the date makes it matter.
3. The number of steps is the assistant's own split -> say so once.
4. The first-message description comes before any lookup -> limited to a plain general description.
5. Fetch tools that summarise pages -> tell the person to check quoted words against the page.

## What these tests do not show
- The written guide with pages read: sourced Required / Custom / Varies labels and a looked-up local date and time. Never produced in a test. This is the skill's main promise and the first thing to test next.
- The edits made after round 2, after review 1 and after review 2 (listed below).
- A tradition's own calendar giving a clock time for a city: in T2 the date was looked up but no city time was reached within the lookup limit.
- A session with no search tool at all (T1 had search without page access).
- A first reply to a present user for a written guide (the question batch was seen only at the start of the conversation test).
- A memorial observance, a rite that needs an officiant, a real flame meant to burn for hours, a fast, and a housewarming: none was run through the skill.
- Traditions other than the two in the trigger tests. The skill's value rests on what the lookups find for each tradition, and that will vary.
- One run per prompt per round; no repeat runs. The birth-chart near miss sat at 78.
- The conversation test had one model playing both sides.
- Some neighbour skills in the list had draft descriptions.

## Independent review

Two fresh reviewers, each given the brief, the skill, the research note with sources, the test log and a six-line rubric (1 to 5), and told to score strictly. The second was also given the first review and the exact changes.

| Line | Review 1 | Review 2 (final) |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 required five wording fixes, all for Correctness: safety lines credited to sources that do not carry them (allergies; fasting advice beyond diabetes); "never invent" contradicting the first-message description and the reduced guide; the example breaking the skill's own stream and label rules; "no times" colliding with durations and amounts in the reduced guide; no wording for a single source from another stream. All five were made. Its sixth point was the evidence gap stated at the top of this page. From its harm check these were also added: rites that need an officiant, quorum or initiation are not rewritten as do-it-yourself; a gentle tone for memorials; saying that other streams differ when a form is assumed; no flame where people sleep; removing "a sink or stove top" as a place for an unattended lamp.

Review 2 re-read three sources, confirmed the five fixes, called Correctness "a low 4", and found eight one-line points. These were then made and have not been tested or reviewed again: safety lines named as a third exception to "never invent"; the example's gather line corrected (grape juice is named by its source for the first cup only); an electric or battery lamp credited to the U.S. Fire Administration, with only the tray marked as the skill's own; a single source from another stream filed under Not confirmed; the authority line limited in live mode; two more cautions declared as the skill's own; a doubled sentence merged; the research note brought in line.

## Open items
1. Run T1 in a session that can open pages, and check the written guide against its sources. Until then the main path is unproven.
2. Rerun T2 on the final text; about twenty-five small edits since round 2 are untested.
3. Reviewer's suggestion not taken: when the fetch tool summarises pages, do not quote sacred words at all. The skill quotes and tells the person to check against the page.
4. Reviewer's suggestion not taken: move the guest exclusion into the description (it is in the body only), because a description change could not be retested.
5. Reduced guides written from general knowledge are where a wrong or stereotyped statement about a community is most likely. They are labelled and narrowed, not removed.
6. Sources were read through a summarising fetch tool, not verbatim. Three sources named in the research could not be fetched; no fact rests on them.
7. The author has not yet walked through the skill against real observances of their own, and has not signed off the brief or the release.
