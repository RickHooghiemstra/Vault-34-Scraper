"""
Google Merchant Center feed generator — UK launch (GBP).

Generates a tab-separated Google Shopping feed for the focused "UK Hero —
Yamaha MT-09 / MT-07" range: the 8 full systems priced >= EUR 600 where our
~26% gross margin survives international shipping and a real ad cost (see
analysis/uk_hero_products.md + analysis/margin_model.py).

EUR -> GBP conversion reuses the live ECB rate from pricing/fx.py
(1 EUR = rates["GBP"]).

    python -m analysis.google_feed
    # -> shopify_exports/google_merchant_feed_uk.tsv

IMPORTANT — price matching:
    Google disapproves items whose feed price drifts from the price shown on
    the landing page. The storefront shows GBP via Shopify Markets auto-
    conversion, which is NOT rounded and fluctuates daily. So this TSV is a
    quick-start / fallback. The recommended hands-off path is the free
    "Google & YouTube" Shopify channel, which syncs the collection and keeps
    GBP pricing in sync automatically. If you use this TSV instead, set a
    FIXED GBP price list in Settings > Markets > United Kingdom so the
    storefront matches these numbers.
"""

import csv
from pathlib import Path

try:
    from pricing.fx import get_rates
except Exception:  # pragma: no cover - allow running standalone
    get_rates = None

OUT = Path(__file__).resolve().parent.parent / "shopify_exports" / "google_merchant_feed_uk.tsv"
STORE = "https://www.vault34exhausts.com"
GOOGLE_CATEGORY = "Vehicles & Parts > Vehicle Parts & Accessories > Motor Vehicle Parts > Motor Vehicle Exhaust"
CDN = "https://cdn.shopify.com/s/files/1/1014/0382/0419/files/"
FALLBACK_EUR_GBP = 0.86  # used only if ECB is unreachable

# The 8 paid-launch heroes (EUR >= 600). road_legal drives the description note.
HEROES = [
    {
        "sku": "14371EBK", "brand": "LeoVince", "eur": 1494.95, "road_legal": True,
        "title": "LeoVince LV Race Full System — Yamaha MT-09 / SP",
        "handle": "leovince-lv-race-full-system-for-yamaha-mt-09-mt-09-sp",
        "image": "update21_lv-race_1-targhetta_bd6cca9a-5ce2-4351-852c-4c840ec53fb5.jpg?v=1778852347",
        "blurb": "Full titanium/carbon race system for the MT-09 triple. Big weight loss, deep CP3 howl.",
    },
    {
        "sku": "Y.066.L2P", "brand": "Mivv", "eur": 1149.95, "road_legal": True,
        "title": "Mivv GP Pro Carbon Full System — Yamaha MT-09 / SP / FZ-09",
        "handle": "mivv-gp-pro-carbon-full-system-for-yamaha-mt-09-sp-fz-09-2021-2023",
        "image": "update21_yamaha_mt-09_2021-_73y066l2p_21_bbc575c0-8168-4cb0-92e7-2f45a834ea08.jpg?v=1778852343",
        "blurb": "Euro 5 GP Pro carbon system. MotoGP-bred silencer, aggressive race note, road-legal.",
    },
    {
        "sku": "14360EBK", "brand": "LeoVince", "eur": 1116.95, "road_legal": True,
        "title": "LeoVince LV One EVO Black Edition Full System (EC-approved) — Yamaha MT-07 / XSR700 / R7",
        "handle": "leovince-lv-one-evo-black-edition-full-system-with-e-keur-for-yamaha-mt-07-xsr700-yzf-r7",
        "image": "update21_lv-one-evo-new-end-cap-black-edition_2_7124df93-6d35-4fee-b8f1-5cb113666d88.jpg?v=1778852383",
        "blurb": "Murdered-out EC-approved full system for the CP2 twin. Black carbon, deep bark, plate legal.",
    },
    {
        "sku": "71037GP", "brand": "Arrow", "eur": 1087.95, "road_legal": True,
        "title": "Arrow Pro-Race Titanium Full System — Yamaha MT-07 / FZ-07",
        "handle": "arrow-pro-race-full-system-racing-for-yamaha-mt-07-2021-2024",
        "image": "arrow_legenden_8_8.jpg?v=1778852297",
        "blurb": "Full titanium Pro-Race system. Serious weight savings and that signature Arrow rasp.",
    },
    {
        "sku": "175-964", "brand": "Ixil", "eur": 1000.95, "road_legal": True,
        "title": "Ixil L3XB Hyperlow Full System — Yamaha MT-07 / Tracer 700",
        "handle": "ixil-l3xb-exhaust-full-system-mt-07-2021-tracer-700-2020",
        "image": "update15_175-964.jpg?v=1778852450",
        "blurb": "Euro 5 E-approved stainless system with the unmistakable Hyperlow XL can.",
    },
    {
        "sku": "14361E", "brand": "LeoVince", "eur": 908.95, "road_legal": True,
        "title": "LeoVince LV One EVO Carbon Full System — Yamaha MT-07 / XSR700 / R7",
        "handle": "leovince-lv-one-evo-full-system-for-yamaha-mt-07-xsr700-xtribute-yzf-r7-2021-2023-14361e",
        "image": "update21_lv-one_new-end-cap_carbonio_2_83bbcb7f-12d4-48ab-8e98-8af236e39aa1.jpg?v=1778852368",
        "blurb": "Full carbon LV One EVO. ~3 kg lighter, race-bred note, premium finish.",
    },
    {
        "sku": "RYA121SYSCEO", "brand": "Scorpion", "eur": 868.95, "road_legal": True,
        "title": "Scorpion Serket Taper Carbon Full System — Yamaha MT-07",
        "handle": "scorpion-full-system-serket-taper-carbon-for-yamaha-mt-07-2022",
        "image": "update21_rya121sysceo_kit-900x900.jpg?v=1778852500",
        "blurb": "Tapered carbon Serket full system. British-built, hand-finished, hard-edged tone.",
    },
    {
        "sku": "Y.065.L6P", "brand": "Mivv", "eur": 608.95, "road_legal": True,
        "title": "Mivv GP Pro Titanium Full System — Yamaha MT-07 / FZ-07",
        "handle": "mivv-gp-pro-titanium-full-system-for-yamaha-mt-07-fz-07-2021-2022",
        "image": "update21_yamaha_mt07_14-_73y045l6p_21_ppg_014de2fd-7e73-4919-8657-7ba73410e269.jpg?v=1778852331",
        "blurb": "Euro 5 titanium GP Pro system — the entry into the hero range. Light, loud, legal.",
    },
]

