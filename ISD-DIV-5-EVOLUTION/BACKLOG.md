# 864zeros Engineering Backlog
## [Protocol] Automated Brick Extraction
**Status:** ACTIVE
**Logic:** Scan `SYSTEM_STRIKE_LOG.md` for successful fixes tagged as #BrickCandidate. Extract to `864z-build-kit/templates/bricks/`.

---

## Active Sprint (Next Strike)

Tasks queued for the next strike's first execution window. Items move OUT of this section into "Recently Completed" when shipped.

| Task | Owner | Priority | Notes |
|---|---|---|---|
| ~~**RULE-004 Compliance Audit — `migration-pilot`**~~ | 864z-SE (Systems Engineer) | ~~HIGH~~ | ✅ **COMPLETED 2026-05-08.** Migration to BRK-UI-004 accordion done. 864-Flux Graphite palette applied. Brick copied to `migration-pilot/lib/bricks/accordion-record-v1/`. README updated with RULE-004 compliance citation. See "Recently Completed". |
| ~~**RULE-004 Compliance Audit — `TabVault`**~~ | 864z-SE (Systems Engineer) | ~~HIGH~~ | ✅ **COMPLETED 2026-05-08.** Vault list migrated from flat `.vault-item` rows to BRK-UI-004 accordion. Restore Tab action present in header (primary icon-button) AND body (secondary text-button) per directive. Body content: URL hot-link, vaulted timestamp, scroll position, session group name. Existing group-level collapse pattern preserved (groups wrap accordion-records). OIA Sage palette retained (`--oia-accent` alias added). See "Recently Completed". |
| Pre-flight scarcity OR — ScriptureScout (`OR-2026-05-XX-SCRIPTURESCOUT.md`) | DIV-1-VULTURE Live Scout | MEDIUM | 8.64 competitive scarcity scan. Charter holds in §Strike Charters below. (Distinct from the readiness OR — `OR_STRIKE_012_PREFLIGHT.md` — already shipped.) |
| **Clipboard Phase 2 — RULE-001 + RULE-003 + RULE-004 full migration** | 864z-SE (Systems Engineer) | HIGH-deferred | Phase 1 audit complete (2026-05-08, see Recently Completed). Phase 2 needs: (1) Options-page restructure to 3-section spec — consolidates AI Settings + Your Plan + Fuel-the-Build into the canonical Subscription & Tiers section; consolidates Data into Data Management; preserves how-to into How to Use. UX impact for shipping users requires Office Architect sign-off. (2) Add tristate select-all + bulk actions (Export selected, Tag selected, Delete selected) to clip queue. (3) Migrate clip-card rendering from `clip-card__expand` inline-text-expand pattern to BRK-UI-004 accordion: header (clip preview + timestamp + copy button), body (full clip + tags + AI summary + actions). Estimated effort: ~6-10h focused work; needs careful regression testing against paid-tier flows. |
| ~~Operator end-to-end smoke test — ScriptureScout `Load unpacked`~~ | Operator | ~~MEDIUM~~ | ✅ **CHECKLIST DELIVERED 2026-05-08.** Copy-pasteable protocol at `extensions/scripture-scout/SMOKE_TEST_CHECKLIST.md` (10 sections, ~10 min total, with explicit pass criteria for BibleHub interlinear extraction + Parchment UI expansion). Operator-driven execution still pending. |
| ~~Designed FHG icons (replace placeholder PNGs)~~ | 864z-TW (Technical Writer) → asset pass | ~~MEDIUM~~ | ✅ **GENERATOR DELIVERED 2026-05-08.** Bronze Compass design at `extensions/scripture-scout/images/generate-fhg-icons.html` — Charcoal field + Bronze compass needle + open scroll backdrop, all 4 sizes (16/32/48/128). Operator runs once → saves PNGs → reloads extension. Placeholder 1×1 transparents seeded at `images/icon{16,32,48,128}.png` so manifest doesn't break before generator runs. |
| Founding 100 waitlist form copy — `864zeros.com/scripturescout` | DIV-4-STUDIO + Operator | MEDIUM | ✅ **DELIVERED 2026-05-08.** Full copy at `extensions/scripture-scout/WAITLIST_FORM_COPY.md` — single mission-alignment question + scoring rubric + good/low-signal examples + approval/decline email templates. |

