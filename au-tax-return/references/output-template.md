# Output template — "What to enter in your ATO return"

Copy this structure when writing `<name>_return_summary.md`. It mirrors the myTax
screens top-to-bottom so the user can fill the form line by line. Delete sections that
don't apply. Every `→ $amount` is a value to type into that field. All rental/CGT
amounts are the **user's ownership share**.

---

```
# <Name> — <YEAR> tax return — what to enter in myTax

Residency: <resident>   |   Private hospital cover full year: <Y/N>   |   HELP debt: <Y/N>
Prepared <date> — ESTIMATE ONLY. Cross-check every figure against ATO prefill before lodging.

## 1. Income — Salary & wages (Item 1)
- [Employer A] Gross payment → $____
- [Employer A] Tax withheld → $____
- Allowances (Item 2) → $____   (note: matching deduction at D_)

## 2. Income — Interest (Item 10) / Dividends (Item 11)
- Interest → $____
- Dividends franked → $____ ; franking credits → $____

## 3. Income — Rent (Item 21)
myTax asks for a **Total** and **Your share** for every line — enter both.

Property details
- Property name → ____
- Address → ____
- Date property genuinely available for rent → dd/mm/yyyy
- Number of weeks property was rented this year → ____
- Ownership percentage → __%

Income                                    Total        Your share
- Rental income                         → $____        $____
- Other rental-related income           → $____        $____

Expenses — show Total, Your share, and the SOURCE DOCUMENT for each.
Only list the fields that apply. Under any field built from several invoices,
itemise each invoice + supplier + amount so every dollar is traceable.

- Interest on loans        → Total $____ | share $____   — *source: bank interest summary*
    · $____ main loan  · $____ equity loan
- Capital works – manually calc. (Div 43) → Total $____ | share $____ — *source: depreciation schedule (yr _)*
- Capital allowances – manually calc. (Div 40) → Total $____ | share $____ — *source: depreciation schedule (new assets only)*
- Insurance                → Total $____ | share $____   — *source: certificate of insurance*
- Council rates            → Total $____ | share $____   — *source: council rates notice*
- Water charges            → Total $____ | share $____   — *source: water bill*
- Agent fees               → Total $____ | share $____   — *source: agent annual statement*
- Repairs                  → Total $____ | share $____   — *source: invoices (itemise below)*
    · $____ <desc> — *Invoice: <supplier>*
    · $____ <desc> — *Invoice: <supplier>*
- Pest control             → Total $____ | share $____   — *source: invoice*
- Cleaning                 → Total $____ | share $____   — *source: invoice*
- Deductible borrowing expenses → Total $____ | share $____ (yr _ of 5) — *source: loan statement*
- Other expenses           → Total $____ | share $____   — *source: <invoice(s)>*
- (Advertising, Body corporate, Gardening, Land tax, Legal fees, Stationery,
   Travel — include only if the user has a document/amount for them.)
- (myTax computes Net rent / Your share of net rent — a loss offsets other income)

## 4. Income — Capital gains (Item 18)
- Total current year capital gains → $____
- Capital losses applied (current + carried forward) → $____
- CGT discount applied → $____
- Net capital gain → $____
- Capital losses carried forward to next year → $____

## 5. Deductions (D1–D12)
- D_ <description> → $____   (method/notes)
- ...

## 6. Offsets / Medicare / adjustments
- Private health insurance: <details / rebate>
- Medicare levy surcharge: <applies? / no — had cover>
- Spouse details: <if relevant>

---

## Estimated outcome
Taxable income $____ → estimated <REFUND/PAYABLE> $____ (estimate only).

## Evidence (figure → source)
| Figure | Amount | Source document |
|---|---|---|
| ... | ... | ... |

## Assumptions & apportionment (please confirm)
- Ownership split __% (basis: ...)
- Days available for rent: ___/365
- <any estimate or judgement call>

## Optimisation notes
- Deductions/offsets applied: ...
- Check you're entitled to: ...

## Records to keep & watch-outs
- ...

## Before lodging
- Open myTax → confirm prefill matches the income figures above.
- Consider a registered tax agent for anything uncertain.
- This tool is decision-support, not lodged tax advice.
```
