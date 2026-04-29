# smart-delivery-eta
AI-powered delivery time prediction dashboard using Machine Learning. The system analyzes distance, traffic, weather, and courier experience to estimate delivery time and provide real-time insights through an interactive Streamlit UI.

# 🛵 Delivery Time Prediction System

A machine learning-based web application that predicts estimated food delivery time using real-world operational factors such as distance, traffic conditions, weather, courier experience, and time of day.

The system uses a trained **Random Forest Regressor** model and is deployed through an interactive **Streamlit dashboard** for real-time prediction and analytics.

Live Demo: https://deliverytimepredictor-me2pawh5dee4nwzhgrdund.streamlit.app/

---

## 📌 Overview

Accurate delivery time estimation is a critical component in logistics and food delivery systems. It directly impacts customer satisfaction, operational efficiency, and resource planning.

This project demonstrates how machine learning can be used to model delivery time by considering multiple dynamic factors such as traffic, weather, and courier performance.

---

## ✨ Key Features

- Real-time delivery time prediction using Machine Learning
- Multi-factor analysis (traffic, weather, distance, courier experience)
- Interactive Streamlit dashboard
- Feature importance interpretation
- Clean and responsive UI
- Instant ETA generation based on user inputs

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Regressor  
- **Estimators:** 100 trees  
- **Framework:** Scikit-learn  
- **Input Features:** 18 engineered features  
- **Output:** Delivery time (in minutes)

---

## 📊 Input Features

### Numeric Features
- Distance (km)
- Preparation Time (minutes)
- Courier Experience (years)

### Weather Conditions
- Clear, Foggy, Rainy, Snowy, Windy

### Traffic Levels
- Low, Medium, High

### Time of Day
- Morning, Afternoon, Evening, Night

### Vehicle Type
- Bike, Car, Scooter

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Delivery_time_predictor.git
cd Delivery_time_predictor

