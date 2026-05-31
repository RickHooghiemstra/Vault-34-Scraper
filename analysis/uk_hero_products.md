# UK Launch Focus — Hero Bikes & Products

**Goal:** concentrate the first paid + SEO push on the UK's highest-volume bikes,
using the products where our ~26% gross margin actually survives shipping and a
real ad cost. Derived from live catalog (vault34exhausts.com) + `margin_model.py`.

## Why UK + these bikes
- UK is the best contribution market (extra-EU = 0% VAT, English, closest of the
  four targets). See `analysis/margin_model.py`.
- **Yamaha MT-07 and MT-09 are perennial UK top-sellers** (naked-bike best-sellers),
  and our catalog has unusually deep coverage of both across 5 brands. High demand
  + deep stock coverage = the obvious beachhead.

## The key margin rule (from the model)
Shipping is a ~€35–75 *fixed* cost per order. On a 26% gross, that means:

| Product price band | UK break-even CAC | Verdict for PAID ads |
|---|---|---|
| ~€320 (entry silencer)   | ~€31  | ❌ too thin — organic/upsell only |
| ~€450                    | ~€58  | ⚠️ marginal |
| ~€600–€900               | ~€90–€157 | ✅ good headroom |
| €1,000+ (full systems)   | ~€245–€310 | ✅ best headroom |

> Put paid spend behind **€600+** products. Use sub-€500 items as organic catalog
> depth, bundle/upsell, and SEO long-tail — not as ad entry points. **Do not run
> cheap items to Australia** (negative contribution after shipping).

## Tier 1 — advertise these first (MT-09, €600+)
| Product | Brand | SKU | Price (EUR) |
|---|---|---|---|
| GP Pro Carbon Full System MT-09/SP/FZ-09 | Mivv | Y.066.L2P | 1,149.95 |
| LV Race Full System MT-09 / SP | LeoVince | 14371EBK | 1,494.95 |

## Tier 1 — advertise these first (MT-07, €600+)
| Product | Brand | SKU | Price (EUR) |
|---|---|---|---|
| GP Pro Titanium Full System MT-07/FZ-07 | Mivv | Y.065.L6P | 608.95 |
| LV One EVO Carbon Full System MT-07/XSR700/R7 | LeoVince | 14361E | 908.95 |
| LV One EVO Black Edition (EC-approved) MT-07/XSR700/R7 | LeoVince | 14360EBK | 1,116.95 |
| Pro-Race Ti Full System MT-07 | Arrow | 71037GP | 1,087.95 |
| Serket Taper Carbon Full System MT-07 | Scorpion | RYA121SYSCEO | 868.95 |
| Ixil L3XB Full System MT-07 / Tracer 700 | Ixil | 175-964 | 1,000.95 |

## Tier 2 — organic / upsell only (good for catalog depth & SEO, not paid entry)
| Product | Brand | SKU | Price (EUR) | Note |
|---|---|---|---|---|
| Thunder Alu Slip-On MT-09 | Arrow | 71931AK / 71931AKN | 453.95 | needs Arrow header set (fitment caveat) |
| Thunder Alu Slip-On MT-07 | Arrow | 71930AK/AO/AON | 319–453 | needs Arrow header set |
| X-M1 Black Full System MT-09 | Mivv | Y.066.LC4B | 255.95 | low ticket |
| Delta Race Carbon MT-09 (RACE_ONLY) | Mivv | Y.066.LDRC | 255.95 | not road-legal — label clearly |

## Also strong in catalog (next models to expand into)
- **Kawasaki Z900** (Arrow racing collector, SKU 71799MI, €841.95) — UK volume naked.
- Worth checking depth next: Honda CB650R/CBR650R, Triumph Trident 660/Street Triple,
  Royal Enfield, Kawasaki Z650 — all high UK registration models.

## Data-quality fixes to make before the feed goes live (cheap conversion wins)
- Several MT-09 **full systems are mis-tagged `TYPE_SlipOn`** (e.g. Mivv Y.066.L2P) and
  some Arrow silencers are tagged `TYPE_HeaderSet`. Fix product_type before building the
  Google Merchant feed — wrong type hurts Shopping relevance and buyer trust.
- `RACE_ONLY` items (e.g. Mivv Delta Race) must say **"track use / not road-legal"** on
  the page and in ad copy — UK buyers filter hard on road legality / E-marking.
- Arrow "Thunder" silencers require a **matching Arrow header set** — state this on-page
  to avoid returns and chargebacks.
