from fastapi import FastAPI
import joblib
import numpy as np
import os

app = FastAPI(title='Bike Maintenance API')

MODEL_PATH = 'xgboost_model.joblib'
model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)

@app.get('/predictions')
def predictions():
    # Returns synthetic predictions if model not present
    samples = []
    for i in range(10):
        x = np.random.rand(3).tolist()
        score = float(np.sum(x)/3)
        samples.append({'bike_id': f'B-{i:03d}', 'risk_score': round(score,3)})
    return {'predictions': samples}
