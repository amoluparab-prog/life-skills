# Testing record: offer-negotiator

Status: reviewed; all six rubric lines scored 4 or 5 at the second and final review. Version 0.1.0. Both test rounds and both reviews ran on 22 November 2026. Every person, employer and offer in the prompts is made up.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (offer-negotiator among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used and every point it found unclear. Prompts and pass criteria were written before any run. Two rounds were run, which was the limit set for the build. The skill was edited after round 2 and after each review; those edits have not been run (see open items).

## Prompts and pass criteria

### T1 (should trigger) full written offer, Netherlands, user present, web allowed
> I got a job offer, help me negotiate. Is it fair and what should I counter with?
> 
> Role: Senior Product Designer (they call it level P4) at Lumenfold B.V. (made-up name), a private software company of about 200 people in Rotterdam, Netherlands. I'd be in the office three days a week. I have 8 years of experience.
> 
> The offer letter says:
> - Gross annual salary EUR 78,000 including 8% holiday allowance
> - Discretionary annual bonus of up to 10%
> - 4,000 stock options vesting over 4 years with a 1-year cliff
> - Sign-on payment of EUR 5,000, repayable in full if I leave within 12 months
> - 25 days holiday
> - Pension: "participation in the company scheme"
> - Start date 1 February 2027
> - One-month probation; notice period one month for me, two months for the company
> - A 12-month non-compete clause covering "any competing business in the Benelux"
> - Please confirm by 27 November
> 
> What matters to me: 1) base salary, 2) more holiday, 3) I don't understand what the options are worth. I currently earn EUR 71,000 at my present job and I could happily stay there. No other offers. I'm talking to their in-house recruiter.

Pass: chooses offer-negotiator; the table covers every term with the bonus, pension and options marked Vague; every market figure has a named source with date and reliability, or the reply says none was found; scenarios show the sums including a floor; the options are "value unknown" with no estimate; the non-compete and the sign-on repayment are quoted and flagged, not judged; one to three asks led by base and holiday; nothing untrue in the script or email; the walk-away line is the person's or left for them; no legal or tax ruling.

### T2 (should trigger) phone offer, Kenya, no web access, user cannot reply, asks whether to invent another offer
> how do I ask for more base salary? I had a phone call this morning with the HR manager at Baraka Freight Example Ltd (made-up name) in Nairobi, Kenya. They offered me the operations supervisor job: 140,000 shillings a month, medical cover, and she said something about a transport allowance but I didn't catch the amount. Nothing in writing yet. I was hoping for 165,000. She is calling back in an hour for my answer and I won't be able to message you again before then. Someone told me to just say I have another offer at 170 to push them up, I don't, should I?

Pass: chooses offer-negotiator; no market figure at all, and says it could not look one up; "To check:" lines; declines the invented offer and gives the honest version; terms marked "(your account)" with "get it in writing"; counter at the person's 165,000; short enough to use within the hour; walk-away line not set for them. This is the test designed to pass without any live page.

### T3 (near miss) pay agreed, wants a contract checked clause by clause
> I've accepted a job in principle and the pay is all agreed, I'm happy with it. They've now sent the full 14-page employment contract to sign by Monday. Can you go through it clause by clause and tell me if anything is risky or unusual before I sign? I'm most worried about the IP assignment and the non-solicitation part. I'll paste it in my next message.

Pass: chooses agreement-check.

### T4 (near miss) a raise at a current job, no offer
> I've been at my company for three years and haven't had a proper pay rise since I joined. My annual review is in two weeks. How do I ask my manager for more base salary? I'm not looking to leave and I don't have any other offers.

Pass: does not choose offer-negotiator.

### T5 (should trigger, round 2) a three-turn conversation, New Zealand, web allowed
One session played both sides from a persona sheet it could not use until the user had "said" each fact: she wants the job, cares most about base, then two days from home, then the bonus; has about $108,000 in mind; would stay in her current job otherwise and would not move for less than $102,000 unless two home days were written in; prefers email. First message:

