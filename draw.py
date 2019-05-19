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

master = drawing.Context(WIDTH, HEIGHT)


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
    for i in range(10):
        x = i / 10
        ctx.label((-5 / ctx.width) + x, -30 / ctx.height, str(i), size=20)
    ctx.label((-5 / ctx.width) + 1, -30 / ctx.height, str(10), size=20)   
    ctx.rect(-1 / ctx.width, .75, 350 / ctx.width, 200 / ctx.height, fill=(255, 255, 255), thickness=0)     
    for s, signal in enumerate(signals):
        ctx.plot(signal, stroke=colors[s], thickness=5.0)
        # master.plot(signal, stroke=colors[l], thickness=5.0)
    p = 50
    ctx.label(20 / ctx.width, 1 - (p / ctx.height), level.replace('_', ' ').upper(), size=28)
    p += 30
    ctx.label(20 / ctx.width, 1 - (p / ctx.height), "REGISTER %s" % (l + 1), size=20)
    p += 30
    ctx.label(20 / ctx.width, 1 - (p / ctx.height), "PITCHES %s" % (','.join(pitches[:l + 1])), size=20)
    p += 30
    if l >= len(pitches) - 1:
        ctx.label(20 / ctx.width, 1 - (p / ctx.height), "AT LINE, PLAY RANDOM PITCH", size=16)        
        p += 20
        ctx.label(20 / ctx.width, 1 - (p / ctx.height), "PLAY EACH PITCH BEFORE REPEATING", size=16)                
        p += 30
    else:
        ctx.label(20 / ctx.width, 1 - (p / ctx.height), "AT LINE, PLAY PITCH", size=16)        
        p += 30        
    ctx.label(20 / ctx.width, 1 - (p / ctx.height), "DYNAMICS / TIMBRE FOLLOWS CURVE", size=16)                        
    ctx.output('scores/%s.png' % level)
    # break

# master.output('scores/master.png')