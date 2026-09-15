
import pandas as pd
import joblib


# Load the trained model
model = joblib.load("greengrid_core_model.pkl")

# Load the weather dataset
df = pd.read_csv("greengrid_weather_solar.csv")


# Features used during model training
features = [
    "hour",
    "temperature_c",
    "cloud_cover_pct",
    "uv_index",
    "wind_speed_kmh",
    "humidity_pct",
    "solar_irradiance_wm2"
]


# Select the latest complete day
latest_date = df["date"].max()

daily_data = df[df["date"] == latest_date].copy()


# Predict solar output for every hour
daily_data["predicted_output_kwh"] = model.predict(
    daily_data[features]
)


# Calculate total daily solar output
total_output = daily_data["predicted_output_kwh"].sum()


# Display the result
print("GreenGrid Energy Daily Prediction")
print("----------------------------------")
print("Date:", latest_date)
print(
    "Predicted total solar output:",
    round(total_output, 4),
    "kWh"
)
