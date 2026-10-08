# Week 11 Log — Power BI Data Integration & Dashboard Preparation

**Week:** 11  
**Date range:** 28 September 2026 – 04 October 2026  
**Team:** Team 08  
**Project:** StayMetrics – Hotel Revenue & Occupancy Analytics Hub

---

## 1. Sprint Goal

The goal of this week was to connect the Databricks Gold-layer analytical tables with Power BI Desktop and prepare the data model for dashboard development. The focus was on validating the available Gold tables, selecting relevant fields, and preparing KPIs and visualizations for hotel revenue, bookings, and occupancy analysis.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Reviewed available Databricks Gold-layer tables | Abhinayasri | Done | Databricks table screenshot |
| Selected relevant Gold tables for Power BI | Abhinayasri | Done | Power BI Navigator screenshot |
| Connected Gold-layer data to Power BI Desktop | Abhinayasri | Done | Power BI Data pane |
| Loaded hotel booking and performance summary tables | Abhinayasri | Done | Power BI model |
| Reviewed fields required for dashboard KPIs | Abhinayasri | Done | Power BI Data pane |
| Created Total Bookings measure | Abhinayasri | Done | DAX measure |
| Created Total Revenue measure | Abhinayasri | Done | DAX measure |
| Created Total Rooms Booked measure | Abhinayasri | Done | DAX measure |
| Created Average Occupancy % measure | Abhinayasri | Done | DAX measure |
| Added initial KPI cards | Abhinayasri | Done | Power BI dashboard screenshot |
| Added initial Property and Channel slicers | Abhinayasri | Done | Power BI dashboard screenshot |

---

## 3. Key Decisions

- Selected the **Gold-layer summary tables** as the primary data source for Power BI because they provide prepared analytical data suitable for dashboard reporting.
- Decided to use **DAX measures** for important KPIs instead of relying only on raw column aggregations.
- Planned the Power BI report as **two dashboard pages** to avoid overcrowding and provide both executive and detailed analysis.
- Selected **Property, Channel, Date and Market Segment** as the main interactive filters.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Some Gold tables had permission/access restrictions during preview | Certain tables could not be directly previewed | Used accessible Gold summary tables for Power BI |
| Multiple tables contained similar revenue and booking fields | Required careful selection of appropriate measures | Validated fields against the Gold-layer structure |
| Large number of available fields | Initial dashboard design required field selection | Reviewed table schemas before visualization |

---

## 5. Evidence Added to GitHub

- Power BI data connection/model screenshots
- Gold-layer table screenshots
- KPI/DAX measure evidence
- Initial dashboard development screenshots
- Updated Week 11 log

Suggested evidence structure:

```text
screenshots/
├── powerbi_gold_tables.png
├── powerbi_data_model.png
└── powerbi_kpi_cards.png

weekly_logs/
└── week_11_log.md
```

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI was used to suggest suitable Gold-layer tables, KPI measures, dashboard structure, slicers, and appropriate Power BI visualizations. |
| What we changed after AI suggestion | We selected the final tables and fields based on the actual available data, adjusted the KPI definitions, and designed the dashboard according to the project requirements. |
| What we verified manually | Data fields, table availability, KPI outputs, Power BI visual behavior, slicers, and calculated values were manually checked. |
| What we can explain without AI | We can explain the Databricks Gold layer, Power BI data connection, DAX measures, KPI cards, slicers, and the purpose of each selected analytical table. |

---

## 7. Next Week Preparation

- Complete the two-page Power BI dashboard.
- Add revenue, occupancy, room-type and market-segment visualizations.
- Apply a consistent colorful and professional dashboard theme.
- Add final dashboard screenshots to GitHub.
- Continue dashboard validation and prepare final project documentation.
