# DIV-5 — 4-Report Cross-OR Analysis
## CEO Review Document — 2026-05-07

**Source ORs:**
- `reports/OR-2026-05-06-ROAMRESCUE.md` (success backfill)
- `reports/OR-2026-05-06-LOOM.md` (failure)
- `reports/OR-2026-05-06-PASSFREE.md` (retroactive failure backfill, manually-patched competitors)
- `reports/OR-2026-05-07-KEYGUARDIAN.md` (pre-flight failure)

**Generator:** `report_generator.py` v1.1 (neutral hub)
**Data lake:** `data_lake/STRIKE_REPORT_*.json` (7 files, consolidated this cycle)

---

## 1. THE 4 ORs AT A GLANCE

| | RoamRescue (006) | Loom | PassFree (008 retro) | KeyGuardian |
|---|---|---|---|---|
| **OR_ID** | OR-2026-05-06-ROAMRESCUE | OR-2026-05-06-LOOM | OR-2026-05-06-PASSFREE | OR-2026-05-07-KEYGUARDIAN |
| **OR type** | full_scan | full_scan | full_scan (patched) | preflight_only |
| **Verdict** | **PASSED** ✓ | TERMINATED | TERMINATED | TERMINATED |
| **Gate fired** | passed_all_gates | scarcity | scarcity | preflight_scarcity |
| **Vulture score** | **11.36** | 0.0 | 0.0 | n/a |
| **Hypothetical (gates bypassed)** | 11.36 | **8.38** | **8.03** | n/a (no full scan) |
| **Scarcity index** | 0 | 10 | 6 | 10 |
| **Z-Convergence** | 0.80 | 0.80 | 0.80 | n/a |
| **Z-Velocity** | 0.5643 | 0.5675 | 0.5012 | n/a |
| **Z-Scarcity** | 1.00 (artifact) | 0.0 | 0.0 | n/a |
| **Pain signals** | 45 | 74 | 77 | n/a |
| **Sentiment (lower=worse)** | 50.78 | 49.73 | 49.61 | n/a |
| **Apify spend** | 13 queries | 15 queries | 13 queries | **3 queries** |
| **Workflow** | full live scan | full live scan | full live scan | pre-flight (cost-saving) |
| **Real / noise (heuristic)** | 0 / 0 | 6 / 4 | 6 / 0 (patched) | 10 / 0 |

---

## 2. MATH FINGERPRINT — STRIKING UNIFORMITY

Across all three full-scan ORs (Roam, Loom, PassFree):
- **Z-Convergence = 0.80 in every case.** Same signal-strength tier — pain signals are abundant, weakness is well-articulated, traffic + stagnation get partial credit. The captured-pain pillar is consistent.
- **Z-Velocity ranges 0.50 – 0.57.** Tight band. Velocity isn't the discriminator.
- **Sentiment 49.6 – 50.8** for all four targets. The pain narrative is *negative-leaning but diluted by listicle/marketing content* — same artifact across the board.

**The discriminator is Z-Scarcity.** Roam shows 1.00 (false-positive blue ocean from A-6 v1 era). The other three show 0.0 (≥4 modern competitors). If Roam's true count were the realistic 2–3 (Logseq, Obsidian, Tana), its Z-Scar would be 0.4–0.6 and score would drop to ~9.75 — still passes, but with margin.

**The scoring engine is doing its job consistently.** It's not a math problem. It's a target-availability problem.

---

## 3. THE THRESHOLD=5 REALITY (Option B Test)

`SCARCITY_THRESHOLD` was bumped from 3 → 5 this session per CEO authorization. Did it change any verdicts in this set?

| OR | Scarcity | At threshold=3 | At threshold=5 | At threshold=7 |
|---|---|---|---|---|
| RoamRescue | 0 | PASS | **PASS** | PASS |
| Loom | 10 | FAIL | **FAIL** (still > 5) | FAIL (still > 7) |
| PassFree | 6 | FAIL | **FAIL** (just barely > 5) | PASS scarcity, then FAIL score (8.03 < 8.64) |
| KeyGuardian | 10 | FAIL | **FAIL** | FAIL |

