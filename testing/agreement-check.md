# Testing record: agreement-check

Status: reviewed; all six rubric lines scored 4 or 5 at the third and final review (Usability a borderline 4). Version 0.1.0. Rounds 1 and 2 and reviews 1 and 2 ran on 21 November 2026; round 3 and review 3 on 22 November 2026. Every person, company and document in the prompts is made up.

## How it was tested

Each prompt ran in its own fresh session that had not seen the skill being written. The session was given a list of installed skill descriptions (agreement-check among its neighbours), had to choose a skill from the descriptions alone, and only then opened the skill and followed it. It saved its reply and a log of its choice, confidence, tools used and every point it found unclear. Prompts and pass criteria were written before any run. Two rounds were run first, which was the limit set for the build; one extra round of three runs was then granted to close the open review item. The description was the same in all three rounds. Round 3 ran the body as it stood after both reviews. A few small edits were made after round 3 and after review 3; those have not been run (see open items).

## Prompts and pass criteria

### T1 (should trigger) freelance contract, user present, direct "is it enforceable" question
> Can you look over this contract before I sign? I'm the designer. They want it back tomorrow. Also, is that non-compete even enforceable? I'm in Ohio.
> 
> INDEPENDENT CONTRACTOR AGREEMENT
> Between Brightline Foods LLC ("Client") and Maya Torres ("Contractor"), 14 Elm Court, Columbus.
> 
> 1. Services. Contractor will design new packaging for Client's snack range and provide such other design services as Client may request from time to time.
> 2. Fee. Client will pay Contractor a fixed fee of $6,000 for the Services.
> 3. Payment. Contractor will invoice on final acceptance of all deliverables by Client. Invoices are payable within 90 days of receipt.
> 4. Revisions. Contractor will make all revisions requested by Client until Client is satisfied.
> 5. Ownership. All work product, including drafts, concepts and unused designs, is the sole property of Client from the moment of creation.
> 6. Term and termination. This Agreement runs until the Services are complete. Client may terminate at any time on written notice. On termination Client will have no further payment obligation.
> 7. Non-competition. For 24 months after this Agreement ends, Contractor will not provide design services to any business in the food and beverage industry.
> 8. Indemnity. Contractor will indemnify Client against all claims, losses and costs arising from the Services.
> 9. Confidentiality. Contractor will keep Client's information confidential indefinitely.
> 10. Governing law. This Agreement is governed by the laws of Delaware and disputes will be heard in the courts of Delaware.
> 11. Entire agreement. This document is the entire agreement between the parties.
> 
> On our call they said they'd pay half up front, by the way.

Pass: chooses agreement-check; side stated as contractor; not-legal-advice said once; "You must" and "They must" lists; table with the fee, 90 days and termination; findings most serious first, each with a quote and clause number, catching no pay on termination (6), ownership from creation (5), the 24-month non-compete (7), unlimited revisions (4), one-way indemnity (8), open-ended scope (1) and 90-day payment after acceptance (3); does not say the non-compete is or is not enforceable in Ohio; ties the spoken half-up-front promise to clause 11; lists what is missing; questions and a send-ready message; a line on when a lawyer is worth it; invents nothing.

### T2 (should trigger) lease, user away
> what am I agreeing to in this lease? heading into a shift, can't reply for hours, just give me what you can
> 
> RESIDENTIAL LEASE - Unit 4B, 220 Harbor Street
> Landlord: Kestrel Property Group. Tenants: Sam Reyes and Jordan Pike.
> 
> 1. Term. 1 February 2027 to 31 January 2028.
> 2. Rent. $1,650 per month, due on the 1st. A late fee of $150 applies from the 2nd, plus $25 for each further day.
> 3. Deposit. Tenant will pay a deposit of $1,650 and a non-refundable move-in fee of $400.
> 4. Utilities. Tenant pays electricity, gas, water and ________.
> 5. Renewal. This lease renews automatically for a further twelve months at the rent then set by Landlord unless Tenant gives written notice at least 60 days before the end of the Term.
> 6. Entry. Landlord and its agents may enter the Unit at any time for any purpose.
> 7. Repairs. Tenant is responsible for the cost of all repairs to the Unit and its appliances, whatever the cause.
> 8. Liability. Each Tenant is jointly and severally liable for all sums due under this lease.
> 9. House Rules. Tenant will comply with the House Rules as amended by Landlord from time to time, which form part of this lease.
> 10. Early termination. If Tenant leaves before the end of the Term, all remaining rent becomes immediately due.
> 11. Pets. No pets without Landlord's written consent.

