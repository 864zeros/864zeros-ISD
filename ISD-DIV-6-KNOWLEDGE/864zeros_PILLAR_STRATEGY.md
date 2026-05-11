# 864zeros: Pillar Strategy [v1.0]

**Authority:** Cross-cutting brand and product doctrine. Synthesizes [`GTM_MANIFEST.md`](../../864zeros-llc/GTM_MANIFEST.md) (v1.1) into a single ingestion-ready strategic view.
**Loaded:** Always — alongside `864zeros_MASTER_CONTEXT.md` and the `BUILD_KIT_RULES.md` rule set.
**Authored:** 2026-05-09 by 864z-OA (Office Architect) under RULE-000.
**Update protocol:** Append-only. Pillar additions, palette evolutions, or hook revisions require Office Architect sign-off per [`ROLES/OFFICE_ARCHITECT.md`](../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md) §VI.
**Format note:** Follows the inferred `864z-markdown-standard` (BUILD_KIT_RULES.md metadata header + MASTER_CONTEXT.md.md atomic body). Standard not yet codified — pending Office Architect sign-off as a future RULE.

---

## I. The Parent Manifesto

> *Most complex problems have simple solutions. Most ADHD applications try to solve a complex mind with complexity. We strive to focus on core challenges and BRIDGE THE GAP simply. Focusing on one challenge at a time. Always simple, always yours, and always private.*

The four words that gate every product decision: **simple · yours · private · one-at-a-time**. Loss of any one breaks the contract across all pillars.

---

## II. The Brand Firewall (Inviolable)

Three pillars. Palettes never bleed. Per-pillar voice never crosses surfaces. Enforced at the DOM level by **RULE-006** (Brand-Prefix Pill on Surface Titles).

| Pillar | Identifier | Palette | Primary Hex | Hook |
|---|---|---|---|---|
| **OIA** (Organize Internal Architecture) | `[OIA]` | Slate & Sage | sage `#8BA888` · slate `#475569` | "Built for ADHD by ADHD." |
| **864-Flux** (Kinetic Bridges) | `[864F]` | Slate & Graphite | graphite `#374151` · slate `#475569` | "Making software friendly again." |
| **FHG** (For His Grace) | `[FHG]` | Charcoal & Bronze | charcoal `#2D2D2D` · bronze `#A67C52` | "Heritage-first technology. Preserving what matters most." |

**Firewall mechanic:** every extension's local `oia-design-system.css` swaps token *values* to its pillar's palette without renaming token *identifiers* — component CSS therefore stays portable across pillars while visual identity stays partitioned.

---

## III. Pillar-Specific Doctrine

### III.a — OIA (Slate & Sage)

- **Wedge:** ADHD knowledge workers managing executive-function tax.
- **Doctrine:** Dopamine-Friendly UI (per GTM §3) — high-contrast focal points, no decorative motion, ≤150 ms feedback, one primary action per screen.
- **Surface tone:** warm sage personality, cool slate professionalism, cream canvas.
- **Architect's Hook:** *"Built for people with ADHD by someone with ADHD. Scientifically proven to work for me. So, we're sharing with you."*
- **Reference impl:** `migration-pilot`, `TabVault`, the `oia.focus.*` family.

### III.b — 864-Flux (Slate & Graphite)

