#!/usr/bin/env python3
"""
report_generator.py - ISD-DIV-5-EVOLUTION Operational Record (OR) generator
                       (Neutral Hub edition — isolated from research repos)

Lives at: 864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py
Imports research code from sibling: ../../vulture-nest/

Two modes:
  - full       Re-runs adapter + Z-factor calculation on a strike report.
               Reimplements the validator's gate logic LOCALLY to avoid the
               side effect of validate() writing to vulture-nest's
               _archive/terminated_leads/ directory. The math
               (calculate_864z_score) is still imported from validator.py
               so the canonical math source-of-truth doesn't drift.
  - preflight  Builds an OR from a pre-flight competitor sniff (no full scan).

Output: markdown with YAML frontmatter (greppable across many ORs).

Usage:
  python report_generator.py full \\
      ../../vulture-nest/OFFICE/DIV-1-VULTURE/STRIKE_REPORT_LOOM.json \\
      --target Loom --codename VideoFree \\
      --traffic 2000000 --stagnation 24 --growth 25 --margin 85 \\
      --output reports/OR-2026-05-06-LOOM.md

  python report_generator.py preflight \\
      --target "Gemini API Key Scope" --codename KeyGuardian \\
      --sniff-target GitGuardian \\
      --competitors "Gitleaks,Appknox,GitHub Advanced Security,..." \\
      --queries-spent 3 \\
      --output reports/OR-2026-05-07-KEYGUARDIAN.md
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

# UTF-8 stdout (mirrors D-3 fix)
if hasattr(sys.stdout, 'reconfigure') and (sys.stdout.encoding or '').lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# === Cross-repo import bridge ===
# Generator lives in 864zeros-ISD/ISD-DIV-5-EVOLUTION/, but the math + adapter
# code live in vulture-nest/. Inject vulture-nest as an importable path.
SCRIPT_DIR = Path(__file__).resolve().parent
VULTURE_NEST = SCRIPT_DIR.parent.parent / "vulture-nest"
if not VULTURE_NEST.exists():
    print(f"[report_generator] FATAL: cannot find vulture-nest at {VULTURE_NEST}", file=sys.stderr)
    print("Expected layout: <root>/864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py", file=sys.stderr)
    print("                 <root>/vulture-nest/                                 (sibling)", file=sys.stderr)
    sys.exit(1)
sys.path.insert(0, str(VULTURE_NEST))

# These imports work because vulture-nest is now on sys.path
from validator import VultureValidator, SCORE_THRESHOLD, SCARCITY_THRESHOLD, RULE_OF_40_THRESHOLD  # noqa: E402
from live_to_validator_adapter import adapt_to_lead  # noqa: E402


# ============================================================================
# Local gate logic (replicates validator.validate() WITHOUT side effects)
# ============================================================================

def evaluate_gates_locally(lead, score, scarcity_thr=SCARCITY_THRESHOLD, score_thr=SCORE_THRESHOLD):
    """
    Mirror validator.validate()'s gate semantics without invoking it (avoids the
    side effect of writing _archive/terminated_leads/ entries every time we
    generate a retrospective OR).
    Gate order matches validator.py:289-336.
    """
    scarcity = len(lead.competitors or [])
    if scarcity > scarcity_thr:
        return {
            "passed": False,
            "gate": "scarcity",
            "failure_reason": f"SCARCITY_EXCEEDED: {scarcity} competitors > {scarcity_thr} threshold",
        }
    if score < score_thr:
        return {
            "passed": False,
            "gate": "score_threshold",
            "failure_reason": f"SCORE_BELOW_THRESHOLD: {round(score, 2)} < {score_thr}",
        }
    return {"passed": True, "gate": "passed_all_gates", "failure_reason": None}


# ============================================================================
# Frontmatter helpers
# ============================================================================

def yaml_escape(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    s = str(value)
    if any(c in s for c in [':', '#', '"', "'", '\n', '[', ']', '{', '}', ',', '&', '*', '!', '|', '>', '%', '@', '`']):
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


def yaml_list(values):
    return "[" + ", ".join(yaml_escape(v) for v in values) + "]"


def emit_frontmatter(d):
    lines = ["---"]
    for k, v in d.items():
        if isinstance(v, list):
            lines.append(f"{k}: {yaml_list(v)}")
        else:
            lines.append(f"{k}: {yaml_escape(v)}")
    lines.append("---")
    return "\n".join(lines)


def extract_top_pain_quotes(strike_report, n=5):
    """
    Pick the most informative pain-signal content strings across all categories.
    Filters URL-only entries and short fragments. Sorts by length (proxy for
    detail richness), takes top N. Each result includes its source category.

    v1.2 addition: surfaces qualitative texture for the Mechanical Gap Analysis
    section. Useful for analyst spot-check ("does the pain match the thesis?").
    """
    all_signals = []
    for category in ("pricing_friction", "export_hostage", "enterprise_pain"):
        for entry in strike_report.get(category) or []:
            content = (entry.get("content") or "").strip()
            # Drop URL-only lines (Apify formats results with URLs in parens)
            if content.startswith("(") and content.endswith(")"):
                continue
            if content.startswith("http"):
                continue
            # Drop very short / fragment lines
            if len(content) < 40:
                continue
            # Drop pure title-case listicle titles (often not real complaints)
            stripped = content.replace("**", "")
            if stripped.startswith("**") or (stripped.endswith("**") and len(stripped) < 80):
                continue
            all_signals.append({
                "content": content[:300],  # cap for readability
                "category": category,
                "len": len(content),
            })
    all_signals.sort(key=lambda s: -s["len"])
    return all_signals[:n]


def derive_thesis(strike_report):
    """
    Extract a thesis statement set from the strike report.

    Primary source: unbundle_opportunity.saas_hostage_indicators (synthesized
    by run_live_scan during Phase 5). Fallback: category-presence summary.
    """
    indicators = (strike_report.get("unbundle_opportunity") or {}).get("saas_hostage_indicators") or []
    if indicators:
        return list(indicators)
    # Fallback derivation
    fallback = []
    if strike_report.get("pricing_friction"):
        fallback.append(f"Pricing friction observed ({len(strike_report['pricing_friction'])} signals)")
    if strike_report.get("export_hostage"):
        fallback.append(f"Export lock-in observed ({len(strike_report['export_hostage'])} signals)")
    if strike_report.get("enterprise_pain"):
        fallback.append(f"Enterprise pain observed ({len(strike_report['enterprise_pain'])} signals)")
    return fallback or ["No thesis surfaced — insufficient signal density"]


def build_mechanical_gap_analysis(strike_report, target):
    """
    Build the Pillar-4 Mechanical Gap Analysis markdown section.

    Surfaces WHY the incumbent is vulnerable to a local-first rescue,
    regardless of competitor count. Auto-flags pivot opportunities when
    the signal mix shows asymmetry (e.g., export-heavy → export-tool lane).
    """
    pricing = strike_report.get("pricing_friction") or []
    export = strike_report.get("export_hostage") or []
    enterprise = strike_report.get("enterprise_pain") or []
    pricing_count, export_count, enterprise_count = len(pricing), len(export), len(enterprise)

    unbundle = strike_report.get("unbundle_opportunity") or {}
    indicators = unbundle.get("saas_hostage_indicators") or []
    local_first = unbundle.get("local_first_possible")
    market_size = unbundle.get("estimated_market_size", 0)

    s = [f"## Mechanical Gap Analysis (Pillar 4)\n"]
    s.append(f"> *Why is {target} vulnerable to a local-first rescue, regardless of competitor count?*\n")

    # === Ransom Mechanism (Pillar 1) ===
    s.append("\n### Ransom Mechanism (Pillar 1)")
    if pricing_count >= 10:
        s.append(f"- **Strong active extraction**: {pricing_count} pricing signals captured. Users notice and articulate the cost.")
    elif pricing_count >= 5:
        s.append(f"- **Moderate pricing pressure**: {pricing_count} pricing signals.")
    elif pricing_count >= 2:
        s.append(f"- **Low ransom thesis**: only {pricing_count} pricing signals. Pain may be elsewhere.")
    else:
        s.append(f"- **No ransom thesis**: {pricing_count} pricing signals.")

    # === Friction Mechanism (Pillar 2) ===
    s.append("\n### Friction Mechanism (Pillar 2)")
    if export_count >= 15:
        s.append(f"- **Heavy export lock-in**: {export_count} export-related complaints. Proprietary format and/or migration cost is the moat.")
    elif export_count >= 5:
        s.append(f"- **Real export friction**: {export_count} export signals.")
    elif export_count >= 2:
        s.append(f"- **Mild friction**: {export_count} export signals.")
    else:
        s.append(f"- **No friction thesis**: {export_count} export signals.")

    # === Architectural Vulnerability ===
    s.append("\n### Architectural Vulnerability")
    if local_first is True:
        s.append("- **Local-first viable** — scan flagged the incumbent's core operations as eligible for unbundle.")
    elif local_first is False:
        s.append("- **Local-first NOT viable** — scan flagged architectural dependencies (cloud-essential operations) that can't be replaced locally.")
    else:
        s.append("- *Local-first viability not flagged in scan output.*")
    if indicators:
        s.append("\n**Hostage indicators (synthesized by Phase 5):**")
        for ind in indicators:
            s.append(f"- {ind}")
    if market_size:
        s.append(f"\n**Estimated market size (scan-derived):** {market_size:,} *(coarse — listicle-driven; treat as order-of-magnitude)*")

    # === Pivot Opportunity flag ===
    s.append("\n### Pivot Opportunity (Option C signal)")
    pivot_flagged = False
    if export_count >= 10 and export_count > pricing_count * 1.5:
        s.append(f"- **EXPORT-HEAVY signal mix** ({export_count} export vs {pricing_count} pricing). The pain is *getting out*, not *paying in*. **Possible Option C pivot: standalone migration tool / export utility, not a full rescue product.** Less competitive density in the export-tool space than the full rescue space.")
        pivot_flagged = True
    if pricing_count >= 10 and pricing_count > export_count * 1.5:
        s.append(f"- **RANSOM-HEAVY signal mix** ({pricing_count} pricing vs {export_count} export). The pain is the price, not the lock-in. **Possible angle: free-tier rescue (--free build) or pay-once positioning.**")
        pivot_flagged = True
    if enterprise_count >= 10 and enterprise_count > (pricing_count + export_count) * 0.4:
        s.append(f"- **ENTERPRISE-HEAVY signal mix** ({enterprise_count} enterprise pain). Rescue product may be unsuited (enterprise sales is hard); consider **B2C-only positioning** or skip target.")
        pivot_flagged = True
    if not pivot_flagged:
        s.append("- *No obvious pivot lever from signal-mix asymmetry. Standard rescue thesis applies.*")

    return "\n".join(s) + "\n"


def assess_competitor_quality(name):
    """Heuristic competitor-name assessment: 'noise' / 'unknown'. Manual review upgrades to 'real'/'adjacent'."""
    if not name:
        return "noise"
    generic = {
        "Competitors", "Course", "Product", "Small", "Large", "Mac", "Windows",
        "Linux", "Calendar", "Email", "List", "Service", "Tool", "Best",
        "Top", "Free", "Paid", "Reader", "Mode", "Available", "Edition",
    }
    first = name.split()[0] if name.split() else ""
    if first in generic or name in generic:
        return "noise"
    parts = name.split()
    if len(parts) >= 2:
        corporate = {"Google", "Microsoft", "Amazon", "Apple", "IBM", "Oracle"}
        service_kw = {"Cloud", "Reader", "Mode", "Drive", "Studio", "Workspace", "Suite"}
        if parts[0] in corporate and parts[1] in service_kw:
            return "noise"
    return "unknown"


# ============================================================================
# Full-scan OR
# ============================================================================

def build_full_scan_or(*, strike_report, target, codename, traffic, stagnation,
                      growth, margin, or_id, strike_report_path=None, apify_queries=None):
    lead = adapt_to_lead(
        strike_report,
        traffic_monthly=traffic,
        last_update_months=stagnation,
        growth_projection=growth,
        margin_projection=margin,
    )

    v = VultureValidator()
    score, z_conv, z_vel, z_scar, rule_of_40, exit_mult = v.calculate_864z_score(lead)
    base_score = (z_conv * 0.45 + z_vel * 0.35 + z_scar * 0.20) * 10
    final_score = base_score * exit_mult

    # Local gate evaluation — no side effects
    gate_result = evaluate_gates_locally(lead, final_score)

    competitors = list(lead.competitors or [])
    quality_labels = {c: assess_competitor_quality(c) for c in competitors}
    flagged_noise = [c for c, q in quality_labels.items() if q == "noise"]
    real_or_adjacent = [c for c, q in quality_labels.items() if q != "noise"]

    # v1.2 additions
    thesis = derive_thesis(strike_report)
    top_quotes = extract_top_pain_quotes(strike_report, n=5)

    fm = {
        "or_id": or_id,
        "or_type": "full_scan",
        "or_version": "1.2",  # 1.2: thesis + top_pain_quotes + Mechanical Gap Analysis (Pillar 4)
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "target": target,
        "codename": codename or "unspecified",
        "scan_timestamp": strike_report.get("meta", {}).get("scan_timestamp", "unknown"),
        "scan_mode": strike_report.get("meta", {}).get("mode", "unknown"),
        "verdict": "PASSED" if gate_result["passed"] else "TERMINATED",
        "verdict_gate": gate_result["gate"],
        "vulture_score": round(final_score, 2) if gate_result["passed"] else 0.0,
        "hypothetical_score_if_gates_bypassed": round(final_score, 2),
        "score_threshold": SCORE_THRESHOLD,
        "scarcity_threshold": SCARCITY_THRESHOLD,
        "scarcity_index": len(competitors),
        "z_convergence": round(z_conv, 4),
        "z_velocity": round(z_vel, 4),
        "z_scarcity": round(z_scar, 4),
        "rule_of_40": round(rule_of_40, 1),
        "exit_multiplier": exit_mult,
        "traffic_monthly": traffic,
        "stagnation_months": stagnation,
        "growth_projection": growth,
        "margin_projection": margin,
        "pain_signal_count": len(lead.pain_signals or []),
        "sentiment_score": round(lead.sentiment_score, 2),
        "competitors_count": len(competitors),
        "competitors": competitors,
        "noise_count_estimate": len(flagged_noise),
        "real_count_estimate": len(real_or_adjacent),
        "apify_queries_spent": apify_queries if apify_queries is not None else "unknown",
        "source_strike_report": str(strike_report_path) if strike_report_path else "n/a",
        # v1.2 fields
        "thesis": thesis,
        "top_pain_quotes_count": len(top_quotes),
    }

    body = f"""# Operational Record {or_id}
