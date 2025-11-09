from joblib import load
from fake_input import get_sensor_data

model = load("model/syngas_model.joblib")
X = get_sensor_data()
prediction = model.predict(X)[0]

h2, co, ch4, co2, n2, efficiency, maintenance = prediction

total = h2 + co + ch4 + co2 + n2
h2_pct = (h2 / total) * 100
co_pct = (co / total) * 100
ch4_pct = (ch4 / total) * 100
co2_pct = (co2 / total) * 100
n2_pct = (n2 / total) * 100

print("\n🔥 Prediction Result")
print(f"System Efficiency: {efficiency * 100:.2f}%")
print(f"H₂: {h2_pct:.2f}%, CO: {co_pct:.2f}%, CH₄: {ch4_pct:.2f}%, CO₂: {co2_pct:.2f}%, N₂: {n2_pct:.2f}%")
print(f"Maintenance Risk: {maintenance * 100:.2f}%")
