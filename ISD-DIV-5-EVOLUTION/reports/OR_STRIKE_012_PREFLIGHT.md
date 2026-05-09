# OR — Strike 012 [FHG] · ScriptureScout · Pre-flight Operational Readiness

**Dossier type:** Pre-flight OR (Operational Readiness)
**Strike:** 012 — ScriptureScout
**Pillar:** FHG (For His Grace)
**Status:** DRAFT — pending Office Architect (864z-OA) sign-off
**Authored:** 2026-05-08
**Authoring authority:** Systems Architect
**Companion docs:**
- [`../BACKLOG.md`](../BACKLOG.md) (Strike 012 charter)
- [`reports/SYSTEM_STRIKE_LOG.md`](./SYSTEM_STRIKE_LOG.md) (entries `STRIKE-012-HARVEST` and `STRIKE-012-FULLY-HARVESTED-PROMOTED`)
- [`../../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md`](../../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md) (sign-off authority per RULE-000)

> **Note on "OR":** Earlier strikes used "OR" for *Operational Reconnaissance* (competitive scarcity scan against the 8.64 gate). This dossier reframes "OR" as *Operational Readiness* (launch-gate dossier). Both meanings live in the workspace. For Strike 012, the competitive-scarcity hypothesis is documented separately in `BACKLOG.md` §Strike Charters → "Pre-flight Scarcity (TBD)" — that scan is still pending and is independent of this readiness dossier.

---

## §1. Scarcity Narrative — The "Founding 100" Gate

### What it is

ScriptureScout will launch behind a deliberate access gate: **the first 100 users only**. Onboarding is by allow-list (manual approval) or invite-code, not open install. The Chrome Web Store listing remains **unlisted** during the Founding 100 phase. After the cohort closes (or after a defined success criterion is met), the listing flips to **public**.

### Why limit access (the four reasons)

1. **Stewardship of support resources.**
   Faith/Heritage software gets used in pastoral and pedagogical contexts where breakage carries real cost (Sunday-morning sermon prep, seminary deadlines). The Office cannot guarantee multi-thousand-user support coverage in v0.1. Capping at 100 means every reported issue gets a personal response from 864zeros within 24h and a fix within 7 days. This is not a marketing scarcity — it's an honest-capacity scarcity.

2. **Mission-alignment check.**
   The FHG pillar's commitment is "Heritage-first technology. Preserving what matters most." The Founding 100 is the smallest defensible cohort for verifying we're attracting the right user — *the serious student of the Word* — rather than experimenters who'll churn after one liberation. Founding 100 enrolment includes a one-question form: "What study work are you trying to liberate?" Answers below threshold (e.g., "just trying it out," vague responses) are deferred to the public launch waitlist.

