# au-tax-return

A reusable **Claude skill** that helps an individual in Australia prepare their own
income tax return (via **myTax** or the paper return), covering:

- **PAYG / salary & wages** and work-related deductions
- **Investment (rental) property** income and the full deduction stack
- **Capital gains tax (CGT)** — gain/loss with the 50% discount and loss ordering

You give it your documents (PDFs/images of PAYG income statements, bank interest
summaries, invoices, depreciation schedules, settlement statements). It reads them,
extracts the figures, asks targeted questions to fill gaps and find every legitimate
deduction, and produces a **"what to enter in myTax" sheet** — each figure mapped to
its ATO return label so you can fill the form top-to-bottom — plus a refund/payable
estimate.

## Key properties

- **Generic & reusable** — no user or document is hardcoded; works for any taxpayer
  and any set of documents.
- **Year-aware** — it asks which income year the return is for and applies the law and
  rates *for that year* (2024–25 and 2025–26 included; add more in
  `references/rates.md` + `scripts/rates.json`).
- **Traceable** — every figure is tied to its source document in an evidence table.
- **Safe** — never invents numbers, maximises only *legitimate* benefit, and reminds
  you to verify against ATO prefill. It is **decision-support, not lodged advice**, and
  not a registered tax agent.

## Layout

```
au-tax-return/
├── SKILL.md                        # orchestration: the interview + output flow
├── references/
│   ├── rates.md                    # rates & rules PER YEAR (human-readable)
│   ├── document-extraction.md      # how to read each document type
│   ├── payg-income.md              # salary/wages + D1–D12 deductions
│   ├── investment-property.md      # rental income + deductions + apportionment
│   ├── capital-gains.md            # CGT calc, loss ordering, 50% discount
│   ├── return-labels.md            # figure → myTax/paper label map
│   └── output-template.md          # the "what to enter in myTax" output shape
└── scripts/
    ├── rates.json                  # machine-readable rates per year (calc uses this)
    └── tax_calc.py                 # tax/Medicare/CGT/rental estimator (+ CLI)
```

## Install

**One command (recommended)** — installs the skill into your Claude skills directory:

```bash
# For the current user (~/.claude/skills/au-tax-return)
npx github:Ajeesh24/au-tax-return

# Into the current project (./.claude/skills/au-tax-return)
npx github:Ajeesh24/au-tax-return --project

# Custom location, or overwrite an existing install
npx github:Ajeesh24/au-tax-return --dir <path>
npx github:Ajeesh24/au-tax-return --force
```

**Manual** — copy the `au-tax-return/` folder into your skills directory, or point
Claude at `SKILL.md`.

## Using it

After installing, **drop your PDFs/photos into the `documents/` folder**
(see `documents/README.md`), restart Claude Code (or reload skills), and ask, e.g.
*"I've added my documents — help me do my 2025–26 tax return."* Claude reads everything
in `documents/`, confirms the year and residency, interviews you, and produces the
summary. Files in `documents/` are git-ignored and stay on your machine.

Quick calculator check:

```bash
python3 scripts/tax_calc.py --year 2025-26 --salary 90000 --deductions 3200 \
    --net-rental -4200 --net-capital-gain 1500 --withheld 22000 --cover
```

## Accuracy & disclaimer

Rates in `rates.json` / `rates.md` are compiled for convenience and marked
`"verified": false` — **confirm current figures on [ato.gov.au](https://www.ato.gov.au)
before lodging.** This project does not lodge returns and is not tax advice. For
anything complex (trusts, businesses, foreign income, complex CGT), see a registered
tax agent.

## Privacy

Personal tax documents must not be committed. The repo `.gitignore` excludes
`attachments/`, `*.eml`, PDFs, images, and generated `*_return_summary.md` files.
