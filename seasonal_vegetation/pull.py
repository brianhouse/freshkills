#!/usr/bin/env python3

import json, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import *

with open('vegetation.json') as f:
    data = json.loads(f.read())
# print(json.dumps(data, indent=4))

metric = 'percent live plant'

ids = list(set([item['plot id'] for item in data]))
ids = ['E3'] # n5 n6 n7 n10 e3 e9 e10
signals = []
for id in ids:
    signal = [item[metric] for item in data if item['plot id'] == id]
    ts = [item['t'] for item in data if item['plot id'] == id]
    # signal = normalize(signal, 0, 100)
    signal = normalize(signal)
    # signal = normalize(signal)
    signal = resample(ts, signal, 1000)
    signal = smooth(signal, 200)
    signals.append(signal)

# signal = np.mean(signals, axis=0)
# print(signal)

save('seasonal_vegetation.pkl', signals)

# n1 = [item['t'] for item in data if item['plot id'] == 'N1']