3. **Iterative feedback loop.**
   Per RULE-000 governance, the Office Architect signs off on every brick promotion and palette evolution. The Founding 100 is the empirical input that informs the next strike's directives. Specifically we want signal on:
   - Which Bible-app source is most-requested next (Logos? Olive Tree? Accordance?)
   - Whether the Charcoal & Bronze palette holds up under sustained reading sessions (or whether Parchment Light needs to become the default)
   - Whether the BibleHub interlinear table format (GFM `| Greek | Translit | English | Strongs |`) matches how users actually want their lexical study work in their vault
   - Whether the FHG brand-firewall (no AI synthesis here — that's Bible Insight territory; see §2) feels disciplined or constraining

4. **Trust runway.**
   ScriptureScout is local-first and never transmits data, but users have to *believe* that. A small, audit-friendly cohort lets us:
   - Publish a privacy-policy companion doc with the actual `chrome://extensions → Permissions → Inspect` evidence
   - Field every "is this ToS-compliant for YouVersion?" question one at a time, rather than at scale where the wrong answer compounds
   - Build a public "Heritage Pledge" page citing Founding 100 testimonials before opening the floodgates

### The gate mechanism

| Stage | Mechanism | Cap |
|---|---|---|
| **Founding 100** | Unlisted CWS install via direct link from `864zeros.com/scripturescout`. One-question pre-install form filters intent. | 100 hard cap |
| **Closed Beta (post-Founding 100)** | Wait-list → batched invites of ~50/week as bandwidth allows | Soft cap = ~500 |
| **Public** | Open install on the Chrome Web Store; Founding 100 testimonials front and center | Unlimited |

### Closure criteria for Founding 100 → Closed Beta

The Founding 100 phase **closes** when **any one** of:
1. 100 users have completed at least one successful Liberation, OR
2. 60 days have elapsed since launch, OR
3. The Office Architect (864z-OA) signs off on early-close based on saturation of feedback signal.

---

## §2. Technical "Wedge" Constraints — What ScriptureScout Does NOT Do

ScriptureScout is the **wedge** for the Faith/Heritage pillar. The wedge does ONE thing well: liberate scripture study from proprietary clouds into the user's sovereign Markdown vault. Premium synthesis features belong to a sibling product (`Bible Insight`), preserving its reason-to-pay.

### Excluded by design (deferred to Bible Insight or out-of-scope entirely)

| Excluded feature | Why excluded | Lives in |
|---|---|---|
| **AI synthesis / topical summary** | Burns the privacy-first promise (cloud AI = sending scripture to third-party servers); also undercuts Bible Insight's premium tier | Bible Insight (Pro tier, with explicit user opt-in per session) |
| **Cross-referencing across translations** | Requires multi-source ingestion + alignment logic — substantial engineering, more naturally part of a study app than a liberation tool | Bible Insight |
| **Topical search / theme grouping** | Requires indexing, embedding, AI tagging — none align with the wedge's "capture & export" focus | Bible Insight |
| **Inline commentary AI** | Same privacy concern as synthesis; commentary is also a content-licensing minefield (modern commentaries aren't public-domain) | Bible Insight (Pro tier) |
| **Collaborative annotations** | Multi-user → cloud sync → end of local-first promise | Out of scope entirely (not a 864zeros pillar) |
| **Pre-loaded Bibles or commentary corpus** | ScriptureScout is not a content product; it's a bridge to user-owned vaults | Bible Insight (Power tier) or third-party Bible-text projects |
| **Cloud sync of captures** | Privacy-first triad ("always private") forbids it as a default; opt-in Drive sync may be added per `agent-drive-sync` brick if Founding 100 demands it | Optional v2 (opt-in only) |
| **Verse-by-verse audio capture** | Out of capture-flow scope; different brick set entirely | Future strike if demand justifies |
| **Lectionary-aware export presets** | Belongs to Power tier when payment infrastructure ships | ScriptureScout Power tier (post-Founding 100) |

### Wedge ↔ Premium ladder (preserve the upsell)

```
ScriptureScout (Free, FHG wedge)
    │  Captures scripture from supported sites → liberates to .md
    │  Frontmatter: reference, translation, source_url, view_source, profile_host
    │  Local-only IndexedDB; no AI; no cross-referencing
    │
    ▼  When user wants synthesis / topical work / multi-source diff:
    │
Bible Insight (Pro / Power, FHG pillar)
    │  AI-augmented study; cross-translation alignment; topical themes
    │  Privacy-redacted before AI calls (per agent-anonymizer-pii brick)
    │  Imports from ScriptureScout's Markdown vault — natural upgrade path
```

**The discipline:** every feature request that smells like synthesis, AI, or multi-source alignment gets the response *"Great use case — that's Bible Insight territory. Here's where it'll land."* This protects Bible Insight's GTM moat and keeps ScriptureScout's wedge sharp.

### Brick exclusions (registered but NOT used by Strike 012)

The following bricks from `BRICK_REGISTRY.json` are **explicitly NOT loaded** by ScriptureScout, even though they're available:

- `agent-ai-summarize` (cloud Gemini call)
- `agent-ai-autotag`
- `agent-ai-vision`
- `agent-ai-chat`
- `agent-anonymizer-pii` (only relevant when calling AI)
- `agent-drawio-converter`
- `agent-feature-gate-tiers` (no paid tier yet — ScriptureScout is fully free in v1)
- `agent-payment-extpay` (no payment infrastructure in v1)
- `agent-credit-ledger` (no AI to credit-meter)

---

## §3. Deployment Path

### §3.1 "Load Unpacked" Smoke Test Protocol (Operator)

Run this before each release candidate is shared with the Founding 100. Total time: ~12 minutes.

#### Pre-flight prep
1. Operator generates final designed icons via `icons/generate-icons.html` (or the chosen icon set), saved as `icon16.png` / `icon48.png` / `icon128.png` in `extensions/scripture-scout/icons/`.
2. Operator confirms `manifest.json` version matches the release tag.
3. Operator clears any prior "ScriptureScout" install: `chrome://extensions` → Remove.

#### Smoke test (12 steps, ~12 minutes)

| # | Action | Pass criterion |
|---|---|---|
| 1 | `chrome://extensions` → Developer mode ON → Load unpacked → select `extensions/scripture-scout/` | Extension loads with **zero errors** in the Errors pane (warnings about icon sizes are acceptable if placeholder icons; **fail otherwise**) |
| 2 | Click toolbar icon | Side panel opens on the right; header shows `[FHG] ScriptureScout`; tagline reads "Heritage-first technology. Preserving what matters most." |
| 3 | Open Options (Cog icon, top-right of side panel) | Options page opens in a new tab; General Settings card visible with Theme Selector + Dopamine-Friendly UI `(*)` info icon |
| 4 | Click `(*)` info icon | Bronze-bordered popover appears with the Dopamine-Friendly UI definition verbatim |
| 5 | Visit `https://www.biblegateway.com/passage/?search=John+3%3A16-17&version=ESV` | BibleGateway page loads normally |
| 6 | Right-click the verse text → "864zeros: Save passage" | Toast appears: "Scout Success — 1 passage from BibleGateway" (or similar); side panel capture count increments to 1 |
| 7 | Click the capture in the side panel | Accordion expands smoothly (~300ms transition); chevron rotates 90°; Parchment reading panel shows the verses |
| 8 | Visit `https://blueletterbible.org/kjv/john/3/16` and right-click → "Save passage" | Capture appears with title "John 3:16" and translation "KJV" |
| 9 | Visit `https://biblehub.com/interlinear/john/3-16.htm` and use the marquee tool from the side panel | Capture appears; banner during marquee reads "ScriptureScout (Bible Hub · interlinear)" |
| 10 | In the side panel, Shift+Click the BibleGateway and BLB captures | Both expand simultaneously (Compare Mode) |
| 11 | Select all three captures via master checkbox → "Liberate to Vault" | 3 `.md` files appear in `~/Downloads/scripture-scout/` (or platform equivalent); cleanup prompt appears |
| 12 | Open the BibleHub interlinear `.md` file | Frontmatter contains `reference`, `translation`, `view_source`, `source_url`, `profile_host: biblehub.com`, `capture_mode: marquee`; body contains `\| Greek \| Translit \| English \| Strongs \|` GFM table |

#### Test environment matrix

| Browser | OS | Required for Founding 100? |
|---|---|---|
| Chrome 120+ | Windows 11 | Yes (largest user base) |
| Chrome 120+ | macOS 14+ | Yes |
| Chrome 120+ | Linux (Ubuntu 22+) | Optional (small but vocal) |
| Edge 120+ (Chromium) | Windows 11 | Optional (untested but likely works) |
| Brave / Vivaldi / Arc | Any | Out of scope for Founding 100 |

If any of the 12 smoke-test steps fails on a required environment, the release is **NOT** shipped to the Founding 100. The defect is logged in `SYSTEM_STRIKE_LOG.md`, fixed, and the smoke test re-run from step 1.

### §3.2 Kill-Switch Criteria

A "kill" means: pause Founding 100 onboarding, optionally remove the unlisted CWS link, ship a fix, restart. ScriptureScout has three tiers of kill triggers.

#### Tier 1 — Immediate Hard Kill (act within 1 hour)

Any one of these triggers an immediate halt to onboarding + a public statement on the marketing page:

- **Data loss bug confirmed.** A capture that the user marked as "Liberated" failed to download AND was also cleared from IndexedDB (silent data destruction).
- **Privacy violation confirmed.** Any network call to a non-Chrome-internal endpoint from the service worker, content script, or popup. (Easy to detect: `chrome://extensions` → Inspect Service Worker → Network tab. Should show ZERO non-`chrome://` traffic during normal use.)
- **Security CVE in a runtime dependency.** jsdom is dev-only (test harness); the runtime has no third-party deps. But if Chrome's MV3 runtime ships a CVE that affects our `chrome.scripting.executeScript` or `chrome.downloads.download` usage, halt + patch.
- **Legal / ToS notice from a target site.** If BibleGateway, BLB, or BibleHub sends a takedown notice or ToS-violation letter regarding the extension's scraping behavior. (Capturing the user's own logged-in highlight data is generally permitted; capturing for redistribution is not. ScriptureScout does the former; defend that vigorously, but pause if challenged formally.)

#### Tier 2 — Soft Kill (act within 24 hours)

Any one triggers pause-onboarding + targeted fix:

- **Selector profile drift.** A target site updates its DOM and the existing selectors (`.passage-content`, `.verse-text`, `.interlinear`) stop matching, breaking the wedge feature for everyone on that site. Fix in `scripts/selectors.js`, bump `profile_version`, re-smoke, resume onboarding.
- **Liberation success rate < 95%** during the first 14 days of Founding 100 (measured by support reports — not telemetry, since we have none). If users report "I clicked Liberate, no file appeared" more than 5% of the time, halt and diagnose.
- **IndexedDB corruption affecting > 3 users.** ScriptureScout uses the standard `agent-indexeddb-store` pattern; corruption is rare but possible if the user's disk fills up mid-write. If reports cluster, ship a recovery import path.
- **Brand-firewall breach.** If a user reports the OIA pillar's "Built for ADHD" copy bleeding into the FHG product (or vice-versa), halt, audit, fix per `OFFICE_ARCHITECT.md` §II.

#### Tier 3 — Feedback-Driven Kill (act within 7 days, by Office Architect sign-off)

If at the 30-day Founding 100 mark **any** of these is true, the strike is rolled back to "build phase" and re-evaluated:

- **< 70% of Founding 100 successfully completed at least one liberation** within their first 7 days post-install. (Measures: feature discoverability, not adoption depth.)
- **< 30% of Founding 100 are still active at week 4** (no captures in the prior 14 days). (Measures: weekly habit formation.)
- **Net Promoter signal is negative.** Founding 100 invitees include a 30-day check-in: "Would you recommend ScriptureScout to another pastor / seminarian?" If <50% say yes, halt public launch and re-charter.
- **A sibling pillar product (Bible Insight) reports cannibalization** — i.e., users churn from Bible Insight Pro because ScriptureScout's free wedge satisfies their need. (This shouldn't happen if §2 wedge constraints are honored; if it does, the constraints need re-tightening.)

