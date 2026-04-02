# UK Graduate Employment Trends: Analysis Report (2019–2023)

**Author:** Beni Vimal Ravichandran  
**Date:** 2024  
**Tools used:** Python, Pandas, Plotly, Streamlit  
**Data sources:** HESA Graduate Outcomes Survey, Office for Students

---

## Executive Summary

This report analyses graduate employment outcomes across 12 UK subject areas between 2019 and 2023. The analysis covers employment rates, median salaries, graduate-level job placement, unemployment trends, and the impact of the COVID-19 pandemic on the graduate labour market.

Key findings indicate a strong post-pandemic recovery by 2022, widening salary gaps between STEM and arts subjects, and growing demand for Data Science graduates. However, structural challenges persist in Creative Arts, and unemployment among Social Sciences graduates remains elevated relative to pre-pandemic levels.

---

## 1. Introduction

The UK graduate employment landscape has undergone significant change over the five-year period studied. The COVID-19 pandemic caused a sharp contraction in graduate employment in 2020, disproportionately affecting non-STEM fields and roles in hospitality, retail, and the creative industries. This report examines the extent of that impact and the trajectory of recovery across disciplines.

Understanding these patterns is relevant to universities, careers advisers, policy makers, and prospective students. The analysis aims to present findings clearly and accessibly, with supporting visualisations.

---

## 2. Data and Methodology

### 2.1 Data Sources

Data was compiled from the following published sources:

- **HESA Graduate Outcomes Survey** — annual survey of UK graduates 15 months after completing their degree, covering employment status, job type, and earnings
- **Office for Students (OfS) graduate outcomes data** — subject-level employment and salary statistics
- **ONS Labour Market Statistics** — contextual unemployment benchmarks

### 2.2 Variables Analysed

| Variable | Definition |
|---|---|
| Employment rate (%) | % of graduates in employment 15 months after graduation |
| Median salary (£) | Median annual salary of employed graduates |
| Graduate-level jobs (%) | % of employed graduates in roles classified as graduate-level (SOC 1–3) |
| Further study (%) | % continuing to postgraduate study |
| Unemployment rate (%) | % actively seeking employment |

### 2.3 Methodology

Data was cleaned and structured using Python (Pandas). Trends were analysed across five annual cohorts (2019–2023) and twelve subject areas. Charts were produced using Plotly and presented in an interactive Streamlit dashboard. Where values were unavailable, estimates were interpolated from published ranges.

---

## 3. Findings

### 3.1 Overall Employment Trends

Average graduate employment across all subjects stood at **83.8%** in 2019, fell to **76.3%** in 2020 at the height of pandemic disruption, and recovered to **82.8%** by 2023 — approaching but not yet fully returning to pre-pandemic levels.

The subjects least affected during 2020 were those with direct public sector demand:

- **Medicine & Dentistry** dropped by only 1.5 percentage points (97.1% → 95.6%), as healthcare demand surged
- **Nursing & Midwifery** remained above 91%, reflecting sustained NHS recruitment

The most severely affected were:

- **Creative Arts** — fell 10.2pp (68.4% → 58.2%), the largest drop of any subject
- **Social Sciences** — fell 8.1pp, with many graduate roles in retail, events, and hospitality suspended

### 3.2 Salary Trends

Median graduate salaries increased across all subjects over the five-year period, driven by general wage inflation and rising demand for STEM skills.

**Highest-paying subjects in 2023:**

| Subject | Median Salary (2023) | Change since 2019 |
|---|---|---|
| Medicine & Dentistry | £42,000 | +£4,000 |
| Economics | £33,000 | +£3,000 |
| Data Science & Statistics | £35,500 | +£4,000 |
| Engineering | £34,000 | +£3,000 |
| Computer Science | £36,500 | +£4,500 |

**Data Science and Computer Science** showed the strongest salary growth in proportional terms — both rising over 12% — reflecting sustained demand for digital and analytical skills in the UK labour market.

**Lowest-paying subjects** remained Creative Arts (£22,000) and Languages (£23,500), both of which also showed the weakest employment and graduate-level job placement figures.

### 3.3 Graduate-Level Job Placement

Graduate-level job placement — the proportion of employed graduates in roles classified as requiring a degree (Standard Occupational Classification 1–3) — varied significantly by subject.

In 2023:

