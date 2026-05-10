# 864zeros: Factory Manifest [v1.65]

**Authority:** Per-extension monetization-readiness ledger. Synthesizes the post-consolidation state of all 15 extensions in `LLC-DIV-3-FACTORY/extensions/`.
**Loaded:** On demand for tier-rollout planning, GTM sequencing, RULE-001 burndown, and operator dashboards.
**Authored:** 2026-05-09 by 864z-OA (Office Architect) per RULE-000.
**Update protocol:** Append a new version after each strike that changes the Tier-0.5 readiness of any extension OR after each new extension joins the factory.
**Sources synthesized:** All 15 `extensions/*/manifest.json` + `_locales/{locale}/messages.json` + `options/*` files (programmatic survey 2026-05-09 post-Strike-014 transparency-consolidation pass) · [`864zeros_TECH_STACK_AUDIT.md`](./864zeros_TECH_STACK_AUDIT.md) (class taxonomy + RULE compliance lens) · [`864zeros_PILLAR_STRATEGY.md`](./864zeros_PILLAR_STRATEGY.md) (pillar doctrine).
**Format note:** Follows the `864z-markdown-standard` (RULE-008).

---

## I. Naming Convention Note

**Per RULE-006 v1.1 the codified pillar tags are:** `[OIA]`, `[864F]`, `[FHG]`. The brand identifier `864-Flux` (full pillar name) appears in the standardized 4-line brand-footer (per GTM_MANIFEST §6) and elsewhere in marketing surfaces. The bracketed tag `[864F]` is the RULE-006 v1.1 enforced form for `manifest.json.name` and rendered surface pills. **`[FLUX]` is not a codified tag** — informal references to "Flux" should normalize to either `[864F]` (in code) or `864-Flux` (in copy).

---

## II. Fleet at a Glance

**12 active extensions** across 3 pillars (post-Strike-016 archival: 3 legacy `oia.focus.*` extensions moved to `_archive/`; TabVault rebranded to DataNap). Tier-0.5 readiness distribution snapshot (2026-05-09 post-Strike-021):

| Status | Count | Extensions |
|---|---|---|
| **✅ TIER-0.5 SHIPPED** | 1 | `864z-chronical` |
| **🏆 SCAFFOLD-READY (Rung 3+ — markup wired + state machine + dev gate + canonical IDs)** | **11** | `Bible-Insight`, `clipboard` ⬆ promoted in Strike 021, `DataNap`, `Focus Note`, `Focus Wall`, `migration-pilot`, `scripture-scout`, `Signal2Noise`, `Time2Focus`, `TuneOut2FocusIn`, `who-is-watching` |
| **🟡 SCAFFOLD-READY (CSS only)** | **0** ✅ |
| **❌ BLOCKED** (no `options_ui` → RULE-001 violation) | **0** ✅ |

**Strike-019 milestones:**
- Bible-Insight RULE-007 §Disclosure block injected (closes the one outstanding P1 from Strike 018 audit; Bible-Insight now fully RULE-007 §Disclosure compliant)
- migration-pilot + scripture-scout promoted Rung 2 → Rung 3 via `lib/tier.js` distribution + inline tier-init script injection
- **11 of 12 active extensions now on Rung 3+ (92%)** — only `clipboard` remains on Rung 1 (Phase-2 HIGH-deferred)
- NEW operational artifact: `LLC-DIV-3-FACTORY/FACTORY_LEDGER.jsonl` (machine-readable JSON-per-line) + `LLC-DIV-3-FACTORY/SESSION_STREAM.md` (human-readable companion) — append-only audit trail of every atomic factory mutation

**Strike-020 milestones (visual-compliance + GTM lock-in):**
- 🏆 **OIA (ADHD) pillar: 8/8 Rung-3+ extensions are now visual-binding compliant** — every OIA extension's options page has the canonical `vault-tier-card` / `current-tier-name` / `vault-lock-watermark` IDs that the inline tier-init script targets. 100% visual-compliance.
- 🏆 **FHG pillar: 2/2 Rung-3+ extensions are now visual-binding compliant** — Bible-Insight + scripture-scout both have canonical IDs. 100% visual-compliance.
- **864-Flux: 1/2** — migration-pilot now visual-compliant (Strike 020 canonical IDs added); clipboard still Rung 1 (Phase-2 HIGH-deferred).
- Bible-Insight tier rebranded **"⌖ Tier-0.5: Vault" → "⌖ Sovereign Research Kit"** per Operator GTM decision; closes Strike-018 P0 GTM-decision item. $2.99 perpetual unlock model adopted (matches Chronicle pattern).

