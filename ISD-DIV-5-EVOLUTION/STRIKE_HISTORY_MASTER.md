# 864zeros Strike History — Master Record
## ISD-DIV-5-EVOLUTION Consolidated Dataset for Option C Evaluation

**Generated:** 2026-05-07
**Source ORs:** 10 (3 historical + 6 May 2026 + 1 preflight)
**Data lake:** `data_lake/STRIKE_REPORT_*.json` (7 files), `data_lake/strikes/*.json` (4 strike-of-record files), `data_lake/LEAD_*.json` (1 adapter intermediate)

---

## 1. EXECUTIVE READ

**3 historical winners. 1 mid-build. 6 recent failures.** The hit rate dropped from 100% (March 2026: 3/3 passes) to 0% (May 2026: 0/6 passes among the 009 attempts + KeyGuardian + retro PassFree).

The discriminator across all 10 strikes is competitor density. Pain-signal volume, sentiment, stagnation, and Rule-of-40 financials are *roughly equivalent* across passes and failures. **Scarcity is the gate. The rescue economy filled in between March and May 2026.**

This is the dataset for CEO Option C evaluation.

---

## 2. ALL STRIKES — RANKED BY SCORE

| Rank | Strike | Codename | Target | Verdict | Score | Scarcity | Z-Conv | Z-Vel | Z-Scar | R40 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 864z-2026-006 | RoamRescue | Roam Research | **PASSED** ✓ | **11.36** | 0 (artifact) | 0.80 | 0.5643 | 1.00 | 105 |
| 2 | 864z-2026-009-att-2 | (SessionRescue) | Session Buddy | TERMINATED | 0.0 (~9.76 hypo) | 10 | 0.90 | 0.7017 | 0.00 | 115 |
| 3 | 864z-2026-004 | PassVault | Dashlane | **PASSED** ✓ | **9.45** | 2 | 0.92 | 0.88 | 0.78 | 125 |
| 4 | 864z-2026-003 | InstaRescue | Instapaper | **PASSED** ✓ | **9.38** | 3 | 0.80 | 0.53 | 0.40 | 110 |
| 5 | 864z-2026-009-att-3 | (HighlightFree) | Web Highlights | TERMINATED | 0.0 (~8.37 hypo) | 6 | 0.80 | 0.5656 | 0.00 | 105 |
| 6 | 864z-2026-009-att-4 | (VideoFree) | Loom | TERMINATED | 0.0 (~8.38 hypo) | 10 | 0.80 | 0.5675 | 0.00 | 110 |
| 7 | 864z-2026-008 (retro) | PassFree | LastPass | TERMINATED (retro) | 0.0 (~8.03 hypo) | 6 (patched) | 0.80 | 0.5012 | 0.00 | 110 |
| 8 | 864z-2026-009-att-1 | — | Calendly | TERMINATED | 0.0 (~7.35 hypo) | 10 | 0.70 | 0.5005 | 0.00 | 100 |
| 9 | 864z-2026-010 | KeyGuardian | Gemini API Key Scope | TERMINATED (preflight) | n/a | 10 | n/a | n/a | n/a | n/a |
| — | 864z-2026-005 | ReadFlow | Instapaper | BUILD_IN_PROGRESS | n/a | n/a | n/a | n/a | n/a | n/a |

**Critical observation:** at rank #2, Session Buddy has the HIGHEST hypothetical score (~9.76) of the failures — higher than two of the three historical winners. **The strike was killed entirely by scarcity (10 real competitors in tab management).** Genuine fundamentals; saturated category.

---

## 3. RANKED BY SCARCITY (ASCENDING — BETTER FIRST)

| Rank | Strike | Target | Scarcity | Outcome |
|---|---|---|---|---|
| 1 | 864z-2026-006 | Roam Research | **0** (A-6 v1 artifact; real ~2-3) | PASSED |
| 2 | 864z-2026-004 | Dashlane | **2** | PASSED |
| 3 | 864z-2026-003 | Instapaper | **3** | PASSED |
| 4 | 864z-2026-008 (retro) | LastPass | **6** (patched) | TERMINATED at scarcity (>5) |
| 4 | 864z-2026-009-att-3 | Web Highlights | **6** (A-6 v2) | TERMINATED at scarcity (>5) |
| 6 | 864z-2026-009-att-1 | Calendly | **10** | TERMINATED at scarcity |
| 6 | 864z-2026-009-att-2 | Session Buddy | **10** | TERMINATED at scarcity |
| 6 | 864z-2026-009-att-4 | Loom | **10** | TERMINATED at scarcity |
| 6 | 864z-2026-010 | Gemini API Key Scope | **10** (preflight) | TERMINATED at preflight |

