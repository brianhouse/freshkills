#!/usr/bin/env python3

import json, sys, os, requests, time, csv, random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from util import *



signal = []
ts = []
for i in range(10):
    signal.append(random.randint(45, 66) / 100)
    ts.append(i)

signal = resample(range(len(signal)), signal, 1000)
signal = smooth(signal, 400)

ctx = drawing.Context(1200, 500)
ctx.plot(signal, stroke=colors[0], thickness=2.0)
ctx.output('test.png')

save("epochal_geology.pkl", [signal])