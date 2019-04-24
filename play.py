#!/usr/bin/env python3

import time
from braid import *
from util import *

class Row:

    def __init__(self):
        self.notes = [1, 2, 4, 5, 7]
        self.i = 0

    def draw(self, t):
        if self.i == len(self.notes):
            self.i = 0
            shuffle(self.notes)
        n = self.notes[self.i]
        self.i += 1
        return n

midi.verbose = True

n = Row().draw

data = load('data.pkl')
signals = []
for signal in data:
    signals.append(timeseries(signal))
    # plot(signals[-1])
# show_plots()

rate(1)  # hz

# total_cycles = 60 * 10  # 10 mins
total_cycles = 60 * 1  # 1 mins

Stratum = make({'volume': 42})

momentary = Stratum(1)
momentary.rate = rate() / 1
momentary.chord = E6, MYX
momentary.pattern = [n]
momentary.velocity = 0.2
momentary.volume = 0
momentary.volume = tween(127, total_cycles, signals[0], saw=True)
momentary.phase = 0
momentary.phase = tween(1.0, 4, osc=True)

diurnal = Stratum(2)
diurnal.rate = rate() / 4
diurnal.chord = E5, MYX
diurnal.pattern = [n]
diurnal.velocity = 0.5
diurnal.volume = 0.0
diurnal.volume = tween(1.0, total_cycles / 4, signals[1], saw=True)
diurnal.phase = 1/7

weekly = Stratum(3)
weekly.rate = rate() / 30
weekly.chord = E4, MYX
weekly.pattern = [n]
weekly.velocity = 0.6
weekly.volume = 0.0
weekly.volume = tween(1.0, total_cycles / 30, signals[2], saw=True)
weekly.phase = 2/7

seasonal = Stratum(4)
seasonal.rate = rate() / 60
seasonal.chord = E3, MYX
seasonal.pattern = [n]
seasonal.velocity = 0.7
seasonal.volume = 0.0
seasonal.volume = tween(1.0, total_cycles / 60, signals[3], saw=True)
seasonal.phase = 3/7

lifetime = Stratum(5)
lifetime.rate = rate() / 180
lifetime.chord = E2, MYX
lifetime.pattern = [n]
lifetime.velocity = 0.8
lifetime.volume = 0.0
lifetime.volume = tween(1.0, total_cycles / 180, signals[4], saw=True)
lifetime.phase = 4/7

generational = Stratum(6)
generational.rate = rate() / 300
generational.chord = E1, MYX
generational.pattern = [n]
generational.velocity = 0.9
generational.volume = 0.0
generational.volume = tween(1.0, total_cycles / 300, signals[5], saw=True)
generational.phase = 5/7

epochal = Stratum(7)
epochal.rate = rate() / 600
epochal.chord = E0, MYX
epochal.pattern = [1]
epochal.velocity = 1.0
epochal.volume = 0.0
epochal.volume = tween(1.0, total_cycles / 600, signals[6], saw=True)
epochal.phase = 6/7


play()