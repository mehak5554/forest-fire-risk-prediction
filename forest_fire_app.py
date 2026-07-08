import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("fire_model.pkl")

# Page settings
st.set_page_config(
    page_title="Forest Fire Risk Prediction",
    page_icon="🌲",
    layout="wide"
)

# Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        to bottom,
        #0f2027,
        #203a43,
        #2c5364
    );
}

h1, h2, h3 {
    text-align: center;
    color: white;
}

[data-testid="stMetricValue"] {
    color: #00ff88;
    font-size: 30px;
}

.stButton>button {
    width: 100%;
    height: 50px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.image(
    "https://images.unsplash.com/photo-1448375240586-882707db888b",
    use_container_width=True
)
st.markdown("""
# 🌲 Forest Fire Risk Prediction System
### Machine Learning Based Forest Fire Prediction
""")
st.caption(
   "Predicting wildfire risk using Machine Learning and environmental indicators."
)

# Sidebar
st.sidebar.title("🌲 About")
st.sidebar.info(
    """
    ### Forest Fire Risk Prediction System

    🤖 Model: Random Forest Classifier

    📊 Dataset: 
    Algerian Forest Fire Dataset

    🎯 Purpose:
    Predict wildfires risk based on
    weather and fire index measurements.

    💻 Developed By:
    Mehak Thakur
    """
)

# Input columns
col1, col2 = st.columns(2)

with col1:
    day = st.text_input("📅 Day", placeholder="1 - 31")
    month = st.text_input("📆 Month", placeholder="6 - 9")

    temperature = st.text_input(
        "🌡 Temperature",
        placeholder="22 - 42"
    )

    rh = st.text_input(
        "💧 Relative Humidity",
        placeholder="21 - 90"
    )

    ws = st.text_input(
        "💨 Wind Speed",
        placeholder="6 - 29"
    )

    rain = st.text_input(
        "🌧 Rain",
        placeholder="0 - 16.8"
    )

with col2:

    ffmc = st.text_input(
        "🔥 FFMC",
        placeholder="28 - 96"
    )

    dmc = st.text_input(
        "🌲 DMC",
        placeholder="1 - 65.9"
    )

    dc = st.text_input(
        "🌳 DC",
        placeholder="7 - 220.4"
    )

    isi = st.text_input(
        "⚡ ISI",
        placeholder="0 - 19"
    )

    bui = st.text_input(
        "📊 BUI",
        placeholder="1 - 68"
    )

    fwi = st.text_input(
        "🚨 FWI",
        placeholder="0 - 31.1"
    )

# Predict button
if st.button("Analyze Fire Risk"):

    try:

        # Convert inputs
        day = float(day)
        month = float(month)
        year = 2012

        temperature = float(temperature)
        rh = float(rh)
        ws = float(ws)
        rain = float(rain)

        ffmc = float(ffmc)
        dmc = float(dmc)
        dc = float(dc)
        isi = float(isi)
        bui = float(bui)
        fwi = float(fwi)

        # Validation
        if not (1 <= day <= 31):
            st.error("Day must be between 1 and 31")
            st.stop()

        if not (6 <= month <= 9):
            st.error("Month must be between 6 and 9")
            st.stop()

        if not (22 <= temperature <= 42):
            st.error("Temperature must be between 22 and 42")
            st.stop()

        if not (21 <= rh <= 90):
            st.error("RH must be between 21 and 90")
            st.stop()

        if not (6 <= ws <= 29):
            st.error("Wind Speed must be between 6 and 29")
            st.stop()

        if not (0 <= rain <= 16.8):
            st.error("Rain must be between 0 and 16.8")
            st.stop()

        # Create dataframe
        data = pd.DataFrame([[
            day,
            month,
            year,
            temperature,
            rh,
            ws,
            rain,
            ffmc,
            dmc,
            dc,
            isi,
            bui,
            fwi
        ]],
        columns=[
            "day",
            "month",
            "year",
            "Temperature",
            "RH",
            "Ws",
            "Rain",
            "FFMC",
            "DMC",
            "DC",
            "ISI",
            "BUI",
            "FWI"
        ])

        # Prediction
        prediction = model.predict(data)
        prob = model.predict_proba(data)

        fire_probability = prob[0][1] * 100

        st.subheader("📊 Prediction Result")

        if fire_probability < 30:
            st.success(
                f"🟢 LOW FIRE RISK({fire_probability:.2f}%)"
            )
        elif fire_probability < 70:
            st.warning(
                f"🟡 MODERATE FIRE RISK({fire_probability:.2f}%)"
            )
        else:
            st.error(
                f"🔴 HIGH FIRE RISK({fire_probability:.2f}%)"
            )
        st.metric(
            "Fire Risk Probability",
            f"{fire_probability:.2f}%"
        )
        st.progress(int(fire_probability))
        st.write("### Risk Meter")
    except ValueError:
        st.warning(
            "⚠ Please enter valid numeric values in all fields."
        )
st.markdown("---")
st.markdown(
    "<center>🌲 Built with Streamlit | Random Forest Classifier | © 2026 Mehak Thakur</center>",
    unsafe_allow_html=True
)