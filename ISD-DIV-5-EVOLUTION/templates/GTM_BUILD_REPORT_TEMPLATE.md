# GTM Build Report Template [v1.1]

> After 25 years in the web industry, and with the rise of AI, the founder knew it was time to create single-focused apps for real daily life and work challenges. Every app is simple by design, easy to use, and always private — because complex problems are best solved simply. No ads. No tracking. Your data stays yours.

**Authority:** Template for the GTM Build Report mandated by [`ROLES/OFFICE_ARCHITECT.md`](../../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md) §IV — no strike is complete until its Build Report is generated. Translates engineering "moats" into commercial "hooks" for the [864zeros.com](https://864zeros.com) website.
**Loaded:** On every strike shipping. The Office Architect (864z-OA) produces (or causes to be produced) one Build Report per shipped strike using this template; the Technical Writer (864z-TW) executes the copy.
**Authored:** 2026-05-11 by 864z-OA (Office Architect) per RULE-000 (Strike 025).
**Update protocol:** Append-only versioning table at §VIII. Each Build Report instance is a separate file (recommended naming: `BR-{strike-id}-{codename}.md`, placed under `ISD-DIV-5-EVOLUTION/reports/`); this template is the source they are forked from. **The BRAND_MISSION header is the single source of truth — keep in lockstep with [`864z-build-kit/references/core/brand-identity.js`](../../../864zeros-llc/864z-build-kit/references/core/brand-identity.js) `BRAND_MISSION` constant** (Strike 025 cross-surface installation).
**Format note:** Follows the `864z-markdown-standard` (RULE-008).

---

## I. Thesis

*What is the engineering moat? What customer pain does this strike address? Why does this matter NOW?*

- **Engineering moat:** {what we built that competitors structurally cannot/will not — e.g., local-first storage, BYOK, sovereign export paths, RULE-007 compliance posture}
- **Customer pain:** {the daily-life or work friction this strike removes}
- **Why now:** {macro shift, incumbent-failure window, AI-driven inflection, or scarcity gate per `STRIKE_HISTORY_MASTER.md`}

---

## II. Target Customer

*Who specifically? Demographics, psychographics, pain triggers. What do they currently do? Who/what are they currently paying?*

- **Primary persona:** {single-sentence archetype}
- **Pain triggers:** {3-5 concrete moments of friction in their current workflow}
- **Current spend:** {what they pay today — incumbent subscriptions, time-cost, switching cost}
- **Scarcity cohort (if any):** {Founding-100 / waitlist / unlisted-launch policy per pillar doctrine}

---

## III. Source Liberation Targets

*Which incumbent / legacy system does this strike liberate users from? Concrete export paths, data-portability guarantees, "leave anytime" attestations.*

- **Source(s):** {named incumbent platforms or formats}
- **Export paths:** {file formats, on-device folders, no-proxy attestation}
- **Sovereignty guarantee (RULE-007):** {chrome.storage.local-only / no 864zeros server / BYOK or BYOA where applicable}

---

## IV. Pricing Tier

*Tier-0.5 / Pro / Power configuration. ExtPay merchant slug. Plan ID. Price point. Recurring vs one-time. "Why this price" rationale.*

| Field | Value |
|---|---|
| Tier | {Tier-0.5 / Pro / Power} |
| ExtPay merchant slug | {e.g., `chronicle`} |
| ExtPay product type | {ONE-TIME perpetual / recurring} |
| Price | ${X.XX} |
| Internal plan label | {e.g., `one-time-tier-05`} |
| Why this price | {one-paragraph rationale; reference Chronicle's $2.99 perpetual as fleet anchor where relevant} |

---

## V. Hook Copy

*864zeros.com website copy — short, founder-voice, no marketing speak.*

- **Headline:** {one-line value proposition; ≤ 70 chars}
- **Subhead:** {supporting sentence; ≤ 140 chars}
- **CTA:** {install-button copy; ≤ 30 chars; per RULE-006 v1.1 brand-prefix pill conventions}
- **Privacy attestation:** {one-line RULE-007 / sovereignty claim — typically "No ads. No tracking. Your data stays yours." matching the brand-footer}

---

## VI. Privacy & RULE-007 Disclosure Block

*Verbatim disclosure paragraph per the extension's `RULE_007_AUDIT.md §VI.a` / §Disclosure block. Cite all high-trust surfaces (BYOK / OAuth / 3rd-party payments / debugger / management / etc.).*

```
{paste the extension's audit §VI.a disclosure block here verbatim}
```

If no per-extension RULE-007 audit exists yet, this section blocks Build Report sign-off — the audit must be authored first.

---

## VII. Strike Verification Checklist

*Mandatory pre-publish gates. The Office Architect signs off only when every box is checked.*

- [ ] **864zeros Trust Vault Integration Verified** — `<div id="trust-vault-root">` present in the extension's `options.html`; canonical `lib/options-tier-init.js` + `lib/trust-vault.js` are SHA-identical to `864z-build-kit/references/core/` masters; Export/Import buttons round-trip a sample payload without server contact (Strike 028 + 029).
- [ ] **RULE-007 §Disclosure Block populated** — verbatim copy from the extension's `RULE_007_AUDIT.md §VI.a` is present in the options.html Privacy section.
- [ ] **Pricing Tier documented in §IV** — ExtPay merchant slug registered + ONE-TIME product live at `extensionpay.com/dashboard`; per `CHRONICLE_CHECKOUT_BLUEPRINT.md` §IV Operator Pre-Integration Checklist if Tier-0.5.
- [ ] **Hook copy reviewed for tone** — founder-voice; within character limits (≤ 70 headline, ≤ 140 subhead, ≤ 30 CTA); RULE-006 v1.1 brand-prefix pill present.
- [ ] **Brand footer canonical** — standardized 4-line `<footer class="brand-footer">` rendered (per `GTM_MANIFEST §6` + RULE-014 transparency consolidation).
- [ ] **`BRAND_MISSION` rendered** — `<div id="brand-mission">` present in options.html (Strike 025 cross-surface installation).

---

## VIII. Cross-References

- [`ROLES/OFFICE_ARCHITECT.md`](../../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md) §IV — the role-doc mandate for this report.
- [`864z-build-kit/references/core/brand-identity.js`](../../../864zeros-llc/864z-build-kit/references/core/brand-identity.js) — `BRAND_MISSION` canonical source.
- [`ISD-DIV-6-KNOWLEDGE/864zeros_FACTORY_MANIFEST.md`](../../ISD-DIV-6-KNOWLEDGE/864zeros_FACTORY_MANIFEST.md) — per-extension Rung 4 / Active-Checkout status (informs Pricing Tier §IV).
- [`ISD-DIV-5-EVOLUTION/STRIKE_HISTORY_MASTER.md`](../STRIKE_HISTORY_MASTER.md) — strike scoring + scarcity gate (informs Thesis §I "why now").
- [`864zeros_PILLAR_STRATEGY.md`](../../ISD-DIV-6-KNOWLEDGE/864zeros_PILLAR_STRATEGY.md) — pillar doctrine (informs Target Customer §II tone + cohort policy).

---

## IX. Versioning

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-11 | Initial template (Strike 025). BRAND_MISSION header (cross-surface canonical); 5 sections per `OFFICE_ARCHITECT.md` §IV (Thesis · Target Customer · Source Liberation Targets · Pricing Tier · Hook Copy); §VI. Privacy & RULE-007 Disclosure Block added because every shipped strike's Build Report should carry the audit-verified disclosure copy verbatim; §VII Cross-References + §VIII Versioning per `864z-markdown-standard` (RULE-008). |
| 1.1 | 2026-05-11 | Strike 030 — added §VII Strike Verification Checklist (6 mandatory pre-publish gates: **864zeros Trust Vault Integration Verified** [operator-mandated first item] + RULE-007 §Disclosure populated + Pricing Tier ExtPay config + Hook copy tone review + Brand footer canonical + BRAND_MISSION rendered). Renumbered §VII Cross-References → §VIII; §VIII Versioning → §IX. The checklist makes the previously-implicit "Office Architect sign-off" criteria explicit + actionable. |

---

*GTM Build Report Template v1.1 · 2026-05-11 · 864zeros LLC · ISD-DIV-5-EVOLUTION/templates/.*
