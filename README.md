# StayMetrics: Hotel Revenue & Occupancy Hub

> Student note: Start with `00_START_HERE.md` and `00_TEMPLATE_INDEX.md`. The placeholder files inside this repository are templates.

**Program:** ZENAIZ × BVRIT Hyderabad Data Engineering Internship Program

**Track:** Data Engineering

**Duration:** 12 Weeks

**Team:** Team 08

**Students:**
- Abhinayasri Bairi
- Manusree Eerla
- Patlolla Akshara Sai Reddy

**AI Teammate:** Used responsibly for explanation, debugging, review, and documentation support.

---

# 1. Project Summary

**Domain:** Hospitality – Fictional Hotel Group

**Core Engineering Problem:**

Hotel booking information is collected from multiple sources such as bookings, guest details, room information, and rate plans. These datasets often contain duplicate records, missing values, invalid room references, inconsistent booking statuses, and incorrect room rates. The objective of this project is to build a reliable data engineering pipeline that cleans, validates, transforms, and integrates the data into trusted business insights.

**Main Pipeline:**

Raw Sources → Bronze → Silver → Data Quality → Gold → Power BI → Streaming Simulation

**Final Outcome:**

Develop a complete end-to-end data engineering solution that produces trusted hotel revenue and occupancy insights through Gold tables, interactive Power BI dashboards, live booking simulations, and complete GitHub documentation.

---

# 2. Tools Used

| Tool | Purpose |
|------|---------|
| Databricks Free Edition | Data processing using Spark SQL and PySpark |
| GitHub | Version control, documentation and weekly evidence |
| Power BI Desktop | Dashboard creation from Gold tables |
| Python | Synthetic data generation |
| Spark SQL | Data transformation and analysis |
| AI Assistant | Documentation, debugging and learning support |

---

# 3. Repository Navigation

| Folder / File | Purpose |
|--------------|---------|
| docs/ | Project documentation, data dictionary and references |
| src/ | Synthetic data generation scripts |
| notebooks/ | Databricks notebooks |
| data_sample/ | Sample datasets |
| dashboard/ | Power BI dashboard files |
| streaming/ | Streaming simulation files |
| screenshots/ | Weekly evidence screenshots |
| weekly_logs/ | Weekly progress logs |
| final_submission/ | Final report and submission files |

---

# 4. 12-Week Execution Map

| Week | Focus | Deliverable |
|------|-------|-------------|
| Week 1 | Project setup | README, Problem Charter, Week 1 Log |
| Week 2 | Dataset design | Data dictionary and sample datasets |
| Week 3 | Databricks exploration | Data exploration notebook |
| Week 4 | Bronze ingestion | Bronze tables |
| Week 5 | Silver standardization | Silver tables |
| Week 6 | Data quality | DQ report |
| Week 7 | Gold metrics | Gold tables |
| Week 8 | Power BI | Initial dashboard |
| Week 9 | Dashboard refinement | Final dashboard |
| Week 10 | Streaming simulation | Live booking metrics |
| Week 11 | Integration | Complete pipeline |
| Week 12 | Final demo | Final presentation |

---

# 5. Important Rules

- Power BI must connect only to Gold tables.
- Use only synthetic hotel booking data.
- Do not upload full datasets to GitHub.
- Maintain weekly GitHub commits.
- Verify AI-generated content before submission.
- Document weekly project progress.

---

# 6. Final Project Proof

By the end of this internship, our repository will demonstrate:

- Synthetic hotel booking dataset generation.
- Bronze layer implementation.
- Silver layer standardization.
- Data quality validation.
- Gold business metrics.
- Power BI dashboard built from Gold tables.
- Streaming booking event simulation.
- Weekly GitHub documentation.
- End-to-end explainable data engineering pipeline.
