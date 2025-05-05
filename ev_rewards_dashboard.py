# Assumed baseline values from Q1 2025 report
baseline_revenue = 12864.7  # in €M
baseline_ebitda = 4643.0    # in €M
baseline_profit = 2004.4    # in €M
baseline_assets = 162187    # in €M
baseline_equity = 60694     # in €M
baseline_liabilities = baseline_assets - baseline_equity

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
user_adj_assets = baseline_assets + (user_chargers * 35)  # assume €35k per charger in €M
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

# Add updated source references
st.write("### Sources (MLA Format)")
st.write("- Iberdrola. ‘Alternative Performance Measures Q1 2025.’ Iberdrola, 2025. [Link](https://www.iberdrola.com/shareholders-investors/financial-information/results-and-presentations)")
st.write("- Iberdrola. ‘Ibewatch Q1 2025 Fact Sheet.’ Iberdrola, 2025. [Link](https://www.iberdrola.com/press-room/news/detail/record-investments-173-billion-last-twelve-months-boost-iberdrolas-profit-first-quarter-more-2-billion)")
