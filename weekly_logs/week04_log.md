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

- Used separate Bronze Delta tables for each approved batch source file.
- Used overwrite mode to support safe rerun behavior without creating duplicate records.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Unity Catalog does not support `input_file_name()` | Source filename metadata could not be captured using the old method | Replaced with a Unity Catalog compatible approach and verified the notebook execution |

---

## 5. Evidence Added to GitHub

- Updated `notebooks/02_bronze_ingestion.ipynb`
- Added Week 4 execution screenshots in `evidence/week_04/`
- Updated `weekly/week_04_log.md`
- Added reconciliation output screenshots
- Added Delta history screenshot

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

- [Action]
- [Action]
