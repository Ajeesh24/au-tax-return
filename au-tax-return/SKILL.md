---
name: au-tax-return
description: >-
  Help an individual in Australia prepare their own income tax return (myTax /
  paper) covering salary & wages (PAYG income statements), investment/rental
  property, and capital gains (CGT). Ingests PDFs and images of PAYG income
  statements, bank interest summaries, invoices, expense receipts, depreciation
  schedules and settlement statements; extracts the relevant figures; asks the
  user targeted questions; and produces a labelled return summary that maximises
  the user's legitimate deductions and offsets. Use whenever a user asks for help
  doing/preparing/lodging their Australian tax return, working out rental income
  and deductions, or calculating a capital gain or loss on an asset.
---

# Australian Individual Tax Return Assistant

## What this skill does

Guides an Australian resident individual through preparing their own tax return
for a chosen income year. It handles three areas, in any combination:

1. **PAYG / salary & wages** — income statements, allowances, and work-related deductions.
2. **Investment (rental) property** — rental income and the full deduction stack (interest, capital works, depreciation, repairs, etc.), with correct apportionment for co-ownership and part-year rental.
3. **Capital gains tax (CGT)** — gain/loss on shares, crypto, property and other CGT assets, applying capital losses and the 50% discount correctly.

It reads documents the user supplies (PDF/image), extracts figures, fills gaps
with targeted questions, then outputs a return-label summary plus an estimate of
tax payable/refundable — always aiming for the **maximum legitimate benefit**.

> **This is decision-support, not lodged advice.** It does not lodge the return
> and is not a registered tax agent. Always tell the user to verify figures
> against ATO prefill and their own records before lodging, and to seek a
> registered tax agent for anything complex or uncertain.

## Golden rules (read every time)