## {target} → {codename or 'unspecified'}

**Type:** Full-scan retrospective (neutral hub, side-effect-free)
**Verdict:** {'**PASSED**' if gate_result['passed'] else '**TERMINATED**'} ({fm['verdict_gate']})
**Score:** {fm['vulture_score']} (hypothetical if gates bypassed: {round(final_score, 2)})

---

## 1. Inputs

| Parameter | Value | Source |
|---|---|---|
| Target | {target} | MCMO selection |
| Codename | {codename or '*unspecified*'} | MCMO |
| Traffic (monthly) | {traffic:,} | Operator-supplied |
| Stagnation (months) | {stagnation} | Operator-supplied |
| Growth projection | {growth}% | Operator-supplied |
| Margin projection | {margin}% | Operator-supplied |
| Scan mode | {fm['scan_mode']} | Live |
| Scan timestamp | {fm['scan_timestamp']} | Live scan |

## 2. Captured Signals

| | Count |
|---|---|
| Total pain signals | {fm['pain_signal_count']} |
| Pricing friction | {len(strike_report.get('pricing_friction') or [])} |
| Export hostage | {len(strike_report.get('export_hostage') or [])} |
| Enterprise pain | {len(strike_report.get('enterprise_pain') or [])} |
| Average sentiment | {fm['sentiment_score']} (lower = more negative) |

