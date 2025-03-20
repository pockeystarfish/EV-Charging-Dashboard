# -*- coding: utf-8 -*-
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dashboard Title
st.title("EV Investment ROI Dashboard - Spain")
st.write("Analyze the profitability of investing in Spain's EV market under different subsidy scenarios.")

# Sidebar Inputs
st.sidebar.header("Investment & Subsidy Options")

# User inputs the amount of dollars to invest
investment_amount = st.sidebar.number_input("Investment Amount (€)", min_value=1000, value=10000, step=1000)

# Average EV price in Europe (€)
ev_cost = 40000  
# User selects the EV manufacturer profit margin
profit_margin = st.sidebar.slider("EV Manufacturer Profit Margin (%)", 2.0, 5.0, 2.5) / 100

# Government purchase subsidy per EV (€)
gov_purchase_subsidy = st.sidebar.slider("Government Purchase Subsidy per EV (€)", 0, 9000, 6000, 1000)
# Electricity cost reduction due to subsidy (%)/100
electricity_subsidy = st.sidebar.slider("Electricity Cost Reduction (%)", 0, 30, 20) / 100

# Adjusted EV cost after subsidy
effective_ev_cost = ev_cost - gov_purchase_subsidy
if effective_ev_cost < 0:
    effective_ev_cost = 0  # Ensure the cost does not become negative

# Base EV sales assumption without subsidies
base_sales = 100000  
# Sales increase factor: A €1,000 subsidy increases sales by 7.7%
sales_increase_factor = gov_purchase_subsidy / 1000 * 7.7  
# New sales calculation incorporating the subsidy effect
new_sales = base_sales * (1 + sales_increase_factor / 100)

# Profit per EV unit calculation
ev_profit_per_unit = ev_cost * profit_margin

# Total profit for manufacturers
total_profit = new_sales * ev_profit_per_unit

# Number of EVs an investor can fund
num_evs_funded = investment_amount / effective_ev_cost if effective_ev_cost > 0 else 0

# Adjusted electricity cost after subsidy
base_electricity_cost = 0.20  # Assume base electricity cost per kWh (€)
adjusted_electricity_cost = base_electricity_cost * (1 - electricity_subsidy)

# Profit per EV adjusted for electricity subsidy
adjusted_ev_profit_per_unit = ev_profit_per_unit + (electricity_subsidy * effective_ev_cost * 0.1)  # Assume 10% of cost savings affect profit

# Investor return calculation based on investment amount
investment_return = num_evs_funded * adjusted_ev_profit_per_unit * (1 + sales_increase_factor / 100)
roi_per_dollar = investment_return / investment_amount if investment_amount > 0 else 0

# Creating a DataFrame to display results
data = {
    "Metric": ["Base EV Sales", "New EV Sales", "Effective EV Cost (€)", "EV Profit Per Unit (€)", "Total Profit (€)", "Investment Amount (€)", "EVs Funded", "Investment Return (€)", "ROI per €1 Invested"],
    "Value": [base_sales, int(new_sales), f"€{effective_ev_cost:.2f}", f"€{adjusted_ev_profit_per_unit:.2f}", f"€{total_profit:.2f}", f"€{investment_amount:,.2f}", f"{num_evs_funded:.2f}", f"€{investment_return:.2f}", f"{roi_per_dollar:.4f}"]
}

df = pd.DataFrame(data)
# Display results in a table
st.table(df)

# Visualization using Matplotlib
fig, ax = plt.subplots()
categories = ["Without Subsidy", "With Subsidy"]
values = [base_sales, new_sales]
ax.bar(categories, values, color=['gray', 'green'])
ax.set_ylabel("EV Sales")
ax.set_title("EV Sales Growth Due to Subsidy")
# Display the plot
st.pyplot(fig)

# Key insights section
st.write("### Key Insights:")
st.write(f"- A purchase subsidy of €{gov_purchase_subsidy} leads to a {sales_increase_factor:.1f}% rise in EV sales.")
st.write(f"- With these assumptions, EV manufacturers earn **€{total_profit:,.2f}** in total profit.")
st.write(f"- The effective EV cost after subsidies is **€{effective_ev_cost:,.2f}**.")
st.write(f"- An investment of **€{investment_amount:,.2f}** can fund **{num_evs_funded:.2f}** EVs.")
st.write(f"- Adjusted electricity costs reduce operational expenses, increasing profits per EV.")
st.write(f"- Increased sales due to subsidies directly enhance investor returns.")
st.write(f"- This investment yields **€{investment_return:,.2f}** in return.")
st.write(f"- Investors see a return of **€{roi_per_dollar:.4f} per €1 invested** in the EV sector.")