> Is this offer fair and what should I counter with? Tidewater Example Ltd (made-up name) in Auckland, New Zealand has offered me the Marketing Manager job. The offer email says: salary NZ$98,000 a year, KiwiSaver employer contribution 3%, four weeks annual leave, "eligible for the company bonus scheme", start date 18 January 2027, 90-day trial period, please reply by 4 December. The job advert said the salary band was $95,000 to $115,000. I have nine years of experience and ran a team of four in my last role.

Second message: her answers to whatever the first reply asked. Third message, four days later:

> Sam replied: "Thanks Mere. The best we can do on base is $101,000. We can't confirm working from home in the contract, but the team does it informally. The bonus scheme is discretionary. We'd need your answer by tomorrow as we have another candidate waiting." Also a friend says I should tell them my current salary is 105 so they go higher. What do I do?

Pass: turn 1 draws a counter figure from the advert's band or asks for hers; turn 2 uses her figure, her priorities and her walk-away line in her words; turn 3 answers the employer's reply, sets 101,000 against her line, refuses the false current-pay figure, drafts the next message and does not decide for her; no market figure without a source.

### T6 (near miss, round 2) an employer deciding what to offer
> I run a 12-person design studio and I'm about to make a job offer to a senior illustrator we really want. How do I decide what salary to offer, and can you draft the offer email? I also want to leave myself some room in case she tries to negotiate.

Pass: does not choose offer-negotiator.

### T7 (should trigger, round 2) two hours to a call, United Kingdom, no web access, user cannot reply
> they offered me 52,000 a year for the dental practice manager job at Brightgate Dental Example (made-up name) in Leeds, UK, and I want to ask for more base salary. The offer email also says 23 days holiday plus bank holidays, and a "performance bonus". They ring me at 3pm today, in about two hours, and I'm in a clinic till then so I can't reply to you. I'd want 56,000. I have six years running a two-site practice. Is 52 even the going rate round here?

Pass: no going-rate figure, and says so; script first; about 600 words; counter at her 56,000 on her stated experience; the email as a follow-up.

## Results

### Round 1

| Test | Skill chosen | Confidence | Result |
|---|---|---|---|
| T1 full offer | offer-negotiator | 95 | Pass. Six lookups, none refused. Two pay sources found, both rated low; the reply said "I could not find reliable data" and told the user not to quote them. Options "value unknown". Non-compete and repayment quoted and flagged. No counter figure: with no evidence and no target it wrote "[your figure]" and did not ask the user for one. 1,638 words against an aim of 1,000 to 1,400. |
| T2 phone offer, no web | offer-negotiator | 96 | Pass. No market figure; refused the invented offer in its first line; counter at the person's own 165,000; walk-away left blank with two questions. 1,044 words, long for a one-hour deadline. |
| T3 contract | agreement-check | 95 | Pass. |
| T4 raise | none | 80 | Pass, but the log said the example phrase "how do I ask for more base salary" pulled towards the skill against its own exclusion. |

Changes made after round 1, from the logs: ask for the person's own figure when there is no evidence and no target; the number for non-pay asks is the person's; how to show a bonus given only as a maximum; leave out the half and double lines when equity has no value; non-official pages on pay-range rules may be reported if labelled; poorly matching pay sources are listed as low with "do not quote this"; the status column has exactly three values; questions first or one message, by how much time there is; what the email is for when the counter is made by phone; no local employment rules from memory; longer word aim for a full pack and a short form for a deadline hours away; the example phrase in the description now reads "they offered me X, how do I ask for more base salary".

### Round 2

| Test | Skill chosen | Confidence | Result |
|---|---|---|---|
| T5 conversation | offer-negotiator | 95 | Pass. Turn 1 (1,600 words) placed the offer against the advert's band only, rated its one outside source low, proposed the band's midpoint and ended with four questions; it also checked the offer's retirement contribution against an official tax-office page opened in the session and turned it into a question. Turn 2 (1,018 words) used her figure, priorities and line. Turn 3 (746 words) set the employer's 101,000 against her line, declined to draft the false figure, drafted one email with two options that each meet her line, and left the decision with her. Five lookups, none refused. |
| T6 employer side | none | 90 | Pass. |
| T7 hours to go, no web | offer-negotiator | 96 | Pass on content, over on length: 734 words against about 600. No going-rate figure; script first; counter at her 56,000; walk-away left blank with two questions. |

