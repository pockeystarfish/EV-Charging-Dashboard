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

# Average EV price in Europe (€)
ev_cost = 40000  
# User selects the EV manufacturer profit margin
profit_margin = st.sidebar.slider("EV Manufacturer Profit Margin (%)", 2.0, 5.0, 2.5) / 100

# Government purchase subsidy per EV (€)
gov_purchase_subsidy = st.sidebar.slider("Government Purchase Subsidy per EV (€)", 0, 9000, 6000, 1000)
# Electricity cost reduction due to subsidy (%)
electricity_subsidy = st.sidebar.slider("Electricity Cost Reduction (%)", 0, 30, 20)

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

# ROI calculation (return per €1 invested)
roi_per_dollar = total_profit / (new_sales * ev_cost)

# Creating a DataFrame to display results
data = {
    "Metric": ["Base EV Sales", "New EV Sales", "EV Profit Per Unit (€)", "Total Profit (€)", "ROI per €1 Invested"],
    "Value": [base_sales, int(new_sales), f"€{ev_profit_per_unit:.2f}", f"€{total_profit:.2f}", f"{roi_per_dollar:.4f}"]
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
st.write(f"- Investors see a return of **€{roi_per_dollar:.4f} per €1 invested** in the EV sector.")

# Displaying the full logic of calculations
st.write("### Calculation Logic:")
st.code("""
# EV Cost Assumption
ev_cost = 40000  # Average EV price in Europe (€)

# Profit Margin Selection
profit_margin = selected_value / 100  # Convert percentage to decimal

# Government Purchase Subsidy Selection
gov_purchase_subsidy = selected_value  # Selected value in €

# Electricity Subsidy Selection
electricity_subsidy = selected_value  # Selected value in %

# Base EV Sales Without Any Subsidy
base_sales = 100000  # Assumption

# Sales Increase Factor: 7.7% Increase per €1,000 Subsidy
sales_increase_factor = gov_purchase_subsidy / 1000 * 7.7

# New Sales Calculation
new_sales = base_sales * (1 + sales_increase_factor / 100)

# Profit Per EV Calculation
ev_profit_per_unit = ev_cost * profit_margin

# Total Profit Calculation
total_profit = new_sales * ev_profit_per_unit

# ROI Calculation (Return per €1 Invested)
roi_per_dollar = total_profit / (new_sales * ev_cost)
""", language='python')