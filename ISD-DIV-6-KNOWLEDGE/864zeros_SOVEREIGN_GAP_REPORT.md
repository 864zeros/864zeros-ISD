# 864zeros: Sovereign Gap Report [v1.0]

**Authority:** Office Architect (864z-OA) per RULE-000.
**Loaded:** 2026-05-09 — first authoritative privacy/data-sovereignty audit of the 15-extension fleet.
**Authored:** 2026-05-09 by 864z-OA per RULE-000.
**Update protocol:** Append-only; new findings land as `[v1.x]` increments under §XII Versioning. Per-extension code citations should be re-validated whenever the originating SHA changes. Disclosure discipline (RULE-007 §Disclosure) preserved throughout: no secret values, prefixes, suffixes, or fingerprints appear below — only structural/pattern findings.
**Sources synthesized:** `LLC-DIV-3-FACTORY/extensions/*` source trees (15 extensions); `864z-build-kit/references/core/BUILD_KIT_RULES.md` (RULE-000 through RULE-008); `ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md` (RULE-007 codification entry `2026-05-08T-DIVISIONS-ATOMIC-READMES-STRIKE`); `ISD-DIV-6-KNOWLEDGE/864zeros_TECH_STACK_AUDIT.md` v1.0; `ISD-DIV-0-CORE/SECURITY_ROTATION_LOG.md`.
**Format note:** Follows the `864z-markdown-standard` (RULE-008).

---

## I. Audit Methodology & Scope

### I.1 Scope

All 15 Chrome extensions under `LLC-DIV-3-FACTORY/extensions/`:

| # | Extension | Class | Pillar |
|---|---|---|---|
| 1 | `864z-chronicle` | AI-Capture | OIA |
| 2 | `Bible-Insight` | Liberation + AI | FHG |
| 3 | `clipboard` | Liberation + AI | OIA |
| 4 | `migration-pilot` | Liberation | OIA |
| 5 | `scripture-scout` | Liberation | FHG |
| 6 | `TabVault` | Tab-mgmt + Drive-sync | OIA |
| 7 | `Signal2Noise` | Focus | OIA |
| 8 | `Time2Focus` | Focus | OIA |
| 9 | `TuneOut2FocusIn` | Focus | OIA |
| 10 | `oia-focus-note` | Focus | OIA |
| 11 | `oia-focus-timer` | Focus | OIA |
| 12 | `oia-focus-wall` | Focus | OIA |
| 13 | `oia.focus.signal` | Focus | OIA |
| 14 | `oia.focus.sound` | Focus | OIA |
| 15 | `who-is-watching` | Recon | 864-Flux |

### I.2 Audit dimensions

Four orthogonal vectors applied to every extension:

1. **Storage mapping** — `chrome.storage.local|sync|session`, `indexedDB`, `localStorage`, `sessionStorage`, `chrome.downloads.download` write surfaces.
2. **Data exit points** — `fetch`, `XMLHttpRequest`, `WebSocket`, `EventSource`, `chrome.runtime.sendNativeMessage` — every URL, method, header, payload classified.
3. **PII pattern scan** — emails, name fields, tokens, `Authorization` / `Bearer` / `x-api-key` headers, user-generated content in transit.
4. **AI provider risk assessment** — provider, key-handling model (BYOK vs bundled vs proxy), prompt content payload, response handling.

### I.3 Method

Read-only static analysis: `Grep` and `Read` only — zero modifications, zero test execution, zero service-worker boot. Markdown documentation under each extension was inspected for design intent but the **shipping JavaScript is the source of truth** for every finding.

### I.4 Coverage Gaps

| Extension | Coverage gap | Mitigation |
|---|---|---|
| `who-is-watching` | `lib/d3.v7.min.js` is minified third-party — `fetch` references inside are D3 source, not extension exfiltration. Only the extension's own SW + content scripts were audited for exit points. | None needed; D3 is purely a rendering library, no network calls invoked from extension code. |
| `clipboard` | Lib contains TWO AI clients (`lib/ai/ai-client.js` proxy-based + `lib/api-client.js` BYOK direct). Only `api-client.js` is imported by the SW; `ai-client.js` is dead code. README still describes the proxy architecture. | Findings reflect the **actually-imported** path (`api-client.js`). Dead-code path flagged in §IX.4. |
| All extensions | Source SHA at audit time not pinned. Re-audit on next major version per extension. | §XII Versioning protocol covers re-audit cadence. |

---

## II. Storage Mapping

### II.1 Fleet summary table

| Extension | `storage.local` | `storage.sync` | `storage.session` | IndexedDB (DB name) | localStorage | sessionStorage | `downloads.download` |
|---|---|---|---|---|---|---|---|
| `864z-chronicle` | settings only | — | — | `chronicle` (entries, exchanges) | — | — | — |
| `Bible-Insight` | settings + token-usage timestamp | — | — | `bibleinsight` (contentItems, tags, contentTags + others) | — | — | YES (PDF/JSON backup) |
| `clipboard` | settings + API key + tier + credits + Drive tokens | — | — | `clipboard` (clips, tags, clip_tags) | — | — | YES (PDF, JSON backup) |
| `migration-pilot` | (none in active code; settings only via library) | — | — | `migration-pilot` (captures) | — | — | YES (Markdown export) |
| `scripture-scout` | settings only | — | — | `scripture-scout` (captures) | — | — | YES (Markdown export) |
| `TabVault` | settings + tab-activity + Drive tokens | — | — | `tabvault` (vaulted-tab metadata) | — | — | — |
| `Signal2Noise` | signals[] + ratio | — | — | — | — | — | — |
| `Time2Focus` | timer state + focus topic + sound/color prefs | — | — | — | — | — | — |
| `TuneOut2FocusIn` | settings | — | — | — | — | — | — |
| `oia-focus-note` | notes[] + cleanup ts | — | — | — | — | — | — |
| `oia-focus-timer` | timer state + sound + last focus text | — | — | — | — | — | — |
| `oia-focus-wall` | notes[] + cleanup ts + version | — | — | — | — | — | — |
| `oia.focus.signal` | signals[] + selectedRatio + cleanup ts | — | — | — | — | — | — |
| `oia.focus.sound` | sound prefs | — | — | — | — | — | — |
| `who-is-watching` | settings + captured identities | — | — | `whoiswatching` (events, identities) | — | — | — |

