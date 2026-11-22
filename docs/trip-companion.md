# trip-companion

Status: tested and reviewed (three test rounds, two independent reviews, every rubric line at 4 on the second review). Small edits made after the last test round and after the last review were checked by the author only; see the testing record. Version 0.1.0.

## What it does

Plans and runs one trip from first idea to the journey home, for anything from a two-day work trip to an international family holiday. It is a companion for the whole run of the trip, not an itinerary writer.

1. Works out where the traveller is (planning, booked and getting ready, at the airport, mid-trip) and asks only for what is missing, in one short batch: who is travelling and any needs, from where to where, dates, purpose, budget, what is booked, passports (valid until about when, and nationality and country of residence; never a number), must-haves and deal-breakers.
2. Scales the process: a light version for a short domestic trip, a standard one, and the full ten phases for a bigger trip.
3. Carries the traveller through the phases, one at a time: shape the trip, flights, stays, preparation timeline, packing and bag rules, check-in and seats, leaving the house, the airport (including delays and cancellations), arrival and the days away, coming home.
4. Looks up anything that can change (entry rules, visas, health requirements, advisories, security and baggage rules, prices, schedules, forecasts) on the official source for that traveller and gives it with the source and the date. What it could not check is marked "not verified", with the page to check.
5. Keeps a short trip sheet so the trip can be picked up later, and offers the dated items (flights, check-in opening, cancellation deadlines, leave-for-the-airport time, document expiry) as calendar entries or reminders, only after showing the list and getting a yes. With no calendar tool it gives a dated list.

Rules it keeps: the traveller makes every booking and payment; it never asks for or stores passport numbers, card details or passwords; safety, medical and accessibility needs come before price; it is not official advice and not a substitute for travel insurance.

The skill is a short SKILL.md plus one reference file per phase and a list of official sources, so only the phase in hand is loaded.

## How it differs from similar public skills

Other public travel-planning skills exist. Two were looked at on 21 November 2026: the "travel-planner" skill in ailabs-393/ai-labs-claude-skills (travel preferences, itineraries, budgets, packing checklists, pre-trip timelines) and apljacob/travel-agent (seven phases from discovery to a PDF itinerary, with live search and no booking; its README lists calendar integration and re-planning during a trip as out of scope). trip-companion goes ahead on a narrower angle: the travel-day half (check-in, leaving the house, the airport, disruption, arrival, coming home), carry-on and checked-bag questions answered from the security authority and the airline, a re-check of passports against every connection country, scaling down for short trips, starting mid-trip, and calendar entries with consent. It does not try to be a destination guide. Nothing was copied from those skills.

## Example

> I'm flying Toronto to Lisbon next Friday with my mum, flights and hotel are booked. Help me get ready.

The reply, in outline: says the date back, skips planning, and asks four short questions (airline, times and whether it is one ticket; the return flight and how they get to the airport; passports in date, nationality and where they live; needs and bags). On the answer it looks up entry rules for their nationality, including the country they change planes in, and the airline's baggage and check-in pages, each with source and date; gives the week-out, two-days-out and night-before lists with a packing list; shows the trip sheet; and offers the dated items for the calendar.

A narrow question is answered straight away:

> Can I take a 20,000 mAh power bank and 150 ml of sunscreen in my carry-on? Chicago to London on Thursday.

One-sentence verdict first, then for each item "carry-on: yes or no, checked bag: yes or no" with the conditions, the watt-hour sum, and the sources with dates.

## Not for

Only choosing a seat on a booked flight (seat-picker in this collection), only deciding what to wear to an event (event-outfit in this collection), a general question about a place with no trip in view, a visa or immigration application for moving country, and expense reports after a trip.

## Limits to know about

- It is only as good as the session's tools. Without web access it gives the process and names the pages to check, and states no rules. Airline and security-authority pages sometimes refuse automated reading; those facts then come back "not verified".
- It is written mainly for trips by air. Trips by car, train or ferry are covered by one paragraph.
- The traveller must still read the official pages for anything that could stop the trip.

## Sources and credits

The skill stores almost no travel facts; it tells Claude where to look. Research was about which official sources to point to and what commonly goes wrong.

Pages opened and read on 21 November 2026, through a summarising fetch tool (not verbatim):

1. FAA PackSafe, lithium batteries (page updated 11 Aug 2026): https://www.faa.gov/hazmat/packsafe/more_info/?hazmat=7
2. TSA, liquids rule (no date shown): https://www.tsa.gov/travel/security-screening/liquids-rule
3. GOV.UK, hand luggage restrictions at UK airports (updated 2 Nov 2026): https://www.gov.uk/hand-luggage-restrictions
4. US Department of Transportation, what airline passengers need to know about the automatic refund rule (18 Nov 2024): https://www.transportation.gov/briefing-room/what-airline-passengers-need-know-about-dots-automatic-refund-rule
5. Your Europe, air passenger rights (last modified 18 Nov 2026): https://europa.eu/youreurope/citizens/travel/passenger-rights/air/index_en.htm
6. US Department of State, Traveler's Checklist (updated 14 Feb 2024): https://travel.state.gov/content/travel/en/international-travel/before-you-go/travelers-checklist.html
7. CDC Travelers' Health, Pack Smart, and the Travelers' Health home page (no date shown): https://wwwnc.cdc.gov/travel/page/pack-smart
8. GOV.UK foreign travel advice (no date noted): https://www.gov.uk/foreign-travel-advice
9. TravelHealthPro (NaTHNaC) (no date noted): https://travelhealthpro.org.uk/
10. UK Civil Aviation Authority, passengers (no date noted): https://www.caa.co.uk/passengers/

The skill's own list of official sources (references/official-sources.md) names more, by role first and by link second. Some were confirmed only by a search listing under the official domain (Canada's travel.gc.ca, CATSA, the Canadian Transportation Agency, Australia's TravelSECURE and CASA, the CAA baggage page, the EU's travel-europe site). Others could not be opened when the file was written; they are named without a link and marked (†) in the file (the search-only ones are marked (‡)), with an instruction to find them by name and confirm they are official.

The author's own judgement, not taken from a source: the layover rules of thumb; the defaults for how early to be at the airport and the time allowances in the leave-time sum; "often 24 to 48 hours" for when check-in opens; the 10 to 15 percent budget cushion; a forecast being useful from about ten days out; 3.7 V as the usual cell voltage when a label shows none; four to six weeks for a travel clinic visit; the three tracks; the word targets. Each is labelled as a rule of thumb or a default in the skill.

No employer, client or confidential material was used.

Testing record: [testing/trip-companion.md](../testing/trip-companion.md)
