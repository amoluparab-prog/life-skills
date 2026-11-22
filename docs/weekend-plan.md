# weekend-plan

Status: tested and reviewed (two test rounds, seven prompts, all passed; two independent reviews, every rubric line at 4 or above). Edits made after the last test round, including fixes from both reviews, are untested; see the testing record. Version 0.1.0.

## What it does

Plans a weekend or day off at or near home for one person, a couple or a family, so the time neither drifts nor gets overfilled.

1. Asks once, in one short message, only for what is missing: the town or area (as the person states it), which days are off, who is involved (ages, energy, mobility), how the week went and the mood they want, budget and currency, transport, fixed commitments (matches, worship, visits, naps, bedtimes), food rules, chores that cannot wait. If the person cannot reply, it asks nothing and states its assumptions.
2. Looks up, on official pages for that place, the forecast and warnings, sunset, and what is really on and open on those dates, with cost, travel and booking for each idea.
3. Writes the plan in a fixed order: a two-line summary; a small table of the days (one main thing a day, a named rest block, at most one chore block); two or three ideas for the main thing, each with time, cost, travel, booking, a status and a source with the date read; the forecast with its source and when to look again; an at-home alternative; easy meals; what to book or buy today; a 20 to 30 minute reset on the last evening; the cost as a sum against the budget; assumptions and a "to check" list.

Rules it keeps throughout: only the place the person states (never guessed, never read from the device unless asked); every place or event named is marked confirmed (read on the venue's own or an official page in that session), unconfirmed or to check, and nothing is invented; no forecast, price, opening time or dated event from memory; rest is planned, not left over; budget, faith observances, food rules and family routines stand as stated, without comment; nothing centred on alcohol unless asked; outdoor ideas carry a short safety note; it books, buys and sends nothing, and adds calendar entries only on request after showing the list; no country, currency, unit or pair of weekend days is the default.

With no search tool, or when pages cannot be read, it says so first and still gives the whole plan: ideas as kinds of thing with what to search for, the forecast marked "to check", spending caps in place of prices, and a short list of what to check in order.

## How it differs from similar public skills

Found by one web search on 22 November 2026: "family-weekend-activity-finder" (cosmicshuai on GitHub; its SKILL.md was read) finds dated children's events near a saved family profile, checks the forecast and ranks options with links; it leans on one country's weather service, units and listing sites and keeps a profile file. "weekend-wiz" (seen as a registry listing only, not read) manages a weekend schedule with reminders. weekend-plan is narrower in one way and wider in another: it is country-neutral and keeps nothing on disk, uses only the stated place, marks every named thing as confirmed, unconfirmed or to check, and plans the whole weekend (rest, chores, meals, a fallback, a reset), not only a list of events. Nothing was copied from those skills.

## Example

(The town, venues and people are invented.)

> Ideas for the long weekend with two kids and not much money? We're in Harbourton, off Saturday to Monday, kids are 4 and 9, no car, about 40 in our money for everything. Rough week. The little one naps 1 to 3. Football practice Saturday 10 to 11.

The reply, in outline. No questions, because enough was given. Saturday: practice, a chore block with an end time, then a rest afternoon. Sunday and Monday: one outing each morning, home for the nap. Three ideas: a free council lantern trail in a park, marked confirmed with the council page and the day it was read, with a note to look at the forecast again; a museum family morning seen only on a listing site, marked unconfirmed with a note to check the museum's own page; a flat harbour walk with a picnic, marked as a permanent place not checked, with the younger child kept within reach near the water. The forecast with its source, the time it was read and when to look again. A film afternoon at home if it pours. A pot of soup for two days. Nothing to book; bus day tickets to buy. A reset on Monday evening. The cost as a sum: 12 + 15 + 4 = 31 of 40, with 9 held back. A "to check" line: the museum's own page, and holiday hours if Monday is a public holiday. Nothing goes into a calendar, because nobody asked.

## Not for

A trip with flights or a night away (trip-companion); a timed route of stops for a day in a city being visited (day-in-city); a gathering the person hosts (host-plan); the work week (week-plan); a layover (layover-plan). If the main thing on one day grows into one of these, the skill says so and plans the rest of the weekend around it.

## Sources and credits

All pages were read on 22 November 2026 through a fetch tool that returns a summary of the page, not its raw text, so a detail could have been mis-summarised. The skill carries no figures from any of them.

1. Sonnentag and Fritz (2007), "The Recovery Experience Questionnaire", Journal of Occupational Health Psychology 12, 204-221. The four parts of recovery in time off: switching off from work, relaxing, accomplishment or learning, and control over one's own time. Read: the authors' university page listing the four scales and the citation (sowi.uni-mannheim.de/en/sonnentag/research/measures-and-tools). Not read: the paper itself; the abstract page on a medical index was refused.
2. Fritz, Sonnentag, Spector and McInroe (2010), "The weekend matters", Journal of Organizational Behavior 31(8), 1137-1162. Weekend recovery carries into the following week's mood. Read: the abstract page in a university repository (digitalcommons.usf.edu/psy_facpub/729).
3. Tonietto and Malkoc (2016), "The Calendar Mindset", Journal of Marketing Research. Exact times can make leisure feel like a task while planning makes it more likely to happen; the authors suggest rough slots as a middle way. Read: the university's news article about the paper (source.washu.edu/2016/03/scheduling-takes-fun-free-time), not the paper; the article reports no test of rough slots.
4. Etkin and Mogilner (2016), "Does variety among activities increase happiness?", Journal of Consumer Research 43(2), 210-229. Variety helps over a day or more and hurts within an hour or less. Read: the business school's summary (fuqua.duke.edu/duke-fuqua-insights/etkin-variety), not the paper.
5. West, Mogilner and DeVoe, "Happiness from treating the weekend like a vacation". Read: a university research brief describing a working paper (anderson-review.ucla.edu/vacation-mindset). Not read: the later journal version. Background only.
6. Sharif, Mogilner and Hershfield (2021), "Having too little or too much time is linked to lower subjective well-being", Journal of Personality and Social Psychology. Read: the publisher's press release (apa.org/news/press/releases/2021/09/too-much-free-time); the title is as a search result gave it. Background for "one main thing a day"; correlational and from one country.
7. International Open Water Drowning Prevention Guidelines, published by the International Life Saving Federation. Read: the federation's page (ilsf.org/international-open-water-drowning-prevention-guidelines), which gives no issue date. The skill's lines for going in the water follow it. The guidelines are written for open water; the skill applies the same lines to pools.

The studies are of working adults, mostly in North America and Europe; none was tested on children, shift workers or other cultures, so the skill says "tends to" and gives no numbers.

The author's own judgement or general know-how, not taken from a source: one main thing of about two to four hours a day; at least one half-day of rest; one chore block of two hours or less; the 20 to 30 minute reset; leaning to rest after a heavy week; looking at the forecast again the evening before; the lines on trails and hills, on being beside water without swimming, and on heat, cold, sun, air quality, insects and wildlife; finishing an hour before sunset in unlit places; the three status words; spending caps when prices cannot be read; the order of the plan; easy meals.

Forecasts, warnings, opening times, prices and local safety advice are not in the skill: it looks them up at use time on the official pages for the person's place, or marks them to check.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/weekend-plan.md](../testing/weekend-plan.md)
