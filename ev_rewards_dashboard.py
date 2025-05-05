# User input for number of chargers to simulate financial impact
user_chargers = st.number_input("Enter the number of EV chargers Iberdrola plans to deploy:", min_value=0, value=1000, step=100)

# Constants based on earlier assumptions
revenue_per_charger = 4000  # €/year
profit_margin = 0.3

# Calculate revenue and profit from user-defined chargers
user_revenue = user_chargers * revenue_per_charger  # in €
user_profit = user_revenue * profit_margin  # in €
user_ebitda = user_profit * 0.8  # assuming 80% EBITDA contribution

# Add to baseline to form adjusted financials
user_adj_revenue = baseline_revenue + user_revenue / 1e6
user_adj_ebitda = baseline_ebitda + user_ebitda / 1e6
user_adj_profit = baseline_profit + user_profit / 1e6

# Display simulated financial statement
st.write("### Simulated Financials Based on User-Defined Charger Deployment")
st.write(f"**Baseline Revenue:** €{baseline_revenue:.2f}M")
st.write(f"**Adjusted Revenue:** €{user_adj_revenue:.2f}M")
st.write(f"**Baseline EBITDA:** €{baseline_ebitda:.2f}M")
st.write(f"**Adjusted EBITDA:** €{user_adj_ebitda:.2f}M")
st.write(f"**Baseline Profit:** €{baseline_profit:.2f}M")
st.write(f"**Adjusted Net Profit:** €{user_adj_profit:.2f}M")

# Visualization - Iberdrola Financial Impact of Charger Deployment
# Assumed baseline values from Q1 2025 report
baseline_revenue = 12864.7  # in €M
baseline_ebitda = 4643.0    # in €M
baseline_profit = 2004.4    # in €M

# Updated values after adding charger business (additive based on calculated profit)
adjusted_revenue = baseline_revenue + iberdrola_revenue / 1e6
adjusted_ebitda = baseline_ebitda + (iberdrola_profit * 0.8) / 1e6  # assuming 80% of profit contributes to EBITDA
adjusted_profit = baseline_profit + iberdrola_profit / 1e6

# Visualization - Revenue, EBITDA, Profit Comparison
fig, ax = plt.subplots()
labels = ["Baseline", "With EV Charging"]
revenue = [baseline_revenue, adjusted_revenue]
ebitda = [baseline_ebitda, adjusted_ebitda]
profit = [baseline_profit, adjusted_profit]
x = np.arange(len(labels))
width = 0.25

ax.bar(x - width, revenue, width, label='Revenue (€M)', color=i_color1)
ax.bar(x, ebitda, width, label='EBITDA (€M)', color=i_color2)
ax.bar(x + width, profit, width, label='Net Profit (€M)', color=i_color3)

ax.set_ylabel("€ Millions")
ax.set_title("Iberdrola Financial Metrics Before vs After EV Infrastructure Investment")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
st.pyplot(fig)

# Add updated source references
st.write("### Sources (MLA Format)")
st.write("- Iberdrola. ‘Alternative Performance Measures Q1 2025.’ Iberdrola, 2025. [Link](https://www.iberdrola.com/shareholders-investors/financial-information/results-and-presentations)")
st.write("- Iberdrola. ‘Ibewatch Q1 2025 Fact Sheet.’ Iberdrola, 2025. [Link](https://www.iberdrola.com/press-room/news/detail/record-investments-173-billion-last-twelve-months-boost-iberdrolas-profit-first-quarter-more-2-billion)")
