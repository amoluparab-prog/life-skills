# agreement-check

Status: reviewed. Three test rounds and three independent reviews were run; at the final review every rubric line scored 4 or 5 (Usability a borderline 4). Eight small edits made after the last test round have not been run, and three of them were made after the last review. Version 0.1.0.

## What it does

Helps an ordinary person read an agreement before they sign or accept it: a lease, a freelance or contractor contract, a job offer letter, a service or subscription contract, terms of service, or an NDA. Given the text and which side the person is on, it writes a review from their side:

1. What the document is, the assumptions made, and a short verdict. For someone in a hurry, the three things to do first.
2. Who must do what: "You must" and "They must".
3. One table of the money, dates, renewal and exit terms, with the total over the full term and the money at stake if it ends early.
4. The clauses that are unusual, one-sided or risky for this person, most serious first, each with a short quote, what it means, why it matters and what to do.
5. What is missing that an agreement of this kind normally has, including documents it refers to that were not provided.
6. Questions to ask the other side.
7. Suggested changes, worded as a message ready to send. For terms nobody can negotiate (terms of service, mass-market subscriptions) it gives the person's choices instead: opt-outs the document offers, reminders to set, what to weigh.
8. What to check before signing, and when a lawyer is worth paying for.

Rules it keeps throughout: every finding rests on a quote from the document, and nothing is invented; it never says a clause is or is not enforceable where the person lives, even when asked, because law differs by place; it says once that it is not legal advice; it treats the document as confidential; it never signs, sends, accepts or clicks anything.

This is a plain-language reading aid, not legal advice, and no lawyer has checked its output.

## How it differs from similar public skills

Many public contract-review skills exist. Two were read: mohitagw15856/pm-claude-skills "contract-review" (any contract; a risk rating, key terms table, flagged clauses and missing clauses; suggested actions are categories, with no drafted wording) and evolsb/claude-legal-skill (NDAs, SaaS, merchant and M&A agreements; redlines and market benchmarks; defaults to US law). Others were seen in search results and not read, among them anthropics/claude-for-legal "vendor-agreement-review" and several skills named "contract-review" or "contract-reviewer". Those are mostly aimed at business agreements and the people who negotiate them. This one is narrower on purpose: a person's own everyday agreements, read from their side, before they sign. Its own ground is the refusal to rule on enforceability, findings that must be quoted, missing terms by kind of agreement, questions plus wording ready to send, choices instead of redlines for fixed terms, and a plain statement of when a lawyer is worth the fee. Nothing was copied from those skills.

## Example

> My landlord sent this, I'm meant to sign by Friday. Anything I should worry about?

followed by a lease that includes "12. This lease renews automatically for a further 12 months unless Tenant gives 90 days' written notice" and "17. Tenant is responsible for all repairs to the premises."

The reply, in outline: "This is a 12-month home lease, read from your side as the tenant. This is a plain-language review, not legal advice." A two-line verdict and three things to do first. A table: rent $1,800 a month (clause 3), total over the term $21,600, deposit $1,800 (clause 5), renewal automatic with 90 days' notice (clause 12), early exit "not stated". Then the findings, such as:

> **High. All repairs fall on you (clause 17).** "Tenant is responsible for all repairs to the premises". As written this covers the roof, heating and plumbing. Rules on what a landlord can pass to a tenant differ by place; your local tenant advice service can tell you. Ask to limit it to damage you cause.

Then what is missing (how the deposit is returned, notice before the landlord enters), questions, and a message to send that begins "Thanks for sending the lease. Before I sign, could we make two changes?"

## Not for

Drafting a new contract or template; a dispute, claim or lawsuit already under way; tax questions; summarising a document that is not an agreement; negotiating pay or writing a salary counter-offer. It is also not a substitute for a lawyer where large sums, property, limits on future work or anything hard to undo are involved, and it says so in the review.

## Sources and credits

Public pages, read on 21 November 2026 through a summarising fetch tool (not verbatim). Sources 1, 5 and 10 were fetched again by the first reviewer and 4 and 9 by the second, and checked against the skill.

1. Financial Consumer Agency of Canada, "Before you sign any contract: 10 things you need to know": https://www.canada.ca/en/financial-consumer-agency/services/signing-contract.html
2. US Federal Trade Commission, "Getting In and Out of Free Trials, Auto-Renewals, and Negative Option Subscriptions": https://consumer.ftc.gov/getting-out-free-trials-auto-renewals-negative-option-subscriptions
3. UK Competition and Markets Authority on GOV.UK, "Unfair terms explained for businesses: full guide": https://gov.uk/guidance/unfair-terms-explained-for-businesses-full-guide
4. Fannie Mae, "Understanding your lease": https://yourhome.fanniemae.com/rent/understanding-your-lease
5. Freelancers Union, "Contracts 101": https://blog.freelancersunion.org/2014/12/19/contracts-101/
6. Citizens Advice (UK), "Check the terms of your employment contract": https://www.citizensadvice.org.uk/work/contracts-of-employment/
7. Outten & Golden, "The fine print: employment contract terms that can limit your rights at work" (a law firm's own article): https://www.outtengolden.com/newsroom/the-fine-print-employment-contract-terms-that-can-limit-your-rights-at-work/
8. US Consumer Financial Protection Bureau, "CFPB study finds that arbitration agreements limit relief for consumers" (an archived page; used only for what an arbitration clause is): https://www.consumerfinance.gov/about-us/newsroom/cfpb-study-finds-that-arbitration-agreements-limit-relief-for-consumers/
9. Oklahoma Bar Association, "Lawyers & Legal Fees": https://www.okbar.org/a2j/lawyers/
10. GOV.UK, "Private renting for tenants: tenancy agreements": https://www.gov.uk/private-renting-tenancy-agreements/what-should-be-in-a-tenancy-agreement

What the sources support: get spoken promises in writing, fill blanks, do not sign under pressure, keep a copy, know how to get out and that a cancellation period may exist under local law (1); what to find in subscription terms (2); the kinds of terms a regulator treats as potentially unfair, which shaped the watch list (3); the lease list apart from the items named below (4, 10); the freelance list (5); that verbal employment terms are hard to prove (6); the employment clauses to watch (7); what an arbitration clause does (8); when to see a lawyer and the free or low-cost routes (9).

The author's own judgement or general know-how, not taken from a source: the three severity levels and their definitions; the cap of about eight findings and 20-word quotes; the word aim, the ceiling of about 1,800 words for long documents and the order in which sections are cut; the two worked figures; inferring the person's side when it is plain; "Your choices" for terms that cannot be negotiated; "If you only do three things"; proposing moderate replacement figures labelled as suggestions; the confidentiality handling; treating documents referred to but not provided as a finding; the whole offer-letter and NDA lists; in the lease list, entry and notice, guests, and joint tenants each being answerable for all of the rent (put as a point to check); in the subscription and terms-of-service lists, refunds, service failure, data and content, account suspension and opt-out windows; the examples of when a lawyer is worth paying for beyond source 9, and weighing the fee against the money at stake; for a signed agreement, asking for a written amendment both sides sign and mentioning a cancel period only for purchases and subscriptions; saying an agreement is "one-sided throughout" when more than four findings would be High; one-line change requests when there are more than about six.

The sources are from the US, UK and Canada. The skill is written to stay neutral about place and makes no statement about what the law requires anywhere.

Built with the Forge skill. Licence: MIT, copyright Amol Parab (see the collection's LICENSE).

Testing record: [testing/agreement-check.md](../testing/agreement-check.md)