## 3. Competitor Landscape (A-6 v2)

**Raw count:** {fm['competitors_count']}
**Estimated real/adjacent:** {fm['real_count_estimate']}
**Estimated noise:** {fm['noise_count_estimate']}

| Name | Heuristic flag |
|---|---|
"""
    for c in competitors:
        body += f"| {c} | {quality_labels.get(c, 'unknown')} |\n"

    body += f"""
> Note: 'noise' flag is heuristic only. 'unknown' = analyst should mark real/adjacent/noise during manual triage.

## 4. Top Pain Quotes (qualitative)

*The 5 most-detailed signals captured (longest content; URL-only and short fragments filtered).*

"""
    if top_quotes:
        for i, q in enumerate(top_quotes, 1):
            body += f"{i}. *[{q['category']}]* {q['content']}\n\n"
    else:
        body += "*No qualifying pain quotes — all captured signals were short fragments or URL-only.*\n\n"

    body += f"""## 5. Thesis (synthesized)

"""
    for t in thesis:
        body += f"- {t}\n"

    body += f"""
{build_mechanical_gap_analysis(strike_report, target)}

## 7. Math Breakdown

```
Z-Convergence: {round(z_conv, 4)}
Z-Velocity:    {round(z_vel, 4)}
Z-Scarcity:    {round(z_scar, 4)}
Rule of 40:    {round(rule_of_40, 1)}%   (threshold: {RULE_OF_40_THRESHOLD}%)
Exit mult:     {exit_mult}x
Base score:    ({round(z_conv,4)}*0.45 + {round(z_vel,4)}*0.35 + {round(z_scar,4)}*0.20) * 10 = {round(base_score, 2)}
Final score:   {round(base_score, 2)} * {exit_mult} = {round(final_score, 2)}
```