**🏆🏆🏆 Strike-021 FLEET-WIDE 100% milestone:**
- **clipboard Phase-2 closure**: clipboard already had the [864F] prefix + SW `type: "module"` + brand-footer + linked `lib/transparency-tier.css` from prior strikes (Strike 014 transparency consolidation + earlier scaffold work). Strike 021 added the missing pieces: `lib/tier.js`, canonical IDs (`vault-tier-card` / `current-tier-name` / `vault-lock-watermark`), Tier-0.5 "Sovereign History" LOCKED card with $2.99 perpetual messaging, dev-override panel + inline tier-init script.
- **clipboard RULE-007 audit delivered**: per-extension `RULE_007_AUDIT.md` (~16 KB; 8 sections). Verdict: ✅ STRUCTURALLY COMPLIANT. Covers BYOK Gemini + debugger bounded to PDF + chrome.identity Google OAuth (BYOA) + ExtPay 3rd-party (NOT a 864zeros proxy) + chrome.management bounded to extension enumeration.
- **🏆 ACTIVE 12-EXTENSION FLEET: 12/12 (100%) Rung 3+ + 12/12 (100%) visual-binding compliant** — every extension in every pillar is now at minimum Rung 3 with full canonical-ID visual binding. Chronicle still holds the only Rung-4 (SHIPPED with stub paywall) position. The Tier-0.5 readiness ladder is no longer a per-extension shortlist; it is now a fleet-wide property.
- 864-Flux pillar: 2/2 visual-compliant (was 1/2). All 3 pillars at 100% visual-compliance.

**Strike-022 milestones (consolidation + payment-architecture spec):**
- **clipboard §Disclosure injected** (closes Strike-021 P1) — verbatim from `clipboard/RULE_007_AUDIT.md §VI.a`; covers all 5 high-trust surfaces (AI BYOK / Google OAuth / ExtPay 3rd-party / debugger / management) in clipboard's Options page.
- **NEW canonical: `864z-build-kit/references/core/options-tier-init.js`** — extracts the inline `<script type="module">` tier-init pattern (Strikes 016/017/018/019/021) into a single shared module. Distributed to per-extension `lib/options-tier-init.js` across **11 extensions** (chronicle excluded — its tier-init lives in `options/options.js`, not inline; touching it risks the reference impl).
- **11 extensions migrated from inline-script to shared-script linkage** — `<script type="module">{...}</script>` blocks replaced with `<script type="module" src="../lib/options-tier-init.js"></script>`. Eliminates ~80 LOC of cross-extension code duplication; future updates to tier-init logic now touch ONE canonical file instead of 11.
- **Chronicle Checkout Blueprint authored** (`extensions/864z-chronical/CHRONICLE_CHECKOUT_BLUEPRINT.md`, ~15 KB / 203 lines, RULE-008 compliant; 8 sections). Identifies 3 ExtPay entry points (SW `initPayments+onPaid`, Options page CTA swap, shared `TIER_UNLOCKED` broadcast listener), 6 operator pre-integration checklist items, 6 failure modes + mitigations, generalization path for the other 11 Rung-3 extensions (~5.5h batched estimate). NOT an implementation — operator-gated.

**Fleet compliance milestone (Strike 017):**
- **RULE-001 (Cog-triggered Options page): 12 / 12 (100%)** — was 9/15 pre-Strike-016
- **RULE-006 v1.1 (`extName` pillar prefix): 12 / 12 (100%)** — was 1/15 pre-Strike-014
- **SW `type: "module"` modernization: 12 / 12 (100%)** — was 14/15 pre-Strike-017 (`who-is-watching` was the lone classic-script SW)

