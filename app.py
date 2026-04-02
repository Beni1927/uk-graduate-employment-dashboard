import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="UK Graduate Employment Trends",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background-color: #f4f6f9; }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }

    h1 { color: #1B3A5C; font-size: 1.85rem; font-weight: 700; letter-spacing: -0.02em; }
    h2 { color: #1B3A5C; font-size: 1.2rem; font-weight: 600; }
    h3 { color: #1B3A5C; font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem; }

    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 1.1rem 1.3rem;
        border: 1px solid #e5e9f0;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        transition: box-shadow 0.2s ease;
    }
    .metric-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .metric-label {
        font-size: 0.7rem;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.07em;
        font-weight: 500;
    }
    .metric-value { font-size: 1.9rem; font-weight: 700; color: #1B3A5C; margin: 6px 0 4px; }
    .metric-delta-pos { font-size: 0.8rem; color: #16a34a; font-weight: 500; }
    .metric-delta-neg { font-size: 0.8rem; color: #dc2626; font-weight: 500; }
    .metric-delta-neutral { font-size: 0.8rem; color: #6b7280; }

    .insight-box {
        background: #EEF4FB;
        border-left: 4px solid #2C5F8A;
        border-radius: 0 10px 10px 0;
        padding: 0.9rem 1.1rem;
        margin: 0.5rem 0;
        font-size: 0.875rem;
        color: #1B3A5C;
        line-height: 1.55;
    }
    .section-divider { border: none; border-top: 1px solid #e0e4ea; margin: 1.5rem 0; }

    .sidebar-header {
        background: linear-gradient(135deg, #1B3A5C 0%, #2C5F8A 100%);
        border-radius: 10px;
        padding: 1rem 1.1rem;
        margin-bottom: 1rem;
        color: white;
    }
    .sidebar-title { font-size: 0.95rem; font-weight: 700; color: white; margin: 0; line-height: 1.3; }
    .sidebar-subtitle { font-size: 0.72rem; color: #b8d4ee; margin-top: 4px; }

    section[data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e5e9f0; }
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("data/uk_graduate_employment.csv")
    return df

df = load_data()
years      = sorted(df["year"].unique())
subjects   = sorted(df["subject"].unique())
COLORS     = px.colors.qualitative.Set2

CHART_FONT = dict(family="Inter, sans-serif", size=12, color="#374151")
CHART_BASE = dict(
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=CHART_FONT,
    hoverlabel=dict(bgcolor="white", bordercolor="#e5e9f0", font=CHART_FONT),
    margin=dict(t=20, b=10),
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <p class="sidebar-title">UK Graduate Employment</p>
        <p class="sidebar-subtitle">2019–2023 · HESA Graduate Outcomes</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Filters**")
    selected_years = st.select_slider(
        "Year range",
        options=years,
        value=(min(years), max(years))
    )
    selected_subjects = st.multiselect(
        "Subjects",
        options=subjects,
        default=subjects
    )
    st.markdown("---")
    st.caption(
        "Analysing UK graduate employment outcomes from 2019–2023 across 12 subject areas. "
        "Data sourced from Graduate Outcomes Survey (HESA) and Office for Students reports."
    )
    st.markdown("Built by **Beni Vimal Ravichandran**")
    st.markdown("[GitHub](https://github.com/benifredvimal) · [LinkedIn](#)")

# ── Filter data ───────────────────────────────────────────────────────────────
mask = (
    (df["year"] >= selected_years[0]) &
    (df["year"] <= selected_years[1]) &
    (df["subject"].isin(selected_subjects))
)
filtered = df[mask].copy()

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<h1>UK Graduate Employment Trends <span style="font-size:1.4rem; font-weight:400; color:#6b7280;">(2019–2023)</span></h1>
<p style="color:#4b5563; font-size:0.95rem; margin-top:-0.3rem; margin-bottom:0.5rem; max-width:700px;">
    An analysis of employment outcomes, salary trends, and sector patterns
    for UK graduates across 12 subject areas over five years.
</p>
""", unsafe_allow_html=True)
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ── KPI row ───────────────────────────────────────────────────────────────────
latest   = df[df["year"] == max(years)]
earliest = df[df["year"] == min(years)]

avg_emp_latest   = latest["employment_rate_pct"].mean()
avg_emp_earliest = earliest["employment_rate_pct"].mean()
avg_sal_latest   = latest["median_salary_gbp"].mean()
avg_sal_earliest = earliest["median_salary_gbp"].mean()
top_subject      = latest.loc[latest["employment_rate_pct"].idxmax(), "subject"]
top_salary_subj  = latest.loc[latest["median_salary_gbp"].idxmax(), "subject"]

emp_delta   = avg_emp_latest - avg_emp_earliest
sal_delta   = avg_sal_latest - avg_sal_earliest
emp_cls     = "metric-delta-pos" if emp_delta >= 0 else "metric-delta-neg"
sal_cls     = "metric-delta-pos" if sal_delta >= 0 else "metric-delta-neg"
emp_arrow   = "▲" if emp_delta >= 0 else "▼"
sal_arrow   = "▲" if sal_delta >= 0 else "▼"

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Avg employment rate (2023)</div>
        <div class="metric-value">{avg_emp_latest:.1f}%</div>
        <div class="{emp_cls}">{emp_arrow} {abs(emp_delta):.1f}pp vs 2019</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Avg median salary (2023)</div>
        <div class="metric-value">£{avg_sal_latest:,.0f}</div>
        <div class="{sal_cls}">{sal_arrow} £{abs(sal_delta):,.0f} vs 2019</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Highest employment (2023)</div>
        <div class="metric-value">{latest['employment_rate_pct'].max():.1f}%</div>
        <div class="metric-delta-neutral">{top_subject}</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Highest median salary (2023)</div>
        <div class="metric-value">£{latest['median_salary_gbp'].max():,}</div>
        <div class="metric-delta-neutral">{top_salary_subj}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Row 1: Employment rate over time + Salary comparison ─────────────────────
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Employment Rate Over Time")
    fig1 = px.line(
        filtered, x="year", y="employment_rate_pct",
        color="subject", markers=True,
        labels={"employment_rate_pct": "Employment rate (%)", "year": "Year", "subject": "Subject"},
        color_discrete_sequence=COLORS
    )
    fig1.update_layout(
        **CHART_BASE,
        legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="left", x=0, font=dict(size=10)),
        height=340,
        yaxis=dict(range=[50, 100], gridcolor="#f0f0f0"),
        xaxis=dict(gridcolor="#f0f0f0")
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("### Median Salary by Subject (2023)")
    latest_filtered = filtered[filtered["year"] == filtered["year"].max()].sort_values("median_salary_gbp", ascending=True)
    fig2 = px.bar(
        latest_filtered, x="median_salary_gbp", y="subject",
        orientation="h",
        labels={"median_salary_gbp": "Median salary (£)", "subject": ""},
        color="median_salary_gbp",
        color_continuous_scale=["#B5D4F4", "#1B3A5C"]
    )
    fig2.update_layout(
        **CHART_BASE,
        coloraxis_showscale=False,
        height=340,
        xaxis=dict(gridcolor="#f0f0f0")
    )
    fig2.update_traces(texttemplate="£%{x:,}", textposition="outside", textfont_size=10)
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2: Graduate vs non-graduate jobs + COVID impact ──────────────────────
col3, col4 = st.columns(2)

with col3:
    st.markdown("### Graduate-Level Employment by Subject (2023)")
    gj = filtered[filtered["year"] == filtered["year"].max()].sort_values("graduate_jobs_pct", ascending=True)
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(
        y=gj["subject"], x=gj["graduate_jobs_pct"],
        name="Graduate-level jobs", orientation="h",
        marker_color="#2C5F8A"
    ))
    fig3.add_trace(go.Bar(
        y=gj["subject"], x=gj["non_graduate_jobs_pct"],
        name="Non-graduate jobs", orientation="h",
        marker_color="#B5D4F4"
    ))
    fig3.update_layout(
        **CHART_BASE,
        barmode="stack",
        legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="left", x=0),
        height=340,
        xaxis=dict(title="% of employed graduates", gridcolor="#f0f0f0")
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.markdown("### Impact of COVID-19 on Employment Rates (2020 vs 2019)")
    impact = df[df["year"].isin([2019, 2020])].pivot(index="subject", columns="year", values="employment_rate_pct")
    impact["change"] = impact[2020] - impact[2019]
    impact = impact.sort_values("change").reset_index()
    colors = ["#E24B4A" if x < 0 else "#1D9E75" for x in impact["change"]]
    fig4 = go.Figure(go.Bar(
        x=impact["change"], y=impact["subject"],
        orientation="h", marker_color=colors,
        text=[f"{v:+.1f}pp" for v in impact["change"]],
        textposition="outside", textfont_size=10
    ))
    fig4.update_layout(
        **CHART_BASE,
        height=340,
        xaxis=dict(title="Percentage point change", gridcolor="#f0f0f0", zeroline=True, zerolinecolor="#aaa")
    )
    st.plotly_chart(fig4, use_container_width=True)

# ── Row 3: Unemployment trend + Further study ─────────────────────────────────
col5, col6 = st.columns(2)

with col5:
    st.markdown("### Unemployment Rate Trend")
    fig5 = px.area(
        filtered[filtered["subject"].isin(
            filtered.groupby("subject")["unemployed_pct"].mean().nlargest(5).index
        )],
        x="year", y="unemployed_pct", color="subject",
        labels={"unemployed_pct": "Unemployment rate (%)", "year": "Year", "subject": "Subject"},
        color_discrete_sequence=COLORS
    )
    fig5.update_layout(
        **CHART_BASE,
        legend=dict(orientation="h", yanchor="bottom", y=-0.35, xanchor="left", x=0, font=dict(size=10)),
        height=300
    )
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    st.markdown("### Further Study vs Employment (2023)")
    scatter_data = filtered[filtered["year"] == filtered["year"].max()]
    fig6 = px.scatter(
        scatter_data,
        x="further_study_pct", y="employment_rate_pct",
        size="median_salary_gbp", color="subject",
        labels={
            "further_study_pct": "Further study rate (%)",
            "employment_rate_pct": "Employment rate (%)",
            "median_salary_gbp": "Median salary",
            "subject": "Subject"
        },
        color_discrete_sequence=COLORS,
        hover_name="subject"
    )
    fig6.update_layout(
        **CHART_BASE,
        legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="left", x=0, font=dict(size=9)),
        height=300
    )
    st.plotly_chart(fig6, use_container_width=True)

# ── Key Insights ─────────────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown("### Key Findings")

i1, i2, i3 = st.columns(3)
with i1:
    st.markdown("""
    <div class="insight-box">
    <strong>Recovery post-COVID:</strong> Graduate employment rates largely recovered to pre-pandemic levels by 2022, with most subjects returning to within 2 percentage points of 2019 figures.
    </div>""", unsafe_allow_html=True)
with i2:
    st.markdown("""
    <div class="insight-box">
    <strong>Data Science salaries rising:</strong> Median salaries for Data Science & Statistics graduates rose from £31,500 in 2019 to £35,500 in 2023 — a 12.7% increase, outpacing most non-STEM subjects.
    </div>""", unsafe_allow_html=True)
with i3:
    st.markdown("""
    <div class="insight-box">
    <strong>Creative Arts remain hardest hit:</strong> Creative Arts graduates consistently show the highest unemployment rates (25–35%) and lowest graduate-level job placement, suggesting structural challenges in the sector.
    </div>""", unsafe_allow_html=True)

# ── Raw data explorer ─────────────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
with st.expander("📋 View raw data"):
    st.dataframe(
        filtered.rename(columns={
            "year": "Year",
            "subject": "Subject",
            "employment_rate_pct": "Employment Rate (%)",
            "median_salary_gbp": "Median Salary (£)",
            "further_study_pct": "Further Study (%)",
            "unemployed_pct": "Unemployed (%)",
            "graduate_jobs_pct": "Graduate-Level Jobs (%)",
            "non_graduate_jobs_pct": "Non-Graduate Jobs (%)"
        }).sort_values(["Year", "Subject"]),
        use_container_width=True,
        hide_index=True
    )
    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button("Download CSV", csv, "uk_graduate_employment_filtered.csv", "text/csv")

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#9ca3af; font-size:0.75rem; line-height:1.6;'>"
    "Data based on the HESA Graduate Outcomes Survey and Office for Students published reports. "
    "Figures are indicative and compiled for analytical purposes. "
    "&#169; 2024 Beni Vimal Ravichandran"
    "</p>",
    unsafe_allow_html=True
)
