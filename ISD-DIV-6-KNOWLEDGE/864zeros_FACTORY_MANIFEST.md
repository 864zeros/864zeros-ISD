# 864zeros: Factory Manifest [v1.4]

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

**12 active extensions** across 3 pillars (post-Strike-016 archival: 3 legacy `oia.focus.*` extensions moved to `_archive/`; TabVault rebranded to DataNap). Tier-0.5 readiness distribution snapshot (2026-05-09 post-Strike-019):

| Status | Count | Extensions |
|---|---|---|
| **✅ TIER-0.5 SHIPPED** | 1 | `864z-chronical` |
| **🟢 SCAFFOLD-READY (Rung 3 — markup wired + state machine + dev gate)** | **10** | `Bible-Insight`, `DataNap`, `Focus Note` (`oia-focus-note`), `Focus Wall` (`oia-focus-wall`), `migration-pilot` ⬆ promoted in Strike 019, `scripture-scout` ⬆ promoted in Strike 019, `Signal2Noise`, `Time2Focus`, `TuneOut2FocusIn`, `who-is-watching` |
| **🟡 SCAFFOLD-READY (CSS only)** | 1 | `clipboard` (Phase 2 deep refactor still HIGH-deferred) |
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
| `clipboard` | 864-Flux | `[864F] ClipBoard` | 1.0.0 | ✅ `options/options.html` | 🟡 **SCAFFOLD-READY (CSS only)** — has shared CSS linked. Existing tier ladder (Free/Starter/Pro/Power) uses different markup; full migration to canonical `tier-card--locked` form is HIGH-deferred (Clipboard Phase 2). |
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

**11 of 12 active extensions on Rung 3+** (post-Strike-019): `864z-chronical` (Rung 4 — Strike 013 reference) + the 7 Strike-016/017 cohort (DataNap, Focus Note, Focus Wall, Signal2Noise, Time2Focus, TuneOut2FocusIn, who-is-watching) + `Bible-Insight` (Strike 018) + `migration-pilot` + `scripture-scout` (Strike 019).

Only `clipboard` remains on Rung 1 — Phase 2 deep refactor is HIGH-deferred per the Active Sprint.

### IV.e — Rung 4: Paywall + dev-override + DEV_NOTES

Extension has a stub or real payment-processor integration on the unlock CTA + the `?dev=1` URL-gated dev-override panel + a `DEV_NOTES.md` documenting both. **This is the "Tier-0.5 SHIPPED" tier.**

**1 extension on Rung 4**: `864z-chronical` (with payment stub flagged for ExtPay replacement before any public release).

**8 extensions are at "Rung 4 minus payment integration"** — they have the dev-override panel + URL gate + tier-state machine, but lack the production unlock CTA wiring. Each needs ~30 min to replicate Chronicle's stub-CTA pattern, then the operator-side payment integration is a separate per-extension call.

---

## V. Recommended Strike Sequence (priority-ordered, post-Strike-020)

| Priority | Strike candidate | Effort | Unlocks |
|---|---|---|---|
| ~~P0~~ | ~~RULE-001 batch scaffold for the 6 BLOCKED extensions~~ | — | ✅ **CLOSED** in Strikes 016 + 017 |
| ~~P0~~ | ~~Bible-Insight RULE-007 audit + `lib/tier.js` distribution~~ | — | ✅ **CLOSED** in Strike 018 |
| ~~P0~~ | ~~Bible-Insight: add RULE-007 §Disclosure block to options page~~ | — | ✅ **CLOSED** in Strike 019 |
| ~~P1 MICRO~~ | ~~migration-pilot + scripture-scout: copy `lib/tier.js` + inline tier-init~~ | — | ✅ **CLOSED** in Strike 019 |
| ~~P0 GTM~~ | ~~Bible-Insight tier-model decision: $2.99 perpetual vs $4.99/mo~~ | — | ✅ **CLOSED** in Strike 020 — operator chose $2.99 perpetual ("Sovereign Research Kit"); Chronicle pattern adopted |
| ~~P1~~ | ~~Canonical IDs for migration-pilot + scripture-scout existing tier-card markup~~ | — | ✅ **CLOSED** in Strike 020 — visual binding now complete on both extensions |
| **P0 (NEW)** | Clipboard Phase 2 (HIGH-deferred) — RULE-001 / 003 / 004 / 005 / 006 / 007 deep refactor + Tier-0.5 wiring | ~6-10h | Now the LAST remaining sub-Rung-3 extension; closes the longest-standing rule-compliance gap; achieves 12/12 Rung-3+ across active fleet |
| **P1** | DataNap Web Store listing update (rebrand publish) | ~1h | Operator-side marketing; required pre-publish |
| **P2** | Extract per-extension inline `<script type="module">` to shared `lib/options-tier-init.js` | ~2h | Eliminates 11-extension code duplication; future maintenance lift |
| **P2** | Replicate chronicle's stub-unlock CTA pattern across the 10 Rung-3 extensions | ~30 min × 10 = ~5h | Promotes 10 extensions from Rung-3 to "Rung-4-minus-payment" |
| **P2** | Bible-Insight: real ExtPay (or equivalent) checkout integration for "Sovereign Research Kit" $2.99 unlock | ~3-4h | Replaces the disabled stub CTA with real payment; gates Bible-Insight public release |
| **P3** | ScriptureScout pre-flight scarcity OR (DIV-1 Live Scout) | ~1-2h | Operator-driven competitive recon; charter held in BACKLOG.md |
| **P3** | Chronicle ExtPay integration (replace stub) | ~2-3h | Promotes chronicle from Rung 4 (stubbed) → Rung 4 (real); enables public release |

---

## VI. Per-Pillar Readiness Snapshot (post-Strike-020 — Visual-Compliance Milestone)

| Pillar | Active Extensions | Avg readiness rung | Visual-binding compliance | Highest-rung | Lowest-rung |
|---|---|---|---|---|---|
| **OIA / ADHD** (Slate & Sage) | 8 | Rung 3.0 | 🏆 **8 / 8 (100%)** | `864z-chronical` (Rung 4) | (no Rung-2 or below) |
| **864-Flux** (Slate & Graphite) | 2 | Rung 2.0 | 🟡 **1 / 2 (50%)** — migration-pilot ✓; clipboard pending Phase 2 | `migration-pilot` (Rung 3, visual-compliant) | `clipboard` (Rung 1) |
| **FHG** (Charcoal & Bronze) | 2 | Rung 3.0 | 🏆 **2 / 2 (100%)** | `Bible-Insight` & `scripture-scout` both Rung 3, visual-compliant | (no Rung-2 or below) |

**🏆 Strike-020 Visual-Compliance Milestone:** the OIA (ADHD) and FHG pillars are now at **100% Rung-3 visual-binding compliance** — every Rung-3+ extension in those pillars has the canonical `vault-tier-card` / `current-tier-name` / `vault-lock-watermark` IDs that the inline tier-init script targets. When the dev gate (or future production payment flow) flips `chrome.storage.local.tier`, every OIA + FHG options page reflects the change visually (locked → unlocked, ⊘ → ✓, "LOCKED" → "UNLOCKED" + sage). Only 864-Flux is at partial visual-compliance (clipboard Rung 1, awaiting Phase 2). When clipboard's Phase 2 lands, the entire active fleet hits 12/12 Rung-3+ visual-compliance.

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

---

*864zeros Factory Manifest v1.4 · 2026-05-09 · 864zeros LLC · DIV-6-KNOWLEDGE.*
