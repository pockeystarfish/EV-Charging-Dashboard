import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Custom Iberdrola colors
i_color1 = "#00A650"  # Green
i_color2 = "#0070C0"  # Blue
i_color3 = "#FFB81C"  # Yellow

# Dashboard Title
st.title("EV Investment & Infrastructure Dashboard - Spain")
st.write("Analyze the impact of government subsidies and electricity discounts on EV sales, charger demand, and Iberdrola's profitability.")

# Sidebar Styling
st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #00A650;
        }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.header("Investment & Subsidy Options")

# User inputs for subsidies and electricity discounts
gov_purchase_subsidy = st.sidebar.slider("Government Purchase Subsidy per EV (€)", 0, 9000, 6000, 1000)
electricity_subsidy = st.sidebar.slider("Electricity Cost Reduction (%)", 0, 30, 20)

# Base values and assumptions
base_ev_sales = 500000  # EV sales in Spain (2025)
ev_price = 40000  # Average EV price (€)
ev_sales_increase_rate = 7.7  # % increase in EV sales per €1000 subsidy
charging_ratio = 10  # One public charger per 10 EVs
iberdrola_market_share = 0.2  # Iberdrola's market share in charging infrastructure
charger_revenue = 4000  # Annual revenue per charger (€)
profit_margin = 0.3  # Charging profit margin
roi_multiplier = 1.5  # ROI per €1 public investment

# Calculate new EV sales
sales_increase_factor = (gov_purchase_subsidy / 1000) * ev_sales_increase_rate
new_ev_sales = base_ev_sales * (1 + sales_increase_factor / 100)

# Calculate charger demand and Iberdrola's share
charger_demand = new_ev_sales / charging_ratio
iberdrola_chargers = charger_demand * iberdrola_market_share

# Calculate Iberdrola revenue and profit
iberdrola_revenue = iberdrola_chargers * charger_revenue
iberdrola_profit = iberdrola_revenue * profit_margin * (1 + (electricity_subsidy / 10) * 0.1)

# Calculate industry-wide ROI and profit
industry_roi = 1_000_000_000 * roi_multiplier * (gov_purchase_subsidy / 6000) * (1 + electricity_subsidy / 100)
industry_profit = industry_roi - 1_000_000_000

# Create DataFrame for display
data = {
    "Metric": ["Base EV Sales", "New EV Sales", "New Charger Demand", "Iberdrola Chargers Installed", "Iberdrola Revenue (€M)", "Iberdrola Profit (€M)", "Industry ROI (€B)", "Industry Net Profit (€B)"],
    "Value": [f"{base_ev_sales:,}", f"{int(new_ev_sales):,}", f"{int(charger_demand):,}", f"{int(iberdrola_chargers):,}", f"€{iberdrola_revenue/1e6:.2f}M", f"€{iberdrola_profit/1e6:.2f}M", f"€{industry_roi/1e9:.2f}B", f"€{industry_profit/1e9:.2f}B"]
}

df = pd.DataFrame(data)
# Display results in a table
st.table(df)

# Rationale Behind Government Subsidies
st.write("### Rationale Behind Government Subsidies")
st.write("Government subsidies for EV purchases and electricity cost reductions are based on policies seen in France and Germany, where strong incentives have significantly increased EV adoption rates.")
st.write("- **France**: Offers purchase grants of up to €7,000 per EV and reduced electricity taxes to encourage adoption.")
st.write("- **Germany**: Implements a bonus-malus system, providing up to €9,000 in purchase grants and tax exemptions for EV owners.")
st.write("- **Spain's Subsidy Strategy**: Based on comparative studies, Spain's proposed subsidy structure of up to €9,000 aligns with successful policies in neighboring countries to boost EV adoption and infrastructure investments.")

# Details on EV Purchase Subsidy Mechanism
st.write("### How the EV Purchase Subsidy Works")
st.write("The EV purchase subsidy directly lowers the upfront cost of EVs, increasing affordability and adoption rates. The key effects include:")
st.write("- **Lowering purchase price**: A €6,000 subsidy effectively reduces the cost of an EV from €40,000 to €34,000, making it more attractive to buyers.")
st.write("- **Boosting demand**: Every €1,000 in subsidies is estimated to increase EV sales by approximately 7.7% (TSE, 2023).")
st.write("- **Accelerating infrastructure growth**: More EVs lead to increased demand for charging infrastructure, benefiting operators like Iberdrola.")

# Visualization - EV Sales Growth
fig, ax = plt.subplots()
categories = ["Without Subsidy", "With Subsidy"]
values = [base_ev_sales, new_ev_sales]
ax.bar(categories, values, color=[i_color1, i_color2])
ax.set_ylabel("EV Sales")
ax.set_title("EV Sales Growth Due to Subsidy")
st.pyplot(fig)

# Visualization - Iberdrola Profit vs. Charger Demand
fig2, ax2 = plt.subplots()
ax2.plot([0, gov_purchase_subsidy], [iberdrola_profit / 1e6, charger_demand], marker='o', linestyle='-', color=i_color3)
ax2.set_xlabel("Government Purchase Subsidy (€)")
ax2.set_ylabel("Iberdrola Profit (€M) / Charger Demand")
ax2.set_title("Iberdrola Profitability & Charger Demand Growth")
st.pyplot(fig2)

# Extra Information Section
st.write("### Additional Information")
st.write("- **Base EV sales**: 500,000 units in Spain (EAFO, 2024).")
st.write("- **EV purchase price**: €40,000 on average (TSE, 2023).")
st.write("- **Sales increase per €1,000 subsidy**: 7.7% (TSE, 2023).")
st.write("- **Charger demand ratio**: 1 charger per 10 EVs (WFW, 2024).")
st.write("- **Iberdrola’s market share**: 20% (Statista, 2023).")
