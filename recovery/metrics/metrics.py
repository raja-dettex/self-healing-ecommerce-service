import requests
from pandas import DataFrame
PROM_URL = 'http://localhost:9090/api/v1/query'


def get_prometheus_data() -> DataFrame:
    query = 'rate(request_latency_seconds_sum[1m])'
    response = requests.get(PROM_URL, params={'query': query})
    data = response.json()['data']['result']
    timestamps, values = [], []
    for result in data:
        timestamps.append(result['value'][0])
        values.append(result['value'][1])

    df = DataFrame({'timestamps': timestamps, 'latency': values})
    return df
