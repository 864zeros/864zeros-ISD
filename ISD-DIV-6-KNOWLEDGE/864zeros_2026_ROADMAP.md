# 864zeros 2026 Engineering Roadmap [v1.0]

**Authority:** Strategic synthesis. Operational ledger remains [`BACKLOG.md`](../ISD-DIV-5-EVOLUTION/BACKLOG.md); this document is the synthesized strategic view for stakeholder ingestion (NotebookLM, founder review, board context).
**Loaded:** On demand for quarterly planning, strike sequencing, founder review.
**Authored:** 2026-05-09 by 864z-OA (Office Architect) under RULE-000.
**Update protocol:** Append a new version after each material strategic pivot OR at quarterly review boundary. Prior versions preserved.
**Format note:** Follows the inferred `864z-markdown-standard` (BUILD_KIT_RULES.md metadata header + MASTER_CONTEXT.md.md atomic body). Standard not yet codified — pending Office Architect sign-off.

---

## I. Roadmap Sources of Truth

| Layer | File | Purpose |
|---|---|---|
| Operational | [`BACKLOG.md`](../ISD-DIV-5-EVOLUTION/BACKLOG.md) | Active Sprint + Recently Completed (week-grain) |
| Historical | [`STRIKE_HISTORY_MASTER.md`](../ISD-DIV-5-EVOLUTION/STRIKE_HISTORY_MASTER.md) | Per-strike outcome record |
| Append-only events | [`reports/SYSTEM_STRIKE_LOG.md`](../ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md) | Gate passes, hook failures, brick promotions, rule codifications |
| **Strategic synthesis (this doc)** | This file | Quarter-grain narrative |

This document is **derived**, not authoritative — when these sources disagree, BACKLOG.md wins for current state and SYSTEM_STRIKE_LOG.md wins for historical claims.

---

## II. Active Sprint State (snapshot 2026-05-09)

