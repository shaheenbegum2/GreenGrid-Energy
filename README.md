# GreenGrid Energy - Solar Output Forecasting

## Project Overview

GreenGrid Energy is an AI/ML project that predicts solar panel energy output using weather and environmental data.

The project uses a Random Forest Regression model to predict solar panel output in kilowatt-hours (kWh).

## Objective

The main objective is to forecast solar energy production using weather-related features such as temperature, cloud cover, UV index, wind speed, humidity, and solar irradiance.

## Dataset

The dataset contains hourly solar and weather information.

Important features include:

* Hour
* Temperature
* Cloud cover
* UV index
* Wind speed
* Humidity
* Solar irradiance

Target variable:

* `panel_output_kwh`

## Machine Learning Model

The project uses a **Random Forest Regressor**.

The dataset was divided into training and testing sets using a chronological split.

## Model Performance

* Mean Absolute Error (MAE): **0.0041 kWh**
* Root Mean Squared Error (RMSE): **0.0078 kWh**

The model achieved an MAE below the project acceptance limit of 0.5 kWh.

## Project Files

* `GreenGrid_Energy_Baseline.ipynb` - Main Google Colab/Jupyter notebook
* `greengrid_weather_solar.csv` - Weather and solar dataset
* `greengrid_core_model.pkl` - Trained Random Forest model
* `greengrid_residual_plot.png` - Residual plot for model evaluation
* `greengrid_7_day_forecast.png` - Seven-day prediction plot
* `predict.py` - Daily solar output prediction script
* `requirements.txt` - Required Python libraries

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Matplotlib
* Google Colab
* GitHub

## Installation

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## How to Run

Run the daily prediction script:

```bash
python predict.py
```

The script loads the trained model and dataset, predicts hourly solar output for the latest complete day, and calculates the total predicted daily output.

## Sample Output

```text
GreenGrid Energy Daily Prediction
----------------------------------
Date: 2025-03-31
Predicted total solar output: 8.1794 kWh
```

## Conclusion

The GreenGrid Energy project demonstrates how machine learning can be used to estimate solar panel energy production from weather and solar-related data. The trained model achieved a low prediction error and can be used as a foundation for future automated forecasting and deployment.