#### What is NOT a kill trigger

To avoid spurious halts:

- Single-user defect reports (those become bug-tracker tickets, not kill triggers)
- Slow performance (optimization, not roll-back)
- Cosmetic feedback ("I wish the chevron were larger") — feature-request queue
- Selector drift on UNSUPPORTED sites (no commitment was made)
- Pre-flight scarcity scan (`OR-2026-05-XX-SCRIPTURESCOUT.md` — separate competitive analysis, not a launch gate)

---

## §4. Rollout Sequence

| Phase | Trigger | Duration |
|---|---|---|
| **Phase 0 — Internal smoke test** | Operator runs §3.1 12-step protocol | 1 day |
| **Phase 1 — Office Architect sign-off** | Per RULE-000, accepts this dossier; smoke test passes | <1 day |
| **Phase 2 — Founding 100 launch** | CWS unlisted listing live; `864zeros.com/scripturescout` form opens | Up to 60 days, capped at 100 successful liberations |
| **Phase 3 — Closure review** | Founding 100 closes per criteria above; Office Architect signs off on Closed Beta or kill/restart | 1 week (review) |
| **Phase 4 — Closed Beta** | ~50/week from waitlist; CWS unlisted | ~4 weeks |
| **Phase 5 — Public** | CWS listing flips to public; `864zeros.com/scripturescout` opens free signup | Indefinite |

