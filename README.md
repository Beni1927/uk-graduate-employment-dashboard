# 📊 UK Graduate Employment Trends (2019–2023)

An interactive data analysis dashboard and written report examining graduate employment outcomes across 12 UK subject areas over five years.

Built by **Beni Vimal Ravichandran** — MSc Data Science, University of Hertfordshire.

---

## What this project does

This project analyses publicly available UK graduate employment data to answer questions like:

- Which subjects produce the highest-earning graduates in the UK?
- How severely did COVID-19 affect different subject areas — and how far has recovery gone?
- What proportion of graduates end up in graduate-level roles vs non-graduate roles?
- How have Data Science and STEM graduate outcomes changed since 2019?

The findings are presented in two ways:
1. An **interactive Streamlit dashboard** with filterable charts
2. A **written analysis report** (`REPORT.md`) with structured findings, a methodology section, and recommendations

---

## Dashboard preview

| Chart | What it shows |
|---|---|
| Employment rate over time | Year-on-year trend lines by subject (2019–2023) |
| Median salary comparison | Bar chart of 2023 salaries across all subjects |
| Graduate vs non-graduate jobs | Stacked bar showing degree-level job placement by subject |
| COVID-19 impact analysis | Change in employment rate 2019 vs 2020, by subject |
| Unemployment trends | Area chart of top 5 subjects by unemployment rate |
| Further study vs employment | Scatter plot showing relationship between further study and employment outcomes |

---

## Project structure

```
uk-graduate-employment/
├── app.py                        # Streamlit dashboard
├── data/
│   └── uk_graduate_employment.csv   # Dataset (2019–2023, 12 subjects)
├── REPORT.md                     # Full written analysis report
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## How to run locally

**Requirements:** Python 3.9+

```bash
# 1. Clone the repository
git clone https://github.com/benifredvimal/uk-graduate-employment.git
cd uk-graduate-employment

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`

---

## Dataset

The dataset (`data/uk_graduate_employment.csv`) covers 12 subject areas across 5 years (2019–2023) with the following variables:

| Column | Description |
|---|---|
| `year` | Graduation cohort year |
| `subject` | Degree subject area |
| `employment_rate_pct` | % of graduates in employment 15 months after graduation |
| `median_salary_gbp` | Median annual salary of employed graduates (£) |
| `further_study_pct` | % continuing to postgraduate study |
| `unemployed_pct` | % actively seeking employment |
| `graduate_jobs_pct` | % of employed graduates in graduate-level roles (SOC 1–3) |
| `non_graduate_jobs_pct` | % of employed graduates in non-graduate roles |

Data compiled from HESA Graduate Outcomes Survey and Office for Students published reports.

---

## Key findings

- Graduate employment rates largely recovered to pre-pandemic levels by 2022, but **Creative Arts and Social Sciences remain below 2019 figures**
- **Data Science & Statistics** median salaries rose 12.7% between 2019 and 2023, the second-highest growth of any subject
- **Medicine, Engineering, and Computer Science** consistently lead on employment rate, salary, and graduate-level job placement
- A significant proportion of **Business and Social Sciences graduates are underemployed** — working in non-graduate roles despite holding a degree
- COVID-19 hit **Creative Arts hardest** with a 10.2 percentage point drop in employment in 2020

Full analysis in [REPORT.md](./REPORT.md)

---

## Skills demonstrated

- **Data analysis** — cleaning, structuring, and deriving insights from tabular data using Pandas
- **Data visualisation** — interactive charts with Plotly; dashboard design with Streamlit
- **Research and reporting** — structured written report with methodology, findings, and recommendations
- **Python** — clean, readable, commented code
- **Communication** — presenting analytical findings clearly for non-technical audiences

---

## About

**Beni Vimal Ravichandran**  
MSc Data Science — University of Hertfordshire (2024)  
BE Electronics and Communication Engineering — First Class, GPA 8.62

📧 benfredvimal@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/your-profile)  
📍 Hatfield, United Kingdom | Graduate visa — eligible to work full-time
