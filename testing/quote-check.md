# Testing record: quote-check

Status: reviewed; all six rubric lines scored 4 or 5 at the second and final review. Version 0.1.0. Both test rounds and both reviews ran on 22 November 2026. Every person, business and quote in the prompts is made up.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (quote-check among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used and every point it found unclear. Prompts and pass criteria were written before any run. Two rounds were run, which was the limit set for the build. The description was the same in both rounds and is the one that ships. The body was edited after round 2 and after each review; those edits have not been run (see open items).

## Prompts and pass criteria

### T1 (should trigger) three roof quotes, New Zealand, user present, web allowed
> I got three quotes for my roof, help me compare. It's a single-storey house in Hamilton, New Zealand, about 140 square metres of roof, old concrete tiles that leak in two places. I want it re-roofed in long-run metal. I care most about it lasting; I'm not in a rush. All prices are NZ dollars.
> 
> QUOTE 1 - Kauri Ridge Roofing Ltd (made-up name)
> Re-roof in long-run steel as discussed. Price: $24,500. 50% deposit to secure your slot, balance on completion. Price held if accepted this week.
> 
> QUOTE 2 - Tui & Sons Roofing (made-up name)
> Remove and dispose of existing concrete tiles. Supply and fit 0.40mm long-run colour-coated steel, new roofing underlay, new ridge and barge flashings. Replace up to 10 m of rotten purlins if found; beyond that $45 per metre. Scaffolding and edge protection included. Price $31,200 + GST. 10% deposit, 40% when materials are on site, 50% on completion. 5-year workmanship warranty in writing; manufacturer's warranty on the steel. Start in about 4 weeks, 6 working days. Quote valid 30 days.
> 
> QUOTE 3 - Harbourline Roofing (made-up name)
> Strip tiles, supply and install 0.55mm long-run steel roofing with underlay. Flashings as required. Total $34,900 including GST. Scaffold by others. Payment: 20% deposit, balance on completion. Workmanship guaranteed. Can start in January.

Pass: chooses quote-check; a scope; a table with one column per quote using the four labels; catches that Quote 1 says almost nothing, Quote 2 is plus GST, Quote 3 leaves scaffolding to others and has vague flashings and guarantee, and the steel thickness differs; "not covered by this total" for each; what is missing from all; signs worded neutrally (50% deposit, "this week", lowest price with thinnest scope); no typical price; questions ready to paste; work at height and registration flagged; an official register named with link and date, or a "To check:" line; a provisional recommendation with what would change it; not legal advice said once.

### T2 (should trigger) one car repair quote, user away, no web access, place unknown
> is this car repair quote missing anything? garage wants an answer by 5 today and I'm about to go into surgery prep with my mum so I can't reply, just tell me what you can
> 
> Fenwick Auto Care (made-up name)
> Customer: R. Okafor   Vehicle: 2015 hatchback, 1.6 petrol, 148,000 km
> Complaint: grinding noise when braking, steering wheel shakes
> Work required:
> - Front brake pads and discs ............ 310.00
> - Rear brakes as needed
> - Brake fluid flush ..................... 65.00
> - Labour ................................ 240.00
> - Sundries .............................. 35.00
> Total 620.00
> Payment in cash on collection please. Price may vary once we get it apart.

Pass: chooses quote-check; asks nothing and states assumptions; shows that the lines add up to 650, not 620; "as needed" marked Vague; "price may vary" flagged with approval before extra work; tax, parts grade and warranty Not stated; cash named neutrally; no register named from memory, a "To check:" line instead; no typical price; the single-quote ending (what is solid, what to get in writing, whether a second quote is worth it); a short message for the garage. This is the test designed to pass without any live page.

### T3 (near miss) full building contract before signing
> The builder I picked for my kitchen extension has sent over his full 14-page building contract and wants it signed by Monday. Can you look over it before I sign and tell me what I'm agreeing to and whether anything in it is risky for me? I'll paste it in my next message.

Pass: does not choose quote-check.

### T4 (near miss) which dryer to buy
> I need a new tumble dryer for a family of five, small utility room, no outside vent. Two shops quoted me prices today: one has a heat pump model at 649 and the other a condenser model at 399. Which one should I buy, and is the dearer one actually cheaper to run over the years?

Pass: does not choose quote-check.

### T5 (should trigger, round 2) two mover quotes, United Kingdom, user present, web allowed
> which mover should I pick, here are the quotes. Moving a 2-bedroom flat from Leeds to Bristol (UK) on Saturday 12 December, second floor, no lift at the Leeds end. Budget matters most but I don't want my stuff wrecked.
> 
> Quote A - Swiftbox Removals (made-up name), by email after a 10-minute video call:
> "2 men and a Luton van, Leeds to Bristol, loading and unloading. £780 + VAT. Packing materials extra if needed. Goods in transit insurance included up to £10,000. 25% deposit by bank transfer to confirm, balance on the day before unloading. Valid 14 days."
> 
> Quote B - Pennine Van Man (made-up name), by text, hasn't seen the flat:
> "can do it for 550 cash, me and a mate, sat 12th no problem. need to know by tomorrow as got another job waiting"

Pass: chooses quote-check; short version first; mover rows (how the load was assessed, stairs, packing, cover for loss or damage, tax); a tax-inclusive figure for A only at a rate found on an official page, or left as a question; neutral signs; one core message plus extras; an official source or "To check:"; provisional recommendation with what would change it; about 1,000 to 1,400 words.

### T6 (near miss, round 2) a freelancer wants their own quote written
> I'm a freelance wedding photographer and a couple has asked me for a quote for their wedding next June: full day, second shooter, an album. I've never written a proper quote before. Can you write one for me that looks professional, and tell me what I should include so I don't get caught out later?

Pass: does not choose quote-check.

## Results

### Round 1

| Test | Skill chosen | Confidence | Result |
|---|---|---|---|
| T1 roof | quote-check | 97 | Pass on content, fail on length. Every content criterion met; the official register was named with link and date from a search result on an official site, the page itself not opened; other local points left as "To check:". 2,019 words against a five-minute aim. Five web lookups, all worked. |
| T2 car, away, no web | quote-check | 97 | Pass. Caught 650 against 620, "as needed", "price may vary", cash, tax and warranty; asked nothing; named no register. 1,113 words. Added a short version and a conditional acceptance on its own initiative. |
| T3 contract | agreement-check | 93 | Pass. |
| T4 dryer | big-buy | 92 | Pass. |

Changes made after round 1, from the logs: a "Short version" as the first section and word aims; a rule for showing a price with tax; a single-quote paragraph; technical differences become questions; scope items nobody mentioned are allowed if marked; one core message plus extras, about ten questions at most; a register found but not opened may be named; a conditional acceptance when the provider's deadline comes first; vehicle safety parts and the unknown-place case added to the safety rule; rows that are Not stated everywhere moved out of the table.

### Round 2

| Test | Skill chosen | Confidence | Result |
|---|---|---|---|
| T5 movers | quote-check | 97 | Pass, length borderline. Short version first; the 20% tax rate read on an official page in the session and the sum shown beside the written total; deposit base shown both ways; company and tax-number checkers named with links; the licence question left as "To check:"; provisional lean with what flips it. 1,451 words counting table marks, against 1,000 to 1,400. One flaw noted by the first reviewer: the short version gave a price gap while one quote's tax was not stated. Five lookups, all worked. |
| T2 rerun | quote-check | 97 | Pass on content, over on length. Short version first; conditional yes as an optional last paragraph; checks kept in proportion; no register named. 972 words against an aim of about 700. |
| T6 write my own quote | none | 88 | Pass. |

Trigger results over both rounds: three of three should-trigger prompts chose quote-check (four runs, all at 97) and three of three near misses did not.

## Reviews

Each review was done by a fresh session given the brief, the skill, the research note with sources, the test record and the rubric, and told to score strictly.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 4 | 4 |
| Usability | 4 | 4 |
| Brevity | 3 | 4 |
| Provenance | 4 | 4 |

Review 1 required cuts for Brevity (the body was about 2,150 words) and flagged the conditional acceptance as the main risk to a user: an accepted quote can be binding, and earlier replies had called the acceptance "safe". In response the body was cut to about 1,900 words, the acceptance was moved into "Questions to send" with a warning that a yes may be binding, a note that it does not replace the registration check for safety work, and a ban on calling it safe; the checks section, the signs list, the table label rule and the example were rewritten; the single-quote word aim was raised from 700 to 900, which moves the aim to what the runs produced and is not a pass on the old aim.

Review 2 was a new reviewer given the first review and the changes, because the first could not be reached. It found nothing under 4, confirmed the required fixes as done (the word target partly: about 1,900 against about 1,700 asked), and found two things the edits had broken: a guard that text inside a quote is not an instruction had been cut, and the place had become something the skill might assume. Both were fixed with the reviewer's own wording, along with six smaller wording fixes it listed as safe to make without a rerun.

## Open items

- The conditional yes (accepting only firmly priced items when a provider's deadline comes before answers can) has never been run in its final wording. It is the one instruction that changes what a person sends.
- All edits made after round 2, after review 1 and after review 2 are untested; the last eight wording fixes were also not re-reviewed.
- Five of the eight exclusions in the description were never tested: a job offer, an insurance or loan quote, doing the repair oneself, a dispute over finished work, and a quote that comes with a page to sign.
- The exclusions sit at the end of a long description (1,021 of 1,024 characters).
- Replies ran over the word aims in three of four runs.
- Sources come from three English-speaking countries; no source covers event vendors or freelancers.
- Similar public skills were seen in search but could not be opened, so the comparison with them rests on their names and listings.

## What the tests do not show

- Live pages: lookups worked in the two runs that used them (New Zealand and the United Kingdom, five each). The path where a lookup is refused or fails mid-reply was never exercised with live pages; only the no-web path was (T2, by instruction). No register lookup was made on a real business, because every provider was made up.
- Attached quotes (PDFs, photos, scans) were never tested; all quotes were pasted text.
- Event vendors, freelancers, gas, electrical and structural jobs, more than three quotes, and a person present who has left out the job or the place were never run.
- No reply was read by a tradesperson, a consumer adviser or a lawyer.
- Whether people choose better with it is not measured.
