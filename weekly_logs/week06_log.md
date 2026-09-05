# Week 06 Log — Data Quality & Trusted Silver

**Week:** 6

**Date range:** [Add official Week 06 date range]

**Team:** Team 08

**Project:** P08 StayMetrics — Hotel Revenue & Occupancy Hub

---

## 1. Sprint Goal

Implement and validate the StayMetrics data quality layer for Silver Candidate data.

Create Trusted Silver and Quarantine routing so that failed records are retained with DQ reasons and severity, while valid records proceed to Trusted Silver. Demonstrate rework and replay of a failed booking.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Implemented StayMetrics data quality rules | Team 08 | Done | `src/data_quality_rules.py` |
| Implemented DQ checks for 8 defined rules | Team 08 | Done | `notebooks/04_data_quality_checks.ipynb` |
| Validated DQ rule failures | Team 08 | Done | DQ results in `04_data_quality_checks.ipynb` |
| Created Trusted Silver booking routing | Team 08 | Done | Cell 40 |
| Validated Trusted booking count | Team 08 | Done | Cell 41 — 2,842 trusted bookings |
| Created booking quarantine routing | Team 08 | Done | Cell 42 |
| Validated booking quarantine | Team 08 | Done | Cell 43 |
| Reconciled booking routing | Team 08 | Done | Cell 44 — 79,997 distinct bookings routed |
| Created Trusted Silver room-night routing | Team 08 | Done | Cell 45 |
| Validated Trusted room-night count | Team 08 | Done | Cell 46 — 117,756 trusted room nights |
| Created room-night quarantine routing | Team 08 | Done | Cell 47 |
| Validated room-night quarantine | Team 08 | Done | Cell 48 — 92,244 quarantined room nights |
| Final Trusted/Quarantine reconciliation | Team 08 | Done | Cell 49 |
| Demonstrated rework and replay | Team 08 | Done | Cells 37–39 — B0000003 |

### DQ Results

The 8 Week 06 rules produced the following rule-level failure counts:

| Rule ID | Severity | Failure Count |
|---|---|---:|
| DQ-BKG-001 | Critical | 4 |
| DQ-CAP-001 | Major | 316,308 |
| DQ-DAT-001 | Critical | 4 |
| DQ-MNY-001 | Major | 4 |
| DQ-RAT-001 | Major | 76,822 |
| DQ-REF-001 | Critical | 224 |
| DQ-RMN-001 | Critical | 92,244 |
| DQ-STS-001 | Critical | 3 |

**Total rule-level failure records: 485,613**

The total is a rule-level count. A single record can fail multiple rules, so it must not be interpreted as the number of unique bad records.

### Routing Results

**Bookings**

- Candidate rows: 80,000
- Candidate distinct booking IDs: 79,997
- Trusted distinct bookings: 2,842
- Quarantined distinct bookings: 77,155
- Trusted + Quarantine: 79,997

The 3-row difference between candidate rows and distinct booking IDs is due to duplicate booking IDs in the candidate data.

**Room Nights**

- Candidate rows: 210,000
- Trusted room nights: 117,756
- Quarantined room nights: 92,244
- Trusted + Quarantine: 210,000

The room-night routing reconciled completely with the candidate dataset.

---

## 3. Key Decisions

- DQ results are retained at rule level so that multiple failures for the same record are not silently removed.
- Failed booking records are routed to `silver_bookings_quarantine` with the failed rule ID, severity, failure reason, and `PENDING_REWORK` status.
- Failed room-night records are routed to `silver_room_nights_quarantine` using `DQ-RMN-001`.
- Trusted Silver contains records that pass the applicable DQ rules.
- Reconciliation uses distinct business IDs where duplicate IDs exist, rather than treating duplicate IDs as missing records.
- Rework must correct the upstream cause and replay the DQ checks before acceptance.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Initial DQ routing required schema verification because the DQ result column names differed from the initial SQL assumptions | Routing SQL required correction before execution | Resolved by checking the Databricks schema/error output |
| Duplicate booking IDs caused an apparent 3-record reconciliation difference | Could be incorrectly interpreted as missing records | Resolved by comparing row counts with distinct booking IDs |
| Multiple DQ failures can occur for the same record | Rule-level counts cannot be treated as unique bad-record counts | Preserved multi-rule failure records in quarantine |

---

## 5. Evidence Added to GitHub

- `src/data_quality_rules.py`
- `notebooks/04_data_quality_checks.ipynb`
- `docs/data_quality_summary.md`
- `weekly_logs/week06_log.md`

The Week 06 notebook and data quality rules were committed and pushed to the Week 06 Git branch.

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI assisted with structuring the PySpark/SQL data quality checks, Trusted Silver routing, Quarantine routing, reconciliation queries, and documentation structure. |
| What we changed after AI suggestion | SQL was adjusted after checking the actual Databricks schema. For example, the DQ result columns were corrected from assumed names to the actual `severity` and `failure_reason` columns. |
| What we verified manually | DQ failure counts, Trusted/Quarantine counts, booking reconciliation, room-night reconciliation, and the B0000003 rework/replay result were executed and checked directly in Databricks. |
| What we can explain without AI | We can explain the purpose of each DQ rule, why failed records are quarantined, why multi-rule failures are retained, how Trusted/Quarantine reconciliation works, and how rework and replay move a record from failure to acceptance. |

---

## 7. Next Week Preparation

- Review the Trusted Silver outputs for downstream Gold aggregation.
- Ensure only validated Trusted Silver data is used for Gold-layer metrics.
- Prepare the Gold aggregation workflow and validation checks.
- Preserve Week 06 Git and Databricks evidence for the project review.
