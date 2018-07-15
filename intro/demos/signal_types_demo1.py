# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot

def signal_types_plot(discrete_time=False, discrete_value=False):

    fs = 800
    if discrete_time:
        fs = 50
    f = 2
    T = 1
    N = int(fs * T)

    t = np.arange(N) / fs
    x = 4 * np.sin(2 * np.pi * f * t)

    if discrete_value:
        x = np.round(x)

    signal_plot(t, x, lollipop=discrete_time)

def signal_types_demo1():
    interact(signal_types_plot, continuous_update=False)
    
    

    

