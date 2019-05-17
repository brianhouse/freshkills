#!/usr/bin/env python3

import json, sys, os, requests, time, csv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from util import *


# data = []
# with open("data.csv") as f:
#     for r, row in enumerate(csv.reader(f)):
#         if r == 0:
#             keys = [item.lower() for item in row]
#         else:
#             data.append(dict(zip(keys, [as_numeric(item) for item in row])))
# with open("data.json", 'w') as f:
#     f.write(json.dumps(data, indent=4))


with open('data.json') as f:
    data = f.read()
    data = json.loads(data)

fields = data[0].keys()
fields = [field for field in fields if (field[:4] != 'decr' and field != 'year')]

signals = []
for field in fields:
    signal = [datum[field] for datum in data]
    signal = resample(range(len(signal)), signal, 1000)
    signal = normalize(signal)
    signal = smooth(signal, 100)
    signals.append(signal)

ctx = drawing.Context(1200, 500)
for s, signal in enumerate(signals):
    ctx.plot(signal, stroke=colors[s], thickness=2.0)
ctx.output('test.png')


save("generational_decay.pkl", [signals[0]])