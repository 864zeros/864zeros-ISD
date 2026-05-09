# 864zeros LLC-DIV-3-FACTORY: Tech Stack Audit [v1.0]

**Authority:** Engineering snapshot. Synthesizes the `manifest.json` from every extension under [`LLC-DIV-3-FACTORY/extensions/`](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/) (15 extensions, scanned 2026-05-09).
**Loaded:** On demand for compliance audits, capability analysis, or pre-strike capacity planning.
**Authored:** 2026-05-09 by 864z-OA (Office Architect) under RULE-000. Audit data extracted programmatically from manifest sources; no manual measurement.
**Update protocol:** Re-audit + append-version after any extension's manifest change OR any new RULE codification. Prior versions preserved for diff trail.
**Format note:** Follows the inferred `864z-markdown-standard` (BUILD_KIT_RULES.md metadata header + MASTER_CONTEXT.md.md atomic body). Standard not yet codified — pending Office Architect sign-off.

---

## I. Stack Baseline (15 / 15 extensions)

| Substrate | Adoption | Status |
|---|---|---|
| Manifest V3 | 15 / 15 | ✅ universal |
| Side-panel surface | 15 / 15 | ✅ universal — confirms the panel-only directive |
| `chrome.storage` permission | 15 / 15 | ✅ universal — no extension uses ad-hoc localStorage |
| `action` (toolbar icon) | 15 / 15 | ✅ universal |
| Service worker present | 15 / 15 | ✅ universal |
| Service worker `type: "module"` | 14 / 15 | 🟡 `who-is-watching` is the lone non-module SW — modernization gap |
| Options page (`options_ui`) | 8 / 15 | 🟴 7 extensions missing — **RULE-001 violation** in 7 places |
| Options opened in tab | 8 / 8 (of those with options) | ✅ — when an Options page exists, it always opens in tab per RULE-001 |
| Content scripts | 7 / 15 | (expected — only host-page-touching extensions need them) |
| `unlimitedStorage` permission | 4 / 15 | The "vault-class" cluster |
| `downloads` permission | 4 / 15 | The "liberation-class" cluster (overlaps vault-class 1:1) |
| Host permissions = `<all_urls>` | 5 / 15 | The broad-reach cluster |

---

## II. Per-Extension Inventory

| Extension | Pillar | Class | Version | Options? (RULE-001) | Brand-prefix? (RULE-006) | Liberation? | Icon path | Sizes |
|---|---|---|---|---|---|---|---|---|
| `scripture-scout` | **FHG** | Liberation | 0.1.0 | ✅ in-tab | ✅ `[FHG]` | ✅ Markdown | `images/` | 16,32,48,128 |
| `Bible-Insight` | **FHG** | Liberation | 1.0.0 | ✅ in-tab | ❓ unaudited | ✅ Markdown | `assets/` | 16,48,128 |
| `clipboard` | **864-Flux** | Liberation | 1.0.0 | ✅ in-tab | ✅ `[864F]` (Phase 1) | ✅ PDF + Markdown | `assets/` | 16,48,128 |
| `migration-pilot` | **864-Flux** | Liberation | 0.1.0 | ✅ in-tab | ✅ `[864F]` | ✅ Markdown (BRK-DL-001 birthplace) | `icons/` | 16,48,128 |
| `TabVault` | **OIA** | Tab-mgmt | 1.0.0 | ✅ in-tab | ✅ `[OIA]` (post-RULE-004 migration) | — | `assets/` | 16,48,128 |
| `Signal2Noise` | **OIA** | Focus | 1.0.0 | ✅ in-tab | ❓ unaudited | — | `assets/` | 16,48,128 |
| `Time2Focus` | **OIA** | Focus | 1.0 | ✅ in-tab | ❓ unaudited | — | `icons/` | 16,48,128 |
| `TuneOut2FocusIn` | **OIA** | Focus | 1.0.0 | ✅ in-tab | ❓ unaudited | — | `assets/` | 16,48,128 |
| `oia-focus-note` | **OIA** | Focus | 1.1.0 | 🟴 missing | ❓ unaudited | — | `icons/` | 16,48,128 |
| `oia-focus-timer` | **OIA** | Focus | 1.1.0 | 🟴 missing | ❓ unaudited | — | `icons/` | 16,48,128 |
| `oia-focus-wall` | **OIA** | Focus | 1.1.0 | 🟴 missing | ❓ unaudited | — | `icons/` | 16,48,128 |
| `oia.focus.signal` | **OIA** | Focus | 1.1.0 | 🟴 missing | ❓ unaudited | — | `icons/` | 16,48,128 |
| `oia.focus.sound` | **OIA** | Focus | 1.1.0 | 🟴 missing | ❓ unaudited | — | `icons/` | 16,48,128 |
| `who-is-watching` | **OIA** | Recon (privacy) | 2.1.6 | 🟴 missing | ❓ unaudited | — | `icons/` | 16,48,128 |
| `864z-chronical` | **OIA** | Recon (AI capture) | 1.0.0 | 🟴 missing | ❓ unaudited | — | `icons/` | 16,48,128 |

