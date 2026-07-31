# Week 03 Log — [StayMetrics Hotel Revenue & Occupancy Hub]

**Week:** 3  
**Date range:** [28 Jul 2026-31Jul 2026]  
**Team:** [Team 08]  
**Project:** [StayMetrics – Hotel Revenue & Occupancy Hub]

---

## 1. Sprint Goal

Set up the Week 3 Databricks environment, explore all raw datasets, validate the data, create temporary SQL views, and build the Bronze demonstration table for the StayMetrics project.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Imported Week 3 notebook into Databricks | Abhinayasri | Done | Databricks screenshots |
| Loaded bookings, guests, rooms, rate plans and room nights datasets | Abhinayasri | Done | 01_data_exploration notebook |
| Performed schema inspection and exploratory data analysis | Abhinayasri | Done | Notebook output |
| Created temporary SQL views | Abhinayasri | Done | Notebook |
| Created Bronze demonstration table | Abhinayasri | Done | SQL execution screenshot |
| Validated Bronze table row count (80,000 rows) | Abhinayasri | Done | SQL result screenshot | |

---

## 3. Key Decisions

- Used Unity Catalog Volume as the data source.
- Read the rooms.json file using the multiline JSON option to resolve parsing issues.
- Verified source and Bronze row counts before continuing.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
JSON parsing issue for rooms.json | Prevented data exploration | Resolved by enabling multiline JSON reading |
| SQL cell executed as Python | SQL syntax error | Fixed using `%sql` magic command |


---

## 5. Evidence Added to GitHub

- Updated Week 03 log
- Added Week 3 Databricks setup screenshots
- Added data exploration screenshots
- Added Bronze table validation screenshots

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Assisted in troubleshooting Databricks notebook execution, JSON parsing issues, SQL syntax, and Bronze table creation. |
| What we changed after AI suggestion | Updated the JSON reader to use multiline mode and executed SQL cells using `%sql`. |
| What we verified manually | Verified schemas, SQL views, Bronze table creation, and confirmed the Bronze table contains 80,000 rows. |
| What we can explain without AI | The complete Week 3 workflow including data loading, exploration, SQL views, Bronze table creation, and validation. |

---

---

## 7. Next Week Preparation

- Begin Silver layer transformations.
- Implement data quality checks.
- Clean and standardize datasets.
- Prepare curated data for Gold layer analytics.
