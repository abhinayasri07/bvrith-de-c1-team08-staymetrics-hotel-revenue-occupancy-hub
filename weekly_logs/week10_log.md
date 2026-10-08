# Week 10 Log — Gold Layer Validation & Power BI Preparation

**Week:** 10  
**Date range:** 21 September 2026 – 27 September 2026  
**Team:** Team 08  
**Project:** StayMetrics – Hotel Revenue & Occupancy Analytics Hub

---

## 1. Sprint Goal

The goal of this week was to validate the Databricks Gold-layer outputs and prepare the required analytical tables for Power BI integration. The focus was on checking the Gold tables, validating important revenue, booking and occupancy fields, and preparing the data for dashboard development.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Reviewed Gold-layer tables and outputs | Abhinayasri | Done | Databricks screenshots |
| Validated Gold summary tables required for reporting | Abhinayasri | Done | Gold table screenshots |
| Checked booking, revenue and occupancy fields | Abhinayasri | Done | Databricks table/schema screenshots |
| Reviewed `gold_booking_summary` | Abhinayasri | Done | Databricks screenshot |
| Reviewed `gold_daily_property_summary` | Abhinayasri | Done | Databricks screenshot |
| Reviewed `gold_daily_channel_segment_summary` | Abhinayasri | Done | Databricks screenshot |
| Reviewed `gold_daily_rate_plan_summary` | Abhinayasri | Done | Databricks screenshot |
| Reviewed `gold_daily_room_type_summary` | Abhinayasri | Done | Databricks screenshot |
| Prepared Gold outputs for Power BI consumption | Abhinayasri | Done | Power BI preparation evidence |
| Identified required KPIs and dashboard dimensions | Abhinayasri | Done | Planning notes / screenshots |

---

## 3. Key Decisions

- Selected the **Gold summary tables** as the main analytical sources for the Power BI dashboard.
- Identified **bookings, revenue, rooms booked, occupancy, room type, rate plan, channel and market segment** as the key business dimensions and metrics.
- Decided to avoid unnecessary raw-layer data in Power BI and use the prepared Gold-layer outputs wherever possible.
- Planned to build an interactive Power BI dashboard using KPIs, slicers and analytical charts.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Some Gold tables had access/permission restrictions | Certain tables could not be directly previewed | Used accessible Gold summary tables |
| Multiple Gold tables contained related revenue metrics | Required careful selection of the correct revenue field | Cross-checked table schemas and business meaning |
| Large number of Gold tables available | Required filtering the tables to those relevant for Power BI | Selected the main analytical summary tables |

---

## 5. Evidence Added to GitHub

- Gold-layer table screenshots
- Gold table validation evidence
- Power BI preparation screenshots
- Updated Week 10 log
- Relevant Databricks notebook/output evidence

Suggested files:

```text
weekly_logs/
└── week_10_log.md

screenshots/
├── gold_booking_summary.png
├── gold_daily_property_summary.png
├── gold_daily_channel_segment_summary.png
├── gold_daily_rate_plan_summary.png
└── gold_daily_room_type_summary.png
```

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped identify relevant Gold-layer tables, suggest important KPIs and recommend which fields could be used for Power BI analysis. |
| What we changed after AI suggestion | We manually selected the final Gold tables and fields based on the actual project data and available tables in Databricks. |
| What we verified manually | Gold table availability, field names, revenue and occupancy columns, table outputs and access permissions were manually checked in Databricks. |
| What we can explain without AI | We can explain the purpose of the Gold layer, the selected analytical tables, the important business metrics, and how the Gold outputs will be used for Power BI dashboard development. |

---

## 7. Next Week Preparation

- Connect the validated Gold tables to Power BI Desktop.
- Create KPI measures for bookings, revenue, rooms and occupancy.
- Add interactive slicers for property, channel, date and market segment.
- Begin development of the professional two-page Power BI dashboard.
