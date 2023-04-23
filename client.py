
import requests
import datetime
import math
import random

# Generate some fake data
time_series = []
for i in range(30):
    time = datetime.datetime.strptime('2022-11-' + str(i + 1), '%Y-%m-%d')
    t = math.floor(time.timestamp()) * 1000
    time_series.append([t, random.random() * (i + 1)])

# Data that we will send in POST request
data = {
    'panes': [{
        'overlays': [{
            'name': 'APE Stock',
            'type': 'Spline',
            'data': time_series,
            'settings': {
                'precision': 2
            }
        }]
    }]
}

# The POST request to our NightVision server
res = requests.post('http://127.0.0.1:7779/plot', json=data)

# Convert response data to json
returned_data = res.json()

print(returned_data)
