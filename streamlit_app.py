import streamlit as st
import numpy as np
import pandas as pd
from joblib import load

# Load full model
model_full = load("model/syngas_model.joblib")

# Load PS+MC model (assume it's trained separately and saved)
try:
    model_psmc = load("model/ps_mc_model.joblib")
except:
    model_psmc = None  # Fallback if not available

# Load training data for range checking
df = pd.read_csv("data/downdraft_gasification_dataset.csv")

# Safe input ranges (based on real downdraft gasifier literature)
RANGES = {
    "Gas (ppm)": (400, 600),
    "Temp (°C)": (650, 800),
    "Air Flow (m³/h)": (10, 20),
    "Fuel Rate (kg/h)": (2.0, 4.0),
    "Particle Size (mm)": (1.0, 4.0),
    "Moisture Content (%)": (5.0, 15.0)
}

def warn_range(value, label):
    r_min, r_max = RANGES[label]
    if not (r_min <= value <= r_max):
        st.warning(f"⚠️ {label} value {value} is out of expected range ({r_min}–{r_max})")

st.title("Biomass Gasification Dashboard ")
st.markdown("Choose your prediction input method:")

mode = st.radio("Select Input Mode:", [
    "Sensor + Particle Size + Moisture",
    "Only Particle Size + Moisture"
])

if mode == "Sensor + Particle Size + Moisture":
    st.subheader("🔍 Enter Sensor and Biomass Parameters")

    gas = st.number_input("Gas Sensor (ppm)", min_value=0.0, value=500.0)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, value=750.0)
    air = st.number_input("Air Flow Rate (m³/h)", min_value=0.1, value=15.0)
    fuel = st.number_input("Fuel Rate (kg/h)", min_value=0.1, value=3.0)
    ps = st.number_input("Particle Size (mm)", min_value=0.5, max_value=10.0, value=3.6)
    mc = st.number_input("Moisture Content (%)", min_value=0.0, max_value=100.0, value=7.5)

    ER = fuel / air if air != 0 else 0
    st.info(f"Calculated ER: {ER:.3f}")

    for key, val in zip(["Gas (ppm)", "Temp (°C)", "Air Flow (m³/h)", "Fuel Rate (kg/h)", "Particle Size (mm)", "Moisture Content (%)"],
                        [gas, temperature, air, fuel, ps, mc]):
        warn_range(val, key)

    if st.button("Predict Full Model"):
        input_data = np.array([[gas, temperature, air, fuel, ER, ps, mc]])
        pred = model_full.predict(input_data)[0]
        h2, co, ch4, co2, n2, eff, risk = pred

        # Normalize gases
        total = h2 + co + ch4 + co2 + n2
        h2, co, ch4, co2, n2 = [x / total * 100 for x in [h2, co, ch4, co2, n2]]

        st.success(f"✅ System Efficiency: {eff * 100:.2f}%")
        st.warning(f"⚠️ Maintenance Risk: {risk * 100:.2f}%")

        st.markdown(f"""
        ### 🧪 **Predicted Syngas Composition**
        - H₂: **{h2:.2f}%**
        - CO: **{co:.2f}%**
        - CH₄: **{ch4:.2f}%**
        - CO₂: **{co2:.2f}%**
        - N₂: **{n2:.2f}%**
        """)

        st.divider()
        st.markdown("### 🎯 Enter Actual Values for Comparison (Optional)")
        eff_actual = st.number_input("Actual Efficiency (0.0 - 1.0)", min_value=0.0, max_value=1.0, value=0.0)
        risk_actual = st.number_input("Actual Maintenance Risk (0.0 - 1.0)", min_value=0.0, max_value=1.0, value=0.0)

        if eff_actual > 0 or risk_actual > 0:
            st.markdown("### 📊 Comparison")
            st.write(f"**Efficiency** - Predicted: {eff:.3f} | Actual: {eff_actual:.3f}")
            st.write(f"**Maintenance** - Predicted: {risk:.3f} | Actual: {risk_actual:.3f}")

elif mode == "Only Particle Size + Moisture":
    st.subheader("🔍 Enter Only Biomass Properties")

    ps = st.number_input("Particle Size (mm)", min_value=0.5, max_value=10.0, value=3.6)
    mc = st.number_input("Moisture Content (%)", min_value=0.0, max_value=100.0, value=7.5)

    warn_range(ps, "Particle Size (mm)")
    warn_range(mc, "Moisture Content (%)")

    if model_psmc is None:
        st.error("⚠️ No simplified model found for PS+MC only prediction. Please train and save it as `ps_mc_model.joblib` in `model/` folder.")
    elif st.button("Predict with PS + MC"):
        input_data = np.array([[ps, mc]])
        pred = model_psmc.predict(input_data)[0]
        h2, co, ch4, co2, n2 = pred

        total = h2 + co + ch4 + co2 + n2
        h2, co, ch4, co2, n2 = [x / total * 100 for x in [h2, co, ch4, co2, n2]]

        st.success("✅ Predicted Syngas Composition:")
        st.markdown(f"""
        - H₂: **{h2:.2f}%**  
        - CO: **{co:.2f}%**  
        - CH₄: **{ch4:.2f}%**  
        - CO₂: **{co2:.2f}%**  
        - N₂: **{n2:.2f}%**
        """)
