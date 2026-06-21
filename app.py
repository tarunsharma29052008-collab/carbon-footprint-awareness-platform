import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Carbon Footprint Pro",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main-title{
    text-align:center;
    color:green;
}
.card{
    padding:15px;
    border-radius:10px;
    background-color:#f0f2f6;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CACHE ----------------
@st.cache_data
def calculate_emission(transport, distance, electricity):
    factors = {
        "Car": 0.21,
        "Bike": 0.10,
        "Bus": 0.08,
        "Train": 0.05
    }

    transport_emission = distance * factors[transport]
    electricity_emission = electricity * 0.4
    total = transport_emission + electricity_emission

    return transport_emission, electricity_emission, total

# ---------------- FUNCTIONS ----------------
def get_eco_score(total):
    if total < 50:
        return 90, "🏆 Green Champion"
    elif total < 100:
        return 70, "🥈 Eco Warrior"
    else:
        return 40, "⚠️ Needs Improvement"

# ---------------- SIDEBAR ----------------
st.sidebar.title("🌍 Eco Dashboard")

st.sidebar.info("""
Carbon Footprint Awareness Platform

✅ Track emissions
✅ Reduce footprint
✅ Save environment
""")

# ---------------- TITLE ----------------
st.markdown(
    "<h1 class='main-title'>🌍 Carbon Footprint Awareness Platform</h1>",
    unsafe_allow_html=True
)

st.caption(
    "Accessible platform for measuring and reducing carbon emissions."
)

with st.expander("ℹ️ About This Calculator"):
    st.write("""
    This calculator estimates your carbon footprint based on:
    - Daily transportation
    - Electricity consumption
    """)

# ---------------- HISTORY ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- INPUTS ----------------
goal = st.slider(
    "🎯 Carbon Reduction Goal (%)",
    0,
    100,
    20
)

col1, col2 = st.columns(2)

with col1:
    transport = st.selectbox(
        "Transport Mode",
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

# ---------------- CALCULATE ----------------
if st.button("🚀 Calculate Carbon Footprint"):

    transport_emission, electricity_emission, total = calculate_emission(
        transport,
        distance,
        electricity
    )

    eco_score, badge = get_eco_score(total)

    trees = round(total / 10)

    # ---------------- RESULT ----------------
    st.success(
        f"🌍 Total Carbon Footprint = {total:.2f} kg CO₂"
    )

    # Metrics
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total CO₂",
        f"{total:.2f} kg"
    )

    c2.metric(
        "Eco Score",
        f"{eco_score}/100"
    )

    c3.metric(
        "Trees Required",
        trees
    )

    st.subheader("🏅 Achievement")

    st.success(badge)

    # ---------------- CATEGORY ----------------
    if total < 50:
        category = "Low"
    elif total < 100:
        category = "Medium"
    else:
        category = "High"

    st.info(f"Carbon Category: {category}")

    # ---------------- AI INSIGHTS ----------------
    st.subheader("🤖 AI Recommendations")

    if transport_emission > electricity_emission:
        st.warning(
            "Most emissions come from transportation. Consider public transport."
        )
    else:
        st.warning(
            "Most emissions come from electricity usage. Save energy."
        )

    # ---------------- GOAL ----------------
    target = total * (1 - goal / 100)

    st.info(
        f"🎯 Target Carbon Footprint = {target:.2f} kg CO₂"
    )

    st.progress(eco_score)

    # ---------------- DATA ----------------
    data = pd.DataFrame({
        "Category": ["Transport", "Electricity"],
        "Emission": [
            transport_emission,
            electricity_emission
        ]
    })

    # ---------------- BAR CHART ----------------
    st.subheader("📊 Emission Breakdown")

    st.bar_chart(
        data.set_index("Category")
    )

    # ---------------- PIE CHART ----------------
    fig, ax = plt.subplots()

    ax.pie(
        data["Emission"],
        labels=data["Category"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

    # ---------------- TREND ----------------
    trend = pd.DataFrame({
        "Month": [
            "Jan","Feb","Mar","Apr","May","Jun",
            "Jul","Aug","Sep","Oct","Nov","Dec"
        ],
        "Emission": [
            total*1.2,
            total*1.1,
            total*1.05,
            total,
            total*0.95,
            total*0.90,
            total*0.85,
            total*0.80,
            total*0.78,
            total*0.75,
            total*0.70,
            total*0.65
        ]
    })

    st.subheader("📈 Yearly Trend")

    st.line_chart(
        trend.set_index("Month")
    )

    # ---------------- SAVE HISTORY ----------------
    st.session_state.history.append({
        "Emission": total,
        "Eco Score": eco_score,
        "Category": category
    })

    # ---------------- REPORT ----------------
    report = f"""
Carbon Footprint Report

Total Emission: {total:.2f} kg CO₂
Eco Score: {eco_score}/100
Trees Required: {trees}
Category: {category}
"""

    st.download_button(
        "📥 Download Report",
        report,
        file_name="carbon_report.txt"
    )

# ---------------- HISTORY TABLE ----------------
if len(st.session_state.history) > 0:

    st.subheader("📜 Previous Calculations")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

    csv = history_df.to_csv(index=False)

    st.download_button(
        "📊 Export History CSV",
        csv,
        file_name="history.csv",
        mime="text/csv"
    )

# ---------------- ECO TIPS ----------------
with st.expander("💡 Eco Friendly Tips"):
    st.write("✅ Use Public Transport")
    st.write("✅ Save Electricity")
    st.write("✅ Use LED Bulbs")
    st.write("✅ Plant Trees")
    st.write("✅ Reduce Fuel Consumption")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "Developed by Tarun Bhardwaj | Carbon Footprint Awareness Platform"
)
