import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from joblib import dump
from sklearn.metrics import r2_score, mean_absolute_error

# Load dataset
df = pd.read_csv("data/final_gasification_dataset.csv")

# ==== Train Full Model ==== #
print("\n🔧 Training full model (Sensor + PS + MC)...")

# Features and Target
X_full = df[[
    "Gas (ppm)", "Temp (°C)", "Air Flow (m³/h)", "Fuel Rate (kg/h)",
    "ER", "Particle Size (mm)", "Moisture Content (%)"
]]
y_full = df[["H2 (%)", "CO (%)", "CH4 (%)", "CO2 (%)", "N2 (%)", "Efficiency", "Maintenance"]]

# Full Model Training
model_full = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
model_full.fit(X_full, y_full)

# Evaluation
y_pred_full = model_full.predict(X_full)
print(f"✅ Full Model R² Score: {r2_score(y_full, y_pred_full):.3f}")
print(f"✅ Full Model MAE: {mean_absolute_error(y_full, y_pred_full):.3f}")

# Save full model
dump(model_full, "model/syngas_model.joblib")
print("✅ Full model saved as model/syngas_model.joblib")

# ==== Train PS+MC Only Model ==== #
print("\n🔧 Training PS+MC model...")

X_psmc = df[["Particle Size (mm)", "Moisture Content (%)"]]
y_psmc = df[["H2 (%)", "CO (%)", "CH4 (%)", "CO2 (%)", "N2 (%)"]]

model_psmc = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
model_psmc.fit(X_psmc, y_psmc)

# Evaluation
y_pred_psmc = model_psmc.predict(X_psmc)
print(f"✅ PS+MC Model R² Score: {r2_score(y_psmc, y_pred_psmc):.3f}")
print(f"✅ PS+MC Model MAE: {mean_absolute_error(y_psmc, y_pred_psmc):.3f}")

# Save PS+MC model
dump(model_psmc, "model/ps_mc_model.joblib")
print("✅ PS+MC model saved as model/ps_mc_model.joblib")
