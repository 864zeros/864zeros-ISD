---
or_id: OR-2026-05-06-ROAMRESCUE
or_type: full_scan
or_version: 1.1
generated_at: "2026-05-07T10:02:33"
target: Roam Research
codename: RoamRescue
scan_timestamp: "2026-05-06T19:27:14.702459"
scan_mode: live
verdict: PASSED
verdict_gate: passed_all_gates
vulture_score: 11.36
hypothetical_score_if_gates_bypassed: 11.36
score_threshold: 8.64
scarcity_threshold: 5
scarcity_index: 0
z_convergence: 0.8
z_velocity: 0.5643
z_scarcity: 1.0
rule_of_40: 105.0
exit_multiplier: 1.5
traffic_monthly: 1000000
stagnation_months: 24
growth_projection: 25.0
margin_projection: 80.0
pain_signal_count: 45
sentiment_score: 50.78
competitors_count: 0
competitors: []
noise_count_estimate: 0
real_count_estimate: 0
apify_queries_spent: 13
source_strike_report: "C:\\dev\\864zeros-ISD\\ISD-DIV-5-EVOLUTION\\data_lake\\STRIKE_REPORT_ROAM_RESEARCH.json"
---

# Operational Record OR-2026-05-06-ROAMRESCUE
## Roam Research → RoamRescue

**Type:** Full-scan retrospective (neutral hub, side-effect-free)
**Verdict:** **PASSED** (passed_all_gates)
**Score:** 11.36 (hypothetical if gates bypassed: 11.36)

---

## 1. Inputs

| Parameter | Value | Source |
|---|---|---|
| Target | Roam Research | MCMO selection |
| Codename | RoamRescue | MCMO |
| Traffic (monthly) | 1,000,000 | Operator-supplied |
| Stagnation (months) | 24 | Operator-supplied |
| Growth projection | 25.0% | Operator-supplied |
| Margin projection | 80.0% | Operator-supplied |
| Scan mode | live | Live |
| Scan timestamp | 2026-05-06T19:27:14.702459 | Live scan |

## 2. Captured Signals

| | Count |
|---|---|
| Total pain signals | 45 |
| Pricing friction | 13 |
| Export hostage | 25 |
| Enterprise pain | 7 |
| Average sentiment | 50.78 (lower = more negative) |

## 3. Competitor Landscape (A-6 v2)

**Raw count:** 0
**Estimated real/adjacent:** 0
**Estimated noise:** 0

| Name | Heuristic flag |
|---|---|

> Note: 'noise' flag is heuristic only. 'unknown' = analyst should mark real/adjacent/noise during manual triage.

## 4. Math Breakdown

```
Z-Convergence: 0.8
Z-Velocity:    0.5643
Z-Scarcity:    1.0
Rule of 40:    105.0%   (threshold: 40%)
Exit mult:     1.5x
Base score:    (0.8*0.45 + 0.5643*0.35 + 1.0*0.20) * 10 = 7.58
Final score:   7.58 * 1.5 = 11.36
```

## 5. Verdict

**STRIKE QUALIFIED** at gate: **passed_all_gates**.

Strike qualified. See validator output for target_mrr / months_to_exit if generate_strike_package was invoked.

## 6. Source Artifacts

- Strike report: `C:\dev\864zeros-ISD\ISD-DIV-5-EVOLUTION\data_lake\STRIKE_REPORT_ROAM_RESEARCH.json` (read from vulture-nest)
- This OR generated: 2026-05-07T10:02:33
- Generator: `864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py` v1.1

---
*OR generated in neutral hub. No vulture-nest writes performed.*