Pass: chooses agreement-check; asks nothing and states its assumptions; table with rent, late fee, deposit, move-in fee, dates, renewal and exit; total over the term shown ($19,800 rent); notice date worked out (2 December 2027); findings quoted for renewal at a rent set by the landlord (5), entry at any time (6), all repairs (7), all remaining rent due (10), late fees (2), joint liability in plain words (8), House Rules not provided and changeable (9), and the blank in clause 4; no enforceability rulings; send-ready message. Round 2 adds: about 1,000 to 1,300 words; "If you only do three things" near the top; at most four findings marked High; two worked figures; suggested figures labelled as suggestions.

### T3 (near miss) drafting a new contract
> I'm a freelance logo designer and I just landed my first proper client, a local bakery. Can you write me a contract I can send them? Flat fee $1,200, two rounds of revisions, half up front. I don't have anything to start from.

Pass: does not choose agreement-check.

### T4 (near miss) negotiating pay
> Got my offer letter from Halden Logistics today: Operations Analyst, base $82,000, start 4 January. I'm happy with everything else in it, but I think the pay is low; similar roles I've seen are around $92-95k. Help me write the email asking for more. How much should I ask for?

Pass: does not choose agreement-check.

### T5 (should trigger, round 2 only) subscription terms that cannot be negotiated, direct "is it legal" question
> about to click accept on this for my one-person bookkeeping business. anything risky in these terms? and is that auto-renew thing even legal in California?
> 
> LEDGERLY SUBSCRIPTION TERMS (last updated 3 March 2026)
> 
> 1. Plan. You are subscribing to Ledgerly Pro. Your first 30 days are free. After the trial we will charge the card on file $49 per month, billed annually in advance.
> 2. Renewal. Your subscription renews automatically each year at our then-current price. To avoid renewal you must cancel at least 30 days before your renewal date by calling our support line during business hours.
> 3. Refunds. All fees are non-refundable, including for unused months.
> 4. Changes. We may change these Terms or our prices at any time by posting the new version on our website. Continued use means you accept the changes.
> 5. Your data. You grant us a perpetual, worldwide licence to use, copy and analyse the data you upload to operate and improve our services and to develop new products. After your account ends we may delete your data at any time without notice.
> 6. Service. The service is provided "as is". Our total liability to you is limited to $50.
> 7. Disputes. Any dispute will be resolved by binding individual arbitration in Austin, Texas. You waive any right to take part in a class action. You may opt out of this clause by emailing optout@ledgerly.example within 30 days of accepting these Terms.
> 8. Suspension. We may suspend or close your account at any time for any reason.

Pass: chooses agreement-check; answers the direct question in a few lines after the verdict without ruling; gives "Your choices" in place of a change message (arbitration opt-out by email within 30 days, cancel reminder, weigh-up); table shows the 30-day trial, $49 x 12 = $588 charged at once, renewal at the then-current price, cancel by phone 30 days before, no refunds; findings quoted for the data licence (5), changes by posting (4), phone-only cancelling (2), no refunds (3), the $50 limit (6), arbitration in Texas (7) and suspension (8); accepts nothing and emails nothing.

### T6 (near miss, round 2 only) a dispute already filed
> My old landlord kept my whole $2,100 deposit and I filed in small claims last month. Hearing is 9 December. The lease I signed said "Tenant shall return the premises in broom-clean condition" and they're claiming $2,100 for repainting and carpet. Help me put together what to say to the judge and what evidence to bring.

Pass: does not choose agreement-check.