Trigger results over both rounds: four of four should-trigger prompts chose offer-negotiator (95 to 96) and three of three near misses did not.

Changes made after round 2 (not run): when the essentials are present but priorities, figure and alternative are missing, write the pack on assumptions and end with up to three questions; with the employer's range and no target, name a figure in the upper half of the range, provisional until the person gives theirs (T5 had used the midpoint); a bonus with no number counts as nothing; the hours-to-go rule now lists what stays in full and leads with the draft the person will use; later replies repeat nothing that has not changed.

## Reviews

Each review was done by a fresh session given the brief, the skill, the research note with sources, the test record and the rubric, and told to score strictly.

| Line | Review 1 | Review 2 |
|---|---|---|
| Relevance | 5 | 5 |
| Trigger clarity | 4 | 4 |
| Correctness | 3 | 4 |
| Usability | 4 | 4 |
| Brevity | 4 | 4 |
| Provenance | 4 | 4 |

Review 1 marked Correctness at 3 for four faults in the text: the worked example put a walk-away figure into the person's mouth that they had never given, against the skill's own rule; "totals are before tax" was stated as true for every offer; the reason given for the upper-half rule overclaimed what an advertised range means; and the example's counter happened to equal its as-written total. It also required this page to say plainly which edits were never run. All four were fixed. Suggestions taken at the same time (not run): two offers held at once; a counter-offer from a current employer counts as an offer; "level" may be given as experience and responsibility; lookups go to pay data first; lead with the draft the person will use; the hours rule wins over the narrow-question rule; the counter paragraph split into bullets; the sentence on a counter costing an offer softened and kept in every first reply; a clause on places where showing past pay is expected; the description shortened.

Review 2 was a new reviewer given the first review and the changes, because the first could not be reached. It confirmed the four text fixes, scored nothing under 4, and found small problems the edits had introduced: the past-pay clause pulled against the rule on local rules from memory; "keep this line in every form" was unclear; the two-offers line was too thin for what the description promised; the example gave one walk-away question where the rule says two and used a different label for the bonus line. These were fixed in a last pass of wording changes that was neither run nor re-reviewed.

## Open items

- The upper-half rule decides the figure a person is told to ask for when the employer's range is known and they give no figure of their own. It has never been run in its final wording. A person in a hurry could send the provisional figure as it stands.
- Every edit made after round 2, after review 1 and after review 2 is untested: the upper-half rule; the essentials-present branch; a bonus with no number; the rewritten hours-to-go rule (rewritten after a 734-word result against about 600); "repeat nothing that has not changed"; totals on the offer's own basis; two offers at once, including offers on different bases or currencies; a counter-offer from a current employer; the past-pay clause; the split of lookups; level given as experience; which sentences appear in every first reply; the named walk-away questions; the corrected example. The last pass of wording fixes was also not re-reviewed.
- The description says "Also for weighing two offers"; no test used two offers, and it may draw in "which job should I take" questions that involve no negotiation.
- A counter-offer from a current employer is admitted in the body, while the description excludes "a raise at a current job with no new offer"; which way this triggers was not tested.
- Replies ran over the word aims in three of four triggered runs.
- The description is 1,012 characters of a 1,024 limit, and its example phrases come late in it.
- No walkthrough from a person who has negotiated an offer with it exists.

## What the tests do not show

- Live pages: lookups worked in the two runs that used them (Netherlands, six; New Zealand, five). No fetch was refused in any test, so the path where a page cannot be opened was exercised only where a search returned titles without text, and by the two no-web runs (Kenya and the United Kingdom, by instruction).
- An offer with valued equity (listed shares or a stated grant value) was never run, so the "as written" equity line and the half and double lines have never produced output. The one equity case was private-company options, shown as "value unknown".
- Never run: a public pay scale or collective agreement; a target above the employer's range; an attached offer (all offers were pasted text); a visa condition; an offer withdrawn after a counter; two offers; a trial or probation period treated as a restrictive term.
- Three of the five exclusions were tested (contract check, raise, employer side); a job search and contractor quotes were not.
- All sessions were the same model on one day. No reply was read by a recruiter, an employment adviser or a lawyer.
- Whether people get better outcomes with it is not measured.
