---
or_id: OR-2026-05-06-SESSION_BUDDY
or_type: full_scan
or_version: 1.1
generated_at: "2026-05-07T10:13:59"
target: Session Buddy
codename: SessionRescue
scan_timestamp: "2026-05-06T21:59:30.377773"
scan_mode: live
verdict: TERMINATED
verdict_gate: scarcity
vulture_score: 0.0
hypothetical_score_if_gates_bypassed: 9.76
score_threshold: 8.64
scarcity_threshold: 5
scarcity_index: 10
z_convergence: 0.9
z_velocity: 0.7017
z_scarcity: 0.0
rule_of_40: 115.0
exit_multiplier: 1.5
traffic_monthly: 1000000
stagnation_months: 36
growth_projection: 25.0
margin_projection: 90.0
pain_signal_count: 44
sentiment_score: 49.43
competitors_count: 10
competitors: [One Tab Group, Webloggle, Dokkio, Linkman, OneTab, Pocket, TabGroup Vault, BEST Private Options, CarryLinks, Diigo]
noise_count_estimate: 0
real_count_estimate: 10
apify_queries_spent: 15
source_strike_report: "C:\\dev\\864zeros-ISD\\ISD-DIV-5-EVOLUTION\\data_lake\\STRIKE_REPORT_SESSION_BUDDY.json"
---

# Operational Record OR-2026-05-06-SESSION_BUDDY
## Session Buddy → SessionRescue

**Type:** Full-scan retrospective (neutral hub, side-effect-free)
**Verdict:** **TERMINATED** (scarcity)
**Score:** 0.0 (hypothetical if gates bypassed: 9.76)

---

## 1. Inputs

| Parameter | Value | Source |
|---|---|---|
| Target | Session Buddy | MCMO selection |
| Codename | SessionRescue | MCMO |
| Traffic (monthly) | 1,000,000 | Operator-supplied |
| Stagnation (months) | 36 | Operator-supplied |
| Growth projection | 25.0% | Operator-supplied |
| Margin projection | 90.0% | Operator-supplied |
| Scan mode | live | Live |
| Scan timestamp | 2026-05-06T21:59:30.377773 | Live scan |

## 2. Captured Signals

| | Count |
|---|---|
| Total pain signals | 44 |
| Pricing friction | 8 |
| Export hostage | 26 |
| Enterprise pain | 10 |
| Average sentiment | 49.43 (lower = more negative) |

## 3. Competitor Landscape (A-6 v2)

**Raw count:** 10
**Estimated real/adjacent:** 10
**Estimated noise:** 0

| Name | Heuristic flag |
|---|---|
| One Tab Group | unknown |
| Webloggle | unknown |
| Dokkio | unknown |
| Linkman | unknown |
| OneTab | unknown |
| Pocket | unknown |
| TabGroup Vault | unknown |
| BEST Private Options | unknown |
| CarryLinks | unknown |
| Diigo | unknown |

> Note: 'noise' flag is heuristic only. 'unknown' = analyst should mark real/adjacent/noise during manual triage.

## 4. Math Breakdown

```
Z-Convergence: 0.9
Z-Velocity:    0.7017
Z-Scarcity:    0.0
Rule of 40:    115.0%   (threshold: 40%)
Exit mult:     1.5x
Base score:    (0.9*0.45 + 0.7017*0.35 + 0.0*0.20) * 10 = 6.51
Final score:   6.51 * 1.5 = 9.76
```

## 5. Verdict

**STRIKE TERMINATED** at gate: **scarcity**.

**Failure reason:** `SCARCITY_EXCEEDED: 10 competitors > 5 threshold`

### Counterfactuals at different scarcity thresholds

- `SCARCITY_THRESHOLD = 3`: scarcity check **FAILS** (10 > 3). Strike still terminates here.
- `SCARCITY_THRESHOLD = 5`: scarcity check **FAILS** (10 > 5). Strike still terminates here.
- `SCARCITY_THRESHOLD = 7`: scarcity check **FAILS** (10 > 7). Strike still terminates here.

## 6. Source Artifacts

- Strike report: `C:\dev\864zeros-ISD\ISD-DIV-5-EVOLUTION\data_lake\STRIKE_REPORT_SESSION_BUDDY.json` (read from vulture-nest)
- This OR generated: 2026-05-07T10:13:59
- Generator: `864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py` v1.1

---
*OR generated in neutral hub. No vulture-nest writes performed.*
