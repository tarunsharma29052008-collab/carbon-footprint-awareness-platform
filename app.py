import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🌍 Carbon Footprint Awareness Platform")

transport = st.selectbox(
    "Transport",
    ["Car","Bike","Bus","Train"]
)

distance = st.number_input("Distance per day (km)",0)

electricity = st.number_input("Electricity Usage (kWh)",0)

transport_emission = 0

if transport=="Car":
    transport_emission = distance*0.21
elif transport=="Bike":
    transport_emission = distance*0.10
elif transport=="Bus":
    transport_emission = distance*0.08
elif transport=="Train":
    transport_emission = distance*0.05

electricity_emission = electricity*0.4

total = transport_emission + electricity_emission

if st.button("Calculate"):
    st.success(f"Total Carbon Footprint = {total:.2f} kg CO₂")

    data = {
        "Category":["Transport","Electricity"],
        "Emission":[transport_emission,electricity_emission]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.pie(df["Emission"], labels=df["Category"], autopct="%1.1f%%")
    st.pyplot(fig)

if total < 50:
    st.success("Eco Score : 90/100")
elif total < 100:
    st.warning("Eco Score : 70/100")
else:
    st.error("Eco Score : 40/100")

trees = round(total / 10)

st.info(f"🌳 Trees Required to Offset = {trees}")

st.subheader("Green Tips")

tips = [
"Use public transport",
"Switch to LED bulbs",
"Save electricity",
"Plant trees"
]

for tip in tips:
    st.write("✅",tip)