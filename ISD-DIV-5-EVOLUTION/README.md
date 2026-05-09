# ISD-DIV-5-EVOLUTION — Strike Tracking, Reporting, Post-Mortems
**Role:** Append-only ledger of every Strike's lifecycle, gate transitions, defect logs, and harvest decisions. Where the system records what it has learned.
**Pillars served:** All three (records strikes by all pillars; tracks per-pillar strike velocity and defect density).
**Source of truth:** `BACKLOG.md` (Active Sprint + Recently Completed), `STRIKE_HISTORY_MASTER.md` (strike outcomes), `reports/SYSTEM_STRIKE_LOG.md` (append-only system event ledger — gate passes, hook failures, brick promotions).
**Governing rules:** RULE-000 (every strike harvest, brick promotion, or rule codification requires Office Architect sign-off AND a SYSTEM_STRIKE_LOG entry — never edit prior entries; append only).
