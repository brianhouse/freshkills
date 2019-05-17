#!/usr/bin/env python3

import csv, json, sys, os
import numpy as np
from datetime import timedelta
from util import *

strata = ['seasonal_vegetation', 'monthly_tides', 'weekly_weather', 'daily_traffic', 'generational_decay']

master = drawing.Context(1200, 500)


for l, level in enumerate(strata):
    signals = load('%s/%s.pkl' % (level, level))

    ctx = drawing.Context(1200, 500)
    for s, signal in enumerate(signals):
        ctx.plot(signal, stroke=colors[s], thickness=2.0)
        master.plot(signal, stroke=colors[l], thickness=2.0)
    ctx.output('scores/%s.png' % level)

master.output('scores/master.png')