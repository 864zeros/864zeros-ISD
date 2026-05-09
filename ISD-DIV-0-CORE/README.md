# ISD-DIV-0-CORE — Canonical Registries
**Role:** Single-source-of-truth datastores. Every other division reads from here; nothing else writes here without RULE-000 sign-off.
**Pillars served:** OIA / 864-Flux / FHG (pillar-agnostic — registries describe the substrate, not the surface).
**Source of truth:** `BRICK_REGISTRY.json` — every brick in the 864zeros stack with version, contract, and authority_rule mapping (RULE-001 through RULE-007).
**Governing rules:** RULE-000 (Architectural Governance — every brick promotion or registry mutation requires Office Architect sign-off + a SYSTEM_STRIKE_LOG entry).