Pillar distribution: **OIA 8 · 864-Flux 2 · FHG 2** (per `864zeros_PILLAR_STRATEGY.md` §VI — pillar inventory now reflects post-archival state).

---

## III. Per-Extension Manifest

12 active extensions (3 archived in Strike 016 — see [`extensions/_archive/README.md`](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/_archive/README.md)).

| Extension | Pillar | Display name (current) | Version | Options page | Tier-0.5 Status |
|---|---|---|---|---|---|
| `864z-chronical` | OIA | `[OIA] Chronicle` | 1.1.0 | ✅ `options/options.html` | **✅ TIER-0.5 SHIPPED** — full implementation: tier card + `lib/tier.js` state helper + Sovereign Link header button + RULE-005 two-tap Clear All + ?dev=1 dev-override panel + DEV_NOTES.md. Strike 013 reference impl. |
| `Bible-Insight` | FHG | `[FHG] Bible Insight` | 1.0.0 | ✅ `html/options.html` | ✅ **Rung 3 — VISUAL-COMPLIANT + RULE-007 §Disclosure compliant + tier rebranded "Sovereign Research Kit"** — Strike 020 closed Strike-018 P0 GTM-decision item: tier renamed `⌖ Tier-0.5: Vault` → `⌖ Sovereign Research Kit`; $2.99 perpetual unlock (Chronicle pattern); 5-feature list (Sovereign Link Backup, Markdown vault export, PDF report archive, cross-translation diffing, all-future-features); "why $2.99 once" rationale. CTA: "Unlock Sovereign Research Kit — $2.99 (coming soon)". Internal tier flag name unchanged (TIER_VAULT) for cross-extension code consistency. |
| `clipboard` | 864-Flux | `[864F] ClipBoard` | 1.0.0 | ✅ `options/options.html` | ✅ **Rung 3+ — VISUAL-COMPLIANT + RULE-007 §Disclosure compliant** — Strike 021 Phase-2 closure (lib/tier.js + Sovereign History card + canonical IDs + dev-override panel + audit doc). **Strike 022**: RULE-007 §Disclosure block injected before brand-footer (verbatim from `RULE_007_AUDIT.md §VI.a`; covers all 5 high-trust surfaces — AI BYOK Gemini / Google Drive OAuth / ExtPay payments / debugger / management). Inline tier-init script extracted to shared `lib/options-tier-init.js` (Strike 022 fleet consolidation; 11 extensions). |
| `DataNap` (was TabVault) | OIA | `[OIA] DataNap` | 1.0.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY** — Strike 016 augmentation. Web Store listing update pending the rebrand. |
| `migration-pilot` | 864-Flux | `[864F] MigrationPilot — Web to Obsidian` | 0.1.0 | ✅ `options/options.html` | ✅ **Rung 3 — VISUAL-COMPLIANT (state machine + binding)** — Strike 020: canonical IDs (`vault-tier-card` / `current-tier-name` / `vault-lock-watermark`) added to first existing `tier-card--locked` div (the "Pro coming" card). Closes the Strike-019 visual-binding partial-state. Card content preserved; ID layer purely additive; renderTier() now toggles visual state when dev gate flips chrome.storage.local.tier. |
| `oia-focus-note` (Focus Note) | OIA | `[OIA] Focus Note` | 1.1.0 | ✅ `options/options.html` (Strike 016) | 🟢 **SCAFFOLD-READY** — full RULE-001 + Tier-0.5 + dev-override scaffold. |
| `oia-focus-wall` (Focus Wall) | OIA | `[OIA] Focus Wall` | 1.1.0 | ✅ `options/options.html` (Strike 016) | 🟢 **SCAFFOLD-READY** — full RULE-001 + Tier-0.5 + dev-override scaffold. |
| `scripture-scout` | FHG | `[FHG] ScriptureScout` | 0.1.0 | ✅ `options/options.html` | ✅ **Rung 3 — VISUAL-COMPLIANT (state machine + binding)** — Strike 020: canonical IDs added to first existing `tier-card--locked` div (mirror change to migration-pilot; templates were forked from same source). Closes the Strike-019 visual-binding partial-state. Founding-100 cohort gates real launch. |
| `Signal2Noise` | OIA | `[OIA] Signal2Noise` | 1.0.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY** — Strike 016 augmentation. |
| `Time2Focus` | OIA | `[OIA] Time2Focus` | 1.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY** — Strike 016 augmentation. |
| `TuneOut2FocusIn` | OIA | `[OIA] TuneOut2FocusIn` | 1.0.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY** — Strike 016 augmentation. |
| `who-is-watching` | OIA | `[OIA] Who Is Watching` | 2.1.6 | ✅ `options/options.html` (Strike 017) | 🟢 **SCAFFOLD-READY** — Strike 017 scaffold + SW `type: "module"` migration in same touch. Highest-version extension in fleet. |