- **Wedge:** vault-native knowledge workers escaping bloated proprietary suites.
- **Doctrine:** the kinetic-bridge thesis (per GTM §2) — *"We fill the gaps that the others can't or won't."* Products are bridges, not destinations; users keep their data and pass through.
- **Surface tone:** Graphite (#374151) authority + Slate professional finish. No warmth — this pillar is about velocity.
- **Audience adjacency:** OIA-curious users who don't self-identify as ADHD but feel the same lock-in pain.
- **Reference impl:** `clipboard`, `migration-pilot` (cross-listed — pillar reassigned 2026-05-08).

### III.c — FHG (Charcoal & Bronze · For His Grace)

- **Wedge:** vault-native knowledge workers in faith vocations — pastors, seminarians, theology grad students, lay Bible-study leaders.
- **Doctrine:** Heritage-first technology. Preserve what matters most. Every product in this pillar must function offline, store locally, and survive its provider's eventual sunset.
- **Surface tone:** Charcoal authority + Bronze warmth + Parchment (#F5F5F5) reading surface for long-form study (per RULE-004 §Reading surface).
- **Trust gate:** Founding 100 enrolment cap (per `OR_STRIKE_012_PREFLIGHT.md` §1) — cohort-limited launch with operator-direct support, scoring rubric for mission-alignment filter (see `extensions/scripture-scout/WAITLIST_FORM_COPY.md`).
- **Reference impl:** `scripture-scout`. `Bible-Insight` (planned) MUST adopt FHG pillar from day 1.

---

## IV. Cross-Pillar Constants (Apply Regardless of Pillar)

| Constant | Source | Enforcement |
|---|---|---|
| Local-first storage; user data never leaves the device without explicit user action | GTM §1 + CLAUDE-base.md | **RULE-007** Secret Sovereignty + privacy gate |
| Standardized 4-line footer with inline lock SVG | GTM §6 | Verbatim HTML; no per-pillar variants |
| Brand-prefix pill on side-panel header AND options heading | GTM §2/§7 | **RULE-006** (DOM-level) |
| Cog-triggered Options page with 3 mandatory sections (How to Use · Subscription & Tiers · Data Management) | — | **RULE-001** |
| Two-tap confirm for every destructive control; no `alert/confirm/prompt` | — | **RULE-005** |
| Selection-mode for any record queue (per-record checkboxes + tristate master + selective destructive actions) | — | **RULE-003** |
| Accordion record UI with Parchment surface + Shift+Click multi-expand | — | **RULE-004** |
| MV3 service-worker downloads via Base64 data URI; `URL.createObjectURL` forbidden in SW | — | **RULE-002** + BRK-DL-001 |
| Architect's Hook attribution credit | GTM §4 | About surfaces, marketing pages, options-page extended footer |

---

## V. Pillar Assignment Protocol

1. Strike charter (DIV-1 → DIV-3 handoff) **MUST** name a pillar before any code is committed.
2. Pillar can only be reassigned by **Office Architect sign-off** under RULE-000. (Precedent: `migration-pilot` reassigned OIA → 864-Flux on 2026-05-08; recorded in BACKLOG `Recently Completed`.)
3. A single product **cannot serve two pillars simultaneously.** Cross-pillar reach is achieved by shipping a sibling product, not by palette-blending.
4. New pillar additions require **GTM_MANIFEST.md §7 update + OFFICE_ARCHITECT.md sign-off + a strike entry in `SYSTEM_STRIKE_LOG.md`** before any extension may adopt it.

---

## VI. Pillar Inventory (2026-05-09)

| Pillar | Active Extensions | Count | Notable |
|---|---|---|---|
| **OIA** | `oia.focus.note`, `oia.focus.timer`, `oia.focus.wall`, `oia.focus.signal`, `oia.focus.sound`, `TabVault`, `Signal2Noise`, `Time2Focus`, `TuneOut2FocusIn`, `who-is-watching`, `864z-chronicle` | 11 | Largest portfolio; the focus.* family is the pillar's quintessential expression |
| **864-Flux** | `clipboard`, `migration-pilot` | 2 | Reference impls for RULE-001 through RULE-005; clipboard awaits Phase 2 deep refactor |
| **FHG** | `scripture-scout`, `Bible-Insight` (planned) | 2 (1 shipping) | scripture-scout is the only pillar member shipping; first directory-format brick (BRK-UI-004) was harvested here |

**Pillar diversification target (2026):** FHG to ≥3 extensions; 864-Flux to ≥3; OIA depth-not-breadth (consolidate the focus.* family).

---

## VII. Cross-References

- [`GTM_MANIFEST.md`](../../864zeros-llc/GTM_MANIFEST.md) — source-of-truth for pillar palette, hooks, footer
- [`864z-build-kit/references/core/BUILD_KIT_RULES.md`](../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md) — RULE-000 through RULE-007
- [`ROLES/OFFICE_ARCHITECT.md`](../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md) — §II Brand Firewall + §VI sign-off authority
- [`864zeros_TECH_STACK_AUDIT.md`](./864zeros_TECH_STACK_AUDIT.md) — per-extension pillar mapping + compliance status
- [`864zeros_2026_ROADMAP.md`](./864zeros_2026_ROADMAP.md) — pillar-diversification targets in Q2/Q3 plan

---

## VIII. Versioning

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-09 | Initial synthesis from GTM_MANIFEST v1.1. Three pillars locked (OIA / 864-Flux / FHG). Cross-pillar constants mapped to RULE-001 through RULE-007. Pillar inventory: 11 OIA + 2 Flux + 2 FHG = 15 extensions. |

---

*864zeros Pillar Strategy v1.0 · 2026-05-09 · 864zeros LLC · For DIV-6 NotebookLM ingestion.*
