import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="🚀 Delivery Time Predictor",
    page_icon="🛵",
    layout="centered",
)

# ── REALISTIC UI ENHANCEMENT CSS ────────────────────────────
st.markdown("""
<style>

/* 🌌 FULL BACKGROUND */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

/* 📦 GLASS CARD EFFECT */
.block-container {
    padding: 2rem;
}

/* TITLE */
.section-title {
    font-size: 1.1rem;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #60a5fa;
}

/* INPUT LABELS */
label {
    color: #a78bfa !important;
    font-weight: 600 !important;
}

/* INPUT BOX STYLE */
.stSelectbox, .stSlider, .stNumberInput {
    background: rgba(255,255,255,0.05);
    padding: 10px;
    border-radius: 10px;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.6rem 1rem;
    border: none;
    box-shadow: 0px 0px 15px rgba(99,102,241,0.5);
}

/* SUCCESS BOX */
.stSuccess {
    background: rgba(34,197,94,0.1);
}

/* WARNING BOX */
.stWarning {
    background: rgba(234,179,8,0.1);
}

/* ERROR BOX */
.stError {
    background: rgba(239,68,68,0.1);
}

</style>
""", unsafe_allow_html=True)
# ── LOAD MODEL ─────────────────────────────────────────────
@st.cache_resource
def load_model():
    return joblib.load("rf_model.pkl")

model = load_model()

# ── HERO IMAGE (FIXED - MEDIUM SIZE) ────────────────────────
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("banner.jpg", width=650)

st.markdown(
    "<h2 style='text-align:center;'>🚀 Smart Delivery Time Predictor</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:gray;'>AI-powered logistics prediction dashboard</p>",
    unsafe_allow_html=True
)

# ── INPUTS ─────────────────────────────────────────────────
distance = st.slider("Distance (km)", 0.5, 50.0, 10.0)
prep_time = st.slider("Preparation Time (min)", 1, 60, 15)
experience = st.number_input("Courier Experience (yrs)", 0.0, 20.0, 3.0)

st.markdown('<div class="section-title">🚀 Courier & Vehicle</div>', unsafe_allow_html=True)
vehicle = st.selectbox("Vehicle Type", ["Bike", "Car", "Scooter"])

st.markdown('<div class="section-title">🌦️ Conditions</div>', unsafe_allow_html=True)
weather = st.selectbox("Weather", ["Clear", "Foggy", "Rainy", "Snowy", "Windy"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])

# ── PREDICTION ─────────────────────────────────────────────
if st.button("⚡ Predict Delivery Time"):

    with st.spinner("Analyzing real-world delivery conditions..."):

        features = {
            "Distance_km": distance,
            "Preparation_Time_min": prep_time,
            "Courier_Experience_yrs": experience,
            "Weather_Clear": 1 if weather == "Clear" else 0,
            "Weather_Foggy": 1 if weather == "Foggy" else 0,
            "Weather_Rainy": 1 if weather == "Rainy" else 0,
            "Weather_Snowy": 1 if weather == "Snowy" else 0,
            "Weather_Windy": 1 if weather == "Windy" else 0,
            "Traffic_Level_High": 1 if traffic == "High" else 0,
            "Traffic_Level_Low": 1 if traffic == "Low" else 0,
            "Traffic_Level_Medium": 1 if traffic == "Medium" else 0,
            "Time_of_Day_Afternoon": 1 if time_of_day == "Afternoon" else 0,
            "Time_of_Day_Evening": 1 if time_of_day == "Evening" else 0,
            "Time_of_Day_Morning": 1 if time_of_day == "Morning" else 0,
            "Time_of_Day_Night": 1 if time_of_day == "Night" else 0,
            "Vehicle_Type_Bike": 1 if vehicle == "Bike" else 0,
            "Vehicle_Type_Car": 1 if vehicle == "Car" else 0,
            "Vehicle_Type_Scooter": 1 if vehicle == "Scooter" else 0,
        }

        X = pd.DataFrame([features])
        prediction = model.predict(X)[0]

    # ── RESULT CARD ───────────────────────────────────────
    st.success(f"🚀 Estimated Delivery Time: {prediction:.2f} minutes")

    # ── AI EXPLANATION ────────────────────────────────────
    st.markdown('<div class="section-title">🧠 AI Explanation</div>', unsafe_allow_html=True)

    reasons = []

    if traffic == "High":
        reasons.append("Heavy traffic is slowing delivery")
    if weather in ["Rainy", "Snowy"]:
        reasons.append("Bad weather affecting speed")
    if distance > 20:
        reasons.append("Long distance increases travel time")
    if experience < 2:
        reasons.append("Low courier experience reduces efficiency")

    if not reasons:
        reasons.append("Optimal conditions for fast delivery")

    for r in reasons:
        st.write("•", r)

    # ── MOOD SCORE ─────────────────────────────────────────
    st.markdown('<div class="section-title">😎 Delivery Mood Score</div>', unsafe_allow_html=True)

    if prediction < 20:
        st.success("🟢 FAST DELIVERY MODE — Order will arrive quickly")
    elif prediction < 40:
        st.warning("🟡 NORMAL DELIVERY MODE — Slight delay possible")
    else:
        st.error("🔴 DELAY RISK MODE — Order may arrive late")

    # ── GAUGE ─────────────────────────────────────────────
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Delivery Time Gauge"},
        gauge={'axis': {'range': [0, 120]}}
    ))
    st.plotly_chart(fig, use_container_width=True)

    # ── GRAPHS ────────────────────────────────────────────
    data = pd.read_csv("large_delivery_data.csv")

    st.markdown('<div class="section-title">📈 Traffic Analysis</div>', unsafe_allow_html=True)

    fig_bar = px.bar(
        data.groupby("Traffic_Level")["time"].mean().reset_index(),
        x="Traffic_Level",
        y="time",
        color="Traffic_Level"
    )

    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown('<div class="section-title">📉 Delivery Insights</div>', unsafe_allow_html=True)

    fig_scatter = px.scatter(
        data,
        x="Distance_km",
        y="time",
        color="Traffic_Level",
        size="Preparation_Time_min",
        hover_data=["Weather", "Vehicle_Type"]
    )

    st.plotly_chart(fig_scatter, use_container_width=True)