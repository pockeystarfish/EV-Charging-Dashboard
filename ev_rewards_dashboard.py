import streamlit as st
import pandas as pd
import numpy as np

# Define reward structure
reward_structure = {
    "Peak Hours (5PM-9PM)": 0.05,   # Lower incentive due to high demand
    "Off-Peak Hours (9PM-6AM)": 0.10,  # Higher incentive to encourage charging
    "Midday Renewable Hours (10AM-3PM)": 0.15,  # Maximum incentive for green energy
    "Standard Hours (6AM-5PM, 9PM-10AM)": 0.07  # Moderate incentive
}

# Streamlit App
st.title("EV Charging Market Dashboard")
st.write("Analyze rewards, competition, and collaboration strategies in the EV charging market.")

# User Inputs
charging_start = st.slider("Charging Start Time (24h format)", 0, 23, 18)
charging_duration = st.slider("Charging Duration (hours)", 1, 12, 2)
kWh_used = st.number_input("Energy Consumption (kWh)", min_value=1.0, max_value=100.0, value=20.0)
competitors = st.slider("Number of Competing EV Charging Providers", 1, 10, 3)
collaboration = st.radio("Would You Consider Collaborating?", ["Yes", "No"])

# Determine time category and apply incentive
reward_rate = []
time_blocks = []

def competition_factor(competitors):
    """ Reduces reward profitability due to increased competition."""
    return max(0.5, 1 - (competitors * 0.05))  # Ensures minimum profitability factor of 0.5

for hour in range(charging_start, charging_start + charging_duration):
    real_hour = hour % 24  # Convert to 24-hour format
    if 17 <= real_hour < 21:
        rate = reward_structure["Peak Hours (5PM-9PM)"]
    elif 21 <= real_hour or real_hour < 6:
        rate = reward_structure["Off-Peak Hours (9PM-6AM)"]
    elif 10 <= real_hour < 15:
        rate = reward_structure["Midday Renewable Hours (10AM-3PM)"]
    else:
        rate = reward_structure["Standard Hours (6AM-5PM, 9PM-10AM)"]
    
    rate *= competition_factor(competitors)  # Adjust rate based on competition
    reward_rate.append(rate)
    time_blocks.append(f"Hour {real_hour}: {rate*100:.2f}% cashback")

# Calculate total reward
total_reward = kWh_used * np.mean(reward_rate)

# Adjust profitability if collaboration is chosen
if collaboration == "Yes":
    total_reward *= 1.2  # Boost rewards by 20% when collaborating

# Display Results
st.subheader("Market-Based Charging Reward Calculation")
st.write(f"Total Reward Earned: **${total_reward:.2f}**")
st.write("Hourly Breakdown:")
st.write("\n".join(time_blocks))

# Competitive Analysis
st.subheader("Competition & Strategy")
if competitors > 5:
    st.write("⚠️ **High competition detected!** Profits may decrease due to price pressure.")
else:
    st.write("✅ **Moderate competition** - Market conditions are favorable.")

if collaboration == "Yes":
    st.write("🤝 **Collaboration Chosen:** Profitability increased by 20%." )
else:
    st.write("⚔️ **Competitive Strategy:** Competing in a free-market dynamic.")

st.write("\n**Insights:**")
st.write("- More competitors reduce profitability per kWh.")
st.write("- Collaboration can yield higher long-term rewards and sustainability goals.")
st.write("- Consider optimizing charge times for maximum profit.")