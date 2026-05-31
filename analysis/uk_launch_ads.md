# UK Launch — €500 Ad Plan, Copy & Pre-Flight Checklist

Focused launch for **Vault 34 Exhausts** (vault34exhausts.com), UK-only, behind the
8-product **UK Hero — Yamaha MT-09 / MT-07 Full Systems** collection. Grounded in
`analysis/margin_model.py` (CAC headroom), `analysis/uk_hero_products.md`, and
`analysis/flywheel.py` (reinvest order margin).

> **Hard rule:** the €500 does not go live until the Pre-Flight Checklist below is
> green. Spending into the current 0%-conversion funnel just buys losses faster.

---

## 1. Pre-Flight Checklist (free, do these first)

**A. Conversion blockers (the funnel currently converts at 0%)**
- [ ] **Shipping** — set a real UK shipping rate + delivery estimate; show it on the
      product page, not just at checkout. Invisible shipping is a top cart-killer.
- [ ] **Duties/VAT messaging** — UK buyers pay import VAT (20%) + possible duty on
      arrival. State this clearly ("UK import VAT/duty may apply on delivery") or, better,
      offer **DDP (prepaid)** so the price they see is the price they pay.
- [ ] **Returns + warranty** policy page, linked from every product page.
- [ ] **Trust** — visible payment badges, an About/Contact with a real address, and
      confirm **Shopify Payments + PayPal** are live (test a £1 order end-to-end).
- [ ] **Road-legality on each PDP** — the 8 heroes are all road-legal (E-marked/EC); say
      so prominently. (Separately, the `RACE_ONLY` Mivv Delta Race — NOT in this range —
      must say "track use only" before it ever runs in ads.)
- [ ] **Fitment clarity** — exact models/years + "direct bolt-on, no header needed" for
      these full systems (vs. the Arrow slip-ons that require a header set).

**B. Pricing/currency (mostly already done)**
- [x] UK market enabled with local currency display (verified live).
- [ ] Decide GBP source: **(preferred)** install the free **Google & YouTube** Shopify
      channel → auto-syncs the collection with correct GBP pricing and keeps the Merchant
      feed in sync; **OR** upload `shopify_exports/google_merchant_feed_uk.tsv` and set a
      **fixed GBP price list** (Settings → Markets → United Kingdom) matching the feed so
      Google doesn't disapprove items for price mismatch.

**C. Tracking**
- [ ] Google Ads conversion tracking + GA4 purchase event firing (test order confirms).

---

## 2. Campaign structure (€500, UK only)

Two options — pick ONE to keep signal concentrated:

**Option A — Standard Shopping (recommended to start).** Simpler, more control, easier to
read early signal on a tiny budget.
- 1 campaign, UK geo only, feed = the 8 heroes.
- Bidding: **Manual CPC** or **Maximize clicks with a max CPC cap (~£0.60)** for the first
  ~2 weeks to gather data, then switch to **Target ROAS** once you have ≥15–20 conversions
  (likely later — don't rush smart bidding on thin data).
- Budget: **€15/day** (~€450/mo) so the test runs ~30 days, not 3.

**Option B — Performance Max.** More reach, less control; needs the asset group below.
Only choose if you also have a couple of lifestyle images/video. On €500 it learns slowly.

**Negatives / settings (both options)**
- Exclude search partners + Display expansion initially (keep spend on Shopping/Search intent).
- Location: **United Kingdom only**, "people in" (not "interested in").
- Add brand + model as the spine: campaigns will naturally serve on "mivv mt-09 exhaust",
  "leovince mt-07 full system", "akrapovic mt-09" etc.

---

## 3. PMax asset group copy (also reusable for Search later)

**Headlines (≤30 chars)**
- MT-09 & MT-07 Full Systems
- Mivv · LeoVince · Arrow
- Titanium & Carbon Systems
- Road-Legal Race Exhausts
- Drop Weight, Wake It Up
- Genuine, EU-Sourced
- Free-Breathing CP2 / CP3
- Yamaha MT Exhaust Upgrade

**Long headlines (≤90 chars)**
- Full titanium & carbon exhaust systems for the Yamaha MT-09 and MT-07 — road-legal.
- Wake up your MT's triple or twin: Mivv, LeoVince, Arrow, Scorpion & Ixil full systems.
- Real weight savings, deeper note, genuine parts — shipped fast across the UK.

**Descriptions (≤90 chars)**
- Premium full systems for the MT-09 & MT-07. Lighter, louder, road-legal. Shop now.
- E-marked race systems from the brands that build them. UK delivery, genuine stock.
- Transform your Yamaha naked — titanium & carbon, hand-finished, dyno-proven gains.
- Mivv, LeoVince, Arrow, Scorpion, Ixil. The hero range for CP2 & CP3 riders.

**Business name:** Vault 34 Exhausts
**Final URL:** https://www.vault34exhausts.com/collections/uk-hero-yamaha-mt-09-mt-07-full-systems

---

## 4. Search themes / keyword seeds (for Search or PMax signals)
`mt-09 exhaust`, `mt-07 exhaust`, `mt-09 full system`, `mt-07 full system`,
`mivv mt-09`, `leovince mt-07`, `arrow mt-07 pro race`, `scorpion mt-07 exhaust`,
`yamaha mt09 akrapovic alternative`, `mt-09 titanium exhaust`, `mt-07 carbon exhaust`,
`road legal mt-09 exhaust`.

**Negatives:** `decat`, `db killer`, `baffle removal`, `repair`, `gasket`, `link pipe`
(low-ticket / wrong intent), plus `slip on` if you want to push full-system value first.

---

## 5. Budget pacing & the flywheel
- Start €15/day. Don't dump €500 in week one — let Shopping learn.
- Watch **clicks → product views → ATC → checkout**. If clicks come but ATC stays at 0,
  the blocker is the PDP/price, not the ads — pause and fix before spending more.
- Per `analysis/margin_model.py`, these €600+ systems carry **~£75–£260 CAC headroom**.
  At ~£260 AOV contribution, **one sale ≈ funds the next ~400 clicks** at £0.60 CPC.
- Target for the test: **first 3–5 UK orders + a CPA under your headroom.** That's the
  green light to scale the budget and clone the playbook to a second market.

---

## 6. Human-only steps (I can't and won't do these)
1. Create/connect **Google Ads** + **Google Merchant Center** accounts.
2. Install the **Google & YouTube** Shopify channel (preferred feed path).
3. Set the **UK shipping rate** and (if doing DDP) duties in Shopify.
4. Set the campaign budget and **commit the €500** spend.
5. Verify a real test order completes end-to-end in GBP.