---

## Recently Completed

| Task | Completion | Notes |
|---|---|---|
| **Accordion Harvest** (Strike 012 → BRK-UI-004 / RULE-004) | ✅ COMPLETED 2026-05-08 | First directory-format brick promoted. JS + CSS + docs at `864z-build-kit/templates/bricks/accordion-record-v1/`. Codified RULE-004 in BUILD_KIT_RULES. Office Architect (864z-OA) signed off per RULE-000. |
| **RULE-004 Compliance Audit — `migration-pilot`** | ✅ COMPLETED 2026-05-08 | First production adopter of BRK-UI-004. Brick copied to `migration-pilot/lib/bricks/accordion-record-v1/`. Sidepanel `buildCaptureCard()` rewritten to canonical `accordion-record-*` class names. AccordionController instantiated with default `shiftMultiExpand: true` (RULE-004-mandated). Per-card View Source / Liberate to Markdown / Remove action row. Local oia-design-system.css palette swapped from OIA Sage to **864-Flux Graphite (`#374151`)**. Pre-RULE-004 `.capture-card-*` rules stripped from local sidepanel/styles.css. README updated with RULE-001/002/003/004 compliance + 864-Flux pillar correction (was mislabeled OIA). |
| **RULE-004 Compliance Audit — `TabVault`** | ✅ COMPLETED 2026-05-08 | Vault list (`.vault-item` flat rows) migrated to BRK-UI-004 accordion. Brick copied to `TabVault/lib/bricks/accordion-record-v1/`. `renderTabItem()` rewritten to produce canonical `.accordion-record + .vault-record` DOM. AccordionController instantiated on `vaultedTabsList`. Restore Tab action present in BOTH header (primary Sage icon-button) and body (secondary text-button) per directive #3. Body content: URL hot-link, vaulted timestamp, scroll position info, session group name when present. Existing `.vault-group` outer-collapse pattern preserved (group-level collapse is independent of per-record accordion). OIA Sage palette retained (`--oia-accent` semantic alias added for brick compatibility). Three production adopters of BRK-UI-004 now exist: scripture-scout (FHG), migration-pilot (864-Flux), TabVault (OIA) — proving Pillar Compatibility = Global. |
| **Global Compliance Audit — `clipboard` (Phase 1)** | 🟡 PARTIAL 2026-05-08 | Audit complete: RULE-002 already compliant (clipboard's PDF generator is the ORIGINAL birthplace of the Base64 SW download pattern that became BRK-DL-001 — predates the rule). Phase 1 SAFE migrations executed: 864-Flux Graphite palette swap (`--oia-sage` → `#374151`, `--oia-accent` alias added); `[864F]` brand-prefix added to sidepanel title; standardized brand-footer added to options.html (alongside existing options-footer for traceability — preserves shipping UX); README compliance citation block prepended; copyright year fix (2025 → 2026). Phase 2 DEFERRED (needs dedicated sprint + UX decisions): RULE-001 options-page restructure from 5-section legacy to 3-section spec (would consolidate General/AI/Plan/Data/Fuel — affects shipping paid users); RULE-003 tristate selection + bulk actions; RULE-004 accordion migration of clip-card rendering (sidepanel/main.js is 2,555 LOC, 5× migration-pilot's size). Reasoning for phasing: clipboard is a SHIPPED extension with paid-tier infrastructure; aggressive in-place refactor risks regressions. |
| **Strike 012 launch polish (FHG icons + smoke checklist + waitlist copy)** | ✅ COMPLETED 2026-05-08 | 864z-TW asset pass: (1) Bronze Compass icon generator at `extensions/scripture-scout/images/generate-fhg-icons.html` — Charcoal #2D2D2D field, Bronze #A67C52 compass needle (NSEW pointer with subtle lean), open scroll backdrop with rolled cylindrical edges + suggested text lines (rendered at ≥48px), four sizes (16/32/48/128). Placeholder 1×1 transparent PNGs seeded at `images/icon{16,32,48,128}.png` so manifest path doesn't break pre-generation. (2) `SMOKE_TEST_CHECKLIST.md` — copy-pasteable 10-section protocol expanding the OR §3.1 12-step into operator-friendly checkboxes; explicit emphasis on BibleHub interlinear (§E) + Parchment UI expansion (§F); ~10 min total. (3) `WAITLIST_FORM_COPY.md` — single-question Founding 100 form ("What study work are you trying to liberate?") + 4-tier scoring rubric + good/low-signal calibration examples + approval/decline email templates. Active Sprint medium-priority items closed. |
| Strike 011 brick harvest (BRK-DL-001, BRK-UI-002, BRK-UI-003) | ✅ COMPLETED 2026-05-08 | See "Strike 011 — HARVEST COMPLETE" section below. |
| FHG (For His Grace) brand expansion in messages.json + README | ✅ COMPLETED 2026-05-08 | scripture-scout |
| GTM_MANIFEST §7 — 864-Flux palette codification (Slate & Graphite) | ✅ COMPLETED 2026-05-08 | |
| Office Architect (864z-OA) role profile | ✅ COMPLETED 2026-05-08 | `ROLES/OFFICE_ARCHITECT.md` + `ROLES/README.md` |
| RULE-000 (Architectural Governance) | ✅ COMPLETED 2026-05-08 | `BUILD_KIT_RULES.md` |
| BRICK_REGISTRY sync for Strike 012 | ✅ COMPLETED 2026-05-08 | BRK-UI-004 registered, audit_summary updated |

