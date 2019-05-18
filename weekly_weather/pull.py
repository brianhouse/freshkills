#!/usr/bin/env python3

import json, sys, os, requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import *
from datetime import timedelta

secret_key = config['darksky']
latitude, longitude = 40.577098, -74.185990

starts = []
starts.append(string_to_dt("2019-05-22 00:00:00"))
for i in range(6):
    starts.append(starts[-1] + timedelta(days=1))
starts = [dt_to_t(start) for start in starts]

hours = []
for start in starts:
    url = 'https://api.darksky.net/forecast/%s/%s,%s,%s?exclude=currently,minutely,alerts,flags' % (secret_key, latitude, longitude, start)
    r = requests.get(url)
    data = r.json()
    hours.extend(data['hourly']['data'])
# days = data['daily']['data']

print(json.dumps(hours, indent=4))

signals = []
# for param in ['temperatureHigh', 'precipProbability', 'humidity']:
for param in ['apparentTemperature']:    
    signal = [hour[param] for hour in hours]
    print(signal)
    signal = normalize(signal)
    signal = resample([i for i in range(len(signal))], signal, 1000)
    signal = smooth(signal, 35)
    signals.append(signal)

ctx = drawing.Context(1200, 500)
for s, signal in enumerate(signals):
    ctx.plot(signal, stroke=colors[s], thickness=2.0)
ctx.output('test.png')    

save('weekly_weather.pkl', signals)