### T7 (should trigger, round 3 only) NDA mentioned, no document supplied
> anything risky in this NDA? a company I might do some consulting for wants it signed and back by Monday

Pass: chooses agreement-check; asks for the text (pasted, attached or a link) and stops; no review from the type alone and no list of "typical NDA risks"; does not ask where the person is; short.

### T8 (should trigger, round 3 only) offer letter already signed
> I signed this offer letter yesterday and sent it back, and now I'm second-guessing it. What did I actually agree to? I'm in Nairobi. In the interview they told me I could work from home two days a week.
> 
> TAMARIND FREIGHT LIMITED
> Offer of employment: Customer Operations Lead
> 
> Dear Wanjiru,
> 
> 1. Role and start. We are pleased to offer you the position of Customer Operations Lead, starting 4 January 2027, reporting to the Head of Operations.
> 2. Pay. Your gross salary will be KSh 180,000 per month, paid on the last working day of each month. Any bonus is at the Company's sole discretion.
> 3. Sign-on payment. You will receive a sign-on payment of KSh 150,000 with your first salary. If your employment ends for any reason within 24 months of your start date, you will repay the sign-on payment in full, and the Company may deduct it from any sums owed to you.
> 4. Hours and place of work. Your hours are those required by the needs of the business. No additional payment is made for extra hours. Your place of work is the Company's Nairobi office or any other location the Company may designate.
> 5. Probation. The first six months are a probationary period, which the Company may extend. During probation the Company may end your employment on 7 days' notice; you must give 30 days' notice.
> 6. Notice after probation. The Company may end your employment on one month's notice. You must give three months' notice.
> 7. Leave. You are entitled to 21 working days of annual leave. Unused leave is forfeited at year end.
> 8. Training. If the Company pays for any training and you leave within 12 months of completing it, you will repay its full cost.
> 9. After you leave. For 12 months after your employment ends you will not work for, advise or hold an interest in any freight, logistics or courier business in East Africa.
> 10. Handbook. You will comply with the Employee Handbook as amended by the Company from time to time, which forms part of your terms of employment.
> 11. Whole agreement. This letter and the Employee Handbook are the whole agreement between you and the Company and replace anything said or written before.
> 
> Signed for the Company: A. Mbeki, Head of People
> Accepted: Wanjiru N., 20 November 2026

Pass: chooses agreement-check; verdict worded as what the person has agreed to, with no "ready to sign" and no "Before you sign" section; says changes now need the other side's consent and that some places give a period to cancel, without saying it applies; no ruling on the 12-month restriction (9); table with the salary, the sign-on payment repayable within 24 months, notice on each side in and after probation, and leave; findings quoted for sign-on repayment for any reason (3), uneven notice (5, 6), the restriction (9), hours and place (4), the Handbook not provided and changeable (10), training repayment (8), and the home-working promise set against clause 11; an "In your favour" line; any figure the model proposes labelled as a suggestion in the line before the message; unknowns in [brackets]; a body named only if sure; within about 1,300 words; nothing sent.

### T9 (should trigger, round 3 only) long consulting agreement
The prompt is a made-up consulting agreement of 24 clauses and two schedules, about 2,600 words (the user calls it eleven pages), too long to reproduce here. The user is the contractor, in Lisbon, wants it back by the end of the following week, and mentions being told on a call that invoices are "paid within two weeks".

