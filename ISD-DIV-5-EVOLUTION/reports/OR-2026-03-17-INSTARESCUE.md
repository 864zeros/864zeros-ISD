---
or_id: OR-2026-03-17-INSTARESCUE
or_type: historical_record
or_version: 1.1
generated_at: "2026-05-07T10:13:23"
target: Instapaper
codename: InstaRescue
strike_id: 864z-2026-003
verdict: PASSED
verdict_gate: passed_all_gates
data_source: factory_build_manifest
vulture_score: 9.38
scarcity_index: 3
scarcity_threshold_current: 5
z_convergence: 0.8
z_velocity: 0.53
z_scarcity: 0.4
rule_of_40: 110.0
exit_multiplier: 1.5
traffic_monthly: 1000000
stagnation_months: 21
growth_projection: 25.0
margin_projection: 85.0
pain_signal_count: 18
sentiment_score: 32.0
competitors_count: 3
build_status: STRIKE_QUALIFIED
competitors: [Pocket, Raindrop, Matter]
---

# Operational Record OR-2026-03-17-INSTARESCUE
## Instapaper → InstaRescue (HISTORICAL)

**Type:** Historical reconstruction — no live scan re-run
**Strike ID:** 864z-2026-003
**Verdict:** PASSED (passed_all_gates)
**Score:** 9.38
**Build status:** STRIKE_QUALIFIED

> **Source notes:** Reconstructed from data_lake/strikes/864z-2026-003.json (validator-format strike record, dated 2026-03-17). Original scan ran under SCARCITY_THRESHOLD=3; strike passed at 3 competitors. At current threshold=5, would still pass.

---

## 1. Strike Profile

| Field | Value |
|---|---|
| Target | Instapaper |
| Codename | InstaRescue |
| Strike ID | 864z-2026-003 |
| Traffic (monthly) | 1,000,000 |
| Stagnation (months) | 21 |
| Growth projection | 25.0% |
| Margin projection | 85.0% |
| Pain signals | 18 |
| Sentiment | 32.0 |

## 2. Math Snapshot (from prior validation)

```
Z-Convergence: 0.8
Z-Velocity:    0.53
Z-Scarcity:    0.4
Rule of 40:    110.0%
Exit mult:     1.5x
Final score:   9.38
```

## 3. Competitor Landscape (at strike time)

**Count:** 3

- Pocket
- Raindrop
- Matter

## 4. Factory State

**Status:** STRIKE_QUALIFIED
**Phase:** unspecified

Factory artifact: `864zeros-llc/LLC-DIV-3-FACTORY/output/864z-2026-003-instarescue/`

## 5. Threshold Counterfactuals (current SCARCITY_THRESHOLD = 5)

- `SCARCITY_THRESHOLD = 3`: scarcity check **PASSES** (3 <= 3)
- `SCARCITY_THRESHOLD = 5`: scarcity check **PASSES** (3 <= 5)
- `SCARCITY_THRESHOLD = 7`: scarcity check **PASSES** (3 <= 7)

## 6. Source Artifacts

- This OR generated: 2026-05-07T10:13:23
- Generator: `report_generator.py` v1.1 — historical mode
- Data provenance: factory_build_manifest

---
*Historical reconstruction. Math values are quoted from original validation; not recomputed in this cycle.*
