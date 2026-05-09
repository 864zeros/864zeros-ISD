# 864zeros: Factory Manifest [v1.0]

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

15 extensions across 3 pillars. Tier-0.5 readiness distribution snapshot (2026-05-09):

| Status | Count | Extensions |
|---|---|---|
| **✅ TIER-0.5 SHIPPED** | 1 | `864z-chronical` |
| **🟢 SCAFFOLD-READY (markup present)** | 2 | `migration-pilot`, `scripture-scout` |
| **🟢 SCAFFOLD-READY (CSS only)** | 6 | `Bible-Insight`, `clipboard`, `Signal2Noise`, `TabVault`, `Time2Focus`, `TuneOut2FocusIn` |
| **❌ BLOCKED** (no `options_ui` → RULE-001 violation) | 6 | `oia-focus-note`, `oia-focus-timer`, `oia-focus-wall`, `oia.focus.signal`, `oia.focus.sound`, `who-is-watching` |

Pillar distribution: **OIA 11 · 864-Flux 2 · FHG 2** (per `864zeros_PILLAR_STRATEGY.md` §VI). All 15 are RULE-006 v1.1 compliant on `extName` (Zero-Point Audit verified 15/15 on 2026-05-09).

---

## III. Per-Extension Manifest

| Extension | Pillar | Display name (post-RULE-006 v1.1) | Version | Options page | Tier-0.5 Status |
|---|---|---|---|---|---|
| `864z-chronical` | OIA | `[OIA] Chronicle` | 1.1.0 | ✅ `options/options.html` | **✅ TIER-0.5 SHIPPED** — full implementation: tier card + `lib/tier.js` state helper + Sovereign Link header button + RULE-005 two-tap Clear All + ?dev=1 dev-override panel + DEV_NOTES.md. Strike 013 reference impl. |
| `Bible-Insight` | FHG | `[FHG] Bible Insight` | 1.0.0 | ✅ `html/options.html` | 🟢 **SCAFFOLD-READY (CSS only)** — has `lib/transparency-tier.css` linked; tier-card markup not yet wired. Pillar confirmed 2026-05-09. |
| `clipboard` | 864-Flux | `[864F] ClipBoard` | 1.0.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY (CSS only)** — has shared CSS linked. Existing tier ladder (Free/Starter/Pro/Power) uses different markup; needs migration to canonical `tier-card--locked` form. |
| `migration-pilot` | 864-Flux | `[864F] MigrationPilot — Web to Obsidian` | 0.1.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY (markup present)** — has `.tier-card` markup + Liberate verb already (matches Sovereign Link intent). Needs: rename `tier-card--upcoming` → `tier-card--locked` (or alias the modifier), add `lib/tier.js`, wire paywall stub. |
| `oia-focus-note` | OIA | `[OIA] oia.focus.note` | 1.1.0 | ❌ NONE | **❌ BLOCKED** — RULE-001 violation. No `options_ui`. Tier-0.5 cannot ship until Options page scaffold lands. |
| `oia-focus-timer` | OIA | `[OIA] oia.focus` | 1.1.0 | ❌ NONE | **❌ BLOCKED** — RULE-001 violation. |
| `oia-focus-wall` | OIA | `[OIA] oia.focus.wall` | 1.1.0 | ❌ NONE | **❌ BLOCKED** — RULE-001 violation. |
| `oia.focus.signal` | OIA | `[OIA] oia.focus.signal` | 1.1.0 | ❌ NONE | **❌ BLOCKED** — RULE-001 violation. |
| `oia.focus.sound` | OIA | `[OIA] oia.focus.sound` | 1.1.0 | ❌ NONE | **❌ BLOCKED** — RULE-001 violation. |
| `scripture-scout` | FHG | `[FHG] ScriptureScout` | 0.1.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY (markup present)** — has `.tier-card` markup + brand-footer + RULE-006 v1.1. Needs: tier-card-locked variant + `lib/tier.js` + paywall flow. Founding-100 cohort gates real launch. |
| `Signal2Noise` | OIA | `[OIA] Signal2Noise` | 1.0.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY (CSS only)** — shared CSS linked; tier-card markup pending. |
| `TabVault` | OIA | `[OIA] TabVault (864z)` | 1.0.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY (CSS only)** — shared CSS linked; tier-card markup pending. (Optional: drop the legacy `(864z)` parenthetical at next routine touch.) |
| `Time2Focus` | OIA | `[OIA] Time2Focus` | 1.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY (CSS only)** — shared CSS linked; tier-card markup pending. |
| `TuneOut2FocusIn` | OIA | `[OIA] Tune Out 2 Focus In` | 1.0.0 | ✅ `options/options.html` | 🟢 **SCAFFOLD-READY (CSS only)** — shared CSS linked; tier-card markup pending. |
| `who-is-watching` | OIA | `[OIA] Who Is Watching` | 2.1.6 | ❌ NONE | **❌ BLOCKED** — RULE-001 violation. Highest-version extension in fleet (2.1.6); also lacks SW `type: "module"` (separate modernization gap). |

---

## IV. Tier-0.5 Readiness Ladder

A four-rung ladder describing what each extension needs to advance to the next tier of Tier-0.5 readiness. Lower rungs are prerequisites for higher rungs.

### IV.a — Rung 0: Cog-triggered Options page (RULE-001)

**Prerequisite for ANY Tier-0.5 work.** An extension cannot host a tier disclosure until it has an `options_ui` page conforming to RULE-001's three mandatory sections (How to Use · Subscription & Tiers · Data Management).