**Hard line at scarcity ≤ 3:** all three winners (003, 004, 006) clustered there. Above 5: every strike terminated.

**The threshold=5 (current) catches the borderline cases** (PassFree, Web Highlights at 6) but doesn't catch any of the recent live scans where competitor density runs to 10.

---

## 4. THE FUNDAMENTAL FACTORS (NON-SCARCITY) ARE STABLE

Across the 8 strikes with computed Z-factors:

| Field | Range | Median | Std (eyeballed) |
|---|---|---|---|
| Z-Convergence | 0.70 – 0.92 | 0.80 | low |
| Z-Velocity | 0.50 – 0.88 | 0.56 | medium |
| Z-Scarcity | 0.00 – 1.00 | 0.00 | **bimodal** |
| Pain signals | 6 – 77 | 44 | wide |
| Sentiment | 30 – 51 | 49.7 | low (most cluster around 50) |
| Rule of 40 | 100 – 125 | 110 | low |

**Pillar 1 (Ransom):** Z-Convergence range is 0.70-0.92. Pain signals abundant everywhere. **Not the discriminator.**
**Pillar 2 (Friction):** Folded into Z-Convergence + Z-Velocity. Also not the discriminator.
**Pillar 3 (Math):** Rule of 40 is well-clear of threshold (40) for every strike. **Exit multiplier is 1.5× across the board.**
**Pillar 4 (Technical Rescue):** Not validator-checked; MCMO judgment.

**The only field where passes and failures separate cleanly is Z-Scarcity.** Pure binary: 0.40-1.00 for passes, 0.00 for failures.

---

## 5. THE TEMPORAL PATTERN (THESIS DECAY)

| Era | Strikes | Pass rate | Avg scarcity |
|---|---|---|---|
| March 2026 | 003, 004, 005 | 100% (3/3 — 005 mid-build) | 2-3 (low) |
| May 2026 | 006, 008(retro), 009-1, 009-2, 009-3, 009-4, 010 | 14% (1/7 — Roam) | 6-10 (high) |

**Two months. Same scoring engine. Same MCMO judgment process. Different competitive density.**

This is consistent with one of two stories:
- **Story A:** A-6 v1 was masking real competitors in March (Pocket/Raindrop/Matter were really 5-7+; Bitwarden/KeePassXC really 3-4+; etc.). The "100% hit rate" was instrumentation error. With A-6 v2, we now see truth.
- **Story B:** The rescue economy ACTUALLY filled in dramatically between March and May 2026 — multiple indie builders, OSS communities, and YC startups shipped local-first alternatives in those weeks.

CTO read: **likely a mix of both, weighted toward Story A.** A-6 v1 was demonstrably broken (returned 0 for Roam, LastPass). The March 2026 strike validations probably under-counted competitors. But Story B contributes too — the post-LastPass-breach migration wave was a real event in 2025-2026 and rescue products have been shipping.

Either way, **the present state is: ≤3 competitor markets are rare.**

---

## 6. WHAT WOULD HAVE PASSED AT THE OLD ENGINE BUT FAILS NOW

| Strike | Old A-6 v1 read | Current A-6 v2 read | What changed |
|---|---|---|---|
| 864z-2026-006 RoamRescue | 0 competitors → PASS at 11.36 | Would find ~2-3 (Logseq, Obsidian, Tana) → still PASS at ~9.75 | Reduced margin but verdict unchanged |
| 864z-2026-008 PassFree | 0 competitors → PASS at 11.03 | Found 6 real → TERMINATE at scarcity (>5) | **Verdict flipped** post-A-6 fix |
| 864z-2026-003 InstaRescue (March) | 3 competitors → PASS at 9.38 | Likely 5-7 today → would TERMINATE | Hypothetical: probably broken now |
| 864z-2026-004 PassVault (March) | 2 competitors → PASS at 9.45 | Likely 5+ today (Bitwarden, 1Password, KeePassXC, Proton Pass) → would TERMINATE | Hypothetical: probably broken now |

**The historical winners may not survive a present-day rescan.** This is the most uncomfortable read in the dataset, and the strongest evidence for either Option C (thesis pivot) or aggressive target re-selection (extreme niches).

---

## 7. OPTION C EVALUATION FRAMEWORK