**Archived (3 — Strike 016):** `oia.focus.signal`, `oia.focus.sound`, `oia-focus-timer` — frozen; not part of active fleet. See `_archive/README.md`.

---

## IV. Tier-0.5 Readiness Ladder

A four-rung ladder describing what each extension needs to advance to the next tier of Tier-0.5 readiness. Lower rungs are prerequisites for higher rungs.

### IV.a — Rung 0: Cog-triggered Options page (RULE-001)

**Prerequisite for ANY Tier-0.5 work.** An extension cannot host a tier disclosure until it has an `options_ui` page conforming to RULE-001's three mandatory sections (How to Use · Subscription & Tiers · Data Management).

**0 extensions on Rung 0** ✅ — fully cleared as of Strike 017 (`who-is-watching` was the last; closed in Strike 017 alongside the SW `type: "module"` migration). Rung-0 is now an empty bucket; the historical 6 entries (5 `oia.focus.*` Focus-class + `who-is-watching`) closed across Strikes 016 and 017.

### IV.b — Rung 1: Transparency baseline (CSS + brand-footer + brand-prefix pill)

Extension has the shared `lib/transparency-tier.css` linked + the standardized 4-line brand-footer rendered + the RULE-006 v1.0 `.brand-prefix` pill in surface headers. **Visual contract for tier disclosure is in place** even if the actual tier card hasn't been built yet.

**12 of 12 active extensions on Rung 1+** ✅ (every active extension after Strikes 014-017).

### IV.c — Rung 2: Tier-card markup wired

Extension's options.html has `<div class="tier-card tier-card--locked">...</div>` markup with the canonical structure (`.tier-card__head`, `.tier-card__name`, `.tier-card__price`, `.tier-features`, `.tier-card__cta`, `.tier-card__lock-watermark`).

**11 of 12 active extensions on Rung 2+** (everything except `clipboard`, which uses a different pre-Tier-0.5 paid-tier ladder; full migration is HIGH-deferred Phase 2).

Strike 018 closed the `tier-card--upcoming` legacy-variant gap: `migration-pilot` and `scripture-scout` now use the canonical `tier-card--locked` class name. Their dead local `--upcoming` CSS rules were replaced with marker comments pointing to `../lib/transparency-tier.css` for the canonical styling.

### IV.d — Rung 3: Tier state machine + locked/unlocked logic

Extension has `lib/tier.js` (or equivalent) exporting `getTier()` / `setTier()` / `isVaultUnlocked()`. Options-page JS reads tier on load and toggles `.tier-card--locked` ↔ `.tier-card--unlocked` accordingly.

**🏆 12 of 12 active extensions on Rung 3+** (post-Strike-021 — fleet-wide 100% milestone): `864z-chronical` (Rung 4 — Strike 013 reference) + the 7 Strike-016/017 cohort (DataNap, Focus Note, Focus Wall, Signal2Noise, Time2Focus, TuneOut2FocusIn, who-is-watching) + `Bible-Insight` (Strike 018) + `migration-pilot` + `scripture-scout` (Strike 019) + `clipboard` (Strike 021 Phase-2 closure).

**Rung 0/1/2 are now empty buckets** for the active fleet. The next ladder advance is Rung 3 → Rung 4 (paywall + dev-override + DEV_NOTES) — that's a per-extension upgrade with cumulative effort but no longer a structural compliance gap.

### IV.e — Rung 4: Paywall + dev-override + DEV_NOTES