**The threshold=5 change does NOT unlock any of these strikes.** PassFree passes scarcity at threshold=7 but fails the score gate (8.03 < 8.64). Loom and KeyGuardian fail at any threshold up to 9 because they have 10 each.

**Conclusion:** Option B (threshold change) was empirically tested. It correctly recalibrates the gate for current market reality, but it doesn't *retroactively rescue* any of these targets. The markets are genuinely crowded enough that the gate change is calibrational, not unlocking.

---

## 4. WHAT WOULD HAVE TO BE TRUE FOR A STRIKE TO PASS

Reverse-engineering from RoamRescue (the only PASSED), the strike profile that clears the gate looks like:

| Field | RoamRescue value | Required ranges (approximate) |
|---|---|---|
| Pain signals | 45 | ≥ 10 (full Z-Conv credit on pain) |
| Stagnation | 24mo | > 24mo for full Z-Conv credit, > 12mo for half |
| Traffic | 1M | > 500k for full Z-Conv credit |
| Sentiment | 50.78 | < 60 for any Z-Conv credit, < 40 for full |
| **Real competitors** | **2–3 (assumed)** | **≤ 5 to clear current scarcity gate; ≤ 3 to also keep Z-Scar boost** |
| Growth | 25% | growth + margin ≥ 40% for 1.5× exit multiplier |
| Margin | 80% | (same) |

**The bottleneck across all 4 ORs is real competitor count.** Loom (6 real), PassFree (6 real), KeyGuardian (10 real) all violate the ≤5 threshold. Only Roam (assumed 2–3 real) clears it — and Roam was itself only confirmed PASSED because A-6 v1 reported 0 (artifactually inflated Z-Scar).

**If MCMO can find a target with all of:**
- 1M+ traffic (full Z-Conv traffic credit)
- 24+ months stagnation (full Z-Conv stagnation credit)
- 10+ pain signals (full Z-Conv pain credit)
- < 40 sentiment (full Z-Conv sentiment credit; harder than current 50ish baseline)
- ≤ 5 real modern competitors (passes scarcity)
- Growth + margin projections that clear Rule of 40

…then a strike clears 8.64 with comfortable margin. The first four are pillar 1+2+signal data the live scout can capture. The fifth is the sticking point.

---

## 5. NOISE-INFLATED VS REAL COMPETITOR COUNTS

A-6 v2 produces noise. The OR generator's heuristic flags some:

| OR | Raw count | Heuristic noise | Real (CTO assessment from prior dossiers) |
|---|---|---|---|
| Loom | 10 | 4 ("Competitors", "Course", "Product", "Small") | 6 real (Tella, ScreenPal, BombBomb, Screen Studio, ScreenFlow, Zoom Clips) |
| PassFree | 6 | 0 (manually patched) | 6 real (Bitwarden, 1Password, KeePass, KeePassXC, Proton Pass, Dashlane) |
| KeyGuardian | 10 | 0 (heuristic missed) | ~7 real (Gitleaks, Appknox, GitHub Advanced Security, Legit Security, CAST, Coverity, Devknox), 3 questionable (BKP365, CodeShield, Dynatrace) |
| RoamRescue | 0 | 0 | 2–3 real (Logseq, Obsidian, Tana — but A-6 v1 missed all) |

**Even taking real-only counts, the verdicts hold:**
- Loom: 6 real > 5 — TERMINATE (correct)
- PassFree: 6 real > 5 — TERMINATE (correct)
- KeyGuardian: 7 real > 5 — TERMINATE (correct)
- RoamRescue: 2-3 real ≤ 5 — pass scarcity (correct)

**The math is honest.** A-6 v2 noise inflation isn't changing any verdicts in this set; even fully cleaned counts produce the same PASS/FAIL pattern.

---

## 6. CEO DECISION MATRIX

The three strategic options I framed in prior dossiers, now tested against this 4-report dataset:

