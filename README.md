# 🌲 Forest Fire Risk Prediction System

A machine learning-based application that predicts forest fire risk using weather conditions and fire index parameters.

## 🚀 Overview

This project uses a trained Machine Learning model to classify forest fire risk based on environmental factors. The application provides an interactive interface where users can enter weather and fire index values to get a prediction along with the fire risk probability score.

The model is deployed using **Streamlit** to create a user-friendly web application.

## ✨ Features

- 🔥 Forest fire risk prediction
- 🤖 Random Forest based classification
- 📊 Fire risk probability score
- 🌡 Weather parameter-based analysis
- ✅ Input validation for user-entered values
- 🎨 Interactive Streamlit dashboard

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

## 🤖 Machine Learning Model

**Algorithm Used:**
- Random Forest Classifier

The model learns patterns from forest fire data and predicts whether the given environmental conditions indicate high or low fire risk.

## 📌 Input Parameters

The application uses the following parameters:

- Day
- Month
- Year
- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- Fine Fuel Moisture Code (FFMC)
- Duff Moisture Code (DMC)
- Drought Code (DC)
- Initial Spread Index (ISI)
- Buildup Index (BUI)
- Fire Weather Index (FWI)

## 📊 Model Performance

- Accuracy: ~98%

## ▶️ Run Locally

Clone the repository:

```bash
git clone your_repository_link