# DIV-4 STUDIO — Extension Manifest Index
## GTM Handoff Document — 2026-05-07

This index aggregates the 13 README "Manifests" produced by the audit cycle. Every extension under `864zeros-llc/LLC-DIV-3-FACTORY/extensions/` now has a README.md in its directory documenting Hook (marketing) / Commercial Gate (sales) / Technical Blueprint (tech).

DIV-4 STUDIO can pull from this index for marketing copy, store-listing prep, and GTM sequencing decisions.

---

## 1. The 13 Extensions At A Glance

### Flagship products (full GTM treatment)

| Extension | Status | T-Shirt | Brand | Free/Paid | Pitch |
|---|---|---|---|---|---|
| **[clipboard](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/clipboard/README.md)** | Engineering 100%, GTM 70% | M | OIA | Freemium ($1.99/$3.99/$5.99/$150 lifetime) | Local-first web clipper. Capture anything. Keep it. Own it. |
| **[Bible-Insight](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/Bible-Insight/README.md)** | Approved (gated on Thaw revenue) | M-L | **FHG** *(separate brand!)* | Freemium ($4.99/mo) | Bible study, locally captured, AI-assisted. For His Glory. |
| **[TabVault](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/TabVault/README.md)** | DEPLOYED (Strike 002) | M | OIA | Freemium (Pro planned) | Deep Sleep for your tabs. OneTab without the data loss. |
| **[Chronicle (864z-chronicle)](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/864z-chronicle/README.md)** | Engineering ready | S | OIA | Free Edition v1 | Your AI conversation history. Captured automatically. |
| **[who-is-watching](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/who-is-watching/README.md)** | v2.1.6 mature | L | OIA | Free Edition v1 | See exactly who is tracking you on every page. Block them in one click. |

### oia.focus series (canonical products)

| Extension | Status | T-Shirt | Pitch |
|---|---|---|---|
| **[Signal2Noise](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/Signal2Noise/README.md)** | Spec finalized | XS-S | What is today's signal? Tune out the noise, focus in on the signal. |
| **[Time2Focus](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/Time2Focus/README.md)** | Spec finalized | S | Set a time. Name your focus. When the timer ends, you remember what matters. |
| **[TuneOut2FocusIn](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/TuneOut2FocusIn/README.md)** | Spec finalized | XS-S | One click. Predictable sound. Distractions masked. Focus restored. |
| **[oia-focus-note](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/oia-focus-note/README.md)** | Mature v1.1.0 | XS | Capture first, organize never. Brain-dump notepad in a side panel. |
| **[oia-focus-wall](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/oia-focus-wall/README.md)** | Mature v1.1.0 | S | Sticky note cork board. Spatial thinking, made digital. |

### Archive (predecessor/superseded — DO NOT MARKET SEPARATELY)

| Extension | Superseded By |
|---|---|
| [oia-focus-timer](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/oia-focus-timer/README.md) | Time2Focus |
| [oia.focus.signal](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/oia.focus.signal/README.md) | Signal2Noise |
| [oia.focus.sound](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/oia.focus.sound/README.md) | TuneOut2FocusIn |

CTO recommendation: rename these directories to `_archive/<name>/` to reduce future confusion. Their READMEs are stub-redirects to their canonical successors.

---

## 2. GTM Readiness Matrix

| Extension | Eng | Pricing wired | OAuth | Marketing assets | Privacy policy | Store listing | Beta | **GTM Score** |
|---|---|---|---|---|---|---|---|---|
| clipboard | ✓ | ✓ scaffolded | ✓ real client_id | ✗ | ✗ placeholder URLs | ✗ | ✗ | **70%** |
| TabVault | ✓ DEPLOYED | ✗ | ✗ placeholder | partial | ✗ | partial | ✓ in production | **65%** |
| Chronicle | ✓ | n/a (free) | n/a | ✗ | ✗ | ✗ | ✗ | **45%** |
| who-is-watching | ✓ v2.1.6 | n/a (free) | n/a | ✗ | ✗ | ✗ | partial | **55%** |
| Bible-Insight | partial (re-skin) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **30%** *(approved-but-gated)* |
| Signal2Noise | spec only | n/a (free) | n/a | ✗ | ✗ | ✗ | ✗ | **25%** |
| Time2Focus | spec only | n/a (free) | n/a | ✗ | ✗ | ✗ | ✗ | **25%** |
| TuneOut2FocusIn | spec only | n/a (free) | n/a | ✗ | ✗ | ✗ | ✗ | **25%** |
| oia-focus-note | mature v1.1 | n/a (free) | n/a | ✗ | ✗ | ✗ | ✗ | **40%** |
| oia-focus-wall | mature v1.1 | n/a (free) | n/a | ✗ | ✗ | ✗ | ✗ | **40%** |

