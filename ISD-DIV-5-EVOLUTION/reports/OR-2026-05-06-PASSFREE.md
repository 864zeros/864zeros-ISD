---
or_id: OR-2026-05-06-PASSFREE
or_type: full_scan
or_version: 1.1
generated_at: "2026-05-07T10:02:57"
target: LastPass
codename: PassFree
scan_timestamp: "2026-05-06T20:25:31.985253"
scan_mode: live
verdict: TERMINATED
verdict_gate: scarcity
vulture_score: 0.0
hypothetical_score_if_gates_bypassed: 8.03
score_threshold: 8.64
scarcity_threshold: 5
scarcity_index: 6
z_convergence: 0.8
z_velocity: 0.5012
z_scarcity: 0.0
rule_of_40: 110.0
exit_multiplier: 1.5
traffic_monthly: 10000000
stagnation_months: 18
growth_projection: 30.0
margin_projection: 80.0
pain_signal_count: 77
sentiment_score: 49.61
competitors_count: 6
competitors: [Bitwarden, 1Password, KeePass, KeePassXC, Proton Pass, Dashlane]
noise_count_estimate: 0
real_count_estimate: 6
apify_queries_spent: 13
source_strike_report: "C:\\dev\\864zeros-ISD\\ISD-DIV-5-EVOLUTION\\data_lake\\STRIKE_REPORT_LASTPASS.json"
---

# Operational Record OR-2026-05-06-PASSFREE
## LastPass → PassFree

**Type:** Full-scan retrospective (neutral hub, side-effect-free)
**Verdict:** **TERMINATED** (scarcity)
**Score:** 0.0 (hypothetical if gates bypassed: 8.03)

---

## 1. Inputs

| Parameter | Value | Source |
|---|---|---|
| Target | LastPass | MCMO selection |
| Codename | PassFree | MCMO |
| Traffic (monthly) | 10,000,000 | Operator-supplied |
| Stagnation (months) | 18 | Operator-supplied |
| Growth projection | 30.0% | Operator-supplied |
| Margin projection | 80.0% | Operator-supplied |
| Scan mode | live | Live |
| Scan timestamp | 2026-05-06T20:25:31.985253 | Live scan |

## 2. Captured Signals

| | Count |
|---|---|
| Total pain signals | 77 |
| Pricing friction | 28 |
| Export hostage | 36 |
| Enterprise pain | 13 |
| Average sentiment | 49.61 (lower = more negative) |

## 3. Competitor Landscape (A-6 v2)

**Raw count:** 6
**Estimated real/adjacent:** 6
**Estimated noise:** 0

| Name | Heuristic flag |
|---|---|
| Bitwarden | unknown |
| 1Password | unknown |
| KeePass | unknown |
| KeePassXC | unknown |
| Proton Pass | unknown |
| Dashlane | unknown |

> Note: 'noise' flag is heuristic only. 'unknown' = analyst should mark real/adjacent/noise during manual triage.

## 4. Math Breakdown

```
Z-Convergence: 0.8
Z-Velocity:    0.5012
Z-Scarcity:    0.0
Rule of 40:    110.0%   (threshold: 40%)
Exit mult:     1.5x
Base score:    (0.8*0.45 + 0.5012*0.35 + 0.0*0.20) * 10 = 5.35
Final score:   5.35 * 1.5 = 8.03
```

## 5. Verdict

**STRIKE TERMINATED** at gate: **scarcity**.

**Failure reason:** `SCARCITY_EXCEEDED: 6 competitors > 5 threshold`

### Counterfactuals at different scarcity thresholds

- `SCARCITY_THRESHOLD = 3`: scarcity check **FAILS** (6 > 3). Strike still terminates here.
- `SCARCITY_THRESHOLD = 5`: scarcity check **FAILS** (6 > 5). Strike still terminates here.
- `SCARCITY_THRESHOLD = 7`: scarcity check **PASSES** (6 <= 7). Would advance to score gate; FAILS (8.03 < 8.64).

## 6. Source Artifacts

- Strike report: `C:\dev\864zeros-ISD\ISD-DIV-5-EVOLUTION\data_lake\STRIKE_REPORT_LASTPASS.json` (read from vulture-nest)
- This OR generated: 2026-05-07T10:02:57
- Generator: `864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py` v1.1

---
*OR generated in neutral hub. No vulture-nest writes performed.*
