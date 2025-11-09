import pandas as pd
import numpy as np

# Base table (from your image, manually filled)
base_data = [
    [3.6, 7.5, 13.6, 17.7, 6.3, 42.6, 19.8],
    [1.1, 10.0, 13.0, 16.1, 6.6, 43.3, 21.0],
    [1.1, 12.5, 13.2, 17.2, 6.2, 41.7, 21.7],
    [3.6, 12.5, 14.0, 17.9, 6.9, 41.9, 19.3],
    [2.6, 10.0, 15.3, 19.2, 6.4, 41.1, 18.0],
    [1.6, 12.5, 14.4, 18.3, 6.3, 41.3, 20.0],
    [2.6, 10.0, 15.5, 19.1, 6.5, 40.5, 18.2],
    [2.6, 5.0, 12.7, 15.8, 6.9, 45.4, 19.2],
    [2.6, 15.0, 14.3, 18.5, 6.8, 41.8, 18.6],
    [4.0, 10.0, 15.2, 19.1, 6.5, 41.0, 18.2],
    [3.6, 10.0, 13.3, 17.4, 6.2, 42.5, 20.8],
    [3.6, 10.0, 14.4, 18.6, 6.3, 41.0, 19.3],
    [1.6, 7.5, 13.2, 15.8, 6.8, 43.0, 20.0],
]

columns = [
    "Particle Size (mm)", "Moisture Content (%)", "CO (%)", "H2 (%)", "CH4 (%)", "N2 (%)", "CO2 (%)"
]

df_base = pd.DataFrame(base_data, columns=columns)

# Function to generate 100+ synthetic samples from base
synthetic_data = []
for _ in range(110):
    sample = df_base.sample(n=1).iloc[0]
    noise = np.random.normal(loc=0, scale=0.5, size=7)
    synthetic_row = sample + noise
    synthetic_row = np.clip(synthetic_row, 0, None)  # no negative values
    synthetic_data.append(synthetic_row)

df_syn = pd.DataFrame(synthetic_data, columns=columns)

# Add realistic sensor values
df_syn["Gas (ppm)"] = np.random.randint(450, 550, size=len(df_syn))
df_syn["Temp (°C)"] = np.random.randint(680, 770, size=len(df_syn))
df_syn["Air Flow (m³/h)"] = np.round(np.random.uniform(12.0, 16.0, size=len(df_syn)), 2)
df_syn["Fuel Rate (kg/h)"] = np.round(np.random.uniform(2.4, 3.4, size=len(df_syn)), 2)
df_syn["ER"] = np.round(np.random.uniform(0.20, 0.25, size=len(df_syn)), 3)
df_syn["Efficiency"] = np.round(np.random.uniform(0.74, 0.84, size=len(df_syn)), 2)
df_syn["Maintenance"] = np.round(np.random.uniform(0.10, 0.17, size=len(df_syn)), 2)

# Reorder columns
final_columns = [
    "Gas (ppm)", "Temp (°C)", "Air Flow (m³/h)", "Fuel Rate (kg/h)", "ER",
    "Particle Size (mm)", "Moisture Content (%)",
    "H2 (%)", "CO (%)", "CH4 (%)", "CO2 (%)", "N2 (%)", "Efficiency", "Maintenance"
]

df_final = df_syn[final_columns]

# Save dataset
df_final.to_csv("data/final_gasification_dataset.csv", index=False)
print("✅ Dataset generated and saved to data/final_gasification_dataset.csv")
