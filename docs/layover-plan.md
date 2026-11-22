# layover-plan

Status: tested and reviewed (two test rounds, two independent reviews, every rubric line at 4 or above). Edits made after the second test round and after each review were checked by the author only; see the testing record. Version 0.1.0.

## What it does

Helps a traveller decide what a wait between connections (about 2 to 24 hours) at an airport or station is really good for, and plan it safely.

1. Asks once, only for what is missing: where, the times, the airline and flight numbers, one ticket or separate, whether bags are checked through, passport and visa status (never a number), who is travelling, energy, budget, interests.
2. Looks up what can be looked up, in this order: entry and transit rules (government sites), the airline's bag, check-in and gate times, the ride, then airport facilities. Every fact carries its source and date.
3. Shows the sums: the gap minus getting off, entry checks, bags, the ride each way, security, the walk, gate closing and a safety margin. What is left is the free time.
4. Gives one verdict: stay airside, leave the terminal but stay near, or go into the city. Anything unconfirmed that could stop the journey goes at the top.
5. Writes a timed plan with a latest time to set out and a hard turn-back time, a stay plan in every case, the basics for bags, transit and money, a list of what to confirm and with whom, and a few safety points.

Rules it keeps: entry and transit rules are never stated from memory, only from a government, airline or airport page read in the session, or marked "to confirm"; it never advises cutting it fine and always states the margin and what a miss would cost; an unknown queue is called unknown and given an allowance; it never suggests skipping a border check or misstating the purpose of a visit; children, limited mobility, tiredness and night shrink the plan first; it books nothing and contacts no one.

Without web access it still gives the sums on allowances, a conditional verdict and a list of what to check and where.

## The default allowances (the author's judgement)

Used only when no better figure is found, and always labelled as allowances: 30 minutes to get off and out (45 at a very large airport); 90 for entry checks on an international arrival; 30 to collect and store bags; the ride at a busy hour plus one wait each way (60 each way to the city or 20 to somewhere near if nothing can be found); 30 for a bag-drop queue; 60 for security and exit checks on an international departure, 30 domestic; 20 to walk to the gate; 30 for a change of terminal; gate closing 30 before departure; a safety margin of 60, or 90 with separate tickets, children, limited mobility, road traffic, night, or no known later flight. Verdict thresholds: 120 minutes free for the city, 45 for somewhere near, one step down for each of tiredness, small children and night.

These are not measurements. Against the published rule of thumb of being back three hours before boarding for an international flight (source 2), the defaults bring the traveller to the terminal door roughly 55 to 70 minutes later with the 60 margin and 25 to 40 later with the 90 margin. The 90 minute entry allowance is a middle figure in that source's one to three hour range, not a cautious one. Treat the numbers as a starting point and replace them with real figures whenever they can be found.

## How it differs from similar public skills

Found on 22 November 2026: a "stopovers" skill in borski/travel-hacking-toolkit (which loyalty programmes allow stopovers on award tickets), a "Layover Flight Finder" on Skywork Skill Hub (finds flights with 6 to 15 hour layovers and writes a half-day tour with a return buffer), and several flight search and flight tracking skills. layover-plan is narrower: it starts from a connection the traveller already has, decides first whether leaving is allowed and worth it, shows the arithmetic, takes rules only from official pages or marks them to confirm, and sets a turn-back time. Nothing was copied from those skills.

## Example

> 9 h 30 at Exampleport, land 06:10 from abroad, leave 15:40 for abroad, same terminal. One ticket, bags through. Passport from Country A, no visas. Rested and curious, small budget.

The reply, in outline. Verdict: stay airside unless Exampleland's immigration site confirms this passport can enter without a visa; if it does, go into the city and leave it by 12:15 whatever happens. The sums: 570 minutes, minus 30 off the plane, 90 entry checks, 35 each way on the train with the wait, 60 security, 20 to the gate, 30 for gate closing and a 60 margin, leaves 210 minutes in the city. Clock times: out of the terminal about 08:10, in the centre 08:45, turn-back 12:15, terminal door 12:50, gate 14:10. Latest time to set out 09:40. Then the stay plan, bags and money, and the confirm list. (Exampleport, Exampleland and Country A are invented.)

## Not for

Planning a whole trip (trip-companion in this collection), choosing a flight seat (seat-picker), a day of sightseeing with no onward connection, stays of more than a day, whether a short connection can be made, or rebooking a missed or cancelled flight. It is not legal or immigration advice.

## Sources and credits

Public pages, read on 22 November 2026 through a summarising fetch tool (not verbatim) unless marked otherwise.

1. KAYAK, "How to decide if you should leave the airport on a layover", Blane Bachelor, 8 Feb 2024: https://www.kayak.com/news/leaving-the-airport-during-a-layover (count back from boarding time; add travel both ways, security, immigration and a buffer; confirm visa needs with the airline or embassy; cash for lockers)
2. Kiwi.com Stories, "Can You Leave the Airport on a Long Layover?", Siegfried Mortkowitz, updated 9 Jan 2026: https://www.kiwi.com/stories/can-you-leave-the-airport-on-a-long-layover-what-to-do-what-to-watch-for-and-when-to-stay-put/ (ranges for each step; back two or three hours before boarding; separate tickets; two alarms). Its country-by-country visa list was deliberately not used.
3. Going, "How Long Should Your Layover Be?", 19 Dec 2023: https://going.com/guides/how-long-should-your-layover-be (minimum connection time is a starting point; the number of later flights changes the cost of a miss)
4. OAG, "Guide to MCTs Explained": https://www.oag.com/hubfs/Inbound-Services/OAG-Guide-to-MCTs-Explained.pdf (what a minimum connection time is and who sets it)
5. GOV.UK, "Check if you need a UK visa": https://www.gov.uk/check-uk-visa (read only as an example of an official checker; no rule taken from it)
6. IATA's page on its travel document database could not be opened (the fetch was refused). Unverified; nothing was taken from it.

The first reviewer opened sources 1 and 2 and found them to match the research note, apart from the "before boarding" wording, since corrected. The step-by-step sums, the default allowances, the thresholds, the latest time to set out, the "official pages only" rule and the handling of separate tickets and overnight waits are the author's own judgement, built on the sources above.

## Testing record

See [testing/layover-plan.md](../testing/layover-plan.md).
