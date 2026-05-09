---
or_id: OR-2026-03-17-PASSVAULT
or_type: historical_record
or_version: 1.1
generated_at: "2026-05-07T10:13:26"
target: Dashlane
codename: PassVault
strike_id: 864z-2026-004
verdict: PASSED
verdict_gate: passed_all_gates
data_source: factory_build_manifest
vulture_score: 9.45
scarcity_index: 2
scarcity_threshold_current: 5
z_convergence: 0.92
z_velocity: 0.88
z_scarcity: 0.78
rule_of_40: 125.0
exit_multiplier: 1.5
traffic_monthly: 1850000
stagnation_months: 24
growth_projection: 35.0
margin_projection: 90.0
pain_signal_count: 6
competitors_count: 2
build_status: STRIKE_INITIATED
competitors: [Bitwarden, KeePassXC]
---

# Operational Record OR-2026-03-17-PASSVAULT
## Dashlane → PassVault (HISTORICAL)

**Type:** Historical reconstruction — no live scan re-run
**Strike ID:** 864z-2026-004
**Verdict:** PASSED (passed_all_gates)
**Score:** 9.45
**Build status:** STRIKE_INITIATED

> **Source notes:** Reconstructed from data_lake/strikes/864z-2026-004.json (validator-format strike record, dated 2026-03-17). Pillar 4 caveat: PassFree (864z-2026-008) targeted same space and was retroactively archived after A-6 audit; PassVault remains separate freemium positioning. Stagnation estimate 24mo from Dashlane's 2022 desktop discontinuation; sentiment not in source.

---

## 1. Strike Profile

| Field | Value |
|---|---|
| Target | Dashlane |
| Codename | PassVault |
| Strike ID | 864z-2026-004 |
| Traffic (monthly) | 1,850,000 |
| Stagnation (months) | 24 |
| Growth projection | 35.0% |
| Margin projection | 90.0% |
| Pain signals | 6 |

## 2. Math Snapshot (from prior validation)

```
Z-Convergence: 0.92
Z-Velocity:    0.88
Z-Scarcity:    0.78
Rule of 40:    125.0%
Exit mult:     1.5x
Final score:   9.45
```

## 3. Competitor Landscape (at strike time)

**Count:** 2

- Bitwarden
- KeePassXC

## 4. Factory State

**Status:** STRIKE_INITIATED
**Phase:** unspecified

Factory artifact: `864zeros-llc/LLC-DIV-3-FACTORY/output/864z-2026-004-passvault/`

## 5. Threshold Counterfactuals (current SCARCITY_THRESHOLD = 5)

- `SCARCITY_THRESHOLD = 3`: scarcity check **PASSES** (2 <= 3)
- `SCARCITY_THRESHOLD = 5`: scarcity check **PASSES** (2 <= 5)
- `SCARCITY_THRESHOLD = 7`: scarcity check **PASSES** (2 <= 7)

## 6. Source Artifacts

- This OR generated: 2026-05-07T10:13:26
- Generator: `report_generator.py` v1.1 — historical mode
- Data provenance: factory_build_manifest

---
*Historical reconstruction. Math values are quoted from original validation; not recomputed in this cycle.*