## 8. Verdict

**{'STRIKE QUALIFIED' if gate_result['passed'] else 'STRIKE TERMINATED'}** at gate: **{fm['verdict_gate']}**.

"""
    if not gate_result["passed"]:
        body += f"""**Failure reason:** `{gate_result['failure_reason']}`

### Counterfactuals at different scarcity thresholds

"""
        for thr in [3, 5, 7]:
            would_pass_scarcity = fm["scarcity_index"] <= thr
            body += f"- `SCARCITY_THRESHOLD = {thr}`: scarcity check **{'PASSES' if would_pass_scarcity else 'FAILS'}** ({fm['scarcity_index']} {'<=' if would_pass_scarcity else '>'} {thr}). "
            if would_pass_scarcity:
                body += f"Would advance to score gate; {'PASSES' if final_score >= SCORE_THRESHOLD else 'FAILS'} ({round(final_score, 2)} {'>=' if final_score >= SCORE_THRESHOLD else '<'} {SCORE_THRESHOLD}).\n"
            else:
                body += "Strike still terminates here.\n"
    else:
        body += "Strike qualified. See validator output for target_mrr / months_to_exit if generate_strike_package was invoked.\n"

    body += f"""
## 9. Source Artifacts

- Strike report: `{strike_report_path or 'n/a'}` (read from vulture-nest)
- This OR generated: {fm['generated_at']}
- Generator: `864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py` v1.2

