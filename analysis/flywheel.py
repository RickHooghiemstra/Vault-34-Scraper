"""
Flywheel model for Vault 34 Exhausts — recycle every order's margin back into ads.

The idea (yours): seed the ad budget, and pump each order's contribution margin
straight back into acquisition so growth self-funds.

The one law that governs it
---------------------------
The flywheel only SPINS if  CAC < contribution-per-order (C).
  multiplier m = C / CAC
    m > 1  -> every euro of ad spend returns >1 euro to spend again -> compounding
    m = 1  -> treadmill: steady-state, no growth
    m < 1  -> it grinds DOWN: you shrink each cycle

So the whole game is: push C up (sell UK €600+ systems, not €320 silencers) and
push CAC down (tight targeting, high-intent search, CR > 0). Right now CR = 0%,
so CAC is infinite and the flywheel cannot start — fixing the funnel is the
prerequisite to spinning it at all.

Run:  python analysis/flywheel.py
"""

# Avg contribution per order for UK, €600+ product focus (see margin_model.py).
CONTRIBUTION_PER_ORDER = 120.0   # EUR
SEED_BUDGET = 500.0              # EUR, the monthly seed you top up
REINVEST_FRACTION = 1.0          # 1.0 = put ALL order margin back into ads
MONTHS = 12

# CAC scenarios to compare (EUR cost to acquire one order).
CAC_SCENARIOS = {
    "stalling (CAC 150 > C)": 150.0,
    "break-even (CAC 120)":   120.0,
    "healthy (CAC 80)":        80.0,
    "strong (CAC 50)":         50.0,
}


def simulate(cac: float) -> list[tuple[int, float, float, float]]:
    """Return [(month, ad_budget, orders, contribution)] for MONTHS months."""
    rows = []
    reinvest = 0.0
    for month in range(1, MONTHS + 1):
        budget = SEED_BUDGET + reinvest
        orders = budget / cac
        contribution = orders * CONTRIBUTION_PER_ORDER
        reinvest = contribution * REINVEST_FRACTION
        rows.append((month, budget, orders, contribution))
    return rows


def main() -> None:
    print("=" * 84)
    print(f"FLYWHEEL  |  C = EUR {CONTRIBUTION_PER_ORDER:.0f}/order  |  seed = EUR "
          f"{SEED_BUDGET:.0f}/mo  |  reinvest {REINVEST_FRACTION*100:.0f}% of margin")
    print("=" * 84)
    print("The multiplier m = C / CAC decides everything:\n")

    for label, cac in CAC_SCENARIOS.items():
        m = CONTRIBUTION_PER_ORDER / cac
        rows = simulate(cac)
        m1, m6, m12 = rows[0], rows[5], rows[11]
        cum_orders = sum(r[2] for r in rows)
        cum_contrib = sum(r[3] for r in rows)
        print(f"-- {label}   (m = {m:.2f}) " + "-" * (50 - len(label)))
        print(f"   month  1: budget EUR {m1[1]:>9,.0f}  -> {m1[2]:>6.1f} orders")
        print(f"   month  6: budget EUR {m6[1]:>9,.0f}  -> {m6[2]:>6.1f} orders")
        print(f"   month 12: budget EUR {m12[1]:>9,.0f}  -> {m12[2]:>6.1f} orders")
        print(f"   12-mo totals: {cum_orders:,.0f} orders, "
              f"EUR {cum_contrib:,.0f} contribution generated\n")

    print("=" * 84)
    print("Takeaways")
    print("=" * 84)
    print("- CAC must be BELOW EUR", int(CONTRIBUTION_PER_ORDER),
          "or the wheel grinds down no matter how much you seed.")
    print("- The first job is CR > 0 (today it's 0%): no conversion = infinite CAC =")
    print("  the wheel never starts. Fix funnel + currency BEFORE scaling spend.")
    print("- Bigger C (UK €600+ systems) widens the CAC headroom that lets it spin.")
    print("- Reinvesting margin is right, but keep a cash buffer: you pay the supplier")
    print("  for each order before the margin is realised — watch working capital.")
    print("- REALITY CHECK: this model is unbounded. In practice CAC rises as you scale")
    print("  (you exhaust the cheapest high-intent clicks) and the MT-09/MT-07 UK demand")
    print("  is finite, so the curve flattens. Treat the m>1 cases as 'it compounds')")
    print("  not as literal 12-month order counts.")


if __name__ == "__main__":
    main()
