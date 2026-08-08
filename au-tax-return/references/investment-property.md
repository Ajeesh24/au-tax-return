# Investment (rental) property

Covers rental income and the full deduction stack. This is where the biggest,
most-often-missed deductions live, so be thorough. Every figure is **per owner's
share** and **apportioned for private use / part-year availability**.

## Questions to establish first

1. **Ownership** — who is on the title and each **share** (e.g. 50/50). Each owner
   reports only their share of income *and* every deduction.
2. **Availability** — was it rented or **genuinely available for rent** for the whole
   income year? If it was owner-occupied part of the year, or listed only part-year,
   apportion by days available. Days it was used privately or not genuinely available
   are excluded.
3. **First year owned?** Interest, borrowing costs and capital works often start
   part-way through the year (from settlement/rental start date).
4. **Loans** — how many, and **what each was used for**. Interest is deductible only
   to the extent the borrowed money was used for the income-producing property
   (includes a separate **equity loan** if its drawdown was fully used for the IP).

## Rental income

- Rent received (or receivable), plus any **bond retained**, **insurance payouts for
  lost rent**, **reimbursements** from tenant. From the managing-agent annual
  statement where available.
- myTax: Income → Rent, per property, **at the owner's share**.

## Deductions — three buckets (this distinction is the core of getting it right)

### 1. Immediately deductible (claim the full year's amount now)

Interest on investment loan(s); council rates; water rates & charges; land tax;
building & landlord insurance; property agent fees/commission & letting fees;
advertising for tenants; repairs & maintenance (see below); pest control; cleaning;
gardening/lawn; body corporate/strata fees (admin fund); smoke alarm & safety checks
(electrical/gas); minor servicing; bank fees on the rental account; quantity surveyor
fee for the depreciation schedule; phone/postage for managing the property.

### 2. Deductible over time

- **Borrowing expenses** (loan establishment fee, LMI, title/mortgage stamp duty for
  the loan, valuation, mortgage broker fee) — spread over **5 years or the loan term
  if shorter** (immediate if total ≤ $100). Pro-rata in the first year by days.
- **Capital works — Division 43** — construction cost of the building & structural
  improvements written off at **2.5% per year over 40 years**. Take the year's figure
  **from the depreciation schedule** (part-year in the first year).
- **Depreciating assets — Division 40** — decline in value of plant & equipment
  (carpet, blinds, oven, hot-water system, air-con). **But**: for **second-hand
  residential** property bought after 7:30pm 9 May 2017, you **cannot** claim Div 40
  on previously-used assets — the schedule flags these "not eligible". You *can* still
  claim Div 40 on assets **you newly purchased** for the property.

### 3. Not deductible (capital — go to CGT cost base instead)

- **Improvements / betterment** (e.g. adding a new structure, upgrading beyond original
  condition, initial repairs to fix defects present at purchase). These are capital —
  either Div 43 capital works or a depreciating asset, and/or added to the CGT cost base.
- Stamp duty on the **purchase** of the property, conveyancing on purchase/sale, agent's
  selling commission — **cost base** for CGT, not a rental deduction.
- Principal portion of loan repayments; private-use portion of any expense.

## Repairs vs improvements (decide for each invoice)

- **Repair** = restoring to original condition (fixing a leaking tap, replacing broken
  fly-screens with equivalents, patching, re-fixing a lock) → **immediate deduction**.
- **Initial repair** = fixing something that was already damaged/worn *when you bought
  it* → **capital**, not immediately deductible.
- **Improvement** = better than original, or a whole new asset (new kitchen, new
  structure, replacing an entire fence with a superior one) → **capital works or
  depreciating asset**.
- Replacing an entire item with a like-for-like functional equivalent may be a repair;
  replacing with something better is an improvement. When genuinely unclear, present
  both treatments and let the user decide, noting the safer position.

## Apportionment

- **Ownership share** applied to income and every deduction.
- **Days available for rent** fraction applied to time-based expenses (interest, rates,
  insurance, capital works, depreciation) when not rented/available all year.
- **Loan use %** — if a loan is part private, only the income-producing portion of
  interest is deductible.

## Negative gearing

If total deductions exceed rental income, the **net rental loss** is deductible against
the owner's other income (salary etc.), reducing overall tax. Feed the per-owner net
rental (negative) into `scripts/tax_calc.py` as `net_rental`.

## myTax form-filling output for this section

**Match the myTax Rent screen exactly.** For EVERY field, myTax asks for a **Total**
(whole-property, 100%) value AND **Your share** value — so output *both* columns for
every line. myTax computes the read-only totals (gross rent, total expenses, net rent).

Output the property block in this exact order and with these exact field names:

**Rental property details**
- `Property name → ____`
- `Address → ____`
- `Date property genuinely available for rent → dd/mm/yyyy`
- `Number of weeks property was rented this year → ____`
- `Ownership percentage → ____%`

**Rental income** — give Total and Your share:
- `Total rental income → $____`  |  `Your share of rental income → $____`
- `Total other rental-related income → $____`  |  `Your share → $____`
  (bond retained, insurance payouts, tenant reimbursements)

**Rental expenses** — myTax lists these exact fields, each with Total + Your share.
Only output the ones that apply; map the user's expenses to these names:
- `Advertising`
- `Body corporate fees`
- `Deductible borrowing expenses` — spread over 5 years; this year's portion only
- `Cleaning`
- `Council rates`
- `Capital allowances – manually calculated` — **Div 40** decline in value (eligible/
  new assets only; not second-hand residential plant)
- `Gardening`
- `Insurance`
- `Interest on loans` — combine all deductible loan interest (main + equity loan)
- `Land tax`
- `Legal fees`
- `Pest control`
- `Agent fees` — property manager commission + letting fees
- `Repairs` — immediate repairs & maintenance (not improvements)
- `Capital works – manually calculated` — **Div 43** (2.5%), this year's amount from
  the depreciation schedule
- `Stationery, phone and postage`
- `Travel expenses` — note: travel to inspect residential rental is generally NOT
  deductible for individuals; usually leave blank
- `Water charges`
- `Other expenses` — anything not fitting above (e.g. safety-check fees, quantity
  surveyor fee, smoke alarm servicing, sundry)

**Ground every figure in its source document.** For each line, show the working AND
the document(s) it came from, so the amount is fully traceable, e.g.:

`Interest on loans → Total $3,367.65 | Your share (50%) $1,683.83`
  · $2,490.11 main loan + $877.54 equity loan — *bank interest summary*

Where a field aggregates several invoices, list each one with its amount and supplier
so the total is auditable, e.g.:

`Repairs → Total $451.50 | Your share (50%) $225.75`
  · $82.50 lock replacement — *Invoice: front lock*
  · $287.00 tap/mould fix — *Invoice: maintenance services*
  · $82.00 fly-screen repair — *Invoice: glass & screens*

If an expense doesn't obviously map (e.g. an electrical/gas safety check), put it in
`Repairs` if it's a repair or `Other expenses` otherwise, name the source invoice, and
note the choice so the user can confirm. **Never enter a rental figure without a
source document or an explicit user-stated amount behind it** — if you can't tie a
number to a document, ask the user rather than guessing.

> Tip: myTax also offers a **"Depreciation and capital allowances tool"** that
> computes Div 40/Div 43 for you. If the user prefers that, they enter asset details
> there instead of typing the capital allowances/capital works figures manually — tell
> them the totals from the depreciation schedule either way.
