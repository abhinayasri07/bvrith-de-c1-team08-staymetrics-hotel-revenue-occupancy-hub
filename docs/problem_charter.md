# Problem Charter

**Week:** 1  
**Owner(s):** Abhinayasri Bairi, Manusree Eerla, Patlolla Akshara Sai Reddy  
**Project:** StayMetrics: Hotel Revenue & Occupancy Hub

---

## 1. Problem Context

StayMetrics represents the operations of a fictional hotel group that manages hotel bookings, room availability, guest information, and revenue. Every booking generates data such as booking details, room type, guest profile, cancellation status, check-in and check-out dates, and payment information.

Since this data comes from multiple sources, it may contain duplicate records, missing values, invalid room references, and inconsistent booking information. Raw data alone cannot provide reliable business insights. Therefore, it must be cleaned, validated, and transformed before it can be used for analysis.

The final dashboards and business metrics will help Revenue Managers, Hotel Operations Managers, Front Office Managers, and Commercial Analysts monitor hotel occupancy, revenue, cancellations, and booking trends for better decision-making.

---

## 2. Engineering Problem

The project converts multiple raw hotel booking source files into trusted Bronze, Silver, Data Quality, Gold, and dashboard-ready outputs using Databricks and Power BI.

The pipeline ensures that inconsistent and low-quality data is identified, validated, standardized, and transformed into reliable business metrics for hotel revenue and occupancy analysis.

---

## 3. Users / Stakeholders

| User / Stakeholder | What they need from the data |
|---|---|
| Revenue Manager | Monitor hotel revenue, ADR, RevPAR, and room performance |
| Hotel Operations Manager | Track occupancy, room availability, and operational efficiency |
| Front Office Manager | Monitor daily check-ins, check-outs, and cancellations |
| Commercial Analyst | Analyze booking trends, customer segments, and cancellation patterns |
| Business Management | Make strategic decisions using trusted business metrics |

---

## 4. Scope Inclusions

The project includes:

- Synthetic hotel booking data generation
- Bronze data ingestion
- Silver data standardization
- Data quality validation
- Gold business metrics
- Power BI dashboard development
- Streaming booking event simulation
- GitHub documentation and weekly evidence

---

## 5. Scope Exclusions

The project will not include:

- Production hotel booking application
- Real hotel or customer data
- Payment gateway integration
- Online booking website development
- Copied internet project submissions
- Fake screenshots or unexplained AI-generated work
- Direct Power BI connection to raw datasets

---

## 6. Success Criteria

By the end of the 12-week internship, the project will be considered successful if:

- The complete data engineering pipeline can be explained from source data to dashboard.
- Bronze, Silver, Data Quality, Gold, Power BI, and Streaming layers are successfully implemented.
- Gold tables provide trusted business metrics for hotel revenue and occupancy.
- Power BI dashboards are built only from Gold outputs.
- GitHub contains complete weekly evidence, documentation, screenshots, and final submission files.
- Every team member can confidently explain the project workflow and implementation.
