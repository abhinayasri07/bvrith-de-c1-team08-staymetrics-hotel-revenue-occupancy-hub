# Week 04 Log — Bronze Ingestion

**Week:** 4  
**Date range:** 31 Jul 2026 – 06 Aug 2026  
**Team:** StayMetrics Team  
**Project:** StayMetrics Hospitality Data Engineering

---

## 1. Sprint Goal

Build the Bronze ingestion layer by reading all approved batch source files from the Unity Catalog Volume into persistent Bronze Delta tables. Preserve the original business values, add ingestion metadata, reconcile source and Bronze record counts, and verify safe rerun behavior.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Environment setup | Akshara | Done | 02_bronze_ingestion.ipynb |
| Source inventory and file check | Akshara | Done | Notebook output |
| Guests Bronze ingestion | Akshara | Done | bronze_guests table |
| Rate Plans Bronze ingestion | Manusree | Done | bronze_rate_plans table |
| Room Nights Bronze ingestion | Manusree | Done | bronze_room_nights table |
| Rooms Bronze ingestion | Abhinaya | Done | bronze_rooms table |
| Bookings Bronze ingestion |Abhinaya | Done | bronze_bookings table |
| Source vs Bronze reconciliation | Abhinaya | Done | Reconciliation output |
| Safe rerun verification | Akshara | Done | DESCRIBE HISTORY output |
| GitHub updates and evidence | All Members | Done | GitHub repository |

---

## 3. Key Decisions

- Created one Bronze Delta table for each approved batch source file.
- Preserved the original source business values without applying business-level cleaning, filtering, aggregation, or deduplication in the Bronze layer.
- Added technical ingestion metadata to support traceability and lineage.
- Used overwrite mode for controlled reruns of the Bronze ingestion process.
- Verified that the controlled rerun did not introduce unintended duplicate records.
- Replaced the unsupported `input_file_name()` approach with a Unity Catalog-compatible method for source/file metadata.
---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Unity Catalog does not support `input_file_name()` | Source filename metadata could not be captured using the old method | Replaced with a Unity Catalog compatible approach and verified the notebook execution |

---

## 5. Evidence Added to GitHub

## 5. Evidence Added to GitHub

- Updated `notebooks/02_bronze_ingestion.ipynb`
- Added Week 4 execution screenshots in the repository evidence folder
- Updated `weekly_logs/week04_log.md`
- Added source-to-Bronze reconciliation evidence
- Added Delta history evidence for rerun verification

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI assisted with organizing the notebook structure, generating PySpark code compatible with Unity Catalog, and preparing the Week 4 documentation. |
| What we changed after AI suggestion | Updated the code to replace unsupported functions with Unity Catalog compatible code and corrected file paths. |
| What we verified manually | Verified all source files, Bronze tables, record counts, rerun behavior, and notebook outputs in Databricks. |
| What we can explain without AI | We can explain the Bronze ingestion workflow, Delta table creation, ingestion metadata, reconciliation process, rerun validation, and the purpose of each notebook section. |
---


## 7. Next Week Preparation

- Begin Bronze-to-Silver transformations for the approved StayMetrics source tables.
- Define the required data types and standardization rules for the Silver Candidate tables.
- Validate that Silver transformations preserve the expected physical row counts.
- Prepare transformation validation and execution evidence for Week 5.