| Priority | Item | Owner | Status |
|---|---|---|---|
| **HIGH-deferred** | Clipboard Phase 2 — RULE-001 / 003 / 004 / 005 / 006 / 007 full migration | 864z-SE | Phase 1 complete; Phase 2 needs paid-tier UX decisions before sprint commit (~6-10h focused work; sidepanel/main.js is 2,555 LOC, 5× migration-pilot's size) |
| **MEDIUM** | Pre-flight scarcity OR — `OR-2026-05-XX-SCRIPTURESCOUT.md` | DIV-1-VULTURE Live Scout | Distinct from the readiness OR — `OR_STRIKE_012_PREFLIGHT.md` already shipped. 8.64 competitive scarcity scan still pending. |

All other Active Sprint items closed in the 2026-05-08 sweep. Net-new items expected post-Founding-100 enrolment.

---

## III. Last 7 Days — Shipped (2026-05-02 → 2026-05-09)

**Strikes harvested:**
- **Strike 011 (MigrationPilot)** — first strike under the brick-extraction protocol; harvested 3 bricks (BRK-DL-001 headless-download-uri, BRK-UI-002 tristate-checkbox-list, BRK-UI-003 two-tap-arm-pattern); codified RULE-001 / RULE-002 / RULE-003.
- **Strike 012 (ScriptureScout)** — full FHG pillar launch lane: Bronze Compass icon generator, 10-section operator smoke-test checklist, Founding 100 waitlist form copy, ScriptureScout sidepanel + options scaffold, BRK-UI-004 accordion-record-v1 promotion (first directory-format brick), RULE-004 codification.
- **Post-Strike-012 launch polish** — RULE-005 (two-tap), RULE-006 (brand-prefix), RULE-007 (secret sovereignty) codified; BRK-UI-003 promoted from RULE-001 §3 sub-clause to first-class RULE-005; BRICK_REGISTRY v1.3 changelog recorded.

**Compliance migrations:**
- **RULE-004 audit + migration: `migration-pilot`** (864-Flux Graphite palette + canonical accordion class names).
- **RULE-004 audit + migration: `TabVault`** (OIA Sage retained; group-collapse pattern preserved over per-record accordion).
- **Global compliance audit Phase 1: `clipboard`** (Graphite palette + brand-prefix + brand-footer + README citation; Phase 2 deferred).

**Governance + documentation:**
- **Office Architect role formalized** in [`ROLES/OFFICE_ARCHITECT.md`](../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md) + [`ROLES/README.md`](../../864zeros-llc/ROLES/README.md).
- **RULE-000 (Architectural Governance)** codified — gates all rule additions and brick promotions.
- **6 cross-repo Division READMEs** written (DIV-0 / DIV-1 / DIV-3 / DIV-4 / DIV-5 / DIV-6).
- **3 DIV-6 Master Documents** authored — `864zeros_PILLAR_STRATEGY.md`, `864zeros_TECH_STACK_AUDIT.md`, this file.

**Active rule set: RULE-000 through RULE-007 (8 active rules).**

---

## IV. Q2 2026 Strategic Targets (current quarter)

### IV.a — Compliance Migration Burndown

| Target | Detail | Effort | Gate |
|---|---|---|---|
| Close 7 RULE-001 violations | 5 `oia.focus.*` (batched scaffold) + `who-is-watching` + `864z-chronicle` | ~3-4h batched + ~2h × 2 individual = ~7-8h | None — pure compliance work |
| Universal RULE-006 audit + injection | 11 unaudited extensions × ~30 min mechanical | ~5-6h | None |
| RULE-007 audit of `864z-chronicle` | AI-conversation capture is secret-adjacent | ~1h | Pre-public-release for that extension |
| `who-is-watching` SW modernization → `type: "module"` | Lone non-module SW; modernization debt | ~2h | Required before adopting any ESM-only brick |
| 32px icon addition across 14 manifests | Mechanical manifest edit + asset gen | ~10 min × 14 = ~2.5h | Retina toolbar rendering polish |

### IV.b — Active Strike Charters

| Strike | Pillar | Status | Next gate |
|---|---|---|---|
| **Clipboard Phase 2** | 864-Flux | Charter held — needs paid-tier UX decisions | UX decision review with Operator |
| **ScriptureScout pre-flight scarcity OR** | FHG | Charter held — DIV-1 Live Scout queue | 8.64 competitive scan pass |
| **Bible Insight (planned)** | FHG | Pre-charter | Strike charter draft + RULE-007 BYOK design from day 1 |

### IV.c — Founding-100 Cohort (FHG)

- **Open intake:** ScriptureScout waitlist form deployed at `864zeros.com/scripturescout` (per [`WAITLIST_FORM_COPY.md`](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/scripture-scout/WAITLIST_FORM_COPY.md)).
- **Closure trigger** (any one fires, per `OR_STRIKE_012_PREFLIGHT.md` §1.2): 100 users complete ≥1 Liberation, OR 60 days elapse, OR Office Architect signs off on early close.
- **Phase 4 Closed Beta gate:** opens after Founding 100 closes; ~50 invitations/week from Score-3 then Score-2 wait-list.

---

## V. Q3 2026 Strategic Themes (next quarter)

| Theme | Why now | Lead |
|---|---|---|
| **Brand-firewall hardening** | RULE-006 universal adoption unlocks reliable Web Store screenshot batches and per-pillar marketing pivots | DIV-4-STUDIO + 864z-OA |
| **Founding-100-grade trust gate universalized** | RULE-007 audit must conclude across all 15 extensions before any cross-extension marketing campaign | 864z-OA + 864z-SE |
| **Brick compounding cadence** | Every Q3 strike must harvest at least 1 new brick OR promote an existing brick under RULE-000 | All Strike Owners |
| **Pillar diversification** | FHG → ≥3 extensions (add 2nd: Bible-Insight; cued 3rd TBD); 864-Flux → ≥3 (clipboard Phase 2 + new strike); OIA depth not breadth (consolidate `oia.focus.*` family or kill underperformers) | Operator + Systems Architect |
| **Public-launch playbook** | After ScriptureScout Founding 100 closes successfully, formalize the playbook (waitlist → cohort → close → Closed Beta → public) for FHG and 864-Flux re-use | DIV-4-STUDIO |

---

## VI. 2026 Strategic Constants (Won't Change This Year)

These are explicit guardrails — **NOT** roadmap items. Drift here triggers Office Architect escalation.

- **Brand Firewall is inviolable.** Three pillars; palettes never bleed (per RULE-006 + GTM_MANIFEST §7).
- **Append-only governance.** RULES never deleted, only superseded. STRIKE LOGS never edited (per RULE-000).
- **Local-first sovereignty.** No user data ever transits 864zeros infrastructure (per RULE-007).
- **Panel-only extensions.** Every Chrome extension is side-panel; no popup, no DevTools surfaces.
- **Strike-and-harvest cadence.** Every shipping strike concludes with a harvest into the build kit.
- **NO FALSE OPTIMISM.** Every DIV-1 lead is terminated unless it passes the 8.64 financial threshold.
- **One challenge at a time.** Every product is single-purpose; no consolidation pressure (per GTM §1).

---

## VII. Risks & Watch Items (2026-05-09)

| Risk | Severity | Mitigation |
|---|---|---|
| Clipboard Phase 2 paid-tier UX risk | HIGH | Phase 2 deferred until UX decisions converge; running incrementally on Phase 1 in production |
| RULE-001 backlog (7 violations) blocking any non-compliant Web Store release | MEDIUM | Q2 scaffold sweep planned (~7-8h batched) |
| `864z-chronicle` RULE-007 audit (secret-adjacent AI capture) | MEDIUM | Q2 scheduled; defer any public release until cleared |
| **DIV-2 numbering gap** in division layout (jumps from DIV-1 to DIV-3) | LOW | Queued for OFFICE_ARCHITECT.md §VI reconciliation; no operational impact |
| **DIV-6 source-of-truth filename typo** (`864zeros_MASTER_CONTEXT.md`) | LOW | Rename queued for next cleanup pass with NotebookLM re-index coordination — not renamed in-place to avoid breaking active ingestion |
| Compliance audit backlog: 10+ extensions UNAUDITED for RULE-001/002/003/005/006 | MEDIUM | Q2 burndown queue published in TECH_STACK_AUDIT §VI |
| 864z-markdown-standard not codified despite being cited | LOW | Inferred standard documented in this doc and the other DIV-6 masters; formal codification queued as a new RULE candidate |

---

## VIII. Cross-References

- Operational backlog: [`ISD-DIV-5-EVOLUTION/BACKLOG.md`](../ISD-DIV-5-EVOLUTION/BACKLOG.md)
- Strike outcome ledger: [`ISD-DIV-5-EVOLUTION/STRIKE_HISTORY_MASTER.md`](../ISD-DIV-5-EVOLUTION/STRIKE_HISTORY_MASTER.md)
- Append-only event log: [`ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md`](../ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md)
- Pillar doctrine: [`864zeros_PILLAR_STRATEGY.md`](./864zeros_PILLAR_STRATEGY.md)
- Engineering snapshot: [`864zeros_TECH_STACK_AUDIT.md`](./864zeros_TECH_STACK_AUDIT.md)
- Rules: [`864z-build-kit/references/core/BUILD_KIT_RULES.md`](../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md) (RULE-000 through RULE-007)
- Office Architect role: [`ROLES/OFFICE_ARCHITECT.md`](../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md)

---

## IX. Versioning

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-09 | Initial synthesis. Q2 2026 targets locked: 7-extension RULE-001 backlog burndown + universal RULE-006 audit + RULE-007 sweep of `864z-chronicle` + 32px icon universalization + `who-is-watching` SW modernization. Q3 themes: brand-firewall hardening, RULE-007 universal audit, brick-compounding cadence, pillar diversification (FHG → ≥3), public-launch playbook formalization. 7 strategic constants flagged as inviolable. 7 risks tracked. |

---

*864zeros 2026 Engineering Roadmap v1.0 · 2026-05-09 · 864zeros LLC · For DIV-6 NotebookLM ingestion.*