---

## Protocol Overview

Engineering wins compound. When a Strike produces a fix or pattern that solves a *cross-cutting* problem (not extension-specific), it should be promoted to a build-kit brick within the same week — before it ossifies into a one-off solution that future strikes will independently re-derive.

### The Pipeline

```
Strike ships fix → SYSTEM_STRIKE_LOG entry written
       │
       ├─→ Author tags entry with #BrickCandidate (in entry body)
       │
       ▼
Backlog scanner picks up tag
       │
       ▼
Audit: is this reusable? generic? has a clear contract?
       │
       ├─ NO  → Drop with rationale logged
       │
       └─ YES → Extract:
                 1. Generic implementation in templates/bricks/
                 2. Codify the rule in BUILD_KIT_RULES.md (if new)
                 3. Update templates/bricks/README.md index
                 4. Update ISD-DIV-0-CORE/BRICK_REGISTRY.json
                 5. Append harvest entry to SYSTEM_STRIKE_LOG
                 6. Cross-link the source strike entry from the brick
```

### What Makes Something a #BrickCandidate

A log entry is a brick candidate if **all** of these hold:

- The fix solves a problem that **applies to every 864zeros extension**, not just the originating Strike.
- The fix has a **clear contract** — defined inputs, defined outputs, no hidden coupling to extension-specific state.
- The fix is **stable** — not a placeholder, not "we'll figure out the API later".
- The fix is **defensive** in the right places — fails loudly at API boundaries, gracefully internally.

When in doubt, tag it. Audit catches false positives cheaply; missed candidates compound into wasted re-work.

---

## Strike 011 (MigrationPilot) — HARVEST COMPLETE 2026-05-08

The protocol's seed run. Three bricks extracted from Strike 011's production code:

| Brick | ID | Source | Authority | Status |
|---|---|---|---|---|
| `headless-download-uri.js` | BRK-DL-001 | `migration-pilot/background/service-worker.js → runLiberation()` | RULE-002 | ✅ Extracted |
| `tristate-checkbox-list.js` | BRK-UI-002 | `migration-pilot/sidepanel/main.js → TristateSelection logic` | RULE-003 | ✅ Extracted |
| `two-tap-arm-pattern.js` | BRK-UI-003 | `migration-pilot/options/main.js → onClearClicked logic` | RULE-001 §3 | ✅ Extracted |

