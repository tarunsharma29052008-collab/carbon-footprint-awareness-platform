import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Settings
st.set_page_config(
    page_title="Carbon Footprint Pro",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
h1 {
    color: green;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🌍 Eco Dashboard")
st.sidebar.info(
    """
    Carbon Footprint Awareness Platform

    Track your emissions
    Save environment
    Live greener
    """
)

# Title
st.title("🌍 Carbon Footprint Awareness Platform")
st.subheader("🎯 Set Your Carbon Reduction Goal")

goal = st.slider(
    "Target Carbon Reduction (%)",
    0,
    100,
    20
)

# Two Columns
col1, col2 = st.columns(2)

with col1:
    transport = st.selectbox(
        "Transport",
        ["Car", "Bike", "Bus", "Train"]
    )

    distance = st.number_input(
        "Distance per day (km)",
        min_value=0
    )

with col2:
    electricity = st.number_input(
        "Electricity Usage (kWh)",
        min_value=0
    )

# Emission Calculation
transport_emission = 0

if transport == "Car":
    transport_emission = distance * 0.21
elif transport == "Bike":
    transport_emission = distance * 0.10
elif transport == "Bus":
    transport_emission = distance * 0.08
elif transport == "Train":
    transport_emission = distance * 0.05

electricity_emission = electricity * 0.4

total = transport_emission + electricity_emission

# Calculate Button
if st.button("Calculate Carbon Footprint"):

    st.success(f"Total Carbon Footprint = {total:.2f} kg CO₂")

    # Eco Score
    if total < 50:
        eco_score = 90
        st.success("🏆 Green Champion")
    elif total < 100:
        eco_score = 70
        st.warning("🥈 Eco Warrior")
    else:
        eco_score = 40
        st.error("⚠️ Needs Improvement")

    # Trees Required
    trees = round(total / 10)

    # Metrics
    c1, c2, c3 = st.columns(3)

    c1.metric("Total CO₂", f"{total:.2f} kg")
    c2.metric("Eco Score", f"{eco_score}/100")
    c3.metric("Trees Required", trees)

    st.info(f"🌳 Trees Required to Offset = {trees}")
    st.subheader("🏅 Achievement Badge")

    if total < 30:
       st.success("🥇 Green Master")
    elif total < 70:
       st.success("🥈 Eco Warrior")
    else:
       st.warning("🥉 Carbon Beginner")

    st.subheader("🤖 AI Recommendations")

if total < 50:
    st.success("""
    Great job! Your carbon footprint is low.

    Recommendations:
    ✅ Continue using eco-friendly transport
    ✅ Maintain energy-efficient habits
    ✅ Encourage others to go green
    """)

elif total < 100:
    st.warning("""
    Your footprint is moderate.

    Recommendations:
    ✅ Reduce electricity usage
    ✅ Use public transport more often
    ✅ Switch to LED bulbs
    ✅ Plant more trees
    """)

else:
    st.error("""
    Your carbon footprint is high.

    Recommendations:
    ✅ Avoid unnecessary vehicle use
    ✅ Use renewable energy if possible
    ✅ Reduce electricity consumption
    ✅ Increase use of public transport
    ✅ Plant trees regularly
    """)

    # Progress Bar
    st.subheader("🌱 Sustainability Progress")

    progress = max(0, min(100, 100 - int(total)))

    st.progress(progress)
    st.subheader("🌎 Compare With Average")

    india_avg = 120

    if total < india_avg:
        st.success("You are below average carbon footprint in India!")
    else:
        st.error("You are above average carbon footprint.")
    st.write(f"Your Goal: Reduce Carbon Footprint by {goal}%")

    target_emission = total * (1 - goal/100)

    st.info(
    f"Target Carbon Footprint: {target_emission:.2f} kg CO₂"
    )

    # Chart Data
    data = {
        "Category": ["Transport", "Electricity"],
        "Emission": [transport_emission, electricity_emission]
    }

    df = pd.DataFrame(data)

    st.subheader("📊 Emission Breakdown")

    st.bar_chart(df.set_index("Category"))
    trend = pd.DataFrame({
    "Month": [
        "Jan","Feb","Mar","Apr",
        "May","Jun","Jul","Aug",
        "Sep","Oct","Nov","Dec"
    ],
    "Emission": [
        total*1.2,
        total*1.1,
        total*1.05,
        total,
        total*0.95,
        total*0.9,
        total*0.85,
        total*0.8,
        total*0.78,
        total*0.75,
        total*0.7,
        total*0.65
    ]
    })

    st.subheader("📈 Yearly Carbon Trend")

    st.line_chart(
        trend.set_index("Month")
    )

    fig, ax = plt.subplots()
    ax.pie(
        df["Emission"],
        labels=df["Category"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

# Green Tips
with st.expander("💡 Eco-Friendly Tips"):
    st.write("✅ Use public transport")
    st.write("✅ Plant more trees")
    st.write("✅ Switch to LED bulbs")
    st.write("✅ Reduce electricity waste")

# Footer
st.markdown("---")
st.markdown(
    "Developed by Tarun Bhardwaj | Carbon Footprint Awareness Platform"
)