- **Medicine & Dentistry** led at 96.4%, as expected given professional accreditation requirements
- **Nursing & Midwifery** (91.8%) and **Engineering** (73.2%) followed
- **Data Science & Statistics** reached 70.8%, reflecting strong absorption into analyst, researcher, and technology roles
- **Creative Arts** had the lowest rate at 35.9%, meaning nearly two-thirds of employed graduates were in non-graduate roles such as retail, service, and administration

This gap is significant. For subjects such as Business & Management (58.1%) and Social Sciences (45.2%), a substantial proportion of graduates are underemployed relative to their qualification level — a structural issue the UK graduate labour market has yet to resolve.

### 3.4 Unemployment

Graduate unemployment peaked in 2020 across all subjects. By 2023, most had returned near to 2019 levels, with some notable exceptions.

**Subjects with highest unemployment in 2023:**

- Creative Arts: 27.5%
- Social Sciences: 15.4%
- Languages: 16.3%

These figures are substantially above the UK national graduate unemployment average and suggest that graduates in these fields face prolonged job searches and greater difficulty securing roles aligned to their qualifications.

**Best-performing subjects** (lowest unemployment in 2023):

- Medicine & Dentistry: 2.0%
- Engineering: 4.4%
- Data Science & Statistics: 3.5%

### 3.5 Further Study

Further study rates remained relatively stable across the five-year period, ranging from 1.2% (Medicine & Dentistry, where further study is already embedded in the professional pathway) to 14.7% (Law, where conversion courses and bar training are common next steps).

The higher further study rates in Law (14.7%) and Economics (13.2%) likely reflect structured professional training pathways rather than unemployment avoidance. In contrast, the Social Sciences and Creative Arts further study rates (12.5% and 6.7% respectively) are more likely driven by graduates seeking to improve their employability.

---

## 4. Key Insights

**1. The graduate labour market has largely recovered from COVID-19 — but unevenly.**  
STEM and healthcare subjects returned to pre-pandemic employment rates by 2021–2022. Social Sciences and Creative Arts have recovered more slowly and remain below 2019 levels in 2023.

**2. Data Science graduates are increasingly well-placed in the UK labour market.**  
Employment rates (85.4%), median salary growth (+12.7% since 2019), and graduate-level placement (70.8%) all point to strong and growing demand for data-literate graduates in UK organisations.

**3. There is a persistent and widening gap between STEM and arts subjects.**  
Across every metric — employment rate, salary, graduate-level placement, and unemployment — STEM graduates consistently outperform arts graduates. The gap in median salary between the highest (Medicine, £42,000) and lowest (Creative Arts, £22,000) subjects is £20,000 annually.

**4. A significant proportion of graduates are underemployed.**  
For Business, Social Sciences, and Creative Arts, a large share of employed graduates are in non-graduate roles. This represents both a personal and economic cost, and is an area where employer engagement and careers support may need to be strengthened.

---

## 5. Recommendations

Based on the analysis, the following recommendations are offered for key stakeholders:

**For universities and careers services:**
- Invest in employer engagement for Social Sciences and Creative Arts graduates, where graduate-level job placement remains low
- Promote data literacy modules across all subject areas, given the salary premium associated with data-related skills

**For policy makers:**
- Monitor the underemployment gap in non-STEM subjects and consider targeted graduate employment schemes
- Ensure Graduate visa and post-study work provisions remain accessible, given that international graduates contribute significantly to sectors with talent shortages

**For prospective students:**
- Data Science, Engineering, and Computer Science offer the strongest near-term employment outcomes in the UK
- Supplementing arts or social science degrees with quantitative or digital skills (Python, SQL, data analysis) substantially improves employment and salary prospects

---

## 6. Limitations

- Data for this analysis is compiled from published survey ranges and is indicative rather than exact. Individual university outcomes may vary significantly from subject-area averages.
- The Graduate Outcomes Survey captures employment status 15 months post-graduation; longer-term career trajectories are not reflected.
- Salary figures are medians and do not capture variation within subjects, regions, or employer types.

---

## 7. Conclusion

The UK graduate employment market has shown resilience, recovering strongly from COVID-19 across most subject areas. The outlook for STEM graduates — and particularly for those with data, digital, and engineering skills — is positive, with rising salaries and strong graduate-level job placement. Structural challenges remain for arts and some social science subjects, where unemployment is higher and graduate-level placement is lower.

This analysis demonstrates the value of systematic, data-driven approaches to understanding labour market dynamics — the kind of structured research and reporting that supports evidence-based decision-making in organisations across sectors.

---

*Report produced as part of a data analysis portfolio project. Data compiled from publicly available HESA and OfS sources.*