### Option A — Discipline target selection
**Status: empirically necessary.** Roam was the only pass, and it scored well primarily because A-6 v1 missed the real competitors. Even Roam at corrected scarcity (~2-3 real) would clear, but barely.
**Action:** MCMO target-selection criteria need to surface targets with ≤5 real modern competitors *and* strong pain fundamentals. Recent broken-faith windows (last 30-90 days) and technical-barrier-rich categories remain the best filters.

### Option B — Adjust scarcity threshold (DONE: 3 → 5)
**Status: applied, didn't help these strikes.** Threshold=5 is calibrationally honest for 2026 market reality but doesn't rescue any of the four targets attempted. The bump was correct policy regardless — but its impact on hit rate is modest.
**Forward implication:** further bumps (5 → 7 or 5 → 9) would start admitting strikes with weak fundamentals. PassFree at threshold=7 illustrates: passes scarcity but fails score gate. Don't keep loosening — the score gate becomes the next sentinel.

### Option C — Pivot the thesis
**Status: increasingly attractive.** If Option A criteria are tightened to extreme niches (≤5 real competitors, fresh wound, technical barrier) and still produce few hits, the underlying "local-first rescue of crowded SaaS" thesis may be exhausted in mainstream categories.
**Adjacent theses worth piloting:**
- Export tools (help users *leave* SaaS, smaller scope)
- AI-augmented locality (local LLMs for what cloud SaaS does server-side; Loom transcription is one example)
- Privacy-as-product (E2E equivalents for surveillance-fatigued segments)

---

## 7. CONCRETE RECOMMENDATIONS

For CEO action this week:

1. **Adopt pre-flight as default.** KeyGuardian saved $2-5 vs full scan. If 4 of 5 recent strikes fail at scarcity, we've been spending ~$15 of avoidable Apify across the recent run. Pre-flight is cheap insurance.

2. **Stop scanning mainstream pain points cold.** Calendly, Loom, LastPass, Session Buddy, Web Highlights — every well-known SaaS pain has been independently mapped by 4-7 rescue products. Don't burn another Apify budget on those.

3. **Take Option C seriously.** Pilot one strike under an adjacent thesis (e.g., target an *export-tool gap* — find a SaaS where the export is technically broken, build a single-purpose migrator). Low scope, low competitive pressure, validates whether the different thesis has different competitive density.

4. **Backfill remaining ORs.** Strike 003 (InstaRescue), Strike 004 (PassVault), Strike 005 (ReadFlow), and the four 009 attempts (Calendly, Session Buddy, Web Highlights, Loom — Loom done) all deserve OR retrospectives for cross-OR pattern analysis. The data_lake has the strike reports; just need the runs.

5. **A-6 v2 has known noise leaks.** Heuristic missed the GitHub Advanced Security / CAST / Dynatrace cases as noise candidates (they ARE real competitors so flagging them as noise would be wrong, but the heuristic also doesn't surface "Calendar" / "Reader Mode" / corporate-prefix patterns reliably). LLM-based extraction is the next step if we want clean ORs without manual triage.

---

## 8. ARTIFACTS

| Path | What |
|---|---|
| `864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py` | Generator v1.1 (neutral hub, side-effect-free gate) |
| `864zeros-ISD/ISD-DIV-5-EVOLUTION/reports/OR-*.md` | Four ORs (this comparison's source) |
| `864zeros-ISD/ISD-DIV-5-EVOLUTION/data_lake/STRIKE_REPORT_*.json` | 7 strike reports (consolidated this cycle) |
| `864zeros-ISD/ISD-DIV-5-EVOLUTION/COMPARISON_2026-05-07.md` | This document |

Total this cycle:
- Created 2 new ORs (RoamRescue success, PassFree retro failure)
- Moved 7 strike reports into data_lake
- Generated 1 cross-OR comparison
- Apify spend: 0 (no new live scans this cycle)

---

— Signed: CEO + CTO + MCMO (augmented office)
— ISD-DIV-5-EVOLUTION 2026-05-07
— End of 4-Report Comparison —
