#!/usr/bin/env python3

import csv, json, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import numpy as np
from datetime import timedelta
from util import *

keys = []
data = []
with open("arthur_kill_tides.csv") as f:
    for r, row in enumerate(csv.reader(f)):
        if r == 0:
            keys = [item.lower() for item in row]
        else:
            data.append(dict(zip(keys, [as_numeric(item) for item in row])))

print(json.dumps(data, indent=4, default=lambda o: str(o)))


signal = [datum['pred'] for datum in data if datum['high/low'] == 'H']
# signal = [datum['pred'] for datum in data]
print(signal)
print(len(signal))
signal = normalize(signal)
signal = resample([i for i in range(len(signal))], signal, 1000)
signal = smooth(signal, 20)
signals = [signal]

save('monthly_tides.pkl', signals)