---
*OR generated in neutral hub. No vulture-nest writes performed.*
*v1.2: thesis extraction + top pain quotes + Mechanical Gap Analysis (Pillar 4 enforcement)*
"""

    return emit_frontmatter(fm) + "\n\n" + body


# ============================================================================
# Pre-flight-only OR
# ============================================================================

def build_preflight_or(*, target, codename, competitors, queries_spent, or_id,
                      sniff_target=None, notes=None):
    competitors = list(competitors or [])
    quality_labels = {c: assess_competitor_quality(c) for c in competitors}
    flagged_noise = [c for c, q in quality_labels.items() if q == "noise"]
    real_or_adjacent = [c for c, q in quality_labels.items() if q != "noise"]

    fm = {
        "or_id": or_id,
        "or_type": "preflight_only",
        "or_version": "1.1",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "target": target,
        "codename": codename or "unspecified",
        "sniff_target": sniff_target or target,
        "verdict": "TERMINATED",
        "verdict_gate": "preflight_scarcity",
        "scarcity_index": len(competitors),
        "scarcity_threshold": SCARCITY_THRESHOLD,
        "competitors_count": len(competitors),
        "competitors": competitors,
        "real_count_estimate": len(real_or_adjacent),
        "noise_count_estimate": len(flagged_noise),
        "apify_queries_spent": queries_spent,
        "full_scan_queries_avoided": 12 if queries_spent == 3 else "unknown",
    }

    body = f"""# Operational Record {or_id}
## {target} → {codename or 'unspecified'}

**Type:** Pre-flight termination (no full scan)
**Verdict:** **TERMINATED** at pre-flight scarcity sniff
**Cost saved:** ~12 Apify queries vs full scan (~80% reduction on rejected strike)

---

## 1. Inputs