**Fleet-wide observations:**

- **Zero `chrome.storage.sync` usage** in any active extension code. RULE-007 §`.sync` forbidden — clean. (One historical doc reference in `864z-chronicle/{864z} chronicle extension (1).md` at lines 1209/1354 references `chrome.storage.sync.get('chronicleTier')` — design spec only, **not present in shipping code**.)
- **Zero `localStorage` / `sessionStorage`** in any active extension code. Only matches are in `IGNORE/` notes folders for `who-is-watching`.
- All 15 extensions use `chrome.storage.local` for at least settings (manifest `storage` permission is universal — confirmed in `864zeros_TECH_STACK_AUDIT.md` §I.1).
- IndexedDB present in 7/15 extensions — exactly the 4 vault-class (Bible-Insight, clipboard, migration-pilot, scripture-scout) plus 864z-chronicle, TabVault, who-is-watching.

### II.2 Per-extension detail (vault-class)

#### II.2.a `Bible-Insight`

**`chrome.storage.local` keys** (from `js/lib/api.js` + `js/options.js` + `js/background.js`):

```text
{APP_SLUG}_initialized          # boolean
{APP_SLUG}_settings             # object {apiKey, bibleApiKey, bibleTranslation, autoDetectVerses, aiMode, crossRefSource, ...}
{APP_SLUG}_lastUpdate           # timestamp
```

**IndexedDB `bibleinsight` schema** (from `js/lib/db.js` + `js/lib/constants.js`):
- `contentItems` — captured page text, selections, PDFs, screenshots, AI-generated analyses
- `tags` — color-based organization
- `contentTags` — junction (compound key `[contentId, tagId]`)
- Additional stores per `DB_SCHEMA` constants

**Stored data classification:** SUBSTANTIAL user content — full captured page text per `MSG_TYPES.SAVE_PAGE`, selections, screenshots (base64), PDFs (deferred to filesystem), AI analyses (verse detections, key points, image descriptions). **Includes the user's Gemini API key in `chrome.storage.local`** under `{APP_SLUG}_settings.apiKey` (RULE-007 compliant — `.local` not `.sync`).

**Downloads:** `chrome.downloads.download` invoked by JSON backup export (`js/options.js` line ~315-325 — Blob → blob URL → click; this works because options page has document context, unlike SW).

#### II.2.b `clipboard`

**`chrome.storage.local` keys** (from `background/service-worker.js` + `lib/api-client.js` + `options/options.js` + `lib/google-drive/drive-client.js`):

```text
{APP_SLUG}_initialized           # boolean
{APP_SLUG}_settings              # object
{APP_SLUG}_ai_api_key            # SECRET — Gemini or Claude API key
drive_access_token               # SECRET — Google OAuth access token
drive_token_expiry               # timestamp
drive_user_email                 # PII — operator's Google email
drive_last_sync_{appSlug}        # timestamp
drive_auto_sync_{appSlug}        # boolean
drive_auto_sync_interval_{appSlug} # number
drive_device_id                  # synthetic UUID
# plus credit / tier keys via lib/payments/credits.js + extpay-wrapper.js
```

**IndexedDB `clipboard` schema** (from `lib/db.js` + `lib/constants.js`):
- `clips` — full content (text + base64 screenshot data + PDF thumbnails), source URL, source title, summary, starred, timestamps
- `tags` — user-created tags
- `clip_tags` — junction

**Stored data classification:** CATASTROPHIC blast radius — full clipped content for the user's entire research history, base64 screenshots, PDF thumbnails, plus the user's AI provider API key AND a Google Drive access token alongside. Backup tied to operator's Google account email.

**Downloads:** `chrome.downloads.download` for PDF capture (`background/service-worker.js` line ~894 — uses Base64 data URI per RULE-002), JSON backup export (`lib/backup.js`).

#### II.2.c `migration-pilot`

**`chrome.storage.local` keys** (from `lib/store.js` + `background/service-worker.js`):

```text
{APP_SLUG}_settings              # object (capture settings, RULE-001 compliant Options page)
```

**IndexedDB `migration-pilot` schema** (from `lib/db.js`):
- `captures` (`{ id (autoIncrement), title, content, source_url, timestamp, tags[], note, captureMode, bounds }`)
- Indexes: `by_timestamp`, `by_source_url`

**Stored data classification:** SUBSTANTIAL user content — captured page text, selections, marquee bounds. **No secrets, no PII fields, no API keys** — true zero-cloud extension.

**Downloads:** `chrome.downloads.download` for Markdown export via Base64 data URI (`background/service-worker.js → runLiberation()` per RULE-002 / BRK-DL-001).

#### II.2.d `scripture-scout`

