#!/usr/bin/env python3

import csv, json, sys, os
import numpy as np
from datetime import timedelta
from util import *

WIDTH, HEIGHT = 1600, 900

strata = [  ('epochal_geology', 1),
            ('generational_decay', 2),
            ('lifetime_climate', 4),
            ('seasonal_vegetation', 8),
            ('monthly_tides', 16),
            ('weekly_weather', 32),
            ('daily_energy', 64),
            ]

pitches = 'E', 'F#', 'A', 'B', 'D-'

master = drawing.Context(WIDTH*3, HEIGHT, hsv=True, margin=150)


for l, stratum in enumerate(strata):
    level, divisions = stratum
    signals = load('%s/%s.pkl' % (level, level))

    ctx = drawing.Context(WIDTH, HEIGHT, margin=50)
    ctx.label(-50 / ctx.width, -30 / ctx.height, "MIN", size=20)
    for i in range(divisions):
        x = i / divisions
        # if x == 0:
        #     x = 5 / ctx.width
        ctx.line(x, 0, x, 1, stroke=(0, 0, 0), thickness=0.5)
        if l == 5:
            master.line(x, 0, x, 1, stroke=(100, 100, 100), thickness=1)
            pass
    for i in range(10):
        x = i / 10
        ctx.label((-5 / ctx.width) + x, -30 / ctx.height, str(i), size=20)
    ctx.label((-5 / ctx.width) + 1, -30 / ctx.height, str(10), size=20)
    ctx.rect(-1 / ctx.width, .75, 350 / ctx.width, 200 / ctx.height, fill=(255, 255, 255), thickness=0)
    for s, signal in enumerate(signals):
        # ctx.plot(signal, stroke=colors[s], thickness=5.0)
        sat = int(l/len(strata) * 255)
        master.plot(signal, stroke=(150, 255, sat), thickness=5.0)
        pass
    p = 50
    ctx.label(20 / ctx.width, 1 - (p / ctx.height), level.replace('_', ' ').upper(), size=28)
    p += 30
    ctx.label(20 / ctx.width, 1 - (p / ctx.height), "REGISTER %s" % (l + 1), size=20)
    p += 30
    ctx.label(20 / ctx.width, 1 - (p / ctx.height), "PITCHES %s" % (','.join(pitches[:l + 1])), size=20)
    p += 30
    if l >= len(pitches) - 1:
        ctx.label(20 / ctx.width, 1 - (p / ctx.height), "CHANGE TO RANDOM PITCH AT LINE", size=16)
        p += 20
        ctx.label(20 / ctx.width, 1 - (p / ctx.height), "PLAY EACH PITCH BEFORE REPEATING", size=16)
        p += 30
    else:
        ctx.label(20 / ctx.width, 1 - (p / ctx.height), "CHANGE PITCH AT LINE", size=16)
        p += 30
    ctx.label(20 / ctx.width, 1 - (p / ctx.height), "DYNAMICS / TIMBRE FOLLOWS CURVE", size=16)
    # ctx.output('scores/%s.png' % level)
    # break

# master.label(.5, .5, "FRESHKILLS SCORE SET #1", size=20)
master.output('scores/master.png')
