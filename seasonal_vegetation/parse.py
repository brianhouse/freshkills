#!/usr/bin/env python3

import csv, json, sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import numpy as np
from datetime import timedelta
from util import *

keys = []
data = []
with open("vegetation.csv") as f:
    for r, row in enumerate(csv.reader(f)):
        if r == 0:
            keys = [item.lower() for item in row]
        else:
            data.append(dict(zip(keys, [as_numeric(item) for item in row])))

string = "May 1, 2018"
start_date = string_to_dt(string)

for datum in data:
    delta = timedelta(days=datum['days since may 1'])
    datum['date'] = start_date + delta
    datum['t'] = dt_to_t(datum['date'])
    del datum['days since may 1']

print(json.dumps(data, indent=4, default=lambda o: str(o)))


