🚀 AI Projects Portfolio 

This repository contains **three complete AI/ML project implementations** with backend APIs, model training scripts, and Streamlit dashboards.

## **1️⃣ Adaptive Traffic Signal Control (Reinforcement Learning + SUMO)**

An RL-based system that optimizes traffic light timing to reduce congestion.

**Includes:**

* DQN model (TensorFlow)
* FastAPI backend (`/status`)
* Training loop (synthetic demo)
* React frontend (placeholder)
* Streamlit demo dashboard
============================================================================================
## **2️⃣ Pest Infestation Forecaster (ConvLSTM + Satellite Data)**

Forecasts pest spread for the next 1–3 days using NDVI, weather, and drone images.

**Includes:**

* NDVI calculator
* ConvLSTM model architecture
* FastAPI backend (drone upload)
* Static frontend placeholder
* Streamlit visualization demo
============================================================================================

## **3️⃣ Predictive Maintenance for Bike-Sharing (XGBoost)**

Predicts component failures in shared bikes and ranks maintenance priority.

**Includes:**

* Synthetic ride data generator
* XGBoost model training script
* FastAPI backend (`/predictions`)
* React UI placeholder
* Streamlit maintenance dashboard

============================================================================================
# 📦 Folder Structure

AI-Projects-Portfolio/
│
├── 1-Adaptive-Traffic-Signal-Control/
├── 2-Pest-Infestation-Forecaster/
├── 3-Predictive-Maintenance-Bike-Sharing/
└── streamlit/
============================================================================================

Each project contains:

* `backend/` — FastAPI app
* `training/` or `models/` — ML model scripts
* `processing/` — Data pipeline scripts
* `frontend/` — React placeholder interface
* `requirements.txt` — Python dependencies

============================================================================================
# ▶️ How to Run

## **Backend (FastAPI)**

Example (Traffic Control):

```bash
cd 1-Adaptive-Traffic-Signal-Control/backend
uvicorn api.main:app --reload --port 8000


## **Model Training**

Example (Bike Predictive Maintenance):

```bash
cd 3-Predictive-Maintenance-Bike-Sharing/backend/model
python model_training.py


## **Streamlit Dashboard**

Run combined dashboard:

```bash
cd streamlit
streamlit run streamlit_app_all.py

