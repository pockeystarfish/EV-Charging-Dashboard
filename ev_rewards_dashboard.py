import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Color palette for graphs
i_color1 = "#00A650"  # Iberdrola Green
i_color2 = "#0070C0"  # Blue
i_color3 = "#FFB81C"  # Yellow

# Assumed baseline values from Q1 2025 report
baseline_revenue = 12864.7  # in €M
baseline_ebitda = 4643.0    # in €M
baseline_profit = 2004.4    # in €M
baseline_assets = 162187    # in €M
baseline_equity = 60694     # in €M
baseline_liabilities = baseline_assets - baseline_equity

# User input for number of chargers to simulate financial impact
user_chargers = st.number_input(
    "Enter the number of EV chargers Iberdrola plans to deploy:",
    min_value=0,
    value=1000,
    step=100
)

# Constants based on earlier assumptions
revenue_per_charger = 4000  # €/year
profit_margin = 0.3

# Calculate revenue and profit from user-defined chargers
user_revenue = user_chargers * revenue_per_charger  # in €
user_profit = user_revenue * profit_margin          # in €
user_ebitda = user_profit * 0.8                     # 80% EBITDA contribution

# Add to baseline to form adjusted financials
user_adj_revenue = baseline_revenue + user_revenue / 1e6
user_adj_ebitda = baseline_ebitda + user_ebitda / 1e6
user_adj_profit = baseline_profit + user_profit / 1e6
user_adj_assets = baseline_assets + (user_chargers * 35 / 1e3)  # €35k per charger in €M
user_adj_equity = baseline_equity + user_profit / 1e6
user_adj_liabilities = user_adj_assets - user_adj_equity

# Display simulated financial statement
st.write("### Simulated Financials Based on User-Defined Charger Deployment")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Profit & Loss Statement (€M)")
    st.write("**Revenue:**")
    st.write(f"- Baseline: €{baseline_revenue:.2f}M")
    st.write(f"- Adjusted: €{user_adj_revenue:.2f}M")
    st.write("**EBITDA:**")
    st.write(f"- Baseline: €{baseline_ebitda:.2f}M")
    st.write(f"- Adjusted: €{user_adj_ebitda:.2f}M")
    st.write("**Net Profit:**")
    st.write(f"- Baseline: €{baseline_profit:.2f}M")
    st.write(f"- Adjusted: €{user_adj_profit:.2f}M")

with col2:
    st.subheader("Balance Sheet (€M)")
    st.write("**Assets:**")
    st.write(f"- Baseline: €{baseline_assets:.0f}M")
    st.write(f"- Adjusted: €{user_adj_assets:.0f}M")
    st.write("**Equity:**")
    st.write(f"- Baseline: €{baseline_equity:.0f}M")
    st.write(f"- Adjusted: €{user_adj_equity:.0f}M")
    st.write("**Liabilities:**")
    st.write(f"- Baseline: €{baseline_liabilities:.0f}M")
    st.write(f"- Adjusted: €{user_adj_liabilities:.0f}M")

# Visualization - Revenue, EBITDA, Profit Comparison
fig, ax = plt.subplots()
labels = ["Baseline", "With EV Charging"]
revenue = [baseline_revenue, user_adj_revenue]
ebitda = [baseline_ebitda, user_adj_ebitda]
profit = [baseline_profit, user_adj_profit]
x = np.arange(len(labels))
width = 0.25

ax.bar(x - width, revenue, width, label='Revenue (€M)', color=i_color1)
ax.bar(x, ebitda, width, label='EBITDA (€M)', color=i_color2)
ax.bar(x + width, profit, width, label='Net Profit (€M)', color=i_color3)

ax.set_ylabel("€ Millions")
ax.set_title("Iberdrola Financial Metrics Before vs After EV Charger Deployment")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
st.pyplot(fig)

# Add explanation section
st.write("### How Does Charger Deployment Affect Financials?")
st.write("The following assumptions and calculations explain how each additional charger affects Iberdrola’s revenue and profitability:")
st.markdown("""
- 📌 **Revenue Per Charger**: Each EV charger is assumed to generate €4,000 in annual revenue based on industry benchmarks (EVBox, Enel X).
- 📌 **Profit Margin**: 30% of revenue is assumed to be profit.
- 📌 **EBITDA Contribution**: 80% of the profit is considered as contributing to EBITDA.
- 📌 **Charger CapEx**: Each charger adds €35,000 to the company’s asset base.
- 📌 **Equity Increase**: Adjusted equity is calculated by adding net profit from chargers to baseline equity.
- 📌 **Liabilities**: Computed as Adjusted Assets - Adjusted Equity.

🧮 **Example Calculation for 1 Charger**:
- Revenue: €4,000
- Profit: €1,200 (30% of revenue)
- EBITDA: €960 (80% of profit)
- Asset increase: €0.035M

These changes are then added to Iberdrola’s baseline financials to project updated performance.
""")

# Add updated source references
st.write("### Sources (MLA Format)")
st.write("- Iberdrola. ‘Alternative Performance Measures Q1 2025.’ Iberdrola, 2025. [Link](https://www.iberdrola.com/shareholders-investors/financial-information/results-and-presentations)")
st.write("- Iberdrola. ‘Ibewatch Q1 2025 Fact Sheet.’ Iberdrola, 2025. [Link](https://www.iberdrola.com/press-room/news/detail/record-investments-173-billion-last-twelve-months-boost-iberdrolas-profit-first-quarter-more-2-billion)")