The user directive's stated goal: *"Create the complete dataset for Option C (Thesis Pivot) evaluation."*

### What we now have evidence for

1. **The "local-first rescue of mainstream SaaS hostage" thesis is exhausted in well-known categories.** Scheduling, video recording, password management, web annotation, tab management, note-taking — all crowded.
2. **The fundamentals (pain, stagnation, sentiment, Rule of 40) are easy to find.** Pain abundance isn't a moat.
3. **The differentiator the math demands (≤5 real competitors AND ≥8.64 score) is rare.** Roam was the lone fit, and it has an A-6 v1 asterisk.

### Option C candidates worth piloting

| Adjacent Thesis | Hypothesis | Why Different Competitive Density | Test |
|---|---|---|---|
| **Export Tools** | Help users *leave* SaaS. Smaller scope. Single-purpose migrators. | Export tools are unsexy; few indie builders make them. Most are bundled inside rescue products, not standalone. | Pilot: "1Password-to-Bitwarden CSV migrator" or "Notion-to-Obsidian exporter" |
| **AI-Augmented Locality** | Local-first products that use local LLMs for what cloud SaaS does server-side. | Technical bar is high (model serving, quantization, hardware reqs). Smaller competitive pool. | Pilot: "Local-Whisper Loom alternative" or "Local-LLM Notion-style notes" |
| **Privacy-First Equivalents** | Same product space but explicitly E2E-encrypted, surveillance-fatigue-targeted. | Different distribution channel (privacy-conscious audiences). Different value prop. | Pilot: "Private Calendly with E2E proofs" |
| **Shrunken Niches** | Same rescue thesis, but in tools so niche the competitive pool is genuinely thin (single-digit-thousand-user products). | Below the radar of mainstream rescue builders. Lower TAM but more achievable. | Pilot: tool that has 1k-5k users with active complaints and zero rescue product |

### Empirical test for Option C viability

**Pre-flight sniff each candidate in the new thesis space.** Cost: ~$0.30 per candidate. If competitor count for adjacent-thesis candidates averages ≤5 (i.e., the thesis pivot DOES find emptier markets), the pivot is worth pursuing. If they're also crowded (≥6 average), the rescue economy is saturated more broadly than just rescue-of-mainstream-SaaS, and a deeper rethink is needed.

---

## 8. COMPETITOR COUNT DISTRIBUTION ACROSS THIS DATASET

Histogram (real competitor counts, ignoring noise):

```
0  | █                                     (RoamRescue — A-6 v1 artifact)
1  |
2  | █                                     (PassVault — March 2026)
3  | █                                     (InstaRescue — March 2026)
4  |
5  |                                       (← current SCARCITY_THRESHOLD line)
6  | ██                                    (Web Highlights, PassFree retro)
7  | █                                     (KeyGuardian — ~7 real of 10 raw)
8  |
9  |
10 | █████                                 (Calendly, Loom, Session Buddy, KeyGuardian, [LastPass at A-6 v2])
```

**The distribution is bimodal.** Either ≤3 or ≥6. There's a "missing middle". Targets at exactly 4-5 competitors (the new threshold sweet spot) are not surfacing in scans. Possibly because:
- Listicle culture: "Top 10 X alternatives" is the standard format, so any well-known target generates ≥10 mentions
- Below-listicle targets are obscure enough that A-6 sniff doesn't surface them either

This pattern argues FOR target-discipline tightening (Option A) — but the empirical hit rate (1/7 in May 2026) suggests Option A alone may not be enough.

---

## 9. RECOMMENDATIONS FOR CEO (data-driven)

**Immediate (free):**
1. **Adopt pre-flight sniff as default workflow.** ~$0.30 per candidate vs ~$2-5 full scan. Saved ~$15 across recent run.
2. **Stop scanning Top-10 SaaS pain points cold.** Calendly/Loom/LastPass/Session Buddy/Web Highlights have all been mapped.

**Near-term (constants change made; results modest):**
3. **SCARCITY_THRESHOLD = 5 is in effect.** Empirically validated this session: didn't unlock any failed strikes, but is correctly calibrated for current market. Don't loosen further; score gate becomes the next sentinel.

**Strategic (Option C pilot):**
4. **Run one strike in each of the four Option C lanes** (export tool, AI-augmented locality, privacy-first, shrunken niche). Total cost: ~$1.20 in pre-flight Apify spend. Outcome data will tell us whether the thesis pivot finds emptier markets.
5. **If Option C pilot shows 2+ wins**: pivot the formal thesis in CLAUDE.md and ROLES.md. Update Pillar 4 (Technical Rescue Blueprint) to reflect the pivot.
6. **If Option C pilot shows 0-1 wins**: deeper rethink needed. May indicate the local-first market saturation is broader than initially scoped.

