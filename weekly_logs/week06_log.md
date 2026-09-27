# Week 06 Log — Data Quality Checks

**Week:** 6

**Date range:** 10 Sep 2026

**Team:** StayMetrics Team

**Project:** StayMetrics Hospitality Data Engineering

---

## 1. Sprint Goal

Run data quality checks on the standardized Silver data to identify missing values, duplicate records, invalid amounts, and missing event timestamps. Document the defined data quality checks and their results for the next stage of the pipeline.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Loaded the `silver_standardized_events` table for data quality validation | Akshara Sai Reddy | Done | `04_data_quality_checks.ipynb` |
| Created the `silver_events` temporary view | Akshara Sai Reddy | Done | `04_data_quality_checks.ipynb` |
| Implemented DQ-01 to check null `record_id` values | Akshara Sai Reddy | Done | `04_data_quality_checks.ipynb` |
| Implemented DQ-02 to identify duplicate `record_id` values | Akshara Sai Reddy | Done | `04_data_quality_checks.ipynb` |
| Implemented DQ-03 to identify negative `amount` values | Akshara Sai Reddy | Done | `04_data_quality_checks.ipynb` |
| Implemented DQ-04 to check null `event_timestamp` values | Akshara Sai Reddy | Done | `04_data_quality_checks.ipynb` |
| Reviewed the data quality checks and validation requirements | Abhinayasri Bairi | Done | Week 6 project work |
| Reviewed the data quality checks and validation requirements | Manusree Eerla | Done | Week 6 project work |
| Prepared the location for documenting data quality results | Akshara Sai Reddy | Done | `docs/data_quality_summary.md` |

---

## 3. Key Decisions

- Used `silver_standardized_events` as the input table for Week 6 data quality checks.
- Created the `silver_events` temporary view to run the SQL validation rules.
- Defined four checks covering null `record_id`, duplicate `record_id`, negative `amount`, and null `event_timestamp`.
- Kept the data quality checks separate so each rule can be reviewed independently.
- Planned to document the data quality results in `docs/data_quality_summary.md`.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Executed failure counts/results were not captured in the current notebook | Final DQ results cannot be reported from the notebook alone | Run the checks and record the actual outputs before final reporting |

---

## 5. Evidence Added to GitHub

- Updated `notebooks/04_data_quality_checks.ipynb`
- Added the four defined data quality checks
- Prepared `docs/data_quality_summary.md` for documenting the results

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI assisted with structuring the data quality checks and organizing the SQL validation logic. |
| What we changed after AI suggestion | The checks were adapted to the StayMetrics Silver table `silver_standardized_events` and its fields such as `record_id`, `amount`, and `event_timestamp`. |
| What we verified manually | The Silver input table, temporary view, four SQL data quality checks, and the documentation path were reviewed manually. |
| What we can explain without AI | We can explain why each data quality check is used and how the SQL identifies null record IDs, duplicate record IDs, negative amounts, and missing event timestamps. |

---

## 7. Next Week Preparation

- Review and document the executed Week 6 data quality results.
- Prepare the validated Silver data for the next stage of the StayMetrics pipeline.
