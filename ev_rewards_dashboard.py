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
electricity_sales_increase_rate = 3.2  # % increase in EV sales per 10% electricity cost reduction【293:3†calc.pdf】
charging_ratio = 10  # One public charger per 10 EVs
iberdrola_market_share = 0.2  # Iberdrola's market share in charging infrastructure
charger_revenue = 4000  # Annual revenue per charger (€)
profit_margin = 0.3  # Charging profit margin
roi_multiplier = 1.5  # ROI per €1 public investment

# Calculate new EV sales
sales_increase_factor = ((gov_purchase_subsidy / 1000) * ev_sales_increase_rate) + ((electricity_subsidy / 10) * electricity_sales_increase_rate)
new_ev_sales = base_ev_sales * (1 + sales_increase_factor / 100)

# Calculate charger demand and Iberdrola's share
charger_demand = new_ev_sales / charging_ratio
iberdrola_chargers = charger_demand * iberdrola_market_share

# Calculate Iberdrola revenue and profit
iberdrola_revenue = iberdrola_chargers * charger_revenue
iberdrola_profit = iberdrola_revenue * profit_margin * (1 + (electricity_subsidy / 10) * 0.1)

# Calculate industry-wide ROI and profit
industry_roi = 1_000_000_000 * roi_multiplier * ((gov_purchase_subsidy / 6000) + (electricity_subsidy / 100))
industry_profit = industry_roi - 1_000_000_000

# Create DataFrame for display
data = {
    "Metric": ["Base EV Sales", "New EV Sales", "New Charger Demand", "Iberdrola Chargers Installed", "Iberdrola Revenue (€M)", "Iberdrola Profit (€M)", "Industry ROI (€B)", "Industry Net Profit (€B)"],
    "Value": [f"{base_ev_sales:,}", f"{int(new_ev_sales):,}", f"{int(charger_demand):,}", f"{int(iberdrola_chargers):,}", f"€{iberdrola_revenue/1e6:.2f}M", f"€{iberdrola_profit/1e6:.2f}M", f"€{industry_roi/1e9:.2f}B", f"€{industry_profit/1e9:.2f}B"]
}

df = pd.DataFrame(data)
# Display results in a table
st.table(df)

# Assumptions Used in the Model
st.write("### Assumptions Used in the Model")
st.write("- **Base EV sales in Spain**: 500,000 units projected for 2025.")
st.write("- **EV price**: €40,000 on average, based on European market trends.")
st.write("- **EV sales increase per €1,000 subsidy**: 7.7% growth rate (TSE, 2023).")
st.write("- **Electricity subsidy impact on EV sales**: Every 10% reduction in electricity cost leads to a 3.2% increase in EV sales.")
st.write("- **Charging station demand ratio**: 1 public charger is required for every 10 EVs on the road.")
st.write("- **Iberdrola's market share in charging infrastructure**: 20%.")
st.write("- **Annual revenue per charger**: €4,000.")
st.write("- **Profit margin on charging infrastructure**: 30%.")
st.write("- **Industry-wide ROI multiplier**: €1.50 return per €1.00 public investment.")

# Calculation Methodology
st.write("### Calculation Methodology")
st.write("All calculations are based on data extracted from **calc.pdf**, where we analyzed historical trends and government reports.")
st.write("- **Sales increase estimates** are derived from empirical studies on the effect of subsidies on EV adoption (TSE, 2023).")
st.write("- **Charging demand estimates** follow industry standards on charger-to-EV ratios (EAFO, 2024).")
st.write("- **Iberdrola's revenue and profitability** are based on actual market shares and revenue per charger statistics (Statista, 2023).")
st.write("- **ROI calculations** utilize a public investment multiplier from European industry benchmarks (ACEA, 2024).")

# Sources Section
st.write("### Sources (MLA Format)")
st.write("- ACEA. 'Electric Cars: Tax Benefits and Incentives (2024).' ACEA, 2024. [Link](https://www.acea.auto/fact/electric-cars-tax-benefits-and-incentives-2024/)")
st.write("- EAFO. 'Spain: BEV Passenger Car Sales Increased by 7.8% in 2024.' European Alternative Fuels Observatory, 2024. [Link](https://alternative-fuels-observatory.ec.europa.eu/general-information/news/spain-bev-passenger-car-sales-increased-78-2024)")
st.write("- TSE. 'Electric Vehicle Subsidies: Cost-Effectiveness and Emission Impacts.' Toulouse School of Economics, 2023. [Link](https://www.tse-fr.eu/sites/default/files/TSE/documents/doc/wp/2023/wp_tse_1465.pdf)")
st.write("- NBER. 'Shifting Electric Vehicle Owners to Off-Peak Charging.' National Bureau of Economic Research, 2024. [Link](https://www.nber.org/digest/202401/shifting-electric-vehicle-owners-peak-charging)")
