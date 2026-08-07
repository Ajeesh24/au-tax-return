# Rates & rules by income year

> ⚠️ **Verify against ato.gov.au before lodging.** These figures are compiled for
> convenience and reflect the law understood to apply *in each named income year*.
> Rates and thresholds are indexed/changed regularly. Always confirm the number
> for the user's year on the ATO website. **Use the row for the user's chosen
> income year — not "current" law.**
>
> The machine-readable copy the calculator uses lives in
> `scripts/rates.json`. **Keep the two in sync.** When you add or correct a year,
> edit both files.

Australian income years run **1 July → 30 June** and are named by the two calendar
years they span (e.g. "2025–26" = 1 Jul 2025 – 30 Jun 2026).

---

## Resident individual income tax rates

Foreign residents and working-holiday makers use different scales — if the user is
not a resident for tax purposes, do **not** use these; ask and look up the correct
scale for their status and year.

### 2024–25 (from 1 July 2024 — revised "Stage 3" brackets)

| Taxable income | Tax on this income |
|---|---|
| $0 – $18,200 | Nil |
| $18,201 – $45,000 | 16c per $1 over $18,200 |
| $45,001 – $135,000 | $4,288 + 30c per $1 over $45,000 |
| $135,001 – $190,000 | $31,288 + 37c per $1 over $135,000 |
| $190,001 and over | $51,638 + 45c per $1 over $190,000 |

### 2025–26

Brackets and marginal rates are **unchanged from 2024–25** (same table as above).
*(Verify — legislated cuts to the 16% rate were proposed to start from 1 July 2026,
i.e. the 2026–27 year, not this one.)*

Excludes the 2% Medicare levy (added separately).

---

## Medicare levy

- **Rate: 2%** of taxable income (both years).
- **Low-income thresholds (reduced/zero levy below these)** — these are indexed each
  year; the singles threshold is roughly **$26,000–$27,000** and the family threshold
  higher, with a phase-in range. **Look up the exact figure for the user's year on
  the ATO "Medicare levy reduction — income thresholds" page before applying a
  reduction.** For most full-time earners the full 2% applies.

## Medicare levy surcharge (MLS)

Applies **only if** the person (and family) did **not** have an appropriate level of
private hospital cover for the period, **and** income for MLS purposes exceeds the
tier-1 threshold. Rates by tier (both 2024–25 and 2025–26 — verify thresholds each year):

| Tier | Singles income | Families income* | Surcharge |
|---|---|---|---|
| Base | ≤ $97,000 | ≤ $194,000 | 0% |
| Tier 1 | $97,001 – $113,000 | $194,001 – $226,000 | 1.0% |
| Tier 2 | $113,001 – $151,000 | $226,001 – $302,000 | 1.25% |
| Tier 3 | ≥ $151,001 | ≥ $302,001 | 1.5% |

\* Family threshold increases by $1,500 for each dependent child after the first.
MLS is calculated on a broader "income for MLS purposes" base (taxable income +
reportable fringe benefits + reportable super + net investment losses etc.).
**Confirm current-year thresholds on ATO — they have been indexed.**

---

## Low Income Tax Offset (LITO)

| Income | Offset |
|---|---|
| ≤ $37,500 | $700 (max) |
| $37,501 – $45,000 | $700 − 5c per $1 over $37,500 |
| $45,001 – $66,667 | $325 − 1.5c per $1 over $45,000 |
| > $66,667 | Nil |

Applies both 2024–25 and 2025–26 (verify). LITO is non-refundable — it can reduce
tax to nil but not below.

---

## Capital gains tax

- **50% CGT discount** for individuals on assets held **> 12 months** (both years).
- Ordering: **apply current-year capital losses, then carried-forward losses, then
  the 50% discount** to the remaining gain. Never discount before applying losses.
- Capital losses cannot offset ordinary income; they carry forward indefinitely.
- Main residence exemption may fully/partly exempt the family home (conditions apply).

---

## Work-related rates

### Car — cents per kilometre method (max 5,000 business km per car)

| Year | Rate |
|---|---|
| 2024–25 | **88c per km** *(verify)* |
| 2025–26 | **88c per km** *(verify — may be re-set; ATO announces annually)* |

### Working from home — fixed rate method

| Year | Fixed rate |
|---|---|
| 2024–25 | **70c per hour** *(verify)* |
| 2025–26 | **70c per hour** *(verify)* |

Covers energy, phone, internet, stationery, consumables. Requires a record of hours
worked from home. Alternative: actual-cost method.

### General substantiation

- Work-related deduction claims totalling **≤ $300** don't need written evidence
  (but must still be genuinely incurred and related to earning income). Over $300 →
  keep receipts.
- Car logbook is valid for 5 years; needed for the logbook (actual %) method.

---

## HELP / HECS study loan

Compulsory repayment is a % of "repayment income" that rises with income, and the
**repayment thresholds are indexed every year**. Do **not** hardcode — look up the
current-year HELP repayment thresholds/rates on ATO for the user's year and apply.
myTax calculates this automatically; the estimate here should note it as approximate.

---

## Adding a new income year

1. Add a section above with the bracket table and any changed thresholds/rules.
2. Mirror the numbers into `scripts/rates.json` under the year key.
3. Mark anything you couldn't verify with *(verify)* and tell the user.