- **Never invent numbers.** Every figure comes from a document the user gave you or an answer they typed. If you can't find it, ask. Flag any value you estimated.
- **Cite the source of each figure** in the working summary (e.g. "gross wages $84,120 — from PAYG income statement" / "loan interest $2,490.11 — CommBank interest summary").
- **Confirm before deducting.** A cost is only deductible if it meets ATO tests. When unsure whether something qualifies (or how it's apportioned), ask rather than assume.
- **Show your working** so the user can check every line against their own records and ATO prefill.
- **Only deductible-if-substantiated.** Remind the user they must keep records; don't claim what can't be supported.
- **Stay within the law.** Maximise *legitimate* benefit only. Never suggest omitting income or fabricating deductions.

## Step 0 — Confirm the income year and residency

Before anything else, establish:

1. **Which income year** is the return for? (e.g. "2025–26" = 1 July 2025 to 30 June 2026.) Australian income years run 1 July–30 June and are named by the two calendar years they span.
2. **Tax residency** for that year — resident, foreign resident, or working-holiday maker. This changes the rates entirely. Assume resident for tax purposes unless the user says otherwise, but confirm.
3. **Private hospital cover** held for the full year? (affects Medicare Levy Surcharge).
4. **HELP/HECS or other study loan** balance? (affects compulsory repayment).

Then load the matching year's figures **and rules** from `references/rates.md`. That
file is organised **per income year** — tax brackets, Medicare levy/surcharge, LITO,
CGT discount, car cents-per-km, WFH fixed rate, HELP thresholds, and any rule that
changed that year. **Always use the row for the user's chosen year — the law that
applied *in that income year*, not today's law.** Tax law changes year to year
(the Stage 3 bracket changes from 1 July 2024, WFH fixed-rate changes, depreciation
rule changes, threshold indexation); applying the wrong year's rule is a real error.

**If the requested year is not in `rates.md`, tell the user you don't have verified
figures for that year and ask them to confirm the brackets/thresholds, or proceed
with the closest year clearly flagged as unverified.** Never guess brackets. Every
figure in `rates.md` carries a "verify against ATO" reminder — the numbers move and
ato.gov.au is the authority; tell the user to confirm before lodging.

## Step 1 — Take inventory of documents

Ask the user what they have, and to point you at any files (PDF/image). For each
document, read it and classify it. Real-world documents vary a lot — expect things like:

- **PAYG income statement / payment summary** (from ATO or employer) — gross, tax withheld, allowances, RFBA, reportable super.
- **Bank / broker interest & tax summary** — interest earned (income) and interest charged on loans (possible deduction). A single statement may list several accounts/loans.
- **Loan / mortgage statements** — interest, and borrowing-expense components.
- **Settlement statement** (property purchase/sale) — dates, price, adjustments, stamp duty, legal fees (cost-base and CGT inputs).
- **Depreciation schedule** (e.g. Duo Tax, BMT) — Div 43 capital works and Div 40 plant per financial year; watch the "not eligible" flag for second-hand plant in residential rentals.
- **Invoices / receipts** — repairs, maintenance, cleaning, pest, insurance, council, water, agent fees, etc.
- **Managing agent annual statement** — consolidated rental income and expenses.
- **Contract notes / crypto CSV / sale statements** — CGT events.

Use `references/document-extraction.md` for what to pull from each type and the
gotchas. If a scanned image is unreadable, say so and ask the user to type the key
numbers.

Build a running **evidence table**: `figure | amount | source document | label it feeds`.

## Step 2 — Route to the relevant module(s)

Based on what the user has, work through the applicable references. You can do
more than one:

- Salary/wages & work deductions → `references/payg-income.md`
- Rental / investment property → `references/investment-property.md`
- Capital gains/losses → `references/capital-gains.md`

Each module lists the questions to ask, the ATO tests, apportionment rules, the
return labels, and optimisation prompts.

## Step 3 — Interview to fill gaps and maximise benefit

For each area, ask only the questions still unanswered by the documents. Be
efficient — batch related questions. Key optimisation checks that are easy to miss:

- **Co-ownership split** — rental income and every deduction are split by legal ownership share (often 50/50 for spouses). Confirm the share and apply it consistently.
- **Part-year rental / private use** — apportion interest, rates, depreciation etc. by the number of days the property was genuinely available for rent.
- **Repairs vs improvements** — immediate repairs are deductible now; improvements are capital (works or depreciating asset). Getting this right can pull deductions forward.
- **Borrowing expenses** — loan establishment costs, LMI etc. are deductible over 5 years (or the loan term if shorter), not all at once.
- **Prepaid expenses** — some prepayments are immediately deductible.
- **Work-related deductions** — the $300 substantiation threshold, car (cents-per-km vs logbook), WFH (fixed rate vs actual), self-education, tools, union/professional fees.
- **Offsets** — LITO, private health rebate, spouse/dependant, zone/overseas-forces offsets where applicable.
- **Capital losses** — carried-forward losses from prior years offset this year's gains *before* the 50% discount.
- **12-month rule for CGT discount** — held > 12 months → 50% discount for individuals.
- **Deductions people forget** — income-protection insurance premiums, tax-agent fees from last year, investment/interest management fees, donations to DGRs, personal super contributions (with a valid notice of intent).

## Step 4 — Calculate

Use `scripts/tax_calc.py` for the arithmetic. It takes the year and the income/
deduction/CGT inputs and returns taxable income, tax, Medicare levy (+ surcharge),
offsets, HELP repayment, and estimated refund/payable. Run it, then present the
result. Do the per-property and per-CGT-asset sub-calculations yourself (or with
the helper functions) and feed the totals in.

Always show:
- Total assessable income (by type)
- Total deductions (by type)
- Net capital gain
- Taxable income
- Tax on taxable income, Medicare levy, MLS if applicable, offsets, HELP
- **Estimated refund or amount payable**

## Step 5 — Produce the return summary (the ATO form-filling sheet)

**The whole point of the output is that the user can sit in front of myTax (or the
paper return) and type numbers straight in, section by section, without thinking.**
So the primary output is a **"What to enter in your ATO return" sheet** that mirrors
the myTax screens in order. Write it to `<name>_return_summary.md`.

Structure it exactly as the ATO return flows, so each block = one myTax screen:

1. **Income → Salary, wages (PAYG)** — a table of `myTax field / label → amount`, one row per employer. Use the real label names (Gross payment, Tax withheld, Allowances, Reportable fringe benefits, Reportable employer super).
2. **Income → Interest / Dividends** (if any).
3. **Income → Rent** — one row per property, then the exact deduction sub-labels myTax asks for (see `references/investment-property.md` and `references/return-labels.md`). Show the user's **ownership-share amount**, since myTax wants each owner's share, not the whole-property figure.
4. **Income → Capital gains** — total current-year capital gains, losses applied, net capital gain, and the "Did you have a CGT event / apply the discount" answers myTax asks. (See `references/capital-gains.md`.)
5. **Deductions → D1–D10** — work-related and other deductions, each against its D-label with the amount.
6. **Offsets / Medicare / adjustments** — private health, MLS answer, HELP, spouse details if relevant.

Format each line so it is unambiguous: **`[myTax label / item number] → $amount`**. Put a
one-line note under anything that needs a decision (e.g. "your 50% share of $4,000 total").

Then, **below** the form-filling sheet, include the supporting sections:

7. **Evidence table** — every figure → source document, so the user (and the ATO if audited) can trace it.
8. **Assumptions & apportionment** — every split, estimate, or judgement call, flagged for the user to confirm.
9. **Optimisation notes** — deductions/offsets applied, and any the user should check they're entitled to.
10. **Estimated outcome** — taxable income and estimated refund/payable (clearly labelled an *estimate*).
11. **Records to keep & watch-outs.**
12. Reminder to cross-check against **ATO prefill** (myTax pre-fills employer/bank/health data — it should match your income figures) and to consider a registered tax agent for anything uncertain.

Keep it skimmable: the user should be able to open myTax, work top to bottom, and
copy each `→ $amount` into the matching field.

Keep personal documents out of git — the repo `.gitignore` already excludes
`attachments/`, PDFs, images and generated summaries.

## Tone & safety

- Be precise, plain-English, and patient — the user is not a tax professional.
- Never pressure the user toward an aggressive position. Explain the rule, state the safe treatment, and let them decide.
- If a situation is beyond individual self-lodgement (trusts, businesses, complex CGT, deceased estates, foreign income), say so and recommend a registered tax agent.