### Recommended launch sequence (CTO + MCMO joint)

1. **Clipboard first** — most engineering-complete, has payment infrastructure scaffolded, biggest revenue potential. Closing the GTM gap is roughly 2-3 weeks of marketing/legal/registration work, no engineering.
2. **TabVault second** — already DEPLOYED and has a real strike-of-record (Strike 864z-2026-002). The placeholder OAuth client_id is the engineering blocker. Marketing angle ("OneTab refugee community") is well-defined.
3. **who-is-watching third** — codebase mature, pure free-tier. Privacy press (PrivacyTools.io, EFF) is an unusual but real distribution channel for this category.
4. **Chronicle fourth** — single-purpose, free, audience-builder. Cheap to ship, good for series brand-building.
5. **OIA series staggered** — Signal2Noise, Time2Focus, TuneOut2FocusIn shipped together as the "ADHD focus suite" with cross-promo in each.
6. **Bible-Insight gated** — wait for Thaw to ship first revenue per CLAUDE.md guidance. FHG brand requires separate publisher account, separate domain.

---

## 3. Brand Architecture

864zeros LLC operates two brand pillars:

### OIA (Organize your Internal Architecture)
- Tagline genus: *"Built for people with ADHD by someone with ADHD"*
- Tagline genus: "Local-first. Privacy-first. Yours-first."
- Color system: documented in `864z-build-kit/lib/aether-ui.css`
- 11 of 13 extensions belong to this pillar

### FHG (For His Glory)
- Tagline: *"Rest. Create. For His Glory."*
- Audience: Christian men (Bible study, sermon notes, theological research)
- Palette: Charcoal #2D2D2D + Bronze #A67C52
- **Brand firewall: NEVER reference OIA, 864zeros, or WebInsight in user-facing surfaces.** Bible-Insight is published under a separate FHG identity.
- 1 of 13 extensions belongs to this pillar (Bible-Insight)

---

## 4. Brick Reuse Map

DIV-4 STUDIO can use this when prepping co-marketing copy that reflects shared infrastructure ("our 14 reusable bricks"):

| Brick | Used In |
|---|---|
| `agent-dom-scraper` | clipboard, Bible-Insight, who-is-watching |
| `agent-pdf-generator` | clipboard, Bible-Insight |
| `agent-anonymizer-pii` | clipboard, Bible-Insight (planned) |
| `agent-ai-summarize / autoTag / vision / chat` | clipboard, Bible-Insight |
| `agent-local-ai-keywords` | Bible-Insight |
| `agent-drive-sync` | clipboard, TabVault (planned), Bible-Insight |
| `agent-local-backup` | clipboard, TabVault, all OIA-series |
| `agent-indexeddb-store` | clipboard, Bible-Insight, TabVault |
| `agent-chrome-storage-store` | clipboard, all OIA-series, oia.focus.* variants |
| `agent-feature-gate-tiers` + `agent-payment-extpay` + `agent-credit-ledger` | clipboard (only one with paid tiers wired) |
| `agent-offscreen-audio` | TuneOut2FocusIn, Time2Focus |
| `agent-tracker-classifier / agent-page-injector` | who-is-watching only |
| `agent-conversation-scraper` | Chronicle only (per-AI-host variants) |
| `TR-06 agent-youtube-transcript` (*planned*) | Bible-Insight (B2B sellable) |
| `TR-07 agent-bible-verse-detector` (*planned*) | Bible-Insight (B2B sellable) |

See `ISD-DIV-0-CORE/BRICK_REGISTRY.json` for full I/O contracts and complexity sizing.

### Critical missing brick
**`agent-markdown-converter`** — flagged as a CRITICAL gap during the brick audit. Required for Strike 011 MigrationPilot (Web Highlights → Obsidian/Capacities export utility). Once built, also unlocks "Export to Obsidian" features in clipboard, Bible-Insight, Chronicle, and the OIA-series — meaningful cross-promo lever.

---

## 5. Migration / Liberation Thesis Threads

Three of the 13 extensions are explicit "rescue from incumbent" plays:

