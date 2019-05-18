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
#             o = dict(zip(keys, [as_numeric(item) for item in row]))
#             if o['zone'] == "N.Y.C.":
#                 del o['zone']
#                 o['date'] = string_to_dt(o['date'])
#                 data.append(o)
# with open("data.json", 'w') as f:
#     f.write(json.dumps(data, indent=4, default=lambda o: str(o)))


with open('data.json') as f:
    data = f.read()
    data = json.loads(data)


ts = [o['date'] for o in data]
signal = [o['load'] for o in data]

signal = resample(range(len(signal)), signal, 1000)
signal = normalize(signal)
signal = smooth(signal, 50)

ctx = drawing.Context(1200, 500)
ctx.plot(signal, stroke=colors[0], thickness=2.0)
ctx.output('test.png')


save("daily_energy.pkl", [signal])