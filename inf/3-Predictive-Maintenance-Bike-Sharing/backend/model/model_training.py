import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

def generate_synthetic_data(n_bikes=200, days=180):
    rows = []
    for bike in range(n_bikes):
        km = np.random.exponential(5, days).cumsum()
        for day in range(days):
            rows.append({
                'bike_id': f'B-{bike:03d}',
                'day': day,
                'avg_vibration': np.random.rand(),
                'total_km': km[day],
                'days_since_service': np.random.randint(0,90),
                'failure_next_15': np.random.binomial(1, 0.02)
            })
    return pd.DataFrame(rows)

if __name__ == '__main__':
    df = generate_synthetic_data()
    X = df[['avg_vibration','total_km','days_since_service']]
    y = df['failure_next_15']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    joblib.dump(model, 'xgboost_model.joblib')
    print('Model trained and saved.')
