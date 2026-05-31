"""
Phase 0 — Per-market net-contribution model for Vault 34 Exhausts.

Purpose
-------
Before spending a single euro on ads, confirm that the ~26% gross margin
(35% markup on net cost) survives real per-order costs in each export market:
international shipping, payment/platform fees, and a returns reserve. Whatever
is left over is the MAXIMUM you can pay to acquire an order (break-even CAC) —
the single most important number for planning the <=500 EUR/mo ad budget.

Economics (confirmed with the business)
---------------------------------------
- You buy from uitlaatstore.nl as a VAT-registered business and reclaim the
  21% input VAT, so true cost = sell_price_net / MARKUP  (net = retail / 1.21).
- You export OUTSIDE the EU (US / JP / AU / post-Brexit UK) and charge 0% VAT.
- Therefore gross margin = sell - cost = sell * (1 - 1/MARKUP).

All shipping / fee / return assumptions are explicit and editable below.
Run:  python analysis/margin_model.py
"""

from dataclasses import dataclass

# --- Pricing constant (mirrors config/settings.py MARKUP) ------------------
MARKUP = 1.35  # sell price = net cost * 1.35

# --- Representative live products (pulled from vault34exhausts.com) ---------
# (title, sell_price_eur, weight_class)  weight_class in {"slip_on", "full_system"}
# Mix of the ad-friendly UK hero band (MT-07/MT-09 slip-ons) and premium systems.
PRODUCTS = [
    ("Arrow Thunder Slip-On Yamaha MT-07",      319.95,  "slip_on"),
    ("Arrow Thunder Slip-On Yamaha MT-09",      453.95,  "slip_on"),
    ("Mivv GP Pro Slip-On Yamaha MT-07",        608.95,  "slip_on"),
    ("Akrapovic Slip-On Vespa GTS 300",         929.95,  "slip_on"),
    ("LeoVince LV Race Full System Yamaha MT-09", 1494.95, "full_system"),
    ("Akrapovic Full System Honda CRF450",     1772.95,  "full_system"),
]

# --- Cost assumptions (EDIT THESE with your real courier quotes) -----------
# Outbound export shipping from NL by courier (DHL/UPS/PostNL), EUR.
SHIPPING_EUR = {
    # market: {weight_class: cost}
    "UK": {"slip_on": 35.0, "full_system": 55.0},
    "US": {"slip_on": 60.0, "full_system": 95.0},
    "JP": {"slip_on": 65.0, "full_system": 105.0},
    "AU": {"slip_on": 75.0, "full_system": 120.0},
}

# Payment + platform fee as a fraction of sell price.
# Shopify Payments ~2.9% + 0.30 EUR, plus cross-border/FX ~1.5%. Rounded to 4%.
PAYMENT_FEE_RATE = 0.04
PAYMENT_FEE_FIXED = 0.30  # EUR per transaction

# Returns reserve: fraction of GROSS margin set aside for returns/restocking.
# Exhaust returns are uncommon but cross-border returns are expensive.
RETURN_RESERVE_RATE = 0.05

# Ad budget context (for the break-even CAC interpretation).
MONTHLY_AD_BUDGET = 500.0


@dataclass
class Result:
    title: str
    market: str
    sell: float
    net_cost: float
    gross: float
    shipping: float
    fees: float
    returns_reserve: float
    contribution_before_cac: float  # == break-even CAC

    @property
    def gross_margin_pct(self) -> float:
        return self.gross / self.sell * 100

    @property
    def contribution_margin_pct(self) -> float:
        return self.contribution_before_cac / self.sell * 100


def evaluate(title: str, sell: float, weight_class: str, market: str) -> Result:
    net_cost = sell / MARKUP
    gross = sell - net_cost
    shipping = SHIPPING_EUR[market][weight_class]
    fees = sell * PAYMENT_FEE_RATE + PAYMENT_FEE_FIXED
    returns_reserve = gross * RETURN_RESERVE_RATE
    contribution = gross - shipping - fees - returns_reserve
    return Result(title, market, sell, net_cost, gross,
                  shipping, fees, returns_reserve, contribution)


def main() -> None:
    markets = list(SHIPPING_EUR.keys())
    print("=" * 100)
    print("PHASE 0 — NET CONTRIBUTION PER ORDER (before ad cost)  |  MARKUP =", MARKUP)
    print("Break-even CAC = the most you can pay in ads per order and still break even.")
    print("=" * 100)

    by_market_contrib: dict[str, list[float]] = {m: [] for m in markets}

    for title, sell, wclass in PRODUCTS:
        print(f"\n{title}   (sell EUR {sell:,.2f}, {wclass})")
        net = sell / MARKUP
        print(f"  net cost EUR {net:,.2f}  |  gross EUR {sell-net:,.2f} "
              f"({(sell-net)/sell*100:.1f}%)")
        print(f"  {'market':<6} {'ship':>7} {'fees':>7} {'ret':>6} "
              f"{'contrib/ord':>12} {'margin%':>8}  break-even CAC")
        for m in markets:
            r = evaluate(title, sell, wclass, m)
            by_market_contrib[m].append(r.contribution_before_cac)
            print(f"  {m:<6} {r.shipping:>7.0f} {r.fees:>7.0f} "
                  f"{r.returns_reserve:>6.0f} {r.contribution_before_cac:>12,.2f} "
                  f"{r.contribution_margin_pct:>7.1f}%  EUR {r.contribution_before_cac:,.0f}")

    print("\n" + "=" * 100)
    print("MARKET SUMMARY — avg net contribution per order (before ad cost)")
    print("=" * 100)
    for m in markets:
        vals = by_market_contrib[m]
        avg = sum(vals) / len(vals)
        # Orders/month at break-even if you spend the whole budget at avg CAC.
        max_orders = MONTHLY_AD_BUDGET / avg if avg > 0 else float("inf")
        print(f"  {m:<4} avg contribution/order EUR {avg:>8,.2f}   "
              f"=> at break-even, {MONTHLY_AD_BUDGET:.0f} EUR buys ~{max_orders:.0f} orders' "
              f"worth of CAC headroom")
    print("\nInterpretation: any market with positive contribution is viable to TEST.")
    print("The bigger the contribution, the more ad inefficiency you can absorb while")
    print("learning. Start with the market that has the best contribution-to-CAC odds.")


if __name__ == "__main__":
    main()