---

## III. Permission Patterns (Extension Classes)

The 15 extensions cluster into 4 classes by their permission fingerprint:

### III.a — Liberation Class (4 extensions)

`Bible-Insight`, `clipboard`, `migration-pilot`, `scripture-scout`

**Fingerprint:** `unlimitedStorage` + `downloads` + `activeTab` + `scripting` + `contextMenus` + host_permissions = `<all_urls>`.

These are vault-class extensions: they extract content from arbitrary host pages, archive locally, then liberate to the user's filesystem as Markdown / PDF. RULE-002 (SW Base64 download) and RULE-007 (Secret Sovereignty / BYOK) apply most strictly here. Three of the four are Strike-promoted reference implementations for various RULES.

### III.b — Tab-Management Class (2 extensions)

`TabVault`, `who-is-watching`

**Fingerprint:** `tabs` + `scripting` + `activeTab` (TabVault adds `alarms` + `identity`; who-is-watching adds `webRequest` + `declarativeNetRequest*`).

Tab-class extensions operate on the user's open-tab state without exporting content. No `downloads` permission. TabVault is the OIA reference impl for RULE-004 accordion adoption.

### III.c — Focus Class (5 extensions)

`oia-focus-note`, `oia-focus-timer`, `oia-focus-wall`, `oia.focus.signal`, `oia.focus.sound`, `Signal2Noise`, `Time2Focus`, `TuneOut2FocusIn`

**Fingerprint:** minimal — `sidePanel` + `storage`, optionally `notifications` / `alarms` / `offscreen` for media features.

Focus-class extensions don't touch host pages. Smallest permission surface; lowest privacy risk; lowest manifest complexity. Trade-off: highest RULE-001 violation rate (5 of 8 lack an options page entirely).

### III.d — Recon Class (1 extension)

`864z-chronical`

**Fingerprint:** `storage` + `sidePanel` + scoped host_permissions to specific AI sites (`gemini.google.com`, `claude.ai`, `chatgpt.com`, `aistudio.google.com`, `chat.openai.com`).

Recon-class extensions silently capture the user's interactions with named third-party services. Strictest scoping — narrow host_permissions instead of `<all_urls>`. Strong RULE-007 candidate for first audit (extracts content potentially containing user secrets).

---

## IV. Compliance Gap Analysis (vs RULE-001 through RULE-007)

### IV.a — RULE-001 Violations (Cog-triggered Options page)

🟴 **7 extensions missing `options_ui` entirely.** Migration backlog:

`oia-focus-note`, `oia-focus-timer`, `oia-focus-wall`, `oia.focus.signal`, `oia.focus.sound`, `who-is-watching`, `864z-chronical`

Each needs a `options/options.html` scaffolded with the 3 RULE-001 sections (How to Use · Subscription & Tiers · Data Management) + a Cog in the side-panel header. The 5 `oia.focus.*` extensions can share a near-identical Options scaffold (Focus class has a near-identical concern set).

### IV.b — RULE-002 Compliance (SW Base64 download)

✅ All 4 Liberation-class extensions verified as compliant (1 reference + 3 inheriting BRK-DL-001). No download-using extension violates this rule.

### IV.c — RULE-003 Compliance (Tristate selection on record queues)

🟡 Audited: `migration-pilot` ✅, `TabVault` ✅. **Not yet audited:** `clipboard` (clip queue), `scripture-scout` (capture queue — RULE-003 status unknown post-launch-polish).

### IV.d — RULE-004 Compliance (Accordion record UI)

✅ 3 production adopters: `scripture-scout` (FHG), `migration-pilot` (864-Flux), `TabVault` (OIA) — proves Pillar Compatibility = Global.
🟴 Pending: `clipboard` (Phase 2 deferred — sidepanel/main.js is 2,555 LOC).

### IV.e — RULE-005 Compliance (Two-tap destructive)

🟡 Verified in `scripture-scout` and `migration-pilot`. **Not yet audited** in the other 13 extensions (the rule was codified 2026-05-08 — post-most-extensions). Repo-wide grep for `alert\|confirm\|prompt` is the cheap first-pass check; deferred to Clipboard Phase 2 sprint.

### IV.f — RULE-006 Compliance (Brand-prefix pill)

| Status | Extensions |
|---|---|
| ✅ Compliant | `scripture-scout`, `migration-pilot`, `clipboard` (Phase 1), `TabVault` |
| ❓ Unaudited | All 11 others |
| 🟴 Known violation | None confirmed yet |

### IV.g — RULE-007 Compliance (Secret Sovereignty / BYOK)

🟡 `clipboard` is the canonical pre-rule-compliant example (BYOK API key flow for AI providers). `Bible-Insight` MUST adopt at strike charter (planned). `864z-chronical` requires audit (captures user-AI conversations — secret-adjacent). Other 12 extensions: no secret handling identified, but formal audit pending.

