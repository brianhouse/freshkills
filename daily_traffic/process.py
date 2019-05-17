#!/usr/bin/env python3

import json, sys, os, requests, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from util import *

with open('data.json') as f:
    data = f.read()
    data = json.loads(data)


ts = []
signal = []

for datum in data:
    ts.append(dt_to_t(string_to_dt(datum['time'])))
    signal.append(datum['CF']['SU'])

# print(signal)

signal = normalize(signal)

signal = resample(ts, signal, 1000)
signal = smooth(signal, 20)


# ctx = drawing.Context(1200, 500)
# ctx.plot(signal, stroke=colors[0], thickness=2.0)
# ctx.output('test.png')

save('daily_traffic.pkl', [signal])