**6 extensions on Rung 0**: `oia-focus-note`, `oia-focus-timer`, `oia-focus-wall`, `oia.focus.signal`, `oia.focus.sound`, `who-is-watching`.

**Estimate to clear:** ~3-4h batched for the 5 `oia.focus.*` extensions (they share a Focus-class scaffold); ~2h for `who-is-watching` (RULE-001 + SW module migration in same touch). Total Rung 0 → Rung 1: ~5-6h focused.

### IV.b — Rung 1: Transparency baseline (CSS + brand-footer + brand-prefix pill)

Extension has the shared `lib/transparency-tier.css` linked + the standardized 4-line brand-footer rendered + the RULE-006 v1.0 `.brand-prefix` pill in surface headers. **Visual contract for tier disclosure is in place** even if the actual tier card hasn't been built yet.

**8 of 9 options-bearing extensions on Rung 1+** (everything except `864z-chronical`, which is on Rung 4). After post-Strike-014 transparency consolidation, all 8 link the shared CSS and have brand-footers.

### IV.c — Rung 2: Tier-card markup wired

Extension's options.html has `<div class="tier-card tier-card--locked">...</div>` markup with the canonical structure (`.tier-card__head`, `.tier-card__name`, `.tier-card__price`, `.tier-features`, `.tier-card__cta`, `.tier-card__lock-watermark`).

**3 extensions on Rung 2+**: `864z-chronical` (canonical), `migration-pilot` (uses `tier-card--upcoming` variant — needs alias or rename to `--locked`), `scripture-scout` (same as migration-pilot).

**Estimate to bring 6 SCAFFOLD-READY-CSS-only extensions up to Rung 2**: ~30 min each (mechanical HTML insertion); ~3h batched.

### IV.d — Rung 3: Tier state machine + locked/unlocked logic

Extension has `lib/tier.js` (or equivalent) exporting `getTier()` / `setTier()` / `isVaultUnlocked()`. Options-page JS reads tier on load and toggles `.tier-card--locked` ↔ `.tier-card--unlocked` accordingly.

**1 extension on Rung 3+**: `864z-chronical` only (Strike 013 implementation).

**Estimate to bring a Rung-2 extension to Rung 3**: ~1h (copy `lib/tier.js` from chronicle, wire on/off in options.js).

### IV.e — Rung 4: Paywall + dev-override + DEV_NOTES

Extension has a stub or real payment-processor integration on the unlock CTA + the `?dev=1` URL-gated dev-override panel + a `DEV_NOTES.md` documenting both. **This is the "Tier-0.5 SHIPPED" tier.**

**1 extension on Rung 4**: `864z-chronical` (with payment stub flagged for ExtPay replacement before any public release).

**Estimate to advance a Rung-3 extension to Rung 4**: ~2-3h (payment integration is the bulk; dev-override + DEV_NOTES are ~30 min copy-paste from chronicle).

---

## V. Recommended Strike Sequence (priority-ordered)

| Priority | Strike candidate | Effort | Unlocks |
|---|---|---|---|
| **P0** | RULE-001 batch scaffold for the 6 BLOCKED extensions | ~5-6h | Promotes 6 from Rung 0 → Rung 1; closes 6 RULE-001 violations |
| **P1** | Tier-card markup wiring for the 6 SCAFFOLD-READY-CSS-only extensions | ~3h batched | Promotes 6 from Rung 1 → Rung 2 |
| **P1** | Bible-Insight RULE-007 audit (`debugger` permission + AI integration audit) | ~2h | Required before any FHG-pillar release; gates Founding-100 trust contract for Bible-Insight |
| **P2** | Migration-pilot + scripture-scout: alias `tier-card--upcoming` → `tier-card--locked` and add `lib/tier.js` | ~1.5h each | Promotes both from Rung 2 → Rung 3 |
| **P2** | Clipboard Phase 2 (HIGH-deferred) — RULE-001/003/004/005/006/007 deep refactor | ~6-10h | Already-shipping product; closes longest-standing rule-compliance gap |
| **P3** | ScriptureScout pre-flight scarcity OR (DIV-1 Live Scout) | ~1-2h | Operator-driven competitive recon; charter held in BACKLOG.md |
| **P3** | Chronicle ExtPay integration (replace stub) | ~2-3h | Promotes chronicle from Rung 4 (stubbed) → Rung 4 (real); enables public release |

---

## VI. Per-Pillar Readiness Snapshot

| Pillar | Extensions | Avg readiness rung | Highest-rung extension | Lowest-rung extensions |
|---|---|---|---|---|
| **OIA** (Slate & Sage) | 11 | Rung 1.0 | `864z-chronical` (Rung 4) | 5 `oia.focus.*` + `who-is-watching` (Rung 0) |
| **864-Flux** (Slate & Graphite) | 2 | Rung 1.5 | `migration-pilot` (Rung 2) | `clipboard` (Rung 1) |
| **FHG** (Charcoal & Bronze) | 2 | Rung 1.5 | `scripture-scout` (Rung 2) | `Bible-Insight` (Rung 1) |

OIA pillar carries the largest portfolio AND the largest Rung-0 backlog. FHG and 864-Flux are smaller portfolios but have higher per-extension maturity. Tier-0.5 monetization rollout will likely lead with FHG (Bible Insight + ScriptureScout — the Founding-100 trust gate has the strongest paying-customer proxy) followed by 864-Flux (clipboard's existing paid-tier infrastructure makes Tier-0.5 a natural addition).

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

---

*864zeros Factory Manifest v1.0 · 2026-05-09 · 864zeros LLC · DIV-6-KNOWLEDGE.*