---

## V. Cross-Extension Inconsistencies (Engineering Hygiene)

### V.a — Naming Convention Drift

Three live conventions:
- **kebab-case:** `migration-pilot`, `scripture-scout`, `oia-focus-note`, `oia-focus-timer`, `oia-focus-wall`, `who-is-watching`, `864z-chronical`
- **dot-case:** `oia.focus.signal`, `oia.focus.sound`
- **PascalCase:** `Bible-Insight`, `Signal2Noise`, `TabVault`, `Time2Focus`, `TuneOut2FocusIn`
- **lowercase:** `clipboard`

**Recommendation:** standardize on kebab-case for new strikes; existing extensions grandfathered until next major version bump.

### V.b — Icon Path Divergence

- `icons/` — 9 extensions (legacy default)
- `assets/` — 5 extensions (`Bible-Insight`, `clipboard`, `Signal2Noise`, `TabVault`, `TuneOut2FocusIn`)
- `images/` — 1 extension (`scripture-scout`, post-FHG-launch-polish)

**Recommendation:** standardize on `assets/` for new strikes (semantic; matches web convention); existing paths grandfathered.

### V.c — Icon Size Coverage

- 16 / 48 / 128: 14 of 15
- 16 / **32** / 48 / 128: 1 of 15 (`scripture-scout` only)

**Recommendation:** add 32×32 to all 14 non-compliant manifests. Required for Chrome Web Store retina toolbar rendering. Single-line manifest delta per extension.

### V.d — `author` Field

10 of 15 manifests have `author: null` or absent. Only `migration-pilot`, `scripture-scout`, `oia-focus-note`, `oia-focus-timer`, `oia-focus-wall`, `oia.focus.signal`, `oia.focus.sound` set a value (and these are inconsistent: "864zeros LLC (OIA pillar)" vs "864zeros LLC (Faith / Heritage pillar)" vs "864zeros").

**Recommendation:** standardize on `"864zeros LLC ({Pillar} pillar)"` format. Mechanical fix.

### V.e — Service Worker Module Type

`who-is-watching` is the only extension shipping a non-module service worker. Modernization gap; should be migrated when a routine touch happens to that extension.

---

## VI. Recommended Migration Priority (Blast-Radius Order)

| Priority | Migration | Affected | Estimated effort | Blocks |
|---|---|---|---|---|
| P0 | Add `options_ui` scaffold to 7 RULE-001-noncompliant extensions | 7 | ~2h each (5 share Focus-class scaffold = ~3h batched) | Web Store release of any non-compliant extension |
| P1 | RULE-006 brand-prefix audit + injection across the 11 unaudited extensions | 11 | ~30 min each (mechanical) | RULE-006 universal compliance milestone |
| P1 | RULE-007 audit of `864z-chronical` (AI conversation capture is secret-adjacent) | 1 | ~1h | Public release / FHG-pillar trust gate |
| P2 | Add 32px icon to 14 manifests | 14 | ~10 min each (manifest edit + asset) | Retina UX polish |
| P2 | Modernize `who-is-watching` SW to `type: "module"` | 1 | ~2h (refactor + test) | Future ESM-only brick adoption |
| P3 | Standardize `author` field across all 15 manifests | 15 | ~5 min each | Tooling that reads author field |
| P3 | Standardize icon path + naming conventions | gradual | per major-version bump | Cosmetic / engineering hygiene |
| **DEFER** | Clipboard Phase 2 — RULE-001/003/004/005/006/007 deep refactor | 1 | ~6-10h focused | All clipboard rule compliance; needs paid-tier UX decisions first |

---

## VII. Cross-References

- Source manifests: [`LLC-DIV-3-FACTORY/extensions/*/manifest.json`](../../864zeros-llc/LLC-DIV-3-FACTORY/extensions/)
- Rules: [`864z-build-kit/references/core/BUILD_KIT_RULES.md`](../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md)
- Brick registry: [`ISD-DIV-0-CORE/BRICK_REGISTRY.json`](../ISD-DIV-0-CORE/BRICK_REGISTRY.json)
- Pillar mapping: [`864zeros_PILLAR_STRATEGY.md`](./864zeros_PILLAR_STRATEGY.md)
- Roadmap targets: [`864zeros_2026_ROADMAP.md`](./864zeros_2026_ROADMAP.md)
- Studio handoff index: [`ISD-DIV-4-STUDIO/EXTENSION_MANIFEST_INDEX.md`](../ISD-DIV-4-STUDIO/EXTENSION_MANIFEST_INDEX.md)

---

## VIII. Versioning

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-09 | Initial audit. 15 extensions scanned. Class taxonomy established (Liberation / Tab-mgmt / Focus / Recon). Compliance status mapped against RULE-001 through RULE-007. 7 P0 RULE-001 violations identified. Migration priority queue published. |

---

*864zeros Tech Stack Audit v1.0 · 2026-05-09 · 864zeros LLC · For DIV-6 NotebookLM ingestion.*
