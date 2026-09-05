# Pipeline Walkthrough

**Week:** 5

**Purpose:** Explain the end-to-end StayMetrics data pipeline and the Week 5 Silver Candidate transformation flow.

---

## 1. Pipeline Run Order

| Step | Notebook / File | Output |
|---:|---|---|
| 1 | `src/generate_synthetic_data.py` | Synthetic raw and streaming source data |
| 2 | `notebooks/01_data_exploration.ipynb` | Data exploration and profiling evidence |
| 3 | `notebooks/02_bronze_ingestion.ipynb` | Bronze Delta tables |
| 4 | `notebooks/03_silver_transformations.ipynb` | Silver Candidate tables |
| 5 | `notebooks/04_data_quality_checks.ipynb` | Data quality rule results and quarantine outputs |
| 6 | `notebooks/05_gold_aggregations.ipynb` | Gold metric and aggregation tables |
| 7 | `notebooks/06_powerbi_export.ipynb` | Gold data prepared for Power BI |
| 8 | `notebooks/07_streaming_simulation.ipynb` | Streaming Bronze and live metric simulation |

---

## 2. Architecture Explanation

The StayMetrics pipeline follows a layered data engineering architecture.

Raw synthetic source files are generated and inspected before ingestion into the Bronze layer.

The Bronze layer stores the source data with lineage information such as ingestion timestamp, source file name, source system, and batch ID.

The Silver Candidate layer transforms Bronze data into typed and standardized tables while preserving the original source grain and row counts.

In Week 5, the `03_silver_transformations.ipynb` notebook creates Silver Candidate tables for bookings, guests, rate plans, rooms, and room nights.

Transformations include trimming string values, standardizing categories, and casting date and timestamp fields to appropriate data types.

Bronze-to-Silver reconciliation checks are performed to confirm that records are not silently lost during transformation.

The Data Quality layer validates business rules and routes invalid records to quarantine where required.

Trusted Silver data is then used by the Gold layer to calculate business metrics such as revenue, occupancy, ADR, and RevPAR.

Gold outputs are prepared for Power BI reporting, while the streaming notebook demonstrates near-real-time event processing.

Overall flow:

`Raw Sources → Bronze → Silver Candidate → Data Quality → Trusted Silver → Gold → Power BI`

Streaming simulation operates alongside the batch pipeline for near-real-time processing evidence.

---

## 3. Week 5 Silver Candidate Transformation

The Week 5 transformation notebook is:

`notebooks/03_silver_transformations.ipynb`

The notebook creates the following Silver Candidate tables:

| Source Bronze Table | Silver Candidate Table | Source Grain |
|---|---|---|
| `bronze_bookings` | `silver_bookings_candidate` | One row per booking |
| `bronze_guests` | `silver_guests_candidate` | One row per guest |
| `bronze_rate_plans` | `silver_rate_plans_candidate` | One row per rate plan |
| `bronze_room_nights` | `silver_room_nights_candidate` | One row per room-night |
| `bronze_rooms` | `silver_rooms_candidate` | One row per room |

The transformation keeps Bronze lineage fields and creates standardized Silver Candidate representations.

Date and timestamp fields are converted to appropriate Spark data types using safe casting where applicable.

String fields are trimmed and categorical fields are standardized to improve consistency.

The transformation does not intentionally drop records because candidate transformation must preserve source grain and support later data-quality validation.

---

## 4. Bronze-to-Silver Reconciliation

Bronze and Silver Candidate row counts were compared after transformation.

| Table | Bronze Count | Silver Candidate Count |
|---|---:|---:|
| Bookings | 80,000 | 80,000 |
| Guests | 55,000 | 55,000 |
| Rate Plans | 3,000 | 3,000 |
| Room Nights | 210,000 | 210,000 |
| Rooms | 1,200 | 1,200 |

The reconciliation confirms that the Silver Candidate transformations preserved the expected source row counts for all five tables.

No silent row loss was observed during the Week 5 transformation and reconciliation checks.

---

## 5. Known Limitations

- The project uses synthetic data rather than production hotel data.
- The Silver Candidate layer focuses on transformation and standardization; business-rule validation is handled in the Data Quality stage.
- Databricks Free Edition is used for development and validation.
- Notebook outputs may not be stored in Git when workspace-level output committing is disabled.
- Power BI integration is dependent on the available development environment and export configuration.
- Streaming functionality is a simulation and does not represent a production streaming infrastructure.
- Some business rules may require additional validation as the project progresses.

---

## 6. How to Reproduce

A mentor can review or reproduce the project using the following sequence:

1. Clone or open the Git repository.

2. Review `README.md` and the project data assumptions.

3. Review or generate the synthetic source data.

4. Run `notebooks/01_data_exploration.ipynb` to understand the source datasets.

5. Run `notebooks/02_bronze_ingestion.ipynb` to create the Bronze tables.

6. Run `notebooks/03_silver_transformations.ipynb` to create the Silver Candidate tables.

7. Verify the Bronze-to-Silver row-count reconciliation.

8. Review `docs/data_dictionary.md` for field definitions and data types.

9. Run `notebooks/04_data_quality_checks.ipynb` for validation and quarantine processing.

10. Run `notebooks/05_gold_aggregations.ipynb` to generate business metrics.

11. Run `notebooks/06_powerbi_export.ipynb` to prepare Gold outputs for Power BI.

12. Run `notebooks/07_streaming_simulation.ipynb` to review the streaming simulation.

13. Review the weekly logs and GitHub evidence for implementation and validation details.

---

## 7. Week 5 Validation Evidence

The following validation activities were completed for the Week 5 Silver Candidate transformation:

- Silver Candidate tables were created successfully.
- Sample records were inspected after transformation.
- Data types were reviewed using table schema information.
- Bronze and Silver Candidate row counts were compared.
- All five source tables retained their expected row counts.
- Source lineage fields were retained in the Candidate tables.
- Changes were committed to the Week 5 Git branch.

---

## 8. Git Evidence

Week 5 implementation was committed and pushed to the Git branch:

`week05-silver-transformations`

Commit message:

`week05: complete silver candidate transformations and validation`

The Week 5 log was also updated with implementation, validation, AI transparency, and next-week preparation details.

---

## 9. Week 6 Handoff

The next stage of the pipeline is Data Quality validation.

Week 6 will build on the Silver Candidate tables by applying data-quality rules, identifying invalid records, and implementing quarantine handling.

The validated records will then form the basis for the Trusted Silver layer used by downstream Gold aggregations.
