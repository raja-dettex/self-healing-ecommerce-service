import numpy as np
from sklearn.ensemble import IsolationForest
from recovery.metrics.metrics import get_prometheus_data
model = IsolationForest(contamination=0.5)

def get_anomalies():
    df = get_prometheus_data()
    X = np.array(df['latency']).reshape(-1,1)
    model.fit(X)
    df['predictions'] = model.predict(X)
    anomalies_df = df[df['predictions'] == -1]
    if (anomalies_df.empty != True):
        return [{'timestamps' : anomaly_df[0], 'latency': anomaly_df[1]} for anomaly_df in anomalies_df.values]
    return []
