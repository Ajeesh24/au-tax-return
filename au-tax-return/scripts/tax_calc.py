#!/usr/bin/env python3
"""Australian resident individual tax estimator.

Year-aware: all rates/rules come from rates.json keyed by income year, so the
calculator applies the law for the year you ask for. This is an ESTIMATE to help
someone self-prepare — always verify against ATO myTax before lodging.

Usage as a library (preferred — call from the skill):

    from tax_calc import estimate, capital_gain, rental_result

    r = estimate(
        year="2025-26",
        salary_income=90000,
        other_income=0,
        deductions=3200,          # work-related + other deductions
        net_rental=-4200,         # negative = net rental loss (negative gearing)
        net_capital_gain=1500,    # already after losses + 50% discount
        has_private_hospital_cover=True,
        is_family=False,
        tax_withheld=22000,       # PAYG withheld, to estimate refund/payable
    )
    print(r)

CLI:

    python3 tax_calc.py --year 2025-26 --salary 90000 --deductions 3200 \
        --net-rental -4200 --net-capital-gain 1500 --withheld 22000 --cover

Helper functions capital_gain() and rental_result() do the per-asset / per-property
sub-calculations with correct ordering (losses before discount) and ownership share.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass, asdict

RATES_PATH = os.path.join(os.path.dirname(__file__), "rates.json")


def load_rates(year: str) -> dict:
    with open(RATES_PATH) as f:
        data = json.load(f)
    years = data["years"]
    if year not in years:
        raise ValueError(
            f"No verified rates for income year {year!r}. Available: "
            f"{sorted(years)}. Add it to rates.json (and references/rates.md) "
            f"after verifying on ato.gov.au, or ask the user to confirm the brackets."
        )
    return years[year]


def tax_on_income(taxable: float, brackets: list[dict]) -> float:
    """Base income tax (excl. Medicare) from a resident bracket table."""
    taxable = max(0.0, taxable)
    applicable = brackets[0]
    for b in brackets:
        if taxable > b["over"]:
            applicable = b
        else:
            break
    return applicable["base"] + (taxable - applicable["over"]) * applicable["rate"]


def lito_offset(taxable: float, lito: dict) -> float:
    if taxable <= lito["full_upto"]:
        return float(lito["max"])
    if taxable <= lito["taper1_upto"]:
        return max(0.0, lito["max"] - (taxable - lito["full_upto"]) * lito["taper1_rate"])
    if taxable < lito["zero_at"]:
        # amount remaining at start of taper2
        at_taper2_start = lito["max"] - (lito["taper1_upto"] - lito["full_upto"]) * lito["taper1_rate"]
        return max(0.0, at_taper2_start - (taxable - lito["taper1_upto"]) * lito["taper2_rate"])
    return 0.0


def medicare_levy(taxable: float, r: dict) -> float:
    """Simplified Medicare levy with single-person low-income phase-in.

    Family thresholds and reductions are more complex — for family situations,
    verify against ATO. This uses the single-person low-income shade-in.
    """
    rate = r["medicare_levy_rate"]
    lower = r.get("medicare_levy_single_threshold")
    upper = r.get("medicare_levy_single_upper")
    if lower is None or taxable <= lower:
        return 0.0 if (lower is not None and taxable <= lower) else taxable * rate
    if upper and taxable <= upper:
        # 10% of the amount over the lower threshold, capped at full levy
        return min((taxable - lower) * 0.10, taxable * rate)
    return taxable * rate


def _tier_rate(income: float, tiers: list[dict]) -> float:
    for t in tiers:
        if t["upto"] is None or income <= t["upto"]:
            return t["rate"]
    return tiers[-1]["rate"]


def medicare_levy_surcharge(mls_income: float, r: dict, has_cover: bool, is_family: bool) -> float:
    if has_cover:
        return 0.0
    tiers = r["mls_family_tiers"] if is_family else r["mls_singles_tiers"]
    return mls_income * _tier_rate(mls_income, tiers)


def capital_gain(proceeds: float, cost_base: float, months_held: float,
                 prior_year_losses: float = 0.0, current_year_losses: float = 0.0,
                 discount_rate: float = 0.5) -> dict:
    """Net capital gain for one asset, applying losses BEFORE the discount.

    Returns the gross gain, gain after losses, whether the discount applies
    (held > 12 months), and the net (taxable) capital gain to include in income.
    A capital loss (negative) is returned as-is for carry-forward — the discount
    never applies to a loss.
    """
    gross = proceeds - cost_base
    if gross <= 0:
        return {"gross": round(gross, 2), "after_losses": round(gross, 2),
                "discount_applied": False, "net_gain": 0.0,
                "capital_loss_to_carry": round(-gross, 2)}
    after_losses = max(0.0, gross - current_year_losses - prior_year_losses)
    discount_applied = months_held > 12
    net = after_losses * (1 - discount_rate) if discount_applied else after_losses
    return {"gross": round(gross, 2), "after_losses": round(after_losses, 2),
            "discount_applied": discount_applied, "net_gain": round(net, 2),
            "capital_loss_to_carry": 0.0}


def rental_result(gross_rent: float, expenses: dict, ownership_share: float = 1.0,
                  days_available_fraction: float = 1.0) -> dict:
    """Net rental result for ONE owner's share of a property.

    expenses: dict of {name: amount} at 100% of the property.
    ownership_share: this owner's legal share (e.g. 0.5).
    days_available_fraction: fraction of the year genuinely available for rent
        (apportions expenses; set 1.0 for full-year rental).

    Rent and expenses are apportioned by availability then by ownership share.
    A negative result is a deductible net rental loss (negative gearing).
    """
    apportioned_rent = gross_rent * ownership_share
    total_exp = sum(expenses.values()) * days_available_fraction * ownership_share
    net = apportioned_rent - total_exp
    return {
        "gross_rent_share": round(apportioned_rent, 2),
        "total_deductions_share": round(total_exp, 2),
        "net_rental": round(net, 2),
        "expense_breakdown_share": {k: round(v * days_available_fraction * ownership_share, 2)
                                     for k, v in expenses.items()},
    }


@dataclass
class Estimate:
    year: str
    assessable_income: float
    taxable_income: float
    income_tax: float
    lito: float
    medicare_levy: float
    medicare_levy_surcharge: float
    total_tax: float
    tax_withheld: float
    estimated_refund_or_payable: float  # positive = refund, negative = payable
    notes: list[str]

    def __str__(self) -> str:
        d = asdict(self)
        lines = [f"Tax estimate for {self.year}", "=" * 34]
        money = {"assessable_income", "taxable_income", "income_tax", "lito",
                 "medicare_levy", "medicare_levy_surcharge", "total_tax",
                 "tax_withheld", "estimated_refund_or_payable"}
        labels = {
            "assessable_income": "Assessable income",
            "taxable_income": "Taxable income",
            "income_tax": "Income tax (before offsets)",
            "lito": "Less LITO",
            "medicare_levy": "Medicare levy",
            "medicare_levy_surcharge": "Medicare levy surcharge",
            "total_tax": "Total tax + levies",
            "tax_withheld": "PAYG tax withheld",
        }
        for k, lbl in labels.items():
            lines.append(f"  {lbl:<32} ${d[k]:>12,.2f}")
        r = self.estimated_refund_or_payable
        verdict = f"REFUND ${r:,.2f}" if r >= 0 else f"PAYABLE ${-r:,.2f}"
        lines.append("-" * 34)
        lines.append(f"  {'Estimated outcome':<32} {verdict}")
        if self.notes:
            lines.append("\nNotes:")
            lines += [f"  - {n}" for n in self.notes]
        return "\n".join(lines)


def estimate(year: str, salary_income: float = 0.0, other_income: float = 0.0,
             deductions: float = 0.0, net_rental: float = 0.0,
             net_capital_gain: float = 0.0, tax_withheld: float = 0.0,
             has_private_hospital_cover: bool = True, is_family: bool = False,
             mls_income_override: float | None = None) -> Estimate:
    r = load_rates(year)
    notes: list[str] = []
    if not r.get("verified", False):
        notes.append("Rates for this year are NOT verified — confirm brackets/thresholds on ato.gov.au.")

    assessable = salary_income + other_income + max(0.0, net_rental) + net_capital_gain
    # A net rental LOSS is a deduction against other income:
    rental_loss_deduction = -min(0.0, net_rental)
    taxable = max(0.0, salary_income + other_income + net_capital_gain
                  + min(0.0, net_rental) - deductions)

    inc_tax = tax_on_income(taxable, r["resident_brackets"])
    lito = lito_offset(taxable, r["lito"])
    ml = medicare_levy(taxable, r)
    mls_income = mls_income_override if mls_income_override is not None else taxable
    mls = medicare_levy_surcharge(mls_income, r, has_private_hospital_cover, is_family)

    total_tax = max(0.0, inc_tax - lito) + ml + mls
    refund = tax_withheld - total_tax

    if net_rental < 0:
        notes.append(f"Net rental loss of ${-net_rental:,.2f} offset against other income (negative gearing).")
    if mls > 0:
        notes.append("Medicare levy surcharge applied — no full-year private hospital cover. "
                     "Verify MLS income base (adds RFB, reportable super, net investment losses).")
    notes.append("HELP/study-loan repayment NOT included — myTax adds it; look up current-year thresholds.")
    notes.append("Estimate only. Cross-check every figure against ATO prefill in myTax.")

    return Estimate(
        year=year,
        assessable_income=round(assessable, 2),
        taxable_income=round(taxable, 2),
        income_tax=round(inc_tax, 2),
        lito=round(lito, 2),
        medicare_levy=round(ml, 2),
        medicare_levy_surcharge=round(mls, 2),
        total_tax=round(total_tax, 2),
        tax_withheld=round(tax_withheld, 2),
        estimated_refund_or_payable=round(refund, 2),
        notes=notes,
    )


def _cli():
    p = argparse.ArgumentParser(description="Australian resident individual tax estimate")
    p.add_argument("--year", required=True, help="e.g. 2025-26")
    p.add_argument("--salary", type=float, default=0.0)
    p.add_argument("--other-income", type=float, default=0.0)
    p.add_argument("--deductions", type=float, default=0.0)
    p.add_argument("--net-rental", type=float, default=0.0, help="negative = net loss")
    p.add_argument("--net-capital-gain", type=float, default=0.0, help="after losses + discount")
    p.add_argument("--withheld", type=float, default=0.0)
    p.add_argument("--cover", action="store_true", help="had full-year private hospital cover")
    p.add_argument("--family", action="store_true")
    args = p.parse_args()
    print(estimate(
        year=args.year, salary_income=args.salary, other_income=args.other_income,
        deductions=args.deductions, net_rental=args.net_rental,
        net_capital_gain=args.net_capital_gain, tax_withheld=args.withheld,
        has_private_hospital_cover=args.cover, is_family=args.family,
    ))


if __name__ == "__main__":
    _cli()