Source log entries:
- `2026-05-08T-MIGRATION-PILOT-SW-DL-FIX` (#BrickCandidate → BRK-DL-001)
- `2026-05-08T-RULE-001-COMMIT` (provided pattern for BRK-UI-003)
- `2026-05-08T-MIGRATION-PILOT-Q4-SELECTIVE-LIBERATION` (provided pattern for BRK-UI-002 — see harvest entry for cross-ref)

Rules codified during this harvest:
- RULE-002: Service Worker Download Pattern
- RULE-003: Selection & Curation UI

---

## Pending Brick Candidates (queue)

*This section grows as future Strike log entries get tagged #BrickCandidate. Empty at protocol seed.*

| Source entry | Candidate brick | Audit status | Notes |
|---|---|---|---|
| *(none yet — log scan reset 2026-05-08)* | | | |

---

## Strike Charters (in flight)

### Strike 012 — ScriptureScout (Faith/Heritage Liberation Lane)

**Status:** CHARTER DRAFT — pending pre-flight scarcity scan
**Codename:** ScriptureScout
**Vertical:** Faith / Heritage
**Authoring authority:** Systems Architect
**Drafted:** 2026-05-08

#### Thesis

The migration/liberation thesis (Strike 011) generalizes. Bible study apps — YouVersion, Logos, Olive Tree, Accordance, BibleGateway — lock highlights, notes, verse-of-the-day collections, and reading-plan progress into proprietary clouds. **There is no MigrationPilot for scripture.** Pastors, seminary students, theologians, and serious lay students want their study work in their own Markdown vaults (Obsidian, Capacities, Logseq), with citation frontmatter that survives translation changes and platform churn. ScriptureScout is that bridge.

#### Target Customer (Wedge → Wave)

| Wedge | Wave |
|---|---|
| Pastors and seminarians who already use Obsidian / Logseq for sermon prep, lecture notes, study journals — and resent re-typing what's locked in YouVersion or Logos | Lay Bible students; Bible study group leaders; theology grad students; church history researchers; hymnody enthusiasts (public-domain hymnal liberation) |

ADHD/OIA crossover is real but secondary — the wedge audience is *vault-native knowledge workers in faith vocations*, not the broader OIA pillar.

#### Source Liberation Targets (the lock-in to dissolve)

- **YouVersion** — highlights, bookmarks, notes (cloud-only; weak export)
- **Logos** — notes, highlights (export limited to Logos format; high-priced library)
- **Olive Tree** — sticky notes, highlights (export per-book; tedious)
- **BlueLetterBible** — public-domain commentaries + Strong's lookups (great content, no export)
- **BibleGateway / Bible Study Tools** — verse-of-the-day, devotionals (RSS exists; structured liberation does not)

ScriptureScout v1 wedge: **YouVersion** (largest user base) + **BlueLetterBible** (public-domain commentary corpus). Logos comes in v2 once API access is negotiated.

#### Bricks Used (compounding from Strike 011)

| Brick | Role |
|---|---|
| `BRK-DL-001` (headless-download-uri) | SW-context download of liberated `.md` files — RULE-002 compliant |
| `BRK-UI-002` (tristate-checkbox-list) | Selective export — choose which highlights/notes/passages to liberate — RULE-003 compliant |
| `BRK-UI-003` (two-tap-arm-pattern) | Clear-DB / Reset destructive confirmation — RULE-001 §3 compliant |
| `agent-markdown-converter` | Markdown rendering with YAML frontmatter (`864z-metadata` spec) |
| `agent-indexeddb-store` | Local capture archive |
| `agent-dom-scraper` | Content extraction from Bible-app web surfaces |
| `agent-local-backup` | JSON dump fallback |
| Side-panel + Options scaffold | Per RULE-001 (Command & Control Standard) |

**Compounding effect:** ScriptureScout starts at ~70% reused infrastructure. Custom code is the strike-specific differentiator only.

#### ScriptureScout-Specific Work (the 30%)

1. **Verse-reference parser** — recognize `John 3:16`, `1 Cor 13:4-7`, `Ps 23`, `Heb. 11:1`, abbreviation tolerance, range expansion. Output normalized canonical refs.
2. **Citation frontmatter spec** — extends `864z-metadata` v1.0:
   - `verse_refs: [{book, chapter, verse_start, verse_end, translation}]`
   - `cross_refs: [...]`
   - `lexicon: [{word, strongs_id, transliteration}]` (when Strong's data present)
   - `commentary_source: { author, work, year, public_domain: bool }`
3. **YouVersion scraper** — DOM-side extraction of highlights/notes from the YouVersion web reader (no public API). Custom CSS selectors per Bible-app version with version-detection fallbacks.
4. **BlueLetterBible commentary import** — public-domain commentaries (Spurgeon's Treasury of David, Matthew Henry's Complete, Geneva Bible footnotes). One-click "Add this passage's commentary to my vault."
5. **Translation-aware diffing** — when the user has the same verse highlighted in ESV and KJV, produce one Markdown file with translation comparisons in the body, not two redundant files.
6. **Vault folder convention** — default export structure: `Bible/{Book}/{Book}-{Ch}.md` with cross-link backlinks. Aligns with Obsidian's wiki-link conventions.

#### Pre-flight Scarcity (TBD — gate not yet run)

Hypothesis: **scarcity ≤ 3 in this niche.** "YouVersion to Obsidian" returns no real direct competitor as of this drafting. Bible study apps focus on study features, not export. The migration-tool-for-scripture niche is genuinely empty. Confirmation requires a formal OR dossier (`OR-2026-05-XX-SCRIPTURESCOUT.md`) before build commits.

If scarcity > 5 → strike is killed at preflight per the 8.64 gate. If ≤ 3 → proceed to build.

#### Tier Plan

| Tier | Price | Unlocks |
|---|---|---|
| **Free** | $0 | YouVersion liberation; BlueLetterBible commentary import (public-domain only); Markdown export with citation frontmatter |
| **Pro** (future) | TBD | Logos integration (when API access secured); multi-translation diffing; batch-export presets |
| **Power** (future) | TBD | Sermon-prep templates; lectionary-aware exports; Hebrew/Greek lexical enrichment via local Strong's database |

Per `CLAUDE-base.md` monetization: **privacy is identical at every tier**. No tier sells data; no tier reduces local-first storage.

#### Open Questions

- **Logos / Olive Tree API access:** request commercial-API tier or stay scrape-only? (Affects v2 scope)
- **Public-domain commentary corpus size:** ship pre-loaded, or download-on-demand from Project Gutenberg / CCEL?
- **Faith-positioning copy:** does ScriptureScout sit under OIA pillar or its own Faith/Heritage pillar? (Affects DIV-4-STUDIO branding pass)
- **YouVersion ToS:** scraping the user's own logged-in highlight data — likely permitted but needs legal review before public launch.

#### Next Action

Run pre-flight scarcity scan (DIV-1-VULTURE Live Scout) targeting "YouVersion export Obsidian", "Bible highlights to Markdown", "scripture migration tool". Produce `OR-2026-05-XX-SCRIPTURESCOUT.md`. If gate passes, scaffold `extensions/scripture-scout/` from the migration-pilot reference impl + new build-kit bricks.

---

## Compliance Migration Backlog

Once a rule is codified, existing extensions that pre-date the rule should be audited and migrated. Tracking here per rule:

### RULE-001 (Command & Control Standard) — codified 2026-05-08

| Extension | Pre-rule status | Audit status | Migration plan |
|---|---|---|---|
| `migration-pilot` | Reference impl, compliant by construction | n/a | n/a |
| `clipboard` | v1 6-section options spec | UNAUDITED | TBD |
| `webinsights` | unknown | UNAUDITED | TBD |
| `Bible-Insight` | unknown | UNAUDITED | TBD |
| `Time2Focus`, `TabVault`, `Signal2Noise`, `TuneOut2FocusIn` | unknown | UNAUDITED | TBD |
| `oia-focus-note`, `oia-focus-timer`, `oia-focus-wall`, `oia.focus.signal`, `oia.focus.sound` | unknown | UNAUDITED | TBD |
| `864z-chronical`, `who-is-watching` | unknown | UNAUDITED | TBD |

### RULE-002 (SW Download Pattern) — codified 2026-05-08

| Extension | Has SW downloads? | Pattern in use | Audit status |
|---|---|---|---|
| `migration-pilot` | Yes (Liberate flow) | RULE-002-compliant (Base64 data URI) | ✅ |
| `clipboard` | Likely (export/PDF features) | UNAUDITED | UNAUDITED |
| Others | UNAUDITED | UNAUDITED | UNAUDITED |

### RULE-003 (Selection & Curation UI) — codified 2026-05-08

| Extension | Has data queues? | Pattern in use | Audit status |
|---|---|---|---|
| `migration-pilot` | Yes (capture queue) | RULE-003-compliant (TristateSelection brick) | ✅ |
| `clipboard` | Yes (clip queue) | UNAUDITED | UNAUDITED |
| `TabVault` | Likely (tab queue) | UNAUDITED | UNAUDITED |
| Others | UNAUDITED | UNAUDITED | UNAUDITED |

### RULE-004 (Interactive Record Accordion) — codified 2026-05-08

| Extension | Has record-queue UI? | Pattern in use | Audit status |
|---|---|---|---|
| `scripture-scout` | Yes (capture queue) | RULE-004-compliant (inline accordion; matches BRK-UI-004 contract via `capture-card-*` class names) | ✅ Reference impl |
| `migration-pilot` | Yes (capture queue) | **RULE-004-compliant** (uses canonical BRK-UI-004 brick at `lib/bricks/accordion-record-v1/`; 864-Flux Graphite palette) | ✅ **MIGRATED 2026-05-08** |
| `TabVault` | Yes (vaulted-tab queue) | **RULE-004-compliant** (uses canonical BRK-UI-004 brick at `lib/bricks/accordion-record-v1/`; OIA Sage palette retained) | ✅ **MIGRATED 2026-05-08** |
| `clipboard` | Yes (clip queue) | 🟡 **PARTIAL** — has own `clip-card__expand` inline-text-expand pattern, NOT BRK-UI-004. Phase 2 migration deferred (sidepanel/main.js is 2,555 LOC; refactor needs dedicated sprint). | 🟡 PHASE-2 PENDING |
| Others | UNAUDITED | UNAUDITED | UNAUDITED |

---

## Protocol Automation Backlog

The protocol currently runs manually. Future automation candidates:

| Item | Priority | Description |
|---|---|---|
| Log scanner script | Medium | `tools/scan-brick-candidates.py` — reads SYSTEM_STRIKE_LOG, emits a list of #BrickCandidate entries that haven't been harvested yet |
| Brick registry sync | Medium | Auto-update `ISD-DIV-0-CORE/BRICK_REGISTRY.json` when files appear/change in `templates/bricks/` |
| Compliance audit runner | Low | Per-rule grep-based audit across `LLC-DIV-3-FACTORY/extensions/*` to flag non-compliant code |
| Brick version drift detector | Low | Compare canonical brick to per-extension copies, emit drift report |

---

## Cross-References

- Brick directory: [`864z-build-kit/templates/bricks/`](../../864zeros-llc/864z-build-kit/templates/bricks/)
- Build-kit rules: [`BUILD_KIT_RULES.md`](../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md)
- Strike log: [`reports/SYSTEM_STRIKE_LOG.md`](./reports/SYSTEM_STRIKE_LOG.md)
- Strike history (outcomes): [`STRIKE_HISTORY_MASTER.md`](./STRIKE_HISTORY_MASTER.md)
- Brick registry: [`864zeros-ISD/ISD-DIV-0-CORE/BRICK_REGISTRY.json`](../ISD-DIV-0-CORE/BRICK_REGISTRY.json)

---

*Backlog v1.0 · seeded 2026-05-08 with Strike 011 harvest.*