| Parameter | Value |
|---|---|
| Target frame | {target} |
| Codename | {codename or '*unspecified*'} |
| Sniff target (proxy) | {sniff_target or target} |
| Apify queries spent | {queries_spent} |
| Full scan queries skipped | ~12 |

{f'> MCMO note: {notes}' if notes else ''}

## 2. Pre-flight Competitor Sniff (A-6 v2)

**Raw count:** {fm['competitors_count']}
**Estimated real/adjacent:** {fm['real_count_estimate']}
**Estimated noise:** {fm['noise_count_estimate']}

| Name | Heuristic flag |
|---|---|
"""
    for c in competitors:
        body += f"| {c} | {quality_labels.get(c, 'unknown')} |\n"

    body += f"""
## 3. Verdict

**STRIKE TERMINATED** at pre-flight scarcity sniff: **{fm['scarcity_index']} competitors > {SCARCITY_THRESHOLD} threshold (current SCARCITY_THRESHOLD)**.

No live scan executed. No strike report exists. No validator auto-archive.

### Counterfactuals at different scarcity thresholds

"""
    for thr in [3, 5, 7]:
        would_pass = fm["scarcity_index"] <= thr
        body += f"- `SCARCITY_THRESHOLD = {thr}`: scarcity check **{'PASSES' if would_pass else 'FAILS'}** ({fm['scarcity_index']} {'<=' if would_pass else '>'} {thr})"
        if would_pass:
            body += " — would have advanced to full scan."
        body += "\n"

    body += f"""
## 4. Source Artifacts

- No strike report (terminated before full scan)
- This OR generated: {fm['generated_at']}
- Generator: `864zeros-ISD/ISD-DIV-5-EVOLUTION/report_generator.py` v1.1

---
*OR generated in neutral hub. No vulture-nest writes performed.*
"""

    return emit_frontmatter(fm) + "\n\n" + body


# ============================================================================
# Historical-record OR (reconstructed from prior data)
# ============================================================================

def build_historical_or(*, target, codename, strike_id, source_notes=None,
                       score=None, scarcity_index=None,
                       z_convergence=None, z_velocity=None, z_scarcity=None,
                       rule_of_40=None, exit_multiplier=None,
                       traffic=None, stagnation=None, growth=None, margin=None,
                       pain_signal_count=None, sentiment_score=None,
                       competitors=None, build_status=None, factory_phase=None,
                       or_id=None):
    """
    Build an OR from manually-supplied historical / reconstructed data.
    No live scan, no adapter run, no math computation. Operator supplies
    values from prior dossiers / strike files. Verdict is inferred from
    supplied score + scarcity (if available), else from build_status.
    """
    competitors = list(competitors or [])

    # Verdict inference
    if score is not None and scarcity_index is not None:
        if scarcity_index > SCARCITY_THRESHOLD:
            verdict, verdict_gate = "TERMINATED", "scarcity"
        elif score < SCORE_THRESHOLD:
            verdict, verdict_gate = "TERMINATED", "score_threshold"
        else:
            verdict, verdict_gate = "PASSED", "passed_all_gates"
    elif build_status:
        verdict, verdict_gate = build_status, "n/a (factory state)"
    else:
        verdict, verdict_gate = "UNKNOWN", "n/a"

    fm = {
        "or_id": or_id,
        "or_type": "historical_record",
        "or_version": "1.1",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "target": target,
        "codename": codename or "unspecified",
        "strike_id": strike_id or "unknown",
        "verdict": verdict,
        "verdict_gate": verdict_gate,
        "data_source": "factory_build_manifest" if build_status else "reconstructed_from_strike_file",
    }

    # Optional fields — only emit what was supplied (keeps frontmatter honest)
    optional = {
        "vulture_score": score,
        "scarcity_index": scarcity_index,
        "scarcity_threshold_current": SCARCITY_THRESHOLD,
        "z_convergence": z_convergence,
        "z_velocity": z_velocity,
        "z_scarcity": z_scarcity,
        "rule_of_40": rule_of_40,
        "exit_multiplier": exit_multiplier,
        "traffic_monthly": traffic,
        "stagnation_months": stagnation,
        "growth_projection": growth,
        "margin_projection": margin,
        "pain_signal_count": pain_signal_count,
        "sentiment_score": sentiment_score,
        "competitors_count": len(competitors) if competitors else None,
        "build_status": build_status,
        "factory_phase": factory_phase,
    }
    for k, v in optional.items():
        if v is not None:
            fm[k] = v
    if competitors:
        fm["competitors"] = competitors

    body = f"""# Operational Record {or_id}