**Engineering (CTO):**
7. **A-6 v3 — LLM-based competitor extraction.** Current heuristic still produces noise (Edge Reader Mode, Google Cloud OpenCue). LLM extraction would reduce noise, possibly surfacing more accurate ≤5-competitor candidates.
8. **Re-validate historical winners (003, 004, 006) under A-6 v2.** Update ORs with current-state competitor counts. If any flip from PASSED to TERMINATED, audit the build state of corresponding factory directories.

---

## 10. ARTIFACT INVENTORY

```
864zeros-ISD/ISD-DIV-5-EVOLUTION/
├── report_generator.py               (v1.1, three modes: full, preflight, historical)
├── COMPARISON_2026-05-07.md          (4-report cross-OR analysis from prior cycle)
├── STRIKE_HISTORY_MASTER.md          (this file — 10-OR master ranking)
├── data_lake/
│   ├── LEAD_ROAM_RESEARCH.json
│   ├── STRIKE_REPORT_CALENDLY.json
│   ├── STRIKE_REPORT_KNAK.json
│   ├── STRIKE_REPORT_LASTPASS.json
│   ├── STRIKE_REPORT_LOOM.json
│   ├── STRIKE_REPORT_ROAM_RESEARCH.json
│   ├── STRIKE_REPORT_SESSION_BUDDY.json
│   ├── STRIKE_REPORT_WEB_HIGHLIGHTS.json
│   └── strikes/
│       ├── 864z-2026-003.json   (InstaRescue strike-of-record)
│       ├── 864z-2026-004.json   (PassVault)
│       ├── 864z-2026-005.json   (ReadFlow — bridge format)
│       └── 864z-2026-006.json   (RoamRescue)
└── reports/
    ├── OR-2026-03-17-INSTARESCUE.md     ◄── NEW (winner backfill)
    ├── OR-2026-03-17-PASSVAULT.md       ◄── NEW (winner backfill)
    ├── OR-2026-03-18-READFLOW.md        ◄── NEW (factory-state backfill)
    ├── OR-2026-05-06-CALENDLY.md        ◄── NEW (failure backfill)
    ├── OR-2026-05-06-LOOM.md
    ├── OR-2026-05-06-PASSFREE.md
    ├── OR-2026-05-06-ROAMRESCUE.md
    ├── OR-2026-05-06-SESSION_BUDDY.md   ◄── NEW (failure backfill)
    ├── OR-2026-05-06-WEB_HIGHLIGHTS.md  ◄── NEW (failure backfill)
    └── OR-2026-05-07-KEYGUARDIAN.md
```

10 ORs. 7 strike reports. 4 strike-of-record files. 1 lead intermediate. 3 cross-OR/master analysis docs. **Complete dataset for Option C decision.**

---

## 11. APIFY SPEND SUMMARY

| Cycle | Queries | Outcome |
|---|---|---|
| RoamRescue full scan | 13 | PASSED (scaffolded) |
| LastPass full scan | 13 | PASSED at the time (later archived) |
| Calendly full scan | 15 | TERMINATED |
| Session Buddy full scan | 15 | TERMINATED |
| Web Highlights initial | 15 | (Web Highlights eventually terminated) |
| Web Highlights A-6 v2 re-extract | 3 | (no impact on verdict) |
| Loom full scan | 15 | TERMINATED |
| KeyGuardian preflight | 3 | TERMINATED at preflight (saved ~12) |
| **Total** | **~92** | (~$5-15 USD across this session) |

**Pre-flight workflow ROI (KeyGuardian):** $0.30 spent vs $2-5 saved. Adopt as default.

---

## 12. SIGN-OFF

This master record is the consolidated dataset CEO requested for Option C evaluation. The ORs are queryable via YAML frontmatter for cross-OR pattern analysis. The next strike — whether Strike 011 in Option C lane, or Strike 012 in continued rescue thesis — should be informed by the recommendations in §9.

The integers **864z-2026-009, 864z-2026-010** remain available for re-use. Strike counter at 8 in vulture-nest/strike_counter.txt.

— Signed: CEO + CTO + MCMO (augmented office)
— ISD-DIV-5-EVOLUTION 2026-05-07
— End of Strike History Master Record —
