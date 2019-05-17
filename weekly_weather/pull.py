#!/usr/bin/env python3

import json, sys, os, requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import *

secret_key = config['darksky']
latitude, longitude = 40.577098, -74.185990

url = 'https://api.darksky.net/forecast/%s/%s,%s?exclude=currently,minutely,hourly,alerts,flags' % (secret_key, latitude, longitude)

r = requests.get(url)

data = r.json()
days = data['daily']['data']

# print(json.dumps(data, indent=4))

signals = []
for param in ['temperatureHigh', 'precipProbability', 'humidity']:
    signal = [day[param] for day in days]
    signal = normalize(signal)
    signal = resample([i for i in range(len(signal))], signal, 1000)
    signal = smooth(signal, 200)
    signals.append(signal)

save('weekly_weather.pkl', signals)
