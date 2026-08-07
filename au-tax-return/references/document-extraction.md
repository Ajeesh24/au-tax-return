# Document extraction guide

How to read each kind of document the user might supply, what to pull, and the
traps. Read PDFs/images directly. If a scan is unreadable, ask the user to type the
key numbers rather than guessing. **Record the source document against every figure**
so it lands in the evidence table.

General approach:
1. Identify the document type from its header/layout.
2. Extract the figures listed below.
3. Note the **date/period** — confirm it falls in the user's income year. A statement
   may span two financial years; only the portion in-year counts.
4. Note **whose name** is on it and **ownership** — for co-owned assets each owner
   reports only their share.

---

## PAYG income statement / payment summary (ATO or employer)

The modern version is an "income statement" in myGov (STP), replacing the old group
certificate. Pull:
- **Gross payments / salary & wages**
- **Tax withheld (PAYG)**
- **Allowances** (car, travel, meal, tool — some are separately itemised and may be
  offset by a deduction)
- **Reportable fringe benefits amount (RFBA)**
- **Reportable employer superannuation contributions (RESC)**
- **Lump sum / ETP** amounts if present
- Employer name/ABN, and the period.

Trap: myTax usually **pre-fills** these from the ATO. Your job is to make sure the
user's figures match prefill and that allowances/deductions are handled correctly.

## Bank / broker interest & tax summary

May list many accounts on one page (e.g. a "Interest and tax summary"). For each line:
- **Interest earned** → assessable interest income.
- **Interest charged** on a loan → potentially deductible **if the loan was used to
  produce assessable income** (e.g. an investment-property loan or equity loan drawn
  down for the property). Interest on a private/home loan is **not** deductible.
- Note the account label so you can tie a loan to its purpose (ask the user what each
  loan was used for — deductibility follows **use**, not the security).
- Watch for **TFN withholding** amounts.

## Loan / mortgage statement

- Total **interest** for the period (tie to the year).
- **Borrowing expenses** (loan establishment fee, lender's mortgage insurance, title
  search, mortgage stamp duty, valuation for loan) — deductible **over 5 years or the
  loan term if shorter**, not immediately (unless total ≤ $100).
- Redraw/offset movements — redraw for private purposes taints deductibility of that
  portion of interest; ask.

## Property settlement statement (buy or sell)

- **Contract date and settlement date** (contract date is the CGT event date).
- **Purchase/sale price**.
- **Stamp duty, legal/conveyancing fees, agent's commission, adjustments** for rates/
  water — these are **cost-base** elements for CGT (purchase) or reduce proceeds (sale).
- On a **purchase**, these feed the CGT cost base for when the property is eventually
  sold — record them even though there's no deduction now.

## Depreciation schedule (Duo Tax, BMT, etc.)

- **Division 43 capital works** — the per-financial-year deductible amount (typically
  2.5% of construction cost over 40 years). Take the amount **for the user's income
  year** from the year-by-year table (a part-year first year is common).
- **Division 40 plant & equipment** — per-year decline in value **only if eligible**.
  For **second-hand residential** property acquired after 7:30pm 9 May 2017, Div 40
  on previously-used assets is **NOT deductible** (schedules flag this "not eligible").
  Don't claim it if flagged.
- Match the schedule's **property address, ownership names, and settlement/rental
  start date** to the user's situation. Apportion by ownership share.

## Invoices / receipts (repairs, maintenance, services)

For each: **supplier, date, amount, what it was for**. Then classify (see
`investment-property.md`): immediate repair vs improvement (capital) vs a depreciating
asset. Cleaning, pest control, gardening, insurance, council rates, water, agent fees,
smoke-alarm/safety checks are typically immediately deductible when the property is
income-producing. A brand-new item or a betterment is capital.

## Managing agent annual statement

Often the single best source — consolidates **rent received, agent commission, letting
fees, repairs paid on your behalf, water/council if paid by agent**. Use it as the
spine and reconcile individual invoices against it to avoid double-counting.

## Contract notes / share & crypto records

- **Buy**: date, quantity, price, brokerage (cost base).
- **Sell**: date, quantity, price, brokerage (proceeds less selling costs).
- Match parcels for the **12-month** discount test and to compute gain/loss per parcel.
- Crypto: each disposal (including crypto-to-crypto and spending) is a CGT event.

---

## Reconciliation checklist before calculating

- [ ] Every figure has a source document or a user answer.
- [ ] Each figure's date falls in the chosen income year.
- [ ] Co-owned amounts reduced to the user's ownership share.
- [ ] No double-counting (agent statement vs individual invoices).
- [ ] Private-use / part-year apportionment applied.
- [ ] Loan interest deductibility confirmed by **use** of funds.
- [ ] Div 40 second-hand residential exclusion respected.
