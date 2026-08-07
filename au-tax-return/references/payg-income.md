# PAYG income & work-related deductions

Covers salary/wages income and the deductions an employee can claim. Goal: capture
all income correctly (matches ATO prefill) and every legitimate work-related deduction.

## Income to capture

| Item | myTax location | Notes |
|---|---|---|
| Salary & wages, per employer | Income → Salary/wages | Gross + tax withheld from each income statement |
| Allowances | shown with salary | Some are assessable; a matching deduction may offset them |
| Reportable fringe benefits (RFBA) | Income statement section | Not taxed directly but counts for MLS, offsets, HELP |
| Reportable employer super (RESC) | Income statement section | Same — affects income tests |
| Lump sum payments / ETP | separate labels | Ask if present |
| Bank interest | Income → Interest | From bank tax summary |
| Dividends (franked/unfranked + franking credits) | Income → Dividends | Franking credits are a refundable offset |

Ask: **how many employers**, any **interest/dividends**, any **allowances** on the
income statement, and whether they had **more than one job** (affects whether enough
tax was withheld).

## Work-related deduction categories (D-labels)

Ask which of these apply, then get amounts + whether records exist:

- **D1 Car expenses** — cents-per-km (max 5,000 business km, rate in `rates.md`) OR
  logbook (business % of actual costs). Home→work commuting is **not** deductible;
  travel between jobs/sites is.
- **D2 Travel** — work travel, accommodation, meals on work trips (not commuting).
- **D3 Clothing/laundry** — compulsory uniform, protective, occupation-specific
  clothing. Not conventional clothes. Laundry $1/load simple claim.
- **D4 Self-education** — courses connected to *current* income-earning work.
- **D5 Other work-related** — **working from home** (fixed rate per hour in `rates.md`,
  covers energy/phone/internet/consumables; requires hours record), tools & equipment
  (immediate write-off if ≤ $300 each, else depreciate), union/professional fees,
  professional subscriptions, phone/internet work %, seminars.
- **D6 Low-value pool depreciation** — for assets being depreciated.
- **D7 Interest deductions** / **D8 Dividend deductions** — costs of earning interest/
  dividends (e.g. investment loan interest, management fees).
- **D9 Gifts/donations** — to deductible gift recipients (DGRs) only; keep receipts.
- **D10 Cost of managing tax affairs** — **last year's tax-agent fee**, tax software,
  ATO interest charges. Commonly forgotten.

## Substantiation

- Total work-related claims **≤ $300**: no written evidence required (still must be
  genuinely incurred and work-related).
- **> $300**: keep receipts. Car logbook valid 5 years. WFH needs an hours record.
- Allowance received ≠ automatic deduction — must have actually incurred the expense.

## Optimisation prompts (ask about the commonly-missed ones)

- Working-from-home hours — even hybrid workers can claim.
- Phone & internet work-use percentage.
- Union / professional association fees, professional indemnity/registration.
- **Income-protection insurance** premiums (if not through super) — deductible.
- Self-education directly related to current job.
- Last year's tax-agent fee (D10).
- Donations to DGRs.
- **Personal deductible super contributions** — if they made after-tax contributions
  and lodged a valid *notice of intent to claim* with the fund, this is a deduction
  (subject to the concessional cap). Ask — this is a big, often-missed lever.
- Tools/equipment bought for work.

## myTax form-filling output for this section

Produce, per employer:
- `Salary/wages — [Employer] — Gross payment → $____`
- `Salary/wages — [Employer] — Tax withheld → $____`

Then deductions, each as: `[D-label] [description] → $____`, with a note on method
(e.g. "D1 car — cents/km: 1,200 km × 88c").
