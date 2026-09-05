# Data Quality Summary

**Week:** 6

**Purpose:** Summarize data quality rules, detected failures, business impact, and handling approach for the StayMetrics Silver data.

---

## 1. Quality Rule Results

| Rule ID | Rule Name | Severity | Failed Count | Business Impact |
|---|---|---|---:|---|
| DQ-BKG-001 | Duplicate booking ID | Critical | 4 | Duplicate bookings can distort booking and revenue metrics |
| DQ-CAP-001 | Room capacity violation | Major | 316,308 | Capacity violations can affect occupancy and room utilization analysis |
| DQ-DAT-001 | Invalid date relationship | Critical | 4 | Invalid dates can make stay-duration and time-based metrics unreliable |
| DQ-MNY-001 | Invalid monetary value | Major | 4 | Invalid monetary values can affect revenue and financial metrics |
| DQ-RAT-001 | Invalid rate plan relationship | Major | 76,822 | Incorrect rate-plan relationships can affect pricing and revenue analysis |
| DQ-REF-001 | Invalid reference key | Critical | 224 | Invalid references can cause unreliable joins between business entities |
| DQ-RMN-001 | Overlapping occupied room allocation | Critical | 92,244 | Overlapping allocations can inflate occupancy and room-night metrics |
| DQ-STS-001 | Invalid booking status | Critical | 3 | Invalid statuses can cause incorrect booking-state reporting |

**Total detected failure records: 485,613**

> Note: Failed counts represent rule-level failure records. They should not be interpreted as the number of unique bad source rows because a single source record may fail more than one rule or may generate multiple failure records.

---

## 2. Failed Record Examples

| Rule ID | Sample Record ID | Failure Reason | Action / Handling |
|---|---|---|---|
| DQ-BKG-001 | `B0000001` | Duplicate booking ID detected | Flag for review and prevent duplicate records from contaminating trusted metrics |
| DQ-REF-001 | `B0000401` | Guest or rate-plan reference could not be matched | Quarantine/flag the affected record for reference-data review |
| DQ-RMN-001 | `RN000000005` | Overlapping occupied room allocation | Flag the room-night allocation for review before trusted occupancy reporting |

---

## 3. What Should Block Gold Metrics?

The following rules should block or strongly flag affected records before they contribute to trusted Gold metrics:

- **DQ-BKG-001 — Duplicate booking IDs:** Duplicate business keys can double-count bookings and revenue.
- **DQ-REF-001 — Invalid reference keys:** Broken references can produce incorrect joins and misleading dimensional analysis.
- **DQ-RMN-001 — Overlapping occupied room allocation:** Overlapping room allocations can inflate occupancy and room-night measures.
- **DQ-DAT-001 — Invalid date relationships:** Invalid stay dates can make duration and time-based metrics unreliable.
- **DQ-STS-001 — Invalid booking status:** Invalid statuses can lead to incorrect booking-state reporting.

Major-severity rules such as capacity, monetary, and rate-plan failures should be flagged and handled according to their impact before affected records are included in trusted Gold metrics.

---

## 4. Quality Summary

The Week 6 checks identified multiple data quality issues across the Silver data.
The largest rule-level failure count was **DQ-CAP-001**, with 316,308 failure records.
The next major failure counts were **DQ-RMN-001** with 92,244 and **DQ-RAT-001** with 76,822.
Critical failures involving duplicate bookings, invalid references, invalid dates, room allocation overlaps, and invalid statuses require particular attention because they can directly affect trusted business metrics.
The checks are designed to detect and document failures rather than silently dropping records.
Affected records should be flagged or quarantined before they are allowed to influence trusted Gold metrics.
The dataset should therefore not be considered fully trusted until the critical failures are reviewed and the DQ/quarantine handling is completed.
The mentor should review the high-volume capacity, room-night, and rate-plan failures carefully and confirm that the intended business rules match the synthetic dataset design.

---

## 5. Week 6 Evidence

The following validation evidence was captured in the Week 6 notebook:

- Silver Candidate tables loaded successfully.
- Candidate row counts were reconciled against Bronze counts.
- Duplicate booking IDs were identified.
- Reference-key failures were identified.
- Room-night allocation failures were identified.
- Capacity, date, monetary, rate-plan, and status checks were executed.
- Rule-level failure counts were summarized.
- Total detected failure records: **485,613**.