- **TabVault** — rescues OneTab refugees (data loss, no sync, memory bloat)
- **clipboard** — rescues Pocket / Evernote / Notion clipper users (privacy, export, AI control)
- **Chronicle** — rescues users from vendor history pruning (ChatGPT / Claude / Gemini history retention games)

The remaining 10 extensions are either:
- Original OIA productivity tools (Signal2Noise, Time2Focus, etc.) — tackling user behavior gaps not vendor friction
- Privacy infrastructure (who-is-watching) — tackling surveillance economy, not a single incumbent
- Specialized vertical (Bible-Insight) — Christian study niche, FHG-branded

When DIV-4 STUDIO writes copy, the **Migration/Liberation framing** applies to TabVault, clipboard, and Chronicle. The OIA-series productivity tools should use **constraint/peripheral-focus framing** ("built for ADHD"), not rescue framing.

---

## 6. Files Created This Cycle

13 README.md files (in each extension directory) + this index = 14 new docs.

```
864zeros-llc/LLC-DIV-3-FACTORY/extensions/
├── clipboard/README.md                   ◄── NEW (or updated)
├── 864z-chronicle/README.md              ◄── UPDATED (existed)
├── TabVault/README.md                    ◄── NEW
├── Bible-Insight/README.md               ◄── NEW
├── who-is-watching/README.md             ◄── UPDATED (existed)
├── Signal2Noise/README.md                ◄── NEW
├── Time2Focus/README.md                  ◄── NEW
├── TuneOut2FocusIn/README.md             ◄── NEW
├── oia-focus-note/README.md              ◄── NEW
├── oia-focus-wall/README.md              ◄── NEW
├── oia-focus-timer/README.md             ◄── NEW (predecessor stub)
├── oia.focus.signal/README.md            ◄── NEW (predecessor stub)
└── oia.focus.sound/README.md             ◄── NEW (predecessor stub)

864zeros-ISD/ISD-DIV-4-STUDIO/
└── EXTENSION_MANIFEST_INDEX.md           ◄── NEW (this file)
```

---

## 7. Open Coordination Items for DIV-4 STUDIO

These are not engineering blockers but require DIV-4 to act before Chrome Web Store launches:

1. **Privacy policies** — every extension needs one. Most can share a master 864zeros policy with extension-specific addenda. Bible-Insight needs its own FHG-branded privacy policy.
2. **Terms of Service URLs** — referenced in `pricing.js` for paid extensions. Currently placeholders.
3. **Marketing screenshots** — Chrome Web Store requires 1-5 screenshots per listing (1280×800 or 640×400). For each flagship: capture, demo flow, key feature, AI/sync flow, settings.
4. **Promo tile** — 440×280, used in store search results. Optional but heavily increases CTR.
5. **Demo video** — Chrome Web Store accepts YouTube embed. ~60-90s recommended.
6. **Store listing copy** — pull from each README's "The Hook (Marketing)" section. Tone is already 864zeros Standard.
7. **Comparison/competitor pages** — many READMEs reference these (TabVault vs OneTab, who-is-watching vs Privacy Badger, etc.). DIV-4 should produce these as separate marketing pages.
8. **Reddit/HN launch sequences** — TabVault → r/OneTab, who-is-watching → r/privacy, clipboard → r/Obsidian (when markdown-converter brick ships).
9. **Archive cleanup** — rename `oia-focus-timer/`, `oia.focus.signal/`, `oia.focus.sound/` to `_archive/` prefix to reduce factory listing noise.

---

## 8. Sign-off

Manifest-First Documentation cycle complete. 13 extensions documented with consistent 864zeros Standard structure. DIV-4 STUDIO has the surface they need to begin GTM coordination immediately.

Engineering work that gates GTM (per Section 2):
- Clipboard: ExtPay registration, real privacy/ToS URLs, marketing assets
- TabVault: real OAuth client_id, marketing assets
- Chronicle, who-is-watching: marketing assets, privacy policy
- OIA series: production icons, marketing assets

The shared-infrastructure narrative ("14 reusable bricks across 11 OIA extensions, 1 FHG vertical, 1 privacy infrastructure tool") is itself marketing-grade material — DIV-4 STUDIO can use it for any "How 864zeros builds" thought-leadership content.

— Signed: CEO + CTO + MCMO (augmented office)
— ISD-DIV-4-STUDIO 2026-05-07
— End of Extension Manifest Index —
