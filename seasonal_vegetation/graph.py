#!/usr/bin/env python3

import json, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from util import *

with open('vegetation.json') as f:
    data = json.loads(f.read())
# print(json.dumps(data, indent=4))

metric = 'percent live plant'

ids = list(set([item['plot id'] for item in data]))
#print(ids)
ids = ['E3'] # n5 n6 n7 n10 e3 e9 e10
#print(ids)
signals = []
signal = []
for id in ids:
    signal = [item[metric] for item in data if item['plot id'] == id]
    """for item in data:
        if item['plot id'] == id:
            print(item['plot id'])
            signal.append(item[metric])
            print(signal)
    """
    ts = [item['t'] for item in data if item['plot id'] == id]
    # signal = normalize(signal, 0, 100)
    signal = normalize(signal)
    # signal = normalize(signal)
    signal = resample(ts, signal, 1000)
    signal = smooth(signal, 200)
    signals.append(signal)

# signal = np.mean(signals, axis=0)
# print(signal)

ctx = drawing.Context(1600, 900)
for s, signal in enumerate(signals):
    ctx.plot(signal, stroke=colors[s], thickness=5.0)

xMin = 0
xMax = 1
x = xMin
reps = 10
while x < xMax:
    ctx.line(x, y1=0, x2=x, y2=1, stroke=colors[s], thickness=1.0, dash=None)
    x += (xMax/reps)

# ctx.plot(signal, stroke=colors[0])
ctx.output('seasonal_vegetation.png')

save('seasonal_vegetation.pkl', signals)

# n1 = [item['t'] for item in data if item['plot id'] == 'N1']
