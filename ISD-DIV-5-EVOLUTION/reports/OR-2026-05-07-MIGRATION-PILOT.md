---
or_id: OR-2026-05-07-MIGRATION-PILOT
or_type: migration_sniff
or_version: 1.2
generated_at: "2026-05-07T15:00:00"
target: "Web Highlights -> Obsidian/Capacities Migration Lane"
codename: MigrationPilot
strike_id: 864z-2026-PILOT-MIGRATION-001
verdict: PASSED_PREFLIGHT
verdict_gate: scarcity_thesis_validated
scan_mode: custom_3query
queries_executed: 3
apify_queries_spent: 3
real_competitors_strict: 1
real_competitors_inclusive: 2
scarcity_threshold_directive: 2
demand_signals_count: 3
thesis_validated: true
data_source: data_lake/MIGRATION_PILOT_SNIFF.json
---

# Operational Record OR-2026-05-07-MIGRATION-PILOT
## Web Highlights → Obsidian/Capacities Migration Lane → MigrationPilot

**Type:** Migration-Pilot Pre-flight Sniff (Option C thesis validation)
**Verdict:** **PASSED PREFLIGHT** — thesis lane validated at scarcity level
**Sniff cost:** 3 Apify queries (~$0.30)

---

## 1. Inputs

| Parameter | Value | Source |
|---|---|---|
| Thesis lane | Migration / Liberation (Option C) | CEO directive |
| Target frame | Help users *leave* Web Highlights, don't *replace* it | MCMO |
| Codename | MigrationPilot | MCMO |
| Sniff queries (3) | "Web Highlights to Obsidian Export" / "Capacities data migration tools" / "Browser highlight extractors" | CEO-supplied (specifically scoped to probe the export-utility space, not the incumbent) |
| Threshold | ≤ 2 real competitors → proceed | CEO directive |
| Generator | ISD-DIV-5-EVOLUTION/report_generator.py v1.2 (hand-crafted output for migration_sniff type — generator doesn't yet auto-handle this OR shape) | CTO |

## 2. Captured Signals

### Query 1: "Web Highlights to Obsidian Export" (8 results)

| Bucket | Count | Note |
|---|---|---|
| **Incumbent self-references** | 4 | Web Highlights' own blog/docs/use-cases — first-party material |
| **Demand signals** | 3 | Obsidian forum + Reddit posts asking "how do I get highlights into my vault?" |
| **Real competitors** | **1** | **Glasp** — direct third-party annotation tool with Obsidian/Notion/Capacities export |

### Query 2: "Capacities data migration tools" (7 results)

| Bucket | Count | Note |
|---|---|---|
| **Incumbent self-references** | 5 | Capacities' own docs (migration overview, paradigm shift, bulk import, import reference, switch from Obsidian) |
| **Off-category** | 2 | Microsoft Fabric (Power BI / data warehouse migration — wrong domain entirely) |
| **Real competitors** | **0** | Zero third-party migration utilities for Capacities |

### Query 3: "Browser highlight extractors" (8 results)

| Bucket | Count | Note |
|---|---|---|
| **Off-category — PDF tools** | 3 | Operate on different source surface (PDF, not browser highlights) |
| **Off-category — YouTube** | 1 | Video highlights, not text annotations |
| **Off-category — Links** | 1 | Link Highlighter Pro extracts URLs, not annotations |
| **Incumbent self-references** | 2 | Web Highlights' own listicles |
| **Code question** | 1 | Stack Overflow JS highlight detection — not a product |
| **Real competitors** | **0** | No tools that migrate browser highlights to vault destinations |

### Demand Quotes (qualitative — articulated user intent)

1. *(Obsidian forum)* "I'm looking for a solution to sync my web highlights to my Obsidian Vault so I can quickly search my web history while writing notes."
2. *(Reddit r/ObsidianMD)* "If only paid solutions exist, I'm looking for solutions without a monthly paid subscription. One time fee is fine though."
3. *(Obsidian forum)* "I am trying to highlight and annotate web pages. Then sync these highlights to obsidian for further organization. What extension/plugin should I use for it?"

**Three explicit migration-intent posts on Obsidian-aligned platforms in a single 3-query sniff.** Demand is real and articulated.

## 3. Competitor Landscape (Migration / Liberation niche)

**Strict count (direct):** 1 — **Glasp**
**Inclusive count (with adjacent):** 2 — Glasp + Highlight Extract (PDF-focused, different surface)

| Name | Category | Surface | Direct competitor? |
|---|---|---|---|
| **Glasp** | Annotation + export | Web pages, YouTube transcripts, PDFs, Kindle | ✓ YES — same surface, same destination set (Obsidian/Notion/Capacities) |
| Highlight Extract | Highlight extractor | PDFs, Word docs | ◐ Adjacent (different source surface) |
| (everything else found) | Different categories | Various | ✗ NO |

**Both interpretations (strict 1, inclusive 2) satisfy the directive's `≤ 2` threshold.**

## 4. Top Pain Quotes (qualitative)

The demand signals captured above ARE the pain quotes for this OR — there is no separate live-scan of an incumbent. The user's articulated migration intent is the qualitative ground truth.

## 5. Thesis (synthesized)

- Web Highlights users articulate migration intent in public forums (3 explicit posts in 24 results)
- Web Highlights' own Markdown export is a manual copy-paste flow — not a programmatic migrator
- **Glasp is the only third-party tool that programmatically exports web highlights to Obsidian/Notion/Capacities**
- The Capacities migration tooling space has **zero** third-party tools (5 of 7 results are first-party Capacities docs)
- Browser-highlight migration as a product category has no recognizable cluster

---

## 6. Mechanical Gap Analysis (Pillar 4)

> *Why is the Web Highlights → Obsidian/Capacities migration niche vulnerable to a local-first export utility, regardless of the rescue-product competitor count?*

### The Hostage Mechanism is the FORMAT, not the SUBSCRIPTION

This is the pivot away from the standard rescue thesis. Web Highlights doesn't extract a price ransom from users (it has a freemium tier with reasonable limits). The hostage mechanism is **data being trapped inside Web Highlights' annotation format**, with manual-only export workflows.

- The cost of leaving Web Highlights isn't dollars (price). It's **friction** (manual copy-paste of highlights one-by-one into your destination tool).
- Users who want to leave aren't price-sensitive defectors. They're **workflow-driven migrators** moving to a different organizing paradigm (Obsidian's vault model, Capacities' object model).
- The rescue isn't "build a free Web Highlights replacement". The rescue is "**build the bridge that doesn't exist**".

### The Export-to-Vault Bridge Architecture

Concrete technical scope of the proposed migrator:

```
USER WORKFLOW:
  1. User clicks the MigrationPilot extension icon while on Web Highlights' web app
  2. Extension scrapes user's highlight database via DOM inspection or the Web Highlights API
  3. Extension converts each highlight to Markdown with YAML frontmatter:
       - source URL
       - highlight text
       - user note / annotation (if any)
       - timestamp
       - tags
  4. Extension writes one .md file per highlight (or one consolidated file) to:
       (a) Obsidian Vault folder (via File System Access API)
       (b) Capacities import-ready format (Capacities supports bulk Markdown import per docs)
       (c) Generic Markdown export (for any vault-style tool)

ARCHITECTURE:
  - Chrome Extension MV3 (per 864zeros standard architecture)
  - IndexedDB for staging during conversion (no cloud dependency)
  - File System Access API for direct vault writes
  - Zero external API calls except optional Web Highlights API for highlight retrieval
  - One-shot tool: install, run migration, optionally uninstall
  - Or: persistent companion that watches new highlights and incrementally syncs
```

### Why the math gate doesn't apply (and why that's the point)

The 864zeros 8.64 gate was designed for **rescue products replacing SaaS hostages** — same product space, different vendor. The Pillar 3 math (Rule of 40, exit valuation, target MRR) presumes a SaaS product with subscribers.

A migration utility doesn't fit that math:
- **No recurring revenue model** — it's a one-shot or low-frequency tool
- **No subscriber base to acquire** — TAM is users actively trying to leave a specific incumbent
- **No exit valuation pattern** — migration utilities aren't typically acquired; they get OSS'd or shut down once the migration wave passes
- **Time-bound opportunity** — the migration window for any incumbent is months, not years

This is a **fundamentally different business shape** and Option C requires either:
1. A new gate calibrated for migration-utility economics (one-time fee × narrow window), or
2. Acceptance that migration tools are loss-leaders / brand-builders that feed into something else (a paid rescue product, a community, a different SaaS)

CTO recommendation: treat MigrationPilot as a **brand+community play** rather than a profit-seeking strike. Ship it free, build a user base of "I left Web Highlights and you can too" advocates, parlay that audience into the next migration tool (Capacities → Notion, Notion → Obsidian, Roam → Logseq, etc.). The competitive density of the migration-tool space is genuinely thin; **own the category before someone else does**.

### Pivot Opportunity (Option C signal — CONFIRMED)

✓ **OPTION C THESIS LANE VALIDATED.** The 3-query sniff confirmed:
- Real competitor count ≤ 2 (well below the directive threshold)
- Demand signals are explicit and current (users asking right now)
- The category has structural shape (Glasp shows what one product looks like; everything else is incumbent self-promo)

The Migration/Liberation thesis appears to be a genuinely emptier market than the standard rescue-product thesis. **First strike under this lane recommended.**

---

## 7. Math Breakdown (with caveats)

The standard validator gate isn't the right tool here, but for completeness:

```
Z-Convergence: n/a    (no live scan; would need a different signal-collection pattern)
Z-Velocity:    n/a    (not applicable for migration-tool economics)
Z-Scarcity:    1.00   (≤ 2 competitors → in the lookup table at 0.8-1.0; using 1.0 for 1 strict competitor)
Rule of 40:    n/a    (no recurring revenue thesis)
Final score:   n/a
```

The score gate (8.64) was calibrated for SaaS-rescue economics. Forcing this strike through it would either reject it (lacking pillar 3 inputs) or fabricate a pass via synthetic financials — neither honest.

**Verdict: thesis-lane validated; math gate non-applicable; needs new evaluation criteria for Option C.**

## 8. Verdict

**THESIS LANE PASSES PREFLIGHT** at scarcity gate (`1 ≤ 2`).

### Counterfactuals at different scarcity thresholds

- `THRESHOLD = 1`: 1 competitor — **PASSES** (1 ≤ 1 by directive)
- `THRESHOLD = 2`: 1 competitor — **PASSES** (1 ≤ 2 — directive's bar)
- `THRESHOLD = 3`: 1 competitor — **PASSES** (1 ≤ 3 — original 864zeros bar)
- `THRESHOLD = 5`: 1 competitor — **PASSES** (1 ≤ 5 — current SaaS-rescue bar)

Even at the strictest possible threshold (1), the niche passes. This is the first strike in this session where scarcity is decisively a non-issue.

### Recommendations for next step

1. **Decision:** does CEO authorize building MigrationPilot as Strike 011?
2. **If yes:** the build is small (XS-S complexity per CLAUDE.md sizing). Chrome Extension MV3 + Web Highlights API/scraping + File System Access API + Markdown converter. Estimated ~10-20 hours of build time per the build-kit phase model.
3. **If yes, monetization:** open-source it. The audience-building value exceeds the direct revenue ceiling for a migration utility. Use it to seed Strike 012 / 013 (other migration utilities — Roam→Logseq, LastPass→Bitwarden, Pocket→Obsidian).
4. **If yes, runway:** ship before the next quarter ends. Migration windows close — once Glasp or anyone else builds the same bridge, the opportunity collapses. Speed > polish.
5. **If no:** archive this OR as evidence that Option C has at least one viable lane; revisit the thesis pivot when ready.

## 9. Source Artifacts

- Sniff data: `data_lake/MIGRATION_PILOT_SNIFF.json` (this OR's structured ground truth)
- This OR generated: 2026-05-07T15:00:00 (hand-crafted to match v1.2 conventions)
- Generator note: standard `report_generator.py` v1.2 doesn't auto-handle `migration_sniff` type. Recommend adding a fourth mode (`migration`) in next generator update for repeatability across future Option C strikes.

---
*OR generated in neutral hub. No vulture-nest writes performed.*
*v1.2 (hand-crafted): thesis extraction + qualitative demand quotes + Mechanical Gap Analysis (Pillar 4) + Pillar-3-not-applicable acknowledgment for migration-tool economics.*

— Signed: CEO + CTO + MCMO (augmented office)
— ISD-DIV-5-EVOLUTION 2026-05-07
— End of MigrationPilot Pre-flight OR —
