# Gold Metrics Definition

**Week:** 7  
**Purpose:** Define dashboard-ready Gold tables and KPI formulas.

---

## 1. Gold Table Catalog

| Gold Table Name | Grain | Source Table(s) | Purpose |
|---|---|---|---|
| `gold_event_summary_by_date` | One row per `booking_date + booking_status` | `silver_standardized_events` | Provide dashboard-ready daily booking metrics by booking status |

---

## 2. KPI Definitions

| KPI Name | Formula | Grain | Dashboard Page | Notes |
|---|---|---|---|---|
| `record_count` | `COUNT(*)` | `booking_date + booking_status` | W08 Dashboard | Number of records for each booking date and booking status |
| `total_amount` | `SUM(nightly_rate)` | `booking_date + booking_status` | W08 Dashboard | Total nightly rate for each booking date and booking status |
| `avg_amount` | `AVG(nightly_rate)` | `booking_date + booking_status` | W08 Dashboard | Average nightly rate for each booking date and booking status |

---

## 3. Validation Checks

Before using Gold tables in Power BI, verify:

- Gold table `gold_event_summary_by_date` was created successfully.
- Gold output contains `booking_date`, `booking_status`, `record_count`, `total_amount`, and `avg_amount`.
- Gold output contains 2,369 rows based on the current successful run.
- No unexpected nulls exist in key dashboard fields.
- KPI totals match manual spot checks.
- Power BI connects to Gold outputs only.
- Metric definitions are documented clearly.
- Gold grain is `booking_date + booking_status`.