**`chrome.storage.local` keys** (from `sidepanel/main.js` + `options/main.js`):

```text
{APP_SLUG}_settings              # object
```

**IndexedDB `scripture-scout` schema** (from `lib/db.js`):
- `captures` (`{ id (autoIncrement), title, content, contentFormat, source_url, timestamp, tags[], note, captureMode, bounds, profile_host, page_variant, metadata, summary, source_name }`)
- Indexes: `by_timestamp`, `by_source_url`

**Stored data classification:** SUBSTANTIAL user content — captured Bible passages with profile metadata (BibleGateway / BLB / BibleHub interlinear). **No secrets, no PII fields, no API keys** — true zero-cloud extension.

**Downloads:** `chrome.downloads.download` for Markdown export via Base64 data URI per RULE-002. Includes per-capture `view_source` frontmatter for traceability.

---

## III. Data Exit Points

### III.1 Fleet exit-point table

| Extension | `fetch()` count | Hardcoded exit URL(s) | BYOK / bundled / none | User content in payload? |
|---|---|---|---|---|
| `864z-chronicle` | 0 | (none) | NONE | NO — local IndexedDB only |
| `Bible-Insight` | ~8 | `https://generativelanguage.googleapis.com/v1beta/...` | BYOK (operator-supplied Gemini key) | YES — full captured page text up to `AI_CONFIG.MAX_CONTENT_CHARS` per call |
| `clipboard` | ~12 | `https://generativelanguage.googleapis.com/...` (Gemini) + `https://api.anthropic.com/v1/messages` (Claude) + Google Drive API + `https://oauth2.googleapis.com/...` + `https://www.googleapis.com/oauth2/v2/userinfo` + `https://accounts.google.com/o/oauth2/auth` (OAuth) + `https://extensionpay.com` (ExtPay payments) | BYOK for AI; OAuth for Drive | YES for AI (clip content, post-redaction); YES for Drive (backup of entire `clips`/`tags`/`clip_tags` IDB) |
| `migration-pilot` | 0 | (none) | NONE | NO — local IndexedDB + filesystem export only |
| `scripture-scout` | 0 | (none) | NONE | NO — local IndexedDB + filesystem export only |
| `TabVault` | ~6 (in `lib/google-drive/drive-client.js`, wired via `options/options.js`) | Google Drive API + OAuth + userinfo | OAuth (operator's own Google account) | YES — vaulted tab metadata (URL, title, favicon, group) backed up to operator's Drive `appdata` folder |
| `Signal2Noise` | 0 | (none) | NONE | NO — local `chrome.storage.local` only |
| `Time2Focus` | 0 | (none) | NONE | NO |
| `TuneOut2FocusIn` | 0 | (none) | NONE | NO |
| `oia-focus-note` | 0 | (none) | NONE | NO |
| `oia-focus-timer` | 0 | (none) | NONE | NO |
| `oia-focus-wall` | 0 | (none) | NONE | NO |
| `oia.focus.signal` | 0 | (none) | NONE | NO |
| `oia.focus.sound` | 0 | (none) | NONE | NO |
| `who-is-watching` | 0 (own code) | (none — D3 lib has fetch references in third-party min.js but is never invoked) | NONE | NO — captures travel only via `chrome.runtime.sendMessage` to extension's own SW |

### III.2 Risk classification per provider host

| Provider host | Touched by | Auth pattern | Sovereignty class |
|---|---|---|---|
| `generativelanguage.googleapis.com` (Gemini) | Bible-Insight, clipboard | `?key=` query param (BYOK) | **DIRECT** — operator-controlled key, no 864zeros relay |
| `api.anthropic.com` (Claude Messages) | clipboard | `x-api-key` header + `dangerously-allow-browser: true` (BYOK) | **DIRECT** — operator-controlled key, no 864zeros relay |
| `www.googleapis.com/drive/v3` (Drive) | clipboard, TabVault | `Authorization: Bearer {token}` (OAuth `drive.appdata`) | **DIRECT** — token in operator's Google account scope; data lands in operator's hidden app folder |
| `accounts.google.com/o/oauth2` | clipboard, TabVault | OAuth implicit flow via `chrome.identity.launchWebAuthFlow` | **DIRECT** — operator-controlled flow |
| `oauth2.googleapis.com` (revoke + userinfo) | clipboard, TabVault | Bearer token | **DIRECT** |
| `extensionpay.com` | clipboard | postMessage origin gate | **THIRD-PARTY** — payment processor; sees ExtPay user_id (synthetic) and email if user provides at checkout |
| `clipboard-864z.864zeros.workers.dev` (Cloudflare Worker proxy) | **NONE — dead code** in `clipboard/lib/ai/ai-client.js` (NOT imported by SW) | (would be unauthenticated POST) | **N/A** — present in source tree but not wired |

### III.3 Critical: the dead-code 864zeros AI proxy

**Location:** `clipboard/lib/ai/ai-client.js`
**Constant:** `const WORKER_URL = 'https://clipboard-864z.864zeros.workers.dev';`
**Status:** UNUSED — the active SW `background/service-worker.js` line 9 imports from `lib/api-client.js` (BYOK direct), NOT from `lib/ai/ai-client.js` (proxy).
**Risk if accidentally re-wired:** Would route all clipboard AI calls through 864zeros-controlled infrastructure → **direct RULE-007 §1 violation** ("zero proxy through 864zeros-owned servers").
**Documentation drift:** `clipboard/README.md` (lines 106-110, 161-168) STILL describes the worker-proxy architecture — describes a path that the code no longer follows. Documentation lies.

---

## IV. PII Pattern Findings

### IV.1 Email handling

| Location | Source | Disposition |
|---|---|---|
| `clipboard/lib/google-drive/drive-client.js` line 67 | `userInfo.email` from `https://www.googleapis.com/oauth2/v2/userinfo` | Stored in `chrome.storage.local` as `drive_user_email`; displayed in Options "Connected as ..." UI; never transmitted by extension |
| `TabVault/lib/google-drive/drive-client.js` line 67 | Same pattern | Same disposition |
| `clipboard/lib/payments/extpay-wrapper.js` line 62 | Hardcoded `email: 'dev@864zeros.com'` in dev/test stub | Dev fixture — only fires in non-prod test path. Document as "Operator should verify this dev email is unreachable in prod build." |
| `clipboard/lib/redactor.js` (referenced by tests) | Pattern-strips emails from content **before** AI call | Defense-in-depth: even though BYOK (data only goes to Gemini/Claude under operator's own key), email patterns are removed pre-redaction |

### IV.2 Token / Authorization headers

All `Authorization: Bearer {token}` and `x-api-key: {token}` references appear in:
- `clipboard/lib/google-drive/drive-client.js` (Drive OAuth Bearer) — RULE-007 compliant (operator's token)
- `TabVault/lib/google-drive/drive-client.js` (same)
- `clipboard/lib/api-client.js` line 212 (`x-api-key: config.apiKey` for Claude) — RULE-007 compliant (operator's BYOK key)
- `Bible-Insight/js/lib/api.js` (Gemini `?key=` URL param — also BYOK)

**No hardcoded tokens, no bundled API keys, no shared secrets.** Confirmed across all 15 extensions.

### IV.3 User-generated content in transit

| Extension | What's transmitted | To where | Encryption | User control |
|---|---|---|---|---|
| `Bible-Insight` | Full captured page text (truncated to `AI_CONFIG.MAX_CONTENT_CHARS`, then sent verbatim) — for "key points", "themes", "verse detection", "verse lookup", "image analysis" | `generativelanguage.googleapis.com` | TLS | Per-call — user invokes from sidepanel; can disable cloudAssist; token usage visible in Options |
| `clipboard` | Clip content (post-`redact()`), images (base64, no redaction), synthesis multi-clip combined content | Gemini OR Claude (operator-selected) | TLS | Per-call — invoked from sidepanel; tier-gated; "ai-summary"/"ai-vision"/"ai-auto-tag"/"synthesize-clips" feature gates |
| `clipboard` (Drive) | **Entire IndexedDB** as JSON backup (clips + tags + clip_tags) | `googleapis.com/upload/drive/v3` (operator's `appdata` folder) | TLS | User must connect via OAuth; can disable auto-sync; max 5 backups retained |
| `TabVault` (Drive) | Vaulted tab metadata (URL, title, favicon, group) as JSON backup | Same | TLS | Same opt-in pattern |
| `864z-chronicle` | **NOTHING transmitted** — DOM-scraped conversations stay in local IndexedDB | (n/a) | (n/a) | N/A — no exit point |
| `who-is-watching` | **NOTHING transmitted** — observed network identities stay in local IndexedDB | (n/a) | (n/a) | N/A |

### IV.4 PII patterns inside captured user content

**Critical observation:** When the user clips a page that itself contains an email address, name, phone number, or token:

- **Bible-Insight**: NO redactor present. Full content goes to Gemini.
- **clipboard**: `lib/redactor.js` strips emails / phones / SSN-like patterns BEFORE AI calls. Drive backups, however, are stored verbatim (no redaction on backup path) — user content goes to Drive in plaintext (TLS-protected to Drive only).
- **864z-chronicle**: User-AI conversations may contain anything — full content captured to local IDB. Since nothing leaves the device, no transit risk.
- **migration-pilot, scripture-scout**: User content stays local; Markdown exports go to user's filesystem.

---

## V. AI Provider Risk Assessment

### V.1 AI-touching extensions

Three of 15 extensions touch AI providers:

| Extension | Provider(s) | Key model | Prompt content |
|---|---|---|---|
| `Bible-Insight` | Google Gemini (`gemini-1.5-*` per `AI_CONFIG.GEMINI_MODEL`) | BYOK (operator's free-tier or paid Gemini key) | Full captured page text + AI-instruction prompt; image base64 + vision instruction; verse-reference + translation request |
| `clipboard` | Google Gemini OR Anthropic Claude (per `config.provider`) | BYOK (operator's key, stored in `chrome.storage.local` as `${APP_SLUG}_ai_api_key`) | Clip content (post-`redact()`) + instruction; image base64 + instruction; multi-clip synthesis (combined truncated content) |
| `864z-chronicle` | NONE — only PASSIVELY READS AI conversation surfaces (gemini.google.com, claude.ai, chatgpt.com, aistudio.google.com, chat.openai.com) | n/a | n/a — no AI calls; only DOM scraping of user's own conversations |

### V.2 RULE-007 compliance per AI-touching extension

| Extension | BYOK? | Bundled key? | 864zeros proxy? | `.sync` storage? | Disclosure in Options? | RULE-007 verdict |
|---|---|---|---|---|---|---|
| `Bible-Insight` | YES | NO | NO | NO (`.local` only) | Settings page exposes API key field; no plain-English secret disclosure section observed | **MOSTLY COMPLIANT** — missing the "plain-English secret-handling disclosure" mandated by RULE-007 §Operations |
| `clipboard` | YES (active path via `lib/api-client.js`) | NO | NO (active path) — but **dead code at `lib/ai/ai-client.js` references `clipboard-864z.864zeros.workers.dev`** | NO | Options shows masked API key + tier + status; README still describes the proxy architecture (drift) | **COMPLIANT in shipping code; AT RISK of regression** if `ai-client.js` is ever re-imported |
| `864z-chronicle` | n/a | n/a | n/a | n/a | n/a | **N/A** — does not touch AI providers in the BYOK sense (DOM scrape only) |

### V.3 Response handling

- **Bible-Insight**: AI responses are stored in IndexedDB as `generated_analysis` items associated with their parent contentItem; displayed in sidepanel; written to PDF reports if generated.
- **clipboard**: AI responses stored on the source clip's `summary` field; synthesis output displayed in the InsightForge UI and stored in the synthesis history.
- Both implement token-usage tracking visible in Options (per-session counters, no upstream telemetry).

### V.4 Prompt-injection / data-leak vectors

- **Bible-Insight `analyzeImage`**: User-supplied images (screenshots) sent base64 to Gemini Vision. If the screenshot contains visible PII (e.g., a screenshot of an email inbox), that PII reaches Gemini. **No image-content redaction layer exists.**
- **clipboard `analyzeImage`**: Same pattern — base64 image to Gemini Vision (or Claude vision when configured). Same image-PII exposure.
- **clipboard `synthesizeClips` "research-dossier" template**: Combines content from up to N clips, sends as one prompt with source URLs and titles in clear text. URL itself can be a leak vector if the URL contains tokens, session IDs, or PII path components (common on auth'd dashboards).

---

## VI. The Risk Gap — "If user clears cache today"

### VI.1 Durability primer

| Browser data class | Survives `Clear cache` (cache only) | Survives `Clear all site data` | Survives device wipe |
|---|---|---|---|
| `chrome.storage.local` | YES | NO (cleared with extension data) | NO |
| `chrome.storage.sync` | YES | NO (locally) but RESTORED on next sign-in via Google account | depends on Google account |
| `indexedDB` | YES | NO (cleared with site/extension data) | NO |
| `localStorage` / `sessionStorage` | YES (cache) / NO (sessionStorage anyway) | NO | NO |
| Files in `~/Downloads/` via `chrome.downloads.download` | YES | YES (operator filesystem) | depends on disk persistence |

**Key insight:** "Clear cache" is **NOT destructive** for any 864zeros extension. The destructive operation users mistakenly conflate with "clear cache" is **`Settings → Reset and clean up → Reset settings`** or **per-extension uninstall**, both of which wipe `chrome.storage.local` AND `indexedDB`.

### VI.2 Per-extension cache-clear durability

| Extension | What's lost on cache-clear | What's lost on full extension wipe | Loss-blast-radius |
|---|---|---|---|
| `864z-chronicle` | NOTHING (cache-only) | Entire `chronicle` IndexedDB (all conversation captures from gemini/claude/chatgpt/aistudio) | **CATASTROPHIC** — irreplaceable AI conversation history |
| `Bible-Insight` | NOTHING | `chrome.storage.local` (settings + Gemini API key) + `bibleinsight` IDB (all captures, tags, AI analyses); PDFs in Downloads survive | **CATASTROPHIC** — sermon notes, theological research, verse cross-references, generated study reports |
| `clipboard` | NOTHING | `chrome.storage.local` (API key + Drive token + tier) + `clipboard` IDB (clips + screenshots + PDFs); Drive backups survive on Drive (operator must Restore) | **SUBSTANTIAL → CATASTROPHIC depending on Drive-sync state** |
| `migration-pilot` | NOTHING | `migration-pilot` IDB; Markdown exports in Downloads survive | **SUBSTANTIAL → TRIVIAL if user has Liberated** (the entire product premise) |
| `scripture-scout` | NOTHING | `scripture-scout` IDB; Markdown exports in Downloads survive | **SUBSTANTIAL → TRIVIAL if Liberated** |
| `TabVault` | NOTHING | `tabvault` IDB (vaulted tab metadata); Drive backups survive on operator's Drive | **SUBSTANTIAL → TRIVIAL if Drive-sync enabled** |
| `Signal2Noise` | NOTHING | `signals[]` array (≤ 10 daily signals + ratio) | **TRIVIAL** — small daily-rebuild surface |
| `Time2Focus` | NOTHING | Last timer state + focus topic + sound prefs | **NONE** — no user content beyond preferences |
| `TuneOut2FocusIn` | NOTHING | Settings | **NONE** |
| `oia-focus-note` | NOTHING | `notes[]` array | **TRIVIAL** |
| `oia-focus-timer` | NOTHING | timer state + last focus text | **NONE** |
| `oia-focus-wall` | NOTHING | `notes[]` array | **TRIVIAL** |
| `oia.focus.signal` | NOTHING | `signals[]` + ratio | **TRIVIAL** |
| `oia.focus.sound` | NOTHING | sound prefs | **NONE** |
| `who-is-watching` | NOTHING | `whoiswatching` IDB (observed identities + events from active session) | **TRIVIAL** — re-observable on next page load |

### VI.3 Headline finding

The user's mental model "if I clear my cache I'll lose my AI conversation history" is **WRONG** — Chronicle's IndexedDB survives cache-clear. The model that's RIGHT is "if I uninstall the extension or run `Clear all site data` for the extension, I lose **everything irreplaceable**."

The four extensions where loss is CATASTROPHIC under "full wipe" are: **864z-chronicle, Bible-Insight, clipboard, migration-pilot** — and three of these (Bible-Insight, clipboard, migration-pilot) have a Liberation/export path the user can pre-emptively run. Chronicle does NOT — it has no Liberate-to-Markdown action yet (loss is unrecoverable).

---

## VII. The Risk Gap — "If they use AI today"

### VII.1 Per-AI-touching-extension leak class

| Extension | Provider endpoint | 864zeros relay? | Prompt content leaked | User opted in? | User can audit before send? | Leak class |
|---|---|---|---|---|---|---|
| `Bible-Insight` (analyze text) | `generativelanguage.googleapis.com/.../generateContent?key={BYOK}` | NO | Full captured page text up to `MAX_CONTENT_CHARS` + the system prompt | YES (user invoked from sidepanel) | NO — content is sent verbatim with no preview gate | **FULL-CAPTURE** of the captured item |
| `Bible-Insight` (analyze image) | Same Gemini Vision | NO | Base64 image + analysis prompt | YES | NO preview gate | **FULL-CAPTURE** of the image (any visible PII included) |
| `Bible-Insight` (verse lookup) | Same | NO | Just the verse reference (e.g., "John 3:16") + translation code | YES | YES — reference is small + visible | **METADATA-ONLY** |
| `Bible-Insight` (cross-refs) | Same | NO | Just the verse reference | YES | YES | **METADATA-ONLY** |
| `Bible-Insight` (semantic verse detection) | Same | NO | Up to 10000 chars of text + detection prompt | YES | NO preview gate | **FULL-CAPTURE** (text only, no images) |
| `clipboard` (summarize) | Gemini OR Claude (BYOK direct) | NO | Clip content **post-`redact()`** (emails/phones/SSN-like patterns stripped) + summarization instruction | YES (tier-gated; user invoked) | NO preview gate but redactor reduces PII | **SELECTED-CONTENT** (defense-in-depth via redactor) |
| `clipboard` (auto-tag) | Same | NO | First 500 chars of clip (post-redact) + tag-suggestion instruction | YES | NO preview gate | **SELECTED-CONTENT** |
| `clipboard` (analyze image) | Same | NO | Base64 image + vision instruction (no image redaction layer) | YES | NO preview gate | **FULL-CAPTURE** of image |
| `clipboard` (synthesize "quick-summary") | Same | NO | Up to 500 chars per clip × N clips, post-redact, + synthesis instruction | YES (tier+credit-gated) | NO preview gate | **SELECTED-CONTENT** |
| `clipboard` (synthesize "research-dossier") | Same | NO | Up to 1500 chars per clip × N clips + source URLs + titles + synthesis instruction. **Source URL leak risk** if URLs contain tokens / PII paths | YES | NO preview gate | **FULL-CAPTURE** (and notable URL exposure) |
| `864z-chronicle` | (none — DOM scrape only) | n/a | (none transmitted by extension; the conversation already exists at the AI provider — it's the user's own session) | n/a | n/a | **NONE** — extension has no AI exit point |

### VII.2 Headline finding

**No 864zeros extension routes user content through 864zeros-owned infrastructure when the user invokes AI.** Every AI call is BYOK direct-to-provider. RULE-007 §1 ("zero proxy through 864zeros-owned servers") is satisfied in the SHIPPING CODE.

The leak class for AI-using extensions is therefore:

- **Worst case:** SELECTED-CONTENT or FULL-CAPTURE → the user's chosen AI provider, under the user's own API key, billed to the user. The provider sees the data per its own ToS — but 864zeros never does.
- **Best case (Bible-Insight verse lookup, cross-refs):** METADATA-ONLY — only the reference string transits.

The single material disclosure gap: **neither Bible-Insight nor clipboard has a per-call "preview the prompt before sending" gate.** Once the user clicks "Summarize", the content is in flight. RULE-007 §Operational hygiene calls for "user can audit / disable / inspect the call before it happens" — partially satisfied (per-feature toggles, tier gates, "ask each time" mode in Bible-Insight) but no per-call preview.

---

## VIII. Per-Extension Sovereign Score

Score key:
- **Durability**: NONE / TRIVIAL / SUBSTANTIAL / CATASTROPHIC (loss on full wipe)
- **Leak**: NONE / METADATA-ONLY / SELECTED-CONTENT / FULL-CAPTURE / UNKNOWN (worst case AI use)
- **RULE-007 score**: 0–10 (10 = perfect compliance + disclosure)

| # | Extension | Durability | Leak | RULE-007 score | Notes |
|---|---|---|---|---|---|
| 1 | `864z-chronicle` | CATASTROPHIC | NONE | 10/10 (no AI exit point) | Local-only; no Liberate path yet (recovery gap) |
| 2 | `Bible-Insight` | CATASTROPHIC | FULL-CAPTURE | 7/10 | BYOK ✓ no proxy ✓; missing plain-English secret disclosure; no per-call prompt preview |
| 3 | `clipboard` | SUBSTANTIAL→CATASTROPHIC | FULL-CAPTURE (images) / SELECTED-CONTENT (text) | 7/10 | Active path BYOK ✓; **dead-code proxy at risk**; redactor present; README drift |
| 4 | `migration-pilot` | SUBSTANTIAL→TRIVIAL | NONE | 10/10 | Reference impl; no AI; pure local→filesystem |
| 5 | `scripture-scout` | SUBSTANTIAL→TRIVIAL | NONE | 10/10 | Reference impl; no AI; pure local→filesystem |
| 6 | `TabVault` | SUBSTANTIAL→TRIVIAL | NONE (no AI) | 9/10 | Drive OAuth (operator's account, `appdata` scope); placeholder client_id `YOUR_CLIENT_ID` in manifest |
| 7 | `Signal2Noise` | TRIVIAL | NONE | 10/10 | |
| 8 | `Time2Focus` | NONE | NONE | 10/10 | |
| 9 | `TuneOut2FocusIn` | NONE | NONE | 10/10 | |
| 10 | `oia-focus-note` | TRIVIAL | NONE | 10/10 | |
| 11 | `oia-focus-timer` | NONE | NONE | 10/10 | |
| 12 | `oia-focus-wall` | TRIVIAL | NONE | 10/10 | |
| 13 | `oia.focus.signal` | TRIVIAL | NONE | 10/10 | |
| 14 | `oia.focus.sound` | NONE | NONE | 10/10 | |
| 15 | `who-is-watching` | TRIVIAL | NONE | 10/10 | Observes identities; never exfiltrates. Has `webRequest` + `declarativeNetRequest` — must monitor for future expansion. |

**Fleet RULE-007 average: 9.4 / 10.** No bundled secrets. No `.sync` for secrets. No active proxy. Two extensions have minor disclosure gaps; one has a dead-code regression risk.

---

## IX. Critical Findings

### IX.1 P0 — Chronicle has no Liberation path

**Severity:** Highest blast radius across the fleet.
**What:** `864z-chronicle` captures the user's entire AI conversation history (every conversation on Gemini, Claude, ChatGPT, AI Studio) into IndexedDB. There is currently NO `chrome.downloads.download` invocation, NO export action, NO Markdown-Liberate flow. `service-worker.js` has a `CLEAR_ALL` handler but no export handler.
**Implication:** A user who uninstalls Chronicle, runs "Clear all site data" for the extension, or has Chrome corruption events loses 100% of captured AI history with zero recovery surface.
**Remediation:** Port the BRK-DL-001 Base64 data URI download brick + RULE-002 SW download pattern into Chronicle. Add a `LIBERATE_TO_MARKDOWN` message handler. Estimated 1–2 hours.

### IX.2 P0 — clipboard's dead-code proxy

**Severity:** Documentation drift + regression-risk.
**What:** `clipboard/lib/ai/ai-client.js` contains a Cloudflare Worker proxy URL pointing at `clipboard-864z.864zeros.workers.dev`. This file is no longer imported (the SW imports `lib/api-client.js` instead — BYOK direct). The README still describes the proxy architecture as if it were live (lines 106-110, 161-168 of `clipboard/README.md`).
**Implication:** A future contributor reading the README and re-importing `ai-client.js` would silently re-introduce a RULE-007 §1 violation — every clipboard AI call would route through 864zeros infrastructure.
**Remediation (choose one):** Delete `lib/ai/ai-client.js` and update README; OR rename to `_legacy-proxy/` with a banner; OR convert the file to a thrown-error stub. Estimated 15 min.

### IX.3 P1 — Bible-Insight + clipboard missing per-call prompt preview

**Severity:** Disclosure / consent quality.
**What:** When the user clicks "Summarize" / "Get key points" / "Detect verses" / "Synthesize", the call fires immediately. Content reaches the AI provider with no prompt-preview / cancel gate.
**Implication:** Soft RULE-007 §"user can audit / disable / inspect the call before it happens" miss. Compliant in spirit (BYOK, no relay) but not in letter (no inspection surface).
**Remediation:** Add a one-time-per-session "First AI call this session: preview prompt? [Send / Cancel]" gate with a "don't ask again" toggle. Estimated 2–3 hours per extension.

### IX.4 P1 — Bible-Insight + clipboard missing plain-English secret disclosure

**Severity:** RULE-007 §Operations soft non-compliance.
**What:** RULE-007 mandates "plain-English secret-handling disclosure required in Options." Both extensions show the API key field and a status label ("API key configured" / "No API key configured") — but neither has a clearly authored "Where this key lives, what it does, what we never do with it" disclosure block.
**Implication:** The Founding 100 trust gate explicitly rests on this disclosure. Without it, ScriptureScout's pre-launch claim "we never see your data" is asserted by behavior but not by visible commitment.
**Remediation:** Author a 4-bullet "About your AI key" block for each Options page:
  1. Stored in `chrome.storage.local` on this device only.
  2. Sent only to {provider} when you invoke AI features.
  3. Never transmitted to 864zeros servers (we don't have any AI servers).
  4. Removable: clear it here, or uninstall the extension to wipe entirely.
  Estimated 1 hour total.

### IX.5 P1 — TabVault placeholder OAuth `client_id`

**Severity:** Manifest hygiene + non-functional Drive sync until fixed.
**What:** `TabVault/manifest.json` declares `oauth2.client_id: "YOUR_CLIENT_ID.apps.googleusercontent.com"`. The Drive client wiring in `options/options.js` calls `initDrive(clientId)`.
**Implication:** Drive sync feature is non-functional in this build. Risk: operator ships the extension and Drive sync silently fails with auth errors.
**Remediation:** Operator-action — provision a Google OAuth 2.0 client_id (TabVault's own, NOT clipboard's) and replace the placeholder. Estimated 30 min including verification.

### IX.6 P2 — Bible-Insight has no content redaction

**Severity:** Defense-in-depth gap relative to clipboard.
**What:** `clipboard/lib/redactor.js` strips emails / phones / SSN-like patterns before AI calls. `Bible-Insight/js/lib/api.js` does not — sends content verbatim to Gemini.
**Implication:** If a user clips a page that contains PII, that PII reaches Gemini. This is operator-controlled (BYOK, user's own Gemini account) but is a defense-in-depth miss.
**Remediation:** Promote `clipboard/lib/redactor.js` to `864z-build-kit/templates/bricks/redactor-v1.js` (BRK-AI-002 candidate). Import in Bible-Insight. Estimated 1 hour.

### IX.7 P2 — clipboard Drive backup is plaintext content

**Severity:** Drive blast-radius beyond AI redaction.
**What:** clipboard's Drive sync uploads the entire `clips` IndexedDB store as JSON, including full clip content (which DID get redacted on AI calls but is NOT redacted on Drive backup). Backup is in operator's `appdata` folder.
**Implication:** If the operator's Google account is compromised, full clipboard history is exposed. (Still operator-scoped — never seen by 864zeros.) Compliance question: should backups themselves be optionally redacted or client-side-encrypted?
**Remediation:** Defer to product decision. If yes, add an Options toggle "Encrypt backups with passphrase (cannot recover if forgotten)" using `crypto.subtle`.

### IX.8 P3 — `who-is-watching` carries `webRequest` + `declarativeNetRequest`

**Severity:** Future-proofing.
**What:** The extension currently OBSERVES tracker traffic and reports to local IndexedDB. The `declarativeNetRequest` permission also enables BLOCKING. Today no rules are loaded that would exfiltrate data anywhere.
**Implication:** Any future feature that uses `chrome.declarativeNetRequest.updateDynamicRules` to redirect requests, or `chrome.webRequest.onBeforeRequest` to mirror payloads, is one PR away from becoming a sovereignty regression.
**Remediation:** Add a CLAUDE.md guard rail to the `who-is-watching/` directory: "This extension OBSERVES — never EXFILTRATES. Any new fetch / webRequest mirror / DNR redirect rule requires 864z-OA sign-off per RULE-000." Estimated 15 min.

---

## X. Recommendations (priority-ordered)

| Priority | Action | Owner | Estimate |
|---|---|---|---|
| **P0** | Add Chronicle Liberate-to-Markdown export (BRK-DL-001 + RULE-002) | 864z-OA → eng | 1–2 h |
| **P0** | Resolve clipboard `lib/ai/ai-client.js` dead code; sync README to BYOK reality | 864z-OA → eng | 15 min |
| **P1** | Author "About your AI key" plain-English disclosure for Bible-Insight + clipboard Options | 864z-OA → studio | 1 h |
| **P1** | Promote `clipboard/lib/redactor.js` → build-kit brick (BRK-AI-002 candidate); import into Bible-Insight | 864z-OA → eng | 1 h + harvest |
| **P1** | Add per-call AI prompt-preview gate to Bible-Insight + clipboard (one-time-per-session) | 864z-OA → eng | 2–3 h × 2 |
| **P1** | Operator-action: provision real OAuth `client_id` for TabVault | Operator | 30 min |
| **P2** | Add `who-is-watching/CLAUDE.md` exfiltration-guardrail | 864z-OA | 15 min |
| **P2** | Codify a fleet-wide "no per-call URL with embedded auth" linter for synthesize-style multi-clip flows | 864z-OA → eng | 2 h |
| **P3** | Defer: optional encrypted Drive backup for clipboard (UX product decision) | Product / 864z-OA | TBD |
| **P3** | Add a CI check that scans for `chrome.storage.sync` writes anywhere a secret-shaped value lives (regex on key names like `*key*`, `*token*`, `*secret*`) | Eng | 1 h |

---

## XI. Cross-References

- [`864z-build-kit/references/core/BUILD_KIT_RULES.md`](../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md) — RULE-000 (Governance), RULE-001 (Options), RULE-002 (SW Download), RULE-007 (Secret Sovereignty), RULE-008 (Markdown Standard) all governing this report.
- [`ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md`](../ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md) — Authoritative log; this audit is recorded as `2026-05-09T-SOVEREIGN-AUDIT-STRIKE`.
- [`ISD-DIV-6-KNOWLEDGE/864zeros_TECH_STACK_AUDIT.md`](864zeros_TECH_STACK_AUDIT.md) — Manifest-level taxonomy; this Sovereign Gap Report is its source-code-level companion.
- [`ISD-DIV-0-CORE/SECURITY_ROTATION_LOG.md`](../ISD-DIV-0-CORE/SECURITY_ROTATION_LOG.md) — Operator credential rotation ledger; this report does not log keys; it audits how extensions handle them.
- [`ISD-DIV-0-CORE/BRICK_REGISTRY.json`](../ISD-DIV-0-CORE/BRICK_REGISTRY.json) — BRK-DL-001 + BRK-AI-001 referenced in remediations.

## XII. Versioning

| Version | Date | Change | Author |
|---|---|---|---|
| v1.0 | 2026-05-09 | Initial report — full 15-extension audit across 4 dimensions | 864z-OA |

**Re-audit triggers** (any of):
- Any extension's `service-worker.js` or `background.js` SHA changes by ≥ 50 lines.
- Any new `fetch()` call introduced.
- Any new `chrome.storage.sync` write introduced.
- Any new external host added to `host_permissions`.
- A new RULE codified in BUILD_KIT_RULES.md that touches secret-handling or data-exit semantics.

---

*864zeros Sovereign Gap Report v1.0 · 2026-05-09 · 864zeros LLC · DIV-6-KNOWLEDGE.*