## {target} → {codename or 'unspecified'} (HISTORICAL)

**Type:** Historical reconstruction — no live scan re-run
**Strike ID:** {strike_id or 'unknown'}
**Verdict:** {verdict} ({verdict_gate})
"""
    if score is not None:
        body += f"**Score:** {score}\n"
    if build_status:
        body += f"**Build status:** {build_status}\n"

    if source_notes:
        body += f"\n> **Source notes:** {source_notes}\n"

    body += "\n---\n\n## 1. Strike Profile\n\n| Field | Value |\n|---|---|\n"
    body += f"| Target | {target} |\n"
    body += f"| Codename | {codename or '*unspecified*'} |\n"
    body += f"| Strike ID | {strike_id or 'unknown'} |\n"
    if traffic is not None:
        body += f"| Traffic (monthly) | {traffic:,} |\n"
    if stagnation is not None:
        body += f"| Stagnation (months) | {stagnation} |\n"
    if growth is not None:
        body += f"| Growth projection | {growth}% |\n"
    if margin is not None:
        body += f"| Margin projection | {margin}% |\n"
    if pain_signal_count is not None:
        body += f"| Pain signals | {pain_signal_count} |\n"
    if sentiment_score is not None:
        body += f"| Sentiment | {sentiment_score} |\n"

    if any(v is not None for v in [score, z_convergence, z_velocity, z_scarcity, rule_of_40]):
        body += f"""
## 2. Math Snapshot (from prior validation)

```
Z-Convergence: {z_convergence if z_convergence is not None else 'n/a'}
Z-Velocity:    {z_velocity if z_velocity is not None else 'n/a'}
Z-Scarcity:    {z_scarcity if z_scarcity is not None else 'n/a'}
Rule of 40:    {rule_of_40 if rule_of_40 is not None else 'n/a'}%
Exit mult:     {exit_multiplier if exit_multiplier is not None else 'n/a'}x
Final score:   {score if score is not None else 'n/a'}
```
"""

    if competitors:
        body += f"\n## 3. Competitor Landscape (at strike time)\n\n**Count:** {len(competitors)}\n\n"
        for c in competitors:
            body += f"- {c}\n"

    if build_status:
        body += f"""
## 4. Factory State

**Status:** {build_status}
**Phase:** {factory_phase or 'unspecified'}

Factory artifact: `864zeros-llc/LLC-DIV-3-FACTORY/output/{strike_id}-{codename.lower() if codename else 'unknown'}/`
"""

    body += f"""
## 5. Threshold Counterfactuals (current SCARCITY_THRESHOLD = {SCARCITY_THRESHOLD})

"""
    if scarcity_index is not None:
        for thr in [3, 5, 7]:
            would_pass = scarcity_index <= thr
            body += f"- `SCARCITY_THRESHOLD = {thr}`: scarcity check **{'PASSES' if would_pass else 'FAILS'}** ({scarcity_index} {'<=' if would_pass else '>'} {thr})\n"
    else:
        body += "*Scarcity data not available for counterfactual.*\n"

    body += f"""
## 6. Source Artifacts

- This OR generated: {fm['generated_at']}
- Generator: `report_generator.py` v1.1 — historical mode
- Data provenance: {fm['data_source']}