---

## §5. Sign-off Gates

Per `ROLES/OFFICE_ARCHITECT.md` §VI, the Office Architect (864z-OA) signs off on this dossier before Founding 100 launch.

| Sign-off | Owner | Required for |
|---|---|---|
| Pre-flight OR (this dossier) accepted | Office Architect (864z-OA) | Founding 100 launch |
| Smoke test pass | Operator | Each release candidate |
| Privacy policy URL live at `864zeros.com/privacy` | 864zeros LLC | CWS submission (any phase) |
| Terms of Use URL live at `864zeros.com/terms` | 864zeros LLC | CWS submission (any phase) |
| FHG-pillar landing page at `864zeros.com/scripturescout` | DIV-4-STUDIO (marketing) | Founding 100 enrolment form |
| Founding 100 testimonial collection process | Office Architect + Operator | Closure review (Phase 3) |

---

## §6. Open Items / Defer to Operator

These items are NOT blocking acceptance of this dossier, but the Operator must close them before Phase 2 launch:

- [ ] Designed FHG icons (replace 1×1 placeholder PNGs in `extensions/scripture-scout/icons/`)
- [ ] Founding 100 pre-install form copy (the one-question filter)
- [ ] Decide whether `864zeros.com` or a sub-domain (`fhg.864zeros.com` or `scripturescout.864zeros.com`) hosts the landing page
- [ ] Privacy policy long-form (the short version is committed in `CLAUDE-base.md` Privacy First section; long form needs legal review)
- [ ] YouVersion ToS legal review — capture-the-user's-own-logged-in-highlights is permitted in spirit; written legal opinion preferred before YouVersion is added to `selectors.js` profiles (currently NOT included; v2 candidate)
- [ ] Founding 100 invitation message template
- [ ] Support email / channel commitment (the 24h response promise needs an inbox)

---

## §7. Cross-References

- [`BACKLOG.md`](../BACKLOG.md) — Strike 012 charter, Active Sprint, Compliance Migration Backlog
- [`reports/SYSTEM_STRIKE_LOG.md`](./SYSTEM_STRIKE_LOG.md) — `STRIKE-012-FULLY-HARVESTED-PROMOTED` entry + Final Seal
- [`../../864zeros-llc/GTM_MANIFEST.md`](../../../864zeros-llc/GTM_MANIFEST.md) — brand canon, FHG pillar, standardized footer
- [`../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md`](../../../864zeros-llc/ROLES/OFFICE_ARCHITECT.md) — sign-off authority for this dossier
- [`../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md`](../../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md) — RULE-001/002/003/004 compliance verified for ScriptureScout
- [`../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/scripture-scout/`](../../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/scripture-scout/) — the build itself

---

*Pre-flight OR · Strike 012 [FHG] · ScriptureScout · v1.0 · 2026-05-08*
