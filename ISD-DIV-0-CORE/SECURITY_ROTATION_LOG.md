# 864zeros: Security Rotation Log [v1.0]

**Authority:** Append-only attestation ledger of credential rotations affecting any 864zeros-internal service-account, API-provider key, or infrastructure secret.
**Loaded:** On demand for security audits, compliance review, incident-response provenance reconstruction.
**Authored:** 2026-05-09 by 864z-OA (Office Architect) per RULE-000.
**Update protocol:** Append-only. Never edit prior entries. Rotation events are recorded after the rotation completes (post-condition log, not pre-condition request).
**Format note:** Follows the 864z-markdown-standard (RULE-008).
**Disclosure discipline:** This log records the FACT of rotation, not the secret values themselves. Key prefixes, suffixes, fingerprints, and any partial credential material are intentionally excluded. Per RULE-007 §Compliance Verification — secret values MUST NEVER appear in repository content, including in attestation logs.

---

## I. Purpose & Authority

This log exists to demonstrate continuous compliance with **RULE-007 (Secret Sovereignty)**. RULE-007 mandates that:

1. No 864zeros-owned API key, service-account token, or shared secret is bundled into shipped extension code (the *prohibitive* clause).
2. Internal 864zeros credentials used by non-shipped infrastructure (DIV-1 Vulture-Nest scrapers, internal AI agents, build-kit tooling, etc.) must be rotated on a published cadence and after any suspected exposure event (the *operational hygiene* clause).

This log attests compliance with the second clause. Compliance with the first clause is verified per-extension at release time via the RULE-007 §Compliance Verification checklist.

---

## II. Rotation Cadence

| Trigger | Required action | Time-to-rotate |
|---|---|---|
| Suspected exposure (commit history, public log, screenshot leak, accidental Slack/Discord paste, etc.) | Rotate the implicated key + audit downstream callers | ≤24 hours |
| Quarterly hygiene rotation | All active provider keys rotated in the same window | Once per quarter |
| Operator transition / role change | Rotate any key the departing operator had access to | ≤7 days |
| Vendor-pushed key-format migration (e.g., provider rolls out a new key namespace) | Rotate to new format; revoke old format key | Per vendor deadline |
| Pre-public-launch milestone | All provider keys rotated to a fresh set; the launch cohort never sees a key that pre-dated the cohort | Before public-cohort enrolment opens |

---

## III. Rotation Events

### III.a — `2026-05-09T-Q2-HYGIENE-ROTATION` — Quarterly Hygiene + Pre-Cohort Refresh

**Date:** 2026-05-09
**Trigger:** Quarterly hygiene rotation, coinciding with the Strike-012 Final Cleanup Strike and immediately preceding ScriptureScout Founding 100 cohort enrolment opening.
**Authority:** 864z-OA (Office Architect) under RULE-000 + Operator (jeff.m.conn@gmail.com) attestation.
**Compliance reference:** RULE-007 §Operational hygiene clause.

**Providers rotated:**

| Provider | Service | Used by | Rotation status | Old key revoked? |
|---|---|---|---|---|
| **Anthropic** | Claude API (claude.ai/api) | Internal AI agent tooling, build-kit research scripts, this very Claude Code session | ✅ Rotated | ✅ Old key revoked at provider |
| **OpenAI** | OpenAI API (api.openai.com) | DIV-1 Vulture-Nest enrichment pipeline, fallback AI agent tooling | ✅ Rotated | ✅ Old key revoked at provider |
| **Apify** | Apify Actor + dataset API (api.apify.com) | DIV-1 Vulture-Nest scraper orchestration | ✅ Rotated | ✅ Old key revoked at provider |

**Verification checklist (post-rotation):**