---
*Historical reconstruction. Math values are quoted from original validation; not recomputed in this cycle.*
"""

    return emit_frontmatter(fm) + "\n\n" + body


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="ISD-DIV-5-EVOLUTION (Neutral Hub) Operational Record generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="mode", required=True)

    p_full = sub.add_parser("full", help="Full-scan retrospective OR.")
    p_full.add_argument("strike_report", help="Path to STRIKE_REPORT_*.json (relative or absolute)")
    p_full.add_argument("--target", required=True)
    p_full.add_argument("--codename", default=None)
    p_full.add_argument("--traffic", type=int, required=True)
    p_full.add_argument("--stagnation", type=int, required=True)
    p_full.add_argument("--growth", type=float, required=True)
    p_full.add_argument("--margin", type=float, required=True)
    p_full.add_argument("--apify-queries", type=int, default=None)
    p_full.add_argument("--or-id", default=None)
    p_full.add_argument("--output", "-o", required=True)

    p_pre = sub.add_parser("preflight", help="Pre-flight-only OR.")
    p_pre.add_argument("--target", required=True)
    p_pre.add_argument("--codename", default=None)
    p_pre.add_argument("--sniff-target", default=None)
    p_pre.add_argument("--competitors", required=True)
    p_pre.add_argument("--queries-spent", type=int, default=3)
    p_pre.add_argument("--notes", default=None)
    p_pre.add_argument("--or-id", default=None)
    p_pre.add_argument("--output", "-o", required=True)

    p_hist = sub.add_parser("historical", help="Historical OR from prior dossier / strike-file data (no scan).")
    p_hist.add_argument("--target", required=True)
    p_hist.add_argument("--codename", default=None)
    p_hist.add_argument("--strike-id", required=True)
    p_hist.add_argument("--score", type=float, default=None)
    p_hist.add_argument("--scarcity", type=int, default=None)
    p_hist.add_argument("--z-conv", type=float, default=None)
    p_hist.add_argument("--z-vel", type=float, default=None)
    p_hist.add_argument("--z-scar", type=float, default=None)
    p_hist.add_argument("--rule-of-40", type=float, default=None)
    p_hist.add_argument("--exit-mult", type=float, default=None)
    p_hist.add_argument("--traffic", type=int, default=None)
    p_hist.add_argument("--stagnation", type=int, default=None)
    p_hist.add_argument("--growth", type=float, default=None)
    p_hist.add_argument("--margin", type=float, default=None)
    p_hist.add_argument("--pain-count", type=int, default=None)
    p_hist.add_argument("--sentiment", type=float, default=None)
    p_hist.add_argument("--competitors", default=None, help="Comma-separated competitor list")
    p_hist.add_argument("--build-status", default=None, help="e.g. STRIKE_QUALIFIED, BUILD_IN_PROGRESS, DEPLOYED")
    p_hist.add_argument("--factory-phase", default=None)
    p_hist.add_argument("--source-notes", default=None)
    p_hist.add_argument("--or-id", default=None)
    p_hist.add_argument("--output", "-o", required=True)

    args = parser.parse_args()

    if args.mode == "full":
        sr_path = Path(args.strike_report).resolve()
        with sr_path.open("r", encoding="utf-8") as f:
            sr = json.load(f)
        # Default OR-ID derived from output filename if --or-id omitted (avoids
        # date drift between filename and frontmatter on retrospective gens).
        or_id = args.or_id or Path(args.output).stem
        text = build_full_scan_or(
            strike_report=sr, target=args.target, codename=args.codename,
            traffic=args.traffic, stagnation=args.stagnation,
            growth=args.growth, margin=args.margin,
            or_id=or_id, strike_report_path=str(sr_path),
            apify_queries=args.apify_queries,
        )
    elif args.mode == "preflight":
        comps = [c.strip() for c in args.competitors.split(",") if c.strip()]
        or_id = args.or_id or Path(args.output).stem
        text = build_preflight_or(
            target=args.target, codename=args.codename,
            sniff_target=args.sniff_target, competitors=comps,
            queries_spent=args.queries_spent, or_id=or_id, notes=args.notes,
        )
    else:  # historical
        comps = [c.strip() for c in args.competitors.split(",") if c.strip()] if args.competitors else None
        or_id = args.or_id or Path(args.output).stem
        text = build_historical_or(
            target=args.target, codename=args.codename, strike_id=args.strike_id,
            source_notes=args.source_notes,
            score=args.score, scarcity_index=args.scarcity,
            z_convergence=args.z_conv, z_velocity=args.z_vel, z_scarcity=args.z_scar,
            rule_of_40=args.rule_of_40, exit_multiplier=args.exit_mult,
            traffic=args.traffic, stagnation=args.stagnation,
            growth=args.growth, margin=args.margin,
            pain_signal_count=args.pain_count, sentiment_score=args.sentiment,
            competitors=comps,
            build_status=args.build_status, factory_phase=args.factory_phase,
            or_id=or_id,
        )

    out = Path(args.output).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"[report_generator] Wrote: {out}")
    print(f"[report_generator] OR ID: {or_id}")


if __name__ == "__main__":
    main()
