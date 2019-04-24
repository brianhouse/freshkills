import pytz, calendar, pickle
import numpy as np
from dateutil import parser
from . import drawing
from .colors import colors

def as_numeric(s):
    if type(s) == int or type(s) == float or type(s) == bool:
        return s
    try:
        s = int(s)
    except (ValueError, TypeError):
        try:
            s = float(s)
        except (ValueError, TypeError):
            pass
    return s

def normalize(signal, minimum=None, maximum=None):
    signal = np.array(signal).astype('float')
    if minimum is None:
        minimum = np.min(signal)
    if maximum is None:
        maximum = np.max(signal)
    signal -= minimum
    maximum -= minimum
    signal /= maximum
    signal = np.clip(signal, 0.0, 1.0)
    return signal    

def resample(ts, values, num_samples=None):
    assert np.all(np.diff(ts) >= 0)
    if num_samples == None:
        num_samples = math.ceil((ts[-1] - ts[0]) / guess_period(ts))
    ts = normalize(ts)
    return np.interp(np.linspace(0.0, 1.0, num_samples), ts, values)

def smooth(signal, size=10, window='blackman'):
    types = ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']
    signal = np.array(signal)
    if size < 3:
        return signal
    s = np.r_[2 * signal[0] - signal[size:1:-1], signal, 2 * signal[-1] - signal[-1:-size:-1]]
    if window == 'flat': # running average
        w = np.ones(size,'d')
    else:
        w = getattr(np, window)(size) # get a series of weights that matches the window and is the correct size 
    y = np.convolve(w / w.sum(), s, mode='same') # convolve the signals
    return y[size - 1:-size + 1]

def string_to_dt(string, tz='America/New_York'):
    date = parser.parse(string)
    tz = pytz.timezone(tz)
    if date.tzinfo is None:
        date = tz.localize(date)
    else:
        date = date.astimezone(tz)
    return date

def dt_to_t(dt):
    tz = pytz.timezone('America/New_York')
    dt = dt.astimezone(tz)
    t = calendar.timegm(dt.timetuple())
    return int(t)

def save(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)    