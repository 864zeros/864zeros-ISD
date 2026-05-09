---
or_id: OR-2026-05-07-KEYGUARDIAN
or_type: preflight_only
or_version: 1.1
generated_at: "2026-05-07T09:49:11"
target: Gemini API Key Scope
codename: KeyGuardian
sniff_target: GitGuardian
verdict: TERMINATED
verdict_gate: preflight_scarcity
scarcity_index: 10
scarcity_threshold: 5
competitors_count: 10
competitors: [Gitleaks, Appknox, GitHub Advanced Security, Legit Security, BKP365, CAST Application Intelligence, CodeShield, Coverity Static, Devknox, Dynatrace]
real_count_estimate: 10
noise_count_estimate: 0
apify_queries_spent: 3
full_scan_queries_avoided: 12
---

# Operational Record OR-2026-05-07-KEYGUARDIAN
## Gemini API Key Scope → KeyGuardian

**Type:** Pre-flight termination (no full scan)
**Verdict:** **TERMINATED** at pre-flight scarcity sniff
**Cost saved:** ~12 Apify queries vs full scan (~80% reduction on rejected strike)

---

## 1. Inputs

| Parameter | Value |
|---|---|
| Target frame | Gemini API Key Scope |
| Codename | KeyGuardian |
| Sniff target (proxy) | GitGuardian |
| Apify queries spent | 3 |
| Full scan queries skipped | ~12 |

> MCMO note: MCMO substituted GitGuardian as proxy because literal 'Gemini API' returns Claude/OpenAI alternatives (wrong category).

## 2. Pre-flight Competitor Sniff (A-6 v2)

**Raw count:** 10
**Estimated real/adjacent:** 10
**Estimated noise:** 0

| Name | Heuristic flag |
|---|---|
| Gitleaks | unknown |
| Appknox | unknown |
| GitHub Advanced Security | unknown |
| Legit Security | unknown |
| BKP365 | unknown |
| CAST Application Intelligence | unknown |
| CodeShield | unknown |
| Coverity Static | unknown |
| Devknox | unknown |
| Dynatrace | unknown |

## 3. Verdict

**STRIKE TERMINATED** at pre-flight scarcity sniff: **10 competitors > 5 threshold (current SCARCITY_THRESHOLD)**.

No live scan executed. No strike report exists. No validator auto-archive.

### Counterfactuals at different scarcity thresholds

- `SCARCITY_THRESHOLD = 3`: scarcity check **FAILS** (10 > 3)
- `SCARCITY_THRESHOLD = 5`: scarcity check **FAILS** (10 > 5)
- `SCARCITY_THRESHOLD = 7`: scarcity check **FAILS** (10 > 7)

## 4. Source Artifacts

- No strike report (terminated before full scan)
- This OR generated: 2026-05-07T09:49:11
- Generator: `864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py` v1.1

---
*OR generated in neutral hub. No vulture-nest writes performed.*
