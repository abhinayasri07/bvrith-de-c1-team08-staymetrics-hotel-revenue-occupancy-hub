# Week 08 Log — Power BI Dashboard

**Week:** 8  

**Date range:** [Add your Week 8 dates]  

**Team:** Team 08  

**Project:** StayMetrics – Hotel Revenue & Occupancy Hub

---

## 1. Sprint Goal

Create the first Power BI dashboard using only the Gold-layer output and present key booking and revenue metrics through clear visualizations.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Export Gold table for Power BI | Abhinayasri | Done | `notebooks/06_powerbi_export` |
| Export `gold_event_summary_by_date` to CSV | Abhinayasri | Done | Gold export in `/Volumes/workspace/default/my_files/gold_exports/gold_event_summary_by_date` |
| Create KPI cards | Abhinayasri | Done | `dashboard/StayMetrics_W08_PowerBI_Dashboard.pbix` |
| Create Bookings Over Time visual | Abhinayasri | Done | `dashboard/StayMetrics_W08_PowerBI_Dashboard.pbix` |
| Create Revenue Over Time visual | Abhinayasri | Done | `dashboard/StayMetrics_W08_PowerBI_Dashboard.pbix` |
| Create Bookings by Status visual | Abhinayasri | Done | `dashboard/StayMetrics_W08_PowerBI_Dashboard.pbix` |
| Save Power BI dashboard | Abhinayasri | Done | `dashboard/StayMetrics_W08_PowerBI_Dashboard.pbix` |

---

## 3. Key Decisions

- Power BI was connected to the Gold output only, following the project requirement.
- The `gold_event_summary_by_date` table was used as the source for dashboard metrics.
- KPI cards were created for Total Bookings, Total Revenue, and Average Nightly Rate.
- Line charts and a status distribution chart were used to present booking and revenue trends.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| No major blockers encountered | None | None |

---

## 5. Evidence Added to GitHub

- `notebooks/06_powerbi_export`
- `dashboard/StayMetrics_W08_PowerBI_Dashboard.pbix`
- Gold export of `gold_event_summary_by_date`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI was used to assist with SQL/query guidance, Power BI dashboard structuring, and troubleshooting during the implementation. |
| What we changed after AI suggestion | The suggested dashboard structure and implementation steps were adapted to the project's actual Gold table and available fields. |
| What we verified manually | The Gold export, Power BI visuals, KPI values, dashboard layout, and saved PBIX file were manually checked. |
| What we can explain without AI | We can explain the Gold table structure, KPI calculations, Power BI fields used, visualizations, and the dashboard data flow. |

---

## 7. Next Week Preparation

- Refine the Power BI dashboard with filters and insight notes.
- Review visual layout and improve dashboard presentation.
- Prepare the dashboard for Week 9 validation.
