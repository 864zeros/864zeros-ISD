# 864zeros: Glossary [v1.0]

**Authority:** Canonical definitions for 864zeros vocabulary. When a term is defined here, that definition supersedes any informal use elsewhere in the workspace.
**Loaded:** On demand whenever a strike, role doc, audit, or external communication needs to use a defined term precisely.
**Authored:** 2026-05-11 by 864z-OA (Office Architect) per RULE-000 (Strike 030).
**Update protocol:** Append-only entries (alphabetical within §I Defined Terms). New terms get a `### Term Name` heading + definition body + (optional) **Source:** line citing the artifact where it originated. Bumping a definition is a versioning event — append a new §V row.
**Format note:** Follows the `864z-markdown-standard` (RULE-008).

---

## I. Defined Terms

### Local-First

**Data that never touches a server we control.**

Practical implications:
- All persistence happens in `chrome.storage.local` or IndexedDB on the user's device.
- Export paths write to the user's local Downloads folder via `Blob` + `URL.createObjectURL` — never through a 864zeros endpoint.
- Sync, when offered, is BYOA (Bring Your Own Account — e.g., user's own Google Drive OAuth) — not via 864zeros infrastructure.
- BYOK secrets (e.g., user's own Gemini / OpenAI API keys) are stored in `chrome.storage.local` only, per RULE-007.

**Source:** Strike 030 (Operator-supplied definition); reinforces RULE-007 §Sovereignty.

### Trust Vault

**The 864zeros proprietary manual-snapshot system.**

Implementation:
- Canonical library: [`864z-build-kit/references/core/trust-vault.js`](../../864zeros-llc/864z-build-kit/references/core/trust-vault.js) (Strike 028).
- Distributed to all 12 active extensions' `lib/trust-vault.js` (Strike 029).
- Two operations: `exportVault(appName, data)` produces a portable Markdown file with the Founder's Guarantee header + a JSON code-fence body; `importVault()` round-trips the same format with an operator-mandated overwrite warning.
- UI rendered by canonical `lib/options-tier-init.js → injectTrustVaultUI()` into any `<div id="trust-vault-root">` element (Strike 029 — 12/12 fleet parity).

**Source:** Strike 030 (Operator-supplied definition); see Strikes 028 + 029 for implementation history.

---

## II. Forthcoming Terms

The following recurring vocabulary appears across the workspace and may warrant glossary entries in future strikes. Listed without definitions so the operator can author each with the same care as the Strike-030 anchor entries.

- **RULE-007** — codified in `864z-build-kit/references/core/BUILD_KIT_RULES.md`; the sovereignty rule that governs Local-First posture in code.
- **Founder's Guarantee** — the standardized 4-line attestation rendered in every extension's brand-footer ("No Ads. No Tracking. Your data stays yours.") and at the head of every Trust Vault export.
- **BYOK** (Bring Your Own Key) — pattern where the user supplies their own 3rd-party API key (e.g., Gemini, OpenAI); the key is stored locally and never proxied through 864zeros.
- **BYOA** (Bring Your Own Account) — pattern where the user authenticates with their own 3rd-party account (e.g., Google Drive OAuth) for optional cloud features; 864zeros never sees the credentials.
- **Tier-0.5** — the perpetual-unlock pricing tier ($2.99 once) sitting between Free and Pro; spec'd in `extensions/864z-chronicle/TIER_0_5_BLUEPRINT.md`.
- **Active Checkout** — Strike-024 Rung-4 sub-state for an extension that has live ExtPay payment integration (vs. Rung-4-stub).
- **Sovereign Link** — local export path that lets a user "liberate" their data without 864zeros intermediation; named in chronicle's `SOVEREIGN_LINK_PROPOSAL.md`.
- **Sovereign Custody** / **Mandatory Custody** — terms from the Strike-030 `trust-vault-terms.md` legal document; awaiting verbatim definition import from that file.

---

## III. Cross-References

- [`864zeros_FACTORY_MANIFEST.md`](./864zeros_FACTORY_MANIFEST.md) — per-extension Rung + Tier-0.5 status (where many of the terms above are used in context).
- [`../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md`](../../864zeros-llc/864z-build-kit/references/core/BUILD_KIT_RULES.md) — RULE-007 + the other 8 active rules.
- [`../../864zeros-llc/864z-build-kit/references/core/brand-identity.js`](../../864zeros-llc/864z-build-kit/references/core/brand-identity.js) — `BRAND_MISSION` canonical source (Strike 025).
- [`../../864zeros-llc/864z-build-kit/references/core/trust-vault.js`](../../864zeros-llc/864z-build-kit/references/core/trust-vault.js) — Trust Vault library (Strike 028).
- [`../ISD-DIV-5-EVOLUTION/templates/GTM_BUILD_REPORT_TEMPLATE.md`](../ISD-DIV-5-EVOLUTION/templates/GTM_BUILD_REPORT_TEMPLATE.md) — references "Trust Vault Integration Verified" checklist item (Strike 030).
- `864z-build-kit/references/legal/trust-vault-terms.md` *(pending — Strike 030 Task 1 awaiting operator-verbatim text)* — Sovereign Custody Notice + Mandatory Custody Disclaimer.

---

## IV. How to Add a Term

1. Pick a heading: `### Term Name` (PascalCase or Title Case as appropriate; canonical capitalization matters).
2. Body: one short bolded sentence answering "what is it?" followed by 2-5 bullets of practical implications OR pointers to canonical implementation.
3. **Source:** line citing the artifact where the definition originated (operator-supplied vs. drafted-from-code).
4. Insert alphabetically within §I.
5. If the term existed in §II Forthcoming, remove its bullet there.
6. Append a new row to §V Versioning describing the addition.

---

## V. Versioning

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-11 | Initial (Strike 030). Two operator-verbatim entries: **Local-First** ("Data that never touches a server we control") + **Trust Vault** ("The 864zeros proprietary manual-snapshot system"). §II Forthcoming lists 8 recurring terms for future operator-authored definitions. RULE-008 doc-block + cross-refs to Factory Manifest, BUILD_KIT_RULES, brand-identity, trust-vault, GTM_BUILD_REPORT_TEMPLATE, and the pending trust-vault-terms.md. |

---

*864zeros Glossary v1.0 · 2026-05-11 · 864zeros LLC · DIV-6-KNOWLEDGE.*
