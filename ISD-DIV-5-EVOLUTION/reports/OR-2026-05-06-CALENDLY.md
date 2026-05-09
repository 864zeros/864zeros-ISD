---
or_id: OR-2026-05-06-CALENDLY
or_type: full_scan
or_version: 1.1
generated_at: "2026-05-07T10:13:56"
target: Calendly
codename: unspecified
scan_timestamp: "2026-05-06T21:06:48.457052"
scan_mode: live
verdict: TERMINATED
verdict_gate: scarcity
vulture_score: 0.0
hypothetical_score_if_gates_bypassed: 7.35
score_threshold: 8.64
scarcity_threshold: 5
scarcity_index: 10
z_convergence: 0.7
z_velocity: 0.5005
z_scarcity: 0.0
rule_of_40: 100.0
exit_multiplier: 1.5
traffic_monthly: 500000
stagnation_months: 18
growth_projection: 15.0
margin_projection: 85.0
pain_signal_count: 61
sentiment_score: 49.84
competitors_count: 10
competitors: [Doodle, Acuity, Cal.com, Calendar, Motion, Schedly, TidyCal, Your Go-To List, Acuity Scheduling Vs, Microsoft Bookings]
noise_count_estimate: 1
real_count_estimate: 9
apify_queries_spent: 15
source_strike_report: "C:\\dev\\864zeros-ISD\\ISD-DIV-5-EVOLUTION\\data_lake\\STRIKE_REPORT_CALENDLY.json"
---

# Operational Record OR-2026-05-06-CALENDLY
## Calendly → unspecified

**Type:** Full-scan retrospective (neutral hub, side-effect-free)
**Verdict:** **TERMINATED** (scarcity)
**Score:** 0.0 (hypothetical if gates bypassed: 7.35)

---

## 1. Inputs

| Parameter | Value | Source |
|---|---|---|
| Target | Calendly | MCMO selection |
| Codename | *unspecified* | MCMO |
| Traffic (monthly) | 500,000 | Operator-supplied |
| Stagnation (months) | 18 | Operator-supplied |
| Growth projection | 15.0% | Operator-supplied |
| Margin projection | 85.0% | Operator-supplied |
| Scan mode | live | Live |
| Scan timestamp | 2026-05-06T21:06:48.457052 | Live scan |

## 2. Captured Signals

| | Count |
|---|---|
| Total pain signals | 61 |
| Pricing friction | 29 |
| Export hostage | 29 |
| Enterprise pain | 3 |
| Average sentiment | 49.84 (lower = more negative) |

## 3. Competitor Landscape (A-6 v2)

**Raw count:** 10
**Estimated real/adjacent:** 9
**Estimated noise:** 1

| Name | Heuristic flag |
|---|---|
| Doodle | unknown |
| Acuity | unknown |
| Cal.com | unknown |
| Calendar | noise |
| Motion | unknown |
| Schedly | unknown |
| TidyCal | unknown |
| Your Go-To List | unknown |
| Acuity Scheduling Vs | unknown |
| Microsoft Bookings | unknown |

> Note: 'noise' flag is heuristic only. 'unknown' = analyst should mark real/adjacent/noise during manual triage.

## 4. Math Breakdown

```
Z-Convergence: 0.7
Z-Velocity:    0.5005
Z-Scarcity:    0.0
Rule of 40:    100.0%   (threshold: 40%)
Exit mult:     1.5x
Base score:    (0.7*0.45 + 0.5005*0.35 + 0.0*0.20) * 10 = 4.9
Final score:   4.9 * 1.5 = 7.35
```

## 5. Verdict

**STRIKE TERMINATED** at gate: **scarcity**.

**Failure reason:** `SCARCITY_EXCEEDED: 10 competitors > 5 threshold`

### Counterfactuals at different scarcity thresholds

- `SCARCITY_THRESHOLD = 3`: scarcity check **FAILS** (10 > 3). Strike still terminates here.
- `SCARCITY_THRESHOLD = 5`: scarcity check **FAILS** (10 > 5). Strike still terminates here.
- `SCARCITY_THRESHOLD = 7`: scarcity check **FAILS** (10 > 7). Strike still terminates here.

## 6. Source Artifacts

- Strike report: `C:\dev\864zeros-ISD\ISD-DIV-5-EVOLUTION\data_lake\STRIKE_REPORT_CALENDLY.json` (read from vulture-nest)
- This OR generated: 2026-05-07T10:13:56
- Generator: `864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py` v1.1

---
*OR generated in neutral hub. No vulture-nest writes performed.*