COLUMNS = [
    "id", "title", "description", "link", "image_link", "availability",
    "price", "brand", "condition", "mpn", "identifier_exists",
    "google_product_category", "product_type",
]


def eur_to_gbp_rate() -> float:
    if get_rates is not None:
        try:
            r = get_rates().get("GBP")
            if r:
                return float(r)
        except Exception:
            pass
    return FALLBACK_EUR_GBP


def gbp_price(eur: float, rate: float) -> str:
    # Round UP to the nearest .95 to keep brand-consistent pricing and avoid
    # ever pricing below the converted cost. Feed currency must match the
    # storefront price list (see module docstring).
    raw = eur * rate
    whole = int(raw)
    price = whole + 0.95 if raw <= whole + 0.95 else whole + 1 + 0.95
    return f"{price:.2f} GBP"


def description(h: dict) -> str:
    legal = ("Road-legal (E-marked / EC-approved)." if h["road_legal"]
             else "Track use only — NOT road-legal.")
    return (f"{h['blurb']} {legal} Genuine {h['brand']} full exhaust system, "
            f"shipped from the EU with worldwide delivery from Vault 34 Exhausts.")


def build_rows(rate: float) -> list[dict]:
    rows = []
    for h in HEROES:
        rows.append({
            "id": h["sku"],
            "title": h["title"],
            "description": description(h),
            "link": f"{STORE}/products/{h['handle']}",
            "image_link": CDN + h["image"],
            "availability": "in stock",
            "price": gbp_price(h["eur"], rate),
            "brand": h["brand"],
            "condition": "new",
            "mpn": h["sku"],
            "identifier_exists": "no",  # no GTIN on these supplier SKUs
            "google_product_category": GOOGLE_CATEGORY,
            "product_type": "Exhausts > Full Systems > Yamaha > MT-07/MT-09",
        })
    return rows


def main() -> None:
    rate = eur_to_gbp_rate()
    rows = build_rows(rate)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(f"EUR->GBP rate (1 EUR = {rate} GBP)")
    print(f"Wrote {len(rows)} products -> {OUT}")
    for r in rows:
        print(f"  {r['id']:<14} {r['price']:>12}  {r['title']}")


if __name__ == "__main__":
    main()