Pass: chooses agreement-check; within about 1,800 words (fail above 2,400); at most about eight findings, three or four High, at least one resting on several clauses; catches pay only on acceptance at the client's sole discretion and 75-day payment, ownership of the contractor's own materials before payment, a worldwide 18-month restriction, unlimited indemnity against a three-month cap on the client's side, seven days' notice with no pay for work in progress, scope changes with no fee change, auto-renewal that only the contractor must stop (90 days' notice by registered post), one-sided variation, arbitration in New York with a client-appointed arbitrator and costs, policies not provided, and a "rate to be agreed"; total over the term EUR 57,600; notice date about 2 November 2027 with the caveat that it is a count and the way notice must be given; the spoken promise tied to the whole-agreement clause; "In your favour"; the figures label before and after the message; no ruling on the restriction or on New York law; a specific lawyer line; nothing sent.

## Results

### Round 1

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T1 | agreement-check | 97 | Passed on content: all seven planted clauses found and quoted, spoken promise tied to clause 11, no ruling on the non-compete, send-ready message, lawyer line. Problems: 1,919 words; five findings marked High; the draft message stated a fact about the user that the user never gave; two bar associations named from general knowledge; the skill did not say where to answer a direct enforceability question, how to treat a contract governed by another state's law, or how to do the worked figures for someone who is being paid. |
| T2 | agreement-check | 97 | Passed on content: asked nothing, assumptions stated, sums and notice date right, every planted clause quoted, blank and missing House Rules flagged, no rulings. Problems: 2,237 words for an 11-clause lease and a hurried user; five worked figures; five Highs; replacement figures in the message chosen by the model (it said so); the skill did not cover a side with no duties. |
| T3 | none | 90 | Passed. |
| T4 | none | 88 | Passed. The tester noted that "job offer letter" early in the description pulls a little; the exclusion at the end settled it. |

Fixes after round 1 (body only): a length aim and caps on list sizes; "If you only do three things" for a hurried or absent reader; where and how to answer a direct "is this legal" question; a different governing law reported as a finding only; name a body only if sure it exists; nothing invented about the person, unknowns in [brackets]; proposed figures allowed but labelled; two worked figures, with a version for someone being paid; High kept to three or four; what to write when one side has no duties.

### Round 2

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T2 rerun | agreement-check | 97 | Passed, except length: 1,359 words (was 2,237) against an aim of about 1,000. "If you only do three things" present, four Highs, two worked figures in the table, figures labelled, unknown names in brackets, no rulings. |
| T5 | agreement-check | 96 | Passed, except length: 1,230 words. Direct question answered in four lines with no ruling; "Your choices" used; opt-out and cancel dates worked out with the assumed acceptance date stated; all planted clauses quoted; nothing accepted or sent. |
| T6 | none | 90 | Passed. |

Fixes after round 2 and the two reviews (body only) are listed under Independent reviews below.

### Round 3 (extra round, run on the text as it stood after review 2)

| Test | Chose | Confidence | Result |
|---|---|---|---|
| T7 | agreement-check | 96 | Passed. 109 words: asked for the text, said which side it would read from, noted the deadline; no review and no "typical" risks. The tester was unsure whether such a reply should mention the deadline, the not-legal-advice line or general watch-points. |
| T8 | agreement-check | 88 | Passed. 1,357 words by a plain word count that includes table marks (1,270 counting words only), after applying every listed cut. Signed-case wording right, no "Before you sign", no ruling, sums and dates right, every planted clause quoted, spoken promise tied to clause 11, figures label before and after the message, no body named. Confidence was lower because the description says "about to sign". The tester had to guess how to write the change message for a signed agreement (it asked for a written addendum) and found the cancel-period line a poor fit for a job. |
| T9 | agreement-check | 97 | Passed. 2,075 words against an aim of about 1,800. Eight findings, four High, two resting on several clauses; every planted clause caught; EUR 57,600 and 2 November 2027 right, with the count caveat and registered post; no ruling on the restriction or New York law. The tester noted that more than four findings met the High test, and that about eleven change requests could not all be written as "change '...' to '...'" inside the length aim, so most were one line each. |

Fixes after round 3 (body only, five lines, **not run**): the no-document reply stays short, lists no "typical" risks and may say it will lead with the urgent points; for a signed agreement the cancel-period line is limited to purchases and subscriptions, the change message is kept as a request for a written amendment, and the useful "Before you sign" lines move elsewhere; the word aim counts the table and the message; if more than four findings would be High, the verdict says the agreement is one-sided throughout; with many changes, only the High ones quote old and new wording.

Triggering over three rounds: 7 of 7 should-trigger runs chose the skill (confidence 88 to 97); 3 of 3 near misses chose no skill (88 to 90).

## Independent reviews

Three fresh reviewers, told to score strictly. Reviewer 1 saw the round 2 text; reviewer 2 saw the text after the fixes for review 1, plus review 1; reviewer 3 saw review 2, the round 3 prompts, replies and logs, and the text after the round 3 fixes.

| Line | Review 1 | Review 2 | Review 3 (final) |
|---|---|---|---|
| Relevance | 5 | 5 | 5 |
| Trigger clarity | 4 | 4 | 4 |
| Correctness | 4 | 4 | 4 |
| Usability | 3 | 3 | 4 |
| Brevity | 4 | 4 | 4 |
| Provenance | 4 | 4 | 4 |

Review 1 asked for: a rule on what gives way when the reply runs long; a sharper test for "in a hurry"; one place for the "in your favour" line; a caveat on worked-out deadlines; handling of two agreement types at once and other languages; findings that rest on several clauses; and runs of the untested branches. It also flagged wording that could mislead ("common practice, not legal requirements"; the already-signed line; where the label on suggested figures sits; "advise accepting it knowingly"; naming bodies) and claims with no source. All the wording fixes were made; the extra test runs were not, because both allowed rounds had been used.

Review 2 confirmed that every wording finding was resolved in the text (one only in part: how notice must be delivered) and found no line that reads as legal advice or as a ruling on enforceability. It kept Usability at 3 and said the whole gap between 3 and 4 is missing tests: the edits made after round 2 have never been run, the word aim was missed in both runs that tested it, and four set-up branches have never been run. It said one more round of four runs would lift it. It also found three small problems the edits had introduced (the example lagging the rules, the governing-law rule sitting under the wrong bullet, no marker on translated quotes) and five one-line gaps (wording for an already-signed agreement, a lawyer line scaled to the size of the deal, severity relative to the deal, a link that cannot be opened, a ceiling for long documents).

Those eight small points and the second half of the notice-delivery point were then fixed in the text; round 3 ran that text.

Review 3 found that every branch reviewer 2 named was run and passed, recounted the sums and dates in the T8 and T9 replies, and judged the five edits made after round 3 sound, with none reading as legal advice or a ruling on enforceability. It called Usability a borderline 4: the 1,000-word aim for a short agreement has not been met in any run (1,230 to 1,359 words), and the edits after round 3 are unrun. It called Brevity a low 4 (90 lines, but long ones, with a few repeats). It required no fixes. It listed three small conflicts, each a one-line fix: a signed agreement whose terms cannot be negotiated (change message or choices), a Medium definition that no longer fitted findings held below High, and "many changes" with no number.

Those three one-line fixes were then made. **They, like the five edits after round 3, have not been run, and they have not been reviewed.**

## Open items

1. Eight small body edits are unrun: five made after round 3 (seen by reviewer 3) and three made after review 3 (seen by no reviewer).
2. The aim of about 1,000 words for a short agreement has not been met in any run; replies landed at 1,230 to 1,359 words. In practice the limit is the "a third over" line where cutting starts.
3. The description was left as tested. Known soft spots: "job offer letter" pulls slightly on pay requests; it says "about to sign" while the body also explains an agreement already signed (chosen at 88 in that run, against 96 to 97 elsewhere).
4. Never tested: a tax question and "summarise this report" as near misses; an unreadable attachment; a link to public terms (no run used a live page); a document in another language; a request where the person's side is unclear; a full NDA review (the NDA run stopped at asking for the text); signed terms that cannot be negotiated.
5. The sources were read through a summarising fetch tool, not verbatim.
6. Brevity: the file is 90 lines but several are long paragraphs, and a few points are said more than once.

## What these tests do not show

- That the reviews are right about any real agreement. The test documents were short, made up, and written with planted problems; real agreements are longer and subtler.
- That the skill catches every risky clause, or that its severity labels match what a lawyer would say. No lawyer checked any output.
- Anything about the law of any place. The skill is built to avoid ruling on that, and the tests only checked that it did avoid it.
- How it behaves in other models, in other languages, or with documents longer than the one long test (about 2,600 words).
- Consistency: each prompt was run once per round.
