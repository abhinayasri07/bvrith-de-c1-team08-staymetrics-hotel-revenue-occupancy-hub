# Pipeline Walkthrough

**Week:** 7

**Purpose:** Explain the end-to-end StayMetrics data pipeline and the Week 7 Gold model, KPI and reconciliation flow.

---

## 1. Pipeline Run Order

| Step | Notebook / File | Output |
|---:|---|---|
| 1 | `src/generate_synthetic_data.py` | Synthetic raw and streaming source data |
| 2 | `notebooks/01_data_exploration.ipynb` | Data exploration and profiling evidence |
| 3 | `notebooks/02_bronze_ingestion.ipynb` | Bronze Delta tables |
| 4 | `notebooks/03_silver_transformations.ipynb` | Silver Candidate tables |
| 5 | `notebooks/04_data_quality_checks.ipynb` | DQ results, Trusted Silver and quarantine outputs |
| 6 | `notebooks/05_gold_aggregations.ipynb` | Gold dimensions, facts, summaries and KPIs |
| 7 | `notebooks/06_powerbi_export.ipynb` | Gold data prepared for Power BI |
| 8 | `notebooks/07_streaming_simulation.ipynb` | Streaming Bronze and live metric simulation |

---

## 2. Architecture Explanation

The StayMetrics pipeline follows a layered data engineering architecture.

Raw synthetic source files are generated and inspected before ingestion into the Bronze layer.

The Bronze layer stores source-preserving data together with lineage information such as ingestion timestamp, source file name, source system and batch ID.

The Silver Candidate layer transforms Bronze data into typed and standardized representations while preserving source grain.

The Data Quality layer applies business and data-quality rules. Invalid records are routed to quarantine while accepted records form the Trusted Silver layer.

The Gold layer consumes Trusted Silver data and creates governed dimensions, facts, daily summaries and business KPIs.

The Gold model separates booking-level and room-night-level grains:

- Booking facts contain one row per trusted booking.
- Room-night facts contain one row per trusted room-night.
- Occupancy, ADR, RevPAR and recognized room revenue are calculated from room-night grain.
- Room-night data is aggregated before being combined with booking-level outputs.

Overall flow:

`Raw Sources → Bronze → Silver Candidate → Data Quality → Trusted Silver → Gold → Power BI`

Streaming simulation operates alongside the batch pipeline for near-real-time processing evidence.

---

## 3. Week 7 Gold Model

The Week 7 implementation is contained in:

`notebooks/05_gold_aggregations.ipynb`

The Gold layer contains the following dimensions:

| Gold Dimension | Grain |
|---|---|
| `gold_dim_property` | One row per property |
| `gold_dim_room` | One row per physical room |
| `gold_dim_room_type` | One row per property and room type |
| `gold_dim_guest_segment` | One row per guest/market segment |

The required Week 7 dimensions were validated for unique business keys.

The Gold layer contains the following facts:

| Gold Fact | Grain |
|---|---|
| `gold_fact_booking` | One row per trusted booking |
| `gold_fact_room_night` | One row per trusted room-night |

The booking fact also contains derived fields including:

- `stay_nights`
- `party_size`
- `booking_month`
- `stay_length_band`

The room-night fact contains the trusted occupancy, availability and revenue measures used by downstream KPIs.

---

## 4. Daily Gold Summaries

The following daily Gold summaries were created from the appropriate fact grain:

| Gold Summary | Grouping |
|---|---|
| `gold_daily_property_summary` | Property + stay date |
| `gold_daily_room_type_summary` | Property + room type + stay date |
| `gold_daily_channel_segment_summary` | Booking date + channel + market segment |
| `gold_daily_rate_plan_summary` | Property + rate plan + stay date |

The daily property summary contains:

- Occupied room nights
- Available room nights
- Recognized room revenue
- Occupancy rate

Available room nights exclude out-of-service inventory.

Recognized room revenue is restricted to revenue-eligible trusted room nights.

---

## 5. KPI Model

The final KPI table is:

`gold_property_kpis_final`

The following KPIs were implemented:

| KPI | Definition |
|---|---|
| Total Bookings | Distinct trusted booking IDs |
| Occupied Room Nights | Sum of occupied room-night flags |
| Available Room Nights | Available inventory excluding out-of-service nights |
| Occupancy Rate | Occupied room nights / available room nights |
| Recognized Room Revenue | Revenue from revenue-eligible trusted room nights |
| ADR | Recognized room revenue / occupied room nights |
| RevPAR | Recognized room revenue / available room nights |
| Cancellation Rate | Cancelled bookings / trusted bookings |
| No-show Rate | No-show bookings / eligible trusted bookings |
| Average Length of Stay | Average stay nights excluding cancelled and no-show bookings |

All ratio calculations use safe zero-denominator handling.