```
[x] New keys provisioned at each provider's dashboard
[x] Local .env files updated on operator workstation (NOT committed — covered by .gitignore additions in this same strike: .env, .env.master, .env.local, *.env, migration-stuff/.env.master)
[x] Old keys revoked at the respective provider dashboards (cannot be silently re-used)
[x] Repository scanned for any historical commit containing key material — clean (per LLC commit 2c22fed "secrets scrubbed" + the .gitignore tightening below)
[x] No bundled key in any shipped extension manifest, source, or build artifact (per RULE-007 §Compliance Verification — verified via grep across all 15 extensions in LLC-DIV-3-FACTORY/extensions/)
[x] No proxy through 864zeros-controlled servers — all rotated keys connect directly from the operator's local environment to the provider's documented endpoint
[x] No telemetry / analytics endpoint receives any of these keys
```

**Disclosure discipline:** No key prefixes, suffixes, fingerprints, or partial values are recorded in this entry. Only the FACT of rotation is logged.

**Operator attestation:** I, the Operator (jeff.m.conn@gmail.com), confirm the above rotations completed on 2026-05-09 prior to this log entry being authored.

**Office Architect attestation:** I, 864z-OA, confirm the rotation events were performed by the Operator and that no rotated key value appears anywhere in the 864zeros-llc or 864zeros-ISD repositories at the time of this entry.

---

## IV. Compliance Posture (Snapshot 2026-05-09)

| Question | Answer | Evidence |
|---|---|---|
| Are any 864zeros-owned credentials bundled in shipped extension code? | **No.** | RULE-007 §Compliance Verification grep across all 15 extension manifests + source files passes. |
| Are user secrets (BYOK API keys for paid providers) stored in `chrome.storage.local`? | **Yes** (in extensions that handle them — `clipboard` is the canonical example). | `extensions/clipboard/options/main.js` — verified. |
| Are user secrets stored in `chrome.storage.sync`? | **No.** | RULE-007 §Required Mechanics explicitly forbids; verified absent. |
| Do any extensions proxy user secrets through 864zeros infrastructure? | **No.** | Network audit during smoke-test cycles confirms zero requests to `*.864zeros.*` hosts when secrets are in play. |
| Are internal credentials (Anthropic/OpenAI/Apify) exposed in any committed file or git history? | **No.** | This rotation cycle + LLC commit `2c22fed` ("secrets scrubbed") + the `.gitignore` hardening committed alongside this log. |
| Is there a published rotation cadence? | **Yes.** | §II of this document. |

---

## V. Cross-References

- [`864z-build-kit/references/core/BUILD_KIT_RULES.md`](../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md) — RULE-007 (Secret Sovereignty) — the rule this log attests compliance with.
- [`ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md`](../ISD-DIV-5-EVOLUTION/reports/SYSTEM_STRIKE_LOG.md) — append-only event ledger; the cleanup strike entry references this rotation.
- [`864zeros-llc/.gitignore`](../../864zeros-llc/.gitignore) — secret-related ignore patterns (`.env`, `.env.master`, `.env.local`, `*.env`, `migration-stuff/.env.master`) added in the same strike as this log.
- [`ISD-DIV-6-KNOWLEDGE/864zeros_TECH_STACK_AUDIT.md`](../ISD-DIV-6-KNOWLEDGE/864zeros_TECH_STACK_AUDIT.md) §IV.g — RULE-007 compliance status per extension.
- [`OR_STRIKE_012_PREFLIGHT.md`](../ISD-DIV-5-EVOLUTION/reports/OR_STRIKE_012_PREFLIGHT.md) §3.2 — Founding-100 trust gate (privacy tier definitions).

---

## VI. Versioning

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-09 | Initial. Logs the 2026-05-09 quarterly hygiene rotation of Anthropic + OpenAI + Apify provider keys. Establishes the rotation-cadence policy + the compliance-posture snapshot template. References RULE-007 (the rule this log attests). |

---

*864zeros Security Rotation Log v1.0 · 2026-05-09 · 864zeros LLC · DIV-0-CORE attestation ledger.*
