# Week 07 Log — Gold Model, KPIs and Reconciliation

**Week:** 7  
**Date range:** 01 September 2026 – 05 September 2026  
**Team:** Team 08  
**Project:** StayMetrics — Hotel Revenue & Occupancy Hub

---

## 1. Sprint Goal

Build the governed Gold layer using Trusted Silver data, including dimensions, booking and room-night facts, daily business summaries, and hotel revenue and occupancy KPIs.

Validate the Gold outputs through reconciliation and manual spot checks so that the model is ready for downstream Power BI reporting.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Created `gold_dim_property` | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created `gold_dim_room` | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created `gold_dim_room_type` | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created `gold_dim_guest_segment` | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created `gold_fact_booking` at one row per trusted booking | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created `gold_fact_room_night` at one row per trusted room-night | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created daily property summary | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created daily room-type summary | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created daily channel/segment summary | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created daily rate-plan summary | Student | Done | `notebooks/05_gold_aggregations.ipynb` |
| Implemented hotel KPIs | Student | Done | `gold_property_kpis_final` |
| Validated Gold keys and fact grains | Student | Done | Notebook validation cells |
| Performed property/date reconciliation | Student | Done | Cell 18 output |
| Performed anchor booking reconciliation | Student | Done | Cell 18 output |
| Documented Gold metric definitions | Student | Done | `docs/gold_metrics_definition.md` |
| Updated pipeline walkthrough | Student | Done | `docs/pipeline_walkthrough.md` |

---

## 3. Key Decisions

- Kept booking facts at one row per trusted booking and room-night facts at one row per trusted room-night.
- Calculated occupancy, ADR, RevPAR and recognized room revenue from room-night grain.
- Available room nights exclude out-of-service inventory.
- Recognized room revenue is restricted to revenue-eligible trusted room nights.
- Implemented safe zero-denominator handling for ratio KPIs.
- Excluded cancelled and no-show bookings from Average Length of Stay.
- Used explicit status handling for cancellation and no-show rate calculations.
- Performed room-night aggregation before combining room-night metrics with booking-level outputs.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Week 5 GitHub PR has an existing merge conflict in `notebooks/03_silver_transformations.ipynb` | May affect final branch merge sequence | Resolve before final merge to `main` |
| One property has no trusted room-night KPI records | Room-night-derived KPIs are unavailable for that property | Review Trusted Silver/DQ routing if required |
| Databricks Free Edition environment | Development and Power BI connectivity options may be limited | Use available export configuration |

---

## 5. Evidence Added to GitHub

- `notebooks/05_gold_aggregations.ipynb`
- `docs/gold_metrics_definition.md`
- `docs/pipeline_walkthrough.md`
- `weekly_logs/week07_log.md`
- Gold dimension validation outputs
- Gold fact validation outputs
- Daily Gold summary validation outputs
- Final KPI reconciliation output
- Manual property/date spot-check output
- Anchor booking spot-check output

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI was used to help structure SQL transformations, Gold dimensions and facts, KPI calculations, validation queries, documentation and reconciliation checks. |
| What we changed after AI suggestion | SQL was adjusted to match the actual StayMetrics schemas and business rules, including the use of `booked_amount`, trusted-table grains, status values, and out-of-service availability handling. |
| What we verified manually | Gold row counts, unique keys, fact grains, daily summary counts, KPI reconciliation, one property/date trace, and one anchor booking trace were manually executed and reviewed in Databricks. |
| What we can explain without AI | The team can explain the Raw → Bronze → Silver Candidate → DQ → Trusted Silver → Gold flow, booking versus room-night grain, KPI formulas, denominator handling, reconciliation logic, and the purpose of each Gold table. |

---

## 7. Next Week Preparation

- Review the validated Gold outputs for downstream consumption.
- Prepare Gold data for Power BI export.
- Establish the Power BI data model and initial reporting structure.
- Carry forward the Gold KPI definitions and reconciliation evidence into the reporting layer.