This prevents divide-by-zero errors when the relevant denominator is zero.

---

## 6. Week 7 Validation and Reconciliation

Gold dimension validation produced:

| Table | Rows | Unique Keys |
|---|---:|---:|
| `gold_dim_property` | 9 | 9 |
| `gold_dim_room` | 1,200 | 1,200 |
| `gold_dim_room_type` | 33 | 33 |
| `gold_dim_guest_segment` | 4 | 4 |

Gold fact validation produced:

| Table | Rows | Unique Keys |
|---|---:|---:|
| `gold_fact_booking` | 2,842 | 2,842 |
| `gold_fact_room_night` | 117,756 | 117,756 |

Daily Gold summaries were successfully created:

| Summary | Rows |
|---|---:|
| `gold_daily_property_summary` | 2,981 |
| `gold_daily_room_type_summary` | 11,851 |
| `gold_daily_channel_segment_summary` | 2,183 |
| `gold_daily_rate_plan_summary` | 84,331 |

The final Gold KPI validation returned:

- 9 properties
- 9 unique properties
- 2,842 trusted bookings
- 117,756 occupied room nights
- 117,756 available room nights
- Recognized room revenue populated

---

## 7. Manual Spot-Check Evidence

A property/date spot check was performed for:

`P01 / 2025-01-01`

The trusted Gold fact values matched the daily property summary:

| Metric | Trusted Fact | Gold Summary | Result |
|---|---:|---:|---|
| Occupied Room Nights | 14 | 14 | PASS |
| Available Room Nights | 14 | 14 | PASS |
| Recognized Room Revenue | 82,241.85 | 82,241.85 | PASS |

An anchor booking check was also performed for:

`B0000012`

| Metric | Trusted Source | Gold Fact | Result |
|---|---:|---:|---|
| Booked Amount | 51,903.18 | 51,903.18 | PASS |
| Booking Status | CHECKED_OUT | CHECKED_OUT | PASS |

The spot checks confirmed that Gold outputs remained traceable to the underlying trusted data.

---

## 8. Known Limitations

- The project uses synthetic data rather than production hotel data.
- Databricks Free Edition is used for development and validation.
- Gold outputs depend on the quality and completeness of Trusted Silver data.
- Some properties may not have trusted room-night records and therefore may have no room-night-derived KPI values.
- Power BI integration is dependent on the available development environment and export configuration.
- Streaming functionality is a simulation and does not represent production streaming infrastructure.

---

## 9. How to Reproduce

A mentor can review or reproduce the project using the following sequence:

1. Clone or open the Git repository.

2. Review `README.md` and the project data assumptions.

3. Review or generate the synthetic source data.

4. Run `notebooks/01_data_exploration.ipynb`.

5. Run `notebooks/02_bronze_ingestion.ipynb`.

6. Run `notebooks/03_silver_transformations.ipynb`.

7. Run `notebooks/04_data_quality_checks.ipynb`.

8. Verify Trusted Silver and quarantine outputs.

9. Run `notebooks/05_gold_aggregations.ipynb`.

10. Validate Gold dimensions and fact keys.

11. Validate the daily Gold summaries.

12. Review `gold_property_kpis_final` and the KPI formulas.

13. Review the manual property/date and anchor-booking reconciliation checks.

14. Run `notebooks/06_powerbi_export.ipynb` for downstream Power BI preparation.

15. Review the weekly logs and GitHub evidence for implementation and validation details.

---

## 10. Week 7 Validation Evidence

The following validation activities were completed for the Week 7 Gold implementation:

- Gold dimensions were created and unique keys were validated.
- Gold booking fact was created at one row per trusted booking.
- Gold room-night fact was created at one row per trusted room-night.
- Daily property, room-type, channel/segment and rate-plan summaries were created.
- KPI formulas were implemented with explicit status exclusions.
- Zero-denominator handling was implemented for ratio KPIs.
- Gold fact and summary outputs were reconciled.
- One property/date was manually traced from the Gold fact to the daily summary.
- One anchor booking was traced from Trusted Silver to the Gold booking fact.
- All five manual spot-check comparisons returned `PASS`.

---

## 11. Git Evidence

Week 7 implementation updates are contained in:

`notebooks/05_gold_aggregations.ipynb`

The Week 7 documentation files are:

- `docs/gold_metrics_definition.md`
- `docs/pipeline_walkthrough.md`
- `weekly_logs/week07_log.md`

The final Week 7 commit should capture the Gold model, KPI, reconciliation and documentation changes.

---

## 12. Week 8 Handoff

The next stage is Gold export and Power BI foundation.

Week 8 will consume the validated Gold outputs to prepare reporting datasets and establish the Power BI model and initial reporting page.

The Week 7 Gold layer provides the governed dimensions, facts, summaries and KPI definitions required for that downstream hand-off.