Extension has a stub or real payment-processor integration on the unlock CTA + the `?dev=1` URL-gated dev-override panel + a `DEV_NOTES.md` documenting both. **This is the "Tier-0.5 SHIPPED" tier.**

**1 extension on Rung 4**: `864z-chronical` (with payment stub flagged for ExtPay replacement before any public release).

**8 extensions are at "Rung 4 minus payment integration"** — they have the dev-override panel + URL gate + tier-state machine, but lack the production unlock CTA wiring. Each needs ~30 min to replicate Chronicle's stub-CTA pattern, then the operator-side payment integration is a separate per-extension call.

---

## V. Recommended Strike Sequence (priority-ordered, post-Strike-022 / EOD 2026-05-09)

> 🔥 **TOMORROW MORNING — START HERE:** **Chronicle ExtPay Integration** (P0-TOP). All compliance work for the active 12-extension fleet is closed; the next strike pivots from compliance to revenue. Full implementation spec is in [`extensions/864z-chronical/CHRONICLE_CHECKOUT_BLUEPRINT.md`](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/864z-chronical/CHRONICLE_CHECKOUT_BLUEPRINT.md) — 3 entry points, 6 operator pre-integration items, 6 failure modes, generalization path for the other 11 Rung-3 extensions.

| Priority | Strike candidate | Effort | Unlocks |
|---|---|---|---|
| **🔥 P0-TOP (TOMORROW)** | **Chronicle ExtPay implementation** per `CHRONICLE_CHECKOUT_BLUEPRINT.md` — 3 entry points: (a) SW `initPayments + onPaid` in `service-worker.js`; (b) Options page `onUnlockVault` swap to `extpay.openPaymentPage()` in `options/options.js`; (c) shared `TIER_UNLOCKED` broadcast listener (one-line addition to canonical `lib/options-tier-init.js`) | ~3-4h | Promotes Chronicle from Rung-4-stub → Rung-4-real-payment; **first revenue-generating extension goes live**; the rollout proves the pattern for the other 11 Rung-3 extensions (per blueprint §VI generalization, ~5.5h batched after) |
| ~~P0~~ | ~~All prior Rung-0/1/2 closures + Bible-Insight audit + Bible-Insight §Disclosure + canonical-IDs + Bible-Insight tier-model + clipboard Phase 2~~ | — | ✅ **ALL CLOSED** across Strikes 016 → 021 |
| ~~P0~~ | ~~clipboard RULE-007 §Disclosure block~~ | — | ✅ **CLOSED** in Strike 022 |
| ~~P2~~ | ~~Extract per-extension inline tier-init scripts to shared `lib/options-tier-init.js`~~ | — | ✅ **CLOSED** in Strike 022 (11 extensions consolidated; chronicle excluded as separate follow-up) |
| **P1** | Migrate chronicle's `options.js` tier-init logic to use shared `lib/options-tier-init.js` (currently the lone holdout — uses options.js not inline script) | ~30 min careful surgery | Brings chronicle into the shared-script pattern; 12/12 fleet uses shared tier-init |
| **P1** | DataNap Web Store listing update (rebrand publish) | ~1h | Operator-side marketing; required pre-publish |
| **P1** | Bible-Insight + clipboard: ExtPay integration replicating Chronicle's pattern (per blueprint §VI generalization path) | ~30 min × 2 = ~1h batched (after Chronicle proves the pattern) | Promotes Bible-Insight (Sovereign Research Kit) + clipboard (Sovereign History) from stub → real payment |
| **P2** | Replicate ExtPay integration across the remaining 9 Rung-3 extensions (per blueprint §VI) | ~30 min × 9 = ~4.5h batched | Promotes 9 extensions from Rung-3 → Rung-4-real-payment |
| **P2** | Vendor canonical `ExtPay.js` SDK to `864z-build-kit/references/core/payments/` (currently only in clipboard's lib) | ~30 min | Single source of truth for ExtPay SDK across the fleet |
| **P3** | ScriptureScout pre-flight scarcity OR (DIV-1 Live Scout) | ~1-2h | Operator-driven competitive recon; charter held in BACKLOG.md |

---

## VI. Per-Pillar Readiness Snapshot (post-Strike-021 — Fleet-Wide 100% Milestone)

| Pillar | Active Extensions | Avg readiness rung | Visual-binding compliance | Highest-rung | Lowest-rung |
|---|---|---|---|---|---|
| **OIA / ADHD** (Slate & Sage) | 8 | Rung 3.0 | 🏆 **8 / 8 (100%)** | `864z-chronical` (Rung 4) | (no sub-Rung-3) |
| **864-Flux** (Slate & Graphite) | 2 | Rung 3.0 ⬆ from 2.0 | 🏆 **2 / 2 (100%)** | `migration-pilot` & `clipboard` ⬆ promoted in Strike 021 | (no sub-Rung-3) |
| **FHG** (Charcoal & Bronze) | 2 | Rung 3.0 | 🏆 **2 / 2 (100%)** | `Bible-Insight` & `scripture-scout` both Rung 3 | (no sub-Rung-3) |

**🏆🏆🏆 Strike-021 FLEET-WIDE 100% Milestone:** all 3 pillars at **100% Rung-3+ visual-binding compliance**. **Active fleet: 12 / 12 (100%)** on every primary axis: RULE-001 + RULE-006 v1.1 + SW `type: "module"` + Tier-0.5 Rung-3+ + canonical-ID visual binding. The Tier-0.5 readiness ladder is no longer a per-extension shortlist; it is now a fleet-wide property. The next ladder advance is Rung 3 → Rung 4 (paywall + DEV_NOTES) — that's a per-extension upgrade with cumulative effort but no longer a structural compliance gap.

---

## VII. Cross-References

- Programmatic source data: `extensions/*/manifest.json` (15 files) + `extensions/*/_locales/*/messages.json` + `extensions/*/options/*` (8 options pages) + `extensions/*/lib/*` (per-extension copies of design-system + transparency-tier).
- Canonical CSS: [`864z-build-kit/references/core/transparency-tier.css`](../../864zeros-llc/864z-build-kit/references/core/transparency-tier.css) — the visual contract that all 9 options-bearing extensions reference.
- Tier-0.5 visual spec: [`extensions/864z-chronical/TIER_0_5_BLUEPRINT.md`](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/864z-chronical/TIER_0_5_BLUEPRINT.md).
- Sovereign Link spec: [`extensions/864z-chronical/SOVEREIGN_LINK_PROPOSAL.md`](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/864z-chronical/SOVEREIGN_LINK_PROPOSAL.md).
- Dev-override discipline: [`extensions/864z-chronical/DEV_NOTES.md`](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/864z-chronical/DEV_NOTES.md) §I.
- Pillar doctrine: [`864zeros_PILLAR_STRATEGY.md`](./864zeros_PILLAR_STRATEGY.md).
- Per-rule compliance audit: [`864zeros_TECH_STACK_AUDIT.md`](./864zeros_TECH_STACK_AUDIT.md).
- Strategic timing: [`864zeros_2026_ROADMAP.md`](./864zeros_2026_ROADMAP.md).
- Privacy/data-sovereignty audit: [`864zeros_SOVEREIGN_GAP_REPORT.md`](./864zeros_SOVEREIGN_GAP_REPORT.md).
- Active sprint state: [`../ISD-DIV-5-EVOLUTION/BACKLOG.md`](../ISD-DIV-5-EVOLUTION/BACKLOG.md).
- Append-only event ledger: [`../ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md`](../ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md).

---

## VIII. Versioning

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-09 | Initial. Programmatic survey of all 15 extensions across 3 pillars (OIA 11 · 864-Flux 2 · FHG 2). Tier-0.5 readiness ladder (Rung 0 → Rung 4) codified with per-rung effort estimates. RULE-006 v1.1 fleet compliance: 15/15 (Zero-Point Audit verified). 1 extension on Rung 4 (chronicle); 2 on Rung 2; 6 on Rung 1; 6 on Rung 0 (BLOCKED on RULE-001). Recommended strike sequence published. |
| 1.1 | 2026-05-09 | Post-Strikes-016+017 update. **Active fleet: 12** (3 archived: `oia.focus.signal/sound`, `oia-focus-timer`). TabVault → DataNap rebrand. 6 OIA extensions promoted Rung 0/1 → Rung 2-3 via Strike 016. who-is-watching promoted Rung 0 → Rung 3 via Strike 017 (also closes SW `type: "module"` modernization gap). **100% fleet compliance milestone: RULE-001 + RULE-006 v1.1 + SW type:module all at 12/12.** Strike sequence updated: P0 batch RULE-001 scaffold ✅ CLOSED; new P0 = Bible-Insight RULE-007 audit + lib/tier.js distribution. Per-pillar avg rung shift: OIA 1.0 → 3.0; 864-Flux unchanged (Phase-2 deferred); FHG 1.5 → 2.0. |
| 1.2 | 2026-05-09 | Post-Strike-018 update. **Bible-Insight promoted Rung 2 → Rung 3** (full state machine + dev gate). Bible-Insight per-extension RULE-007 audit doc delivered (verdict: structurally compliant; BYOK Gemini, debugger bounded to PDF generation, no proxy; one outstanding §Disclosure UX gap = new P0). migration-pilot + scripture-scout `tier-card--upcoming` → `tier-card--locked` HTML alias (matches Chronicle Standard); dead local CSS rules replaced with marker comments. Rung 3+ cohort grew 8 → 9 (75% of active fleet). FHG avg rung 2.0 → 2.5 (Bible-Insight at Rung 3; scripture-scout still Rung 2 pending lib/tier.js). New P1 MICRO: copy lib/tier.js + inline tier-init script to migration-pilot + scripture-scout (~10 min batched) — would bring active fleet to 11/12 on Rung 3+. |
| 1.3 | 2026-05-09 | Post-Strike-019 update. **Three sub-strike deliverables:** (1) Bible-Insight RULE-007 §Disclosure block injected before brand-footer (verbatim from audit doc §V.a) — closes the one outstanding P1 from Strike 018 audit; (2) `lib/tier.js` distributed to migration-pilot + scripture-scout + dev-override panel + inline `<script type='module'>` tier-init injected — both promoted Rung 2 → Rung 3; (3) NEW operational artifacts at LLC-DIV-3-FACTORY/ root: `FACTORY_LEDGER.jsonl` (machine-readable JSON-per-line audit stream) + `SESSION_STREAM.md` (human-readable companion) — append-only audit trail of every atomic factory mutation. **Rung 3+ cohort grew 9 → 11 (92% of active fleet)** — only `clipboard` remains on Rung 1 (Phase-2 HIGH-deferred). 864-Flux avg rung 1.5 → 2.0; FHG avg rung 2.5 → 3.0 (now full uniformity at Rung 3). Honest defect: 2 ledger entries were written prematurely (in parallel with failed Edits requiring Read-first); correction entry appended honoring CLAUDE-INTEGRITY. |
| 1.4 | 2026-05-09 | Post-Strike-020 update. **🏆 Visual-compliance milestone**: OIA (ADHD) and FHG pillars are now **100% Rung-3 visual-binding compliant** — every options page in those pillars (10 of 10 active OIA+FHG extensions) has the canonical `vault-tier-card` / `current-tier-name` / `vault-lock-watermark` IDs that the inline tier-init script targets; visual state transitions on tier-flip work end-to-end. 864-Flux is at 1/2 (clipboard pending Phase 2). **Bible-Insight tier rebrand**: "⌖ Tier-0.5: Vault" → "⌖ Sovereign Research Kit" per Operator GTM decision; $2.99 perpetual unlock model (Chronicle pattern); closes Strike-018 P0 GTM-decision. 5-feature list expanded; "why $2.99 once" rationale added. Internal tier flag name unchanged (TIER_VAULT) for cross-extension code consistency. **Strike Sequence**: 6 prior items marked CLOSED; new P0 = Clipboard Phase 2 (now the LAST sub-Rung-3 extension); new P2 = Bible-Insight ExtPay integration for Sovereign Research Kit. |
| 1.5 | 2026-05-09 | Post-Strike-021 — **🏆🏆🏆 FLEET-WIDE 100% RUNG-3 MILESTONE.** clipboard Phase-2 closure: prior strikes had already given clipboard the [864F] prefix + SW type:module + brand-footer + linked transparency-tier.css; Strike 021 added the missing pieces (`lib/tier.js`, NEW Sovereign History tier-card with canonical IDs, dev-override panel + inline tier-init, `id="current-tier-name"` on existing tier-badge). Per-extension `RULE_007_AUDIT.md` delivered (~16 KB; 8 sections covering BYOK Gemini + debugger + chrome.identity Google OAuth + ExtPay 3rd-party + chrome.management; verdict: structurally compliant; one P1 §Disclosure UX gap pending). **Active 12-extension fleet: 12/12 (100%) Rung 3+ AND 12/12 (100%) visual-binding compliant. All 3 pillars (OIA/ADHD + 864-Flux + FHG) at 100% Rung-3 visual-compliance.** The Tier-0.5 readiness ladder is now a fleet-wide property; Rung 0/1/2 buckets are empty. Per-pillar avg rung: OIA 3.0 (unchanged) · 864-Flux 2.0 → 3.0 · FHG 3.0 (unchanged). Strike Sequence: ALL prior P0 items CLOSED across Strikes 016-021; new P0 = clipboard RULE-007 §Disclosure block injection (~30 min). |
| 1.6 | 2026-05-09 | Post-Strike-022 — **CONSOLIDATION + PAYMENT-ARCHITECTURE SPEC.** Three deliverables: (1) clipboard RULE-007 §Disclosure block injected (verbatim from audit §VI.a; covers all 5 high-trust surfaces); closes Strike-021 P1. (2) Shared `lib/options-tier-init.js` extracted from per-extension inline scripts; canonical at `864z-build-kit/references/core/options-tier-init.js`; distributed to 11 extensions (chronicle excluded — uses `options/options.js` not inline; queued as P1 follow-up). 11 inline `<script type="module">` blocks replaced with `<script src="../lib/options-tier-init.js">` linkage; eliminates ~80 LOC of cross-extension duplication. (3) Chronicle Checkout Blueprint authored (`extensions/864z-chronical/CHRONICLE_CHECKOUT_BLUEPRINT.md`, ~15 KB / 8 sections). Identifies 3 ExtPay entry points (SW initPayments+onPaid, Options page CTA swap, shared TIER_UNLOCKED listener), 6 operator pre-integration checklist items, 6 failure modes + mitigations, generalization path for the other 11 Rung-3 extensions. Strike Sequence: 3 prior items marked CLOSED (clipboard §Disclosure, shared options-tier-init.js extraction, RULE-008 strike sequence cleanup); new P0 = Chronicle ExtPay implementation per blueprint (~3-4h); new P1 = chronicle migration to shared options-tier-init.js (~30 min); new P1 = Bible-Insight + clipboard ExtPay replication after Chronicle proves the pattern. Active fleet readiness unchanged at 12/12 Rung 3+ (Strike 022 was consolidation + spec, not a Rung promotion). |
| 1.65 | 2026-05-09 EOD | Post-Strike-023 EOD wrap-up — **COMPLIANCE-TO-REVENUE PIVOT.** Three deliverables: (1) FACTORY_LEDGER.jsonl + SESSION_STREAM.md audit verified — 39 entries (38 from Strike 019-022 arc + 1 from Strike 023 init); 39/39 valid JSON; 39/39 schema-complete (all 7 required fields); timestamps monotonic; stream/ledger 1:1 correspondence intact. (2) §V Strike Sequence reorganized: **Chronicle ExtPay Integration moved to ABSOLUTE TOP of P0 queue** (🔥 P0-TOP) with "TOMORROW MORNING — START HERE" annotation; first revenue-generating strike. (3) NEW EOD_LOG.md at `LLC-DIV-3-FACTORY/EOD_LOG.md` summarizing today's compliance-to-revenue pivot (Strike 016 → 022 = 7 strikes closing all Rung-0/1/2 gaps + 100% fleet milestone + payment blueprint). No Rung promotions in Strike 023 (audit + sequence reorganization only); active fleet remains 12/12 Rung 3+. |

---

*864zeros Factory Manifest v1.65 · 2026-05-09 EOD · 864zeros LLC · DIV-6-KNOWLEDGE.*
