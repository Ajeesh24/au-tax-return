# Capital gains tax (CGT)

Covers gains/losses on disposing of CGT assets — shares, ETFs, crypto, investment
property, collectables, etc. Goal: correct gain/loss per asset, losses applied in the
right order, 50% discount only where eligible, and the minimum legitimate net gain.

## When there is a CGT event

Disposal (sale), but also gifting, transferring, or (crypto) swapping one asset for
another or spending it. The **CGT event date is the contract/trade date**, not
settlement. The main residence (family home) is generally **exempt** — ask if the
asset was ever their home.

## Per-asset calculation

For each asset/parcel:

1. **Capital proceeds** = sale price − selling costs (brokerage, agent commission,
   legal). For property, proceeds less selling costs.
2. **Cost base** = purchase price + incidental costs of buying (brokerage, stamp duty,
   conveyancing, legal) + certain ownership costs (for property, non-deductible rates/
   interest can be included via the 3rd element if never claimed) + capital improvement
   costs. **Reduce the cost base by any capital works (Div 43) deductions already
   claimed** on a rental property.
3. **Gross gain/loss** = proceeds − cost base.
4. If a **loss**, it's a **capital loss** — cannot offset salary; carries forward
   indefinitely to offset future capital gains.

## Applying losses and the discount — ORDER MATTERS

1. Sum this year's **capital gains**.
2. Subtract this year's **capital losses**.
3. Subtract **carried-forward** capital losses from prior years.
4. **Then** apply the **50% discount** to any remaining gain on assets held **> 12
   months** (individuals). Assets held ≤ 12 months get **no discount**.
5. The result is the **net capital gain** added to assessable income.

Optimisation: apply losses **against the non-discounted (or shortest-held) gains
first** where you have a choice, so the 50% discount is preserved on the discounted
gains — this minimises the net gain. The helper `capital_gain()` in
`scripts/tax_calc.py` enforces "losses before discount"; do the cross-asset loss
allocation thoughtfully when there are several assets.

## Questions to ask

- What was disposed of, and the **buy date & sell date** (for the 12-month test)?
- Buy price + buying costs; sell price + selling costs.
- Any **carried-forward capital losses** from prior returns?
- Was it ever the **main residence**? Any period rented out?
- For an inherited or gifted asset, special cost-base rules apply — flag for a tax agent.

## myTax form-filling output for this section

- `Capital gains — Total current year capital gains → $____`
- `Capital gains — Capital losses applied (current + carried forward) → $____`
- `Capital gains — CGT discount applied → $____`
- `Capital gains — Net capital gain → $____`
- `Capital losses carried forward to next year → $____` (if any)
- Answer to myTax's "Did you have a CGT event?" = Yes, and note per-asset working in
  the evidence table so the user can reconstruct it.

Feed the final **net capital gain** into `estimate(..., net_capital_gain=__)`.
