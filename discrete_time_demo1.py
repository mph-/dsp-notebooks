from __future__ import print_function
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from signal_plot import signal_plot

def discrete_time_plot(fs=50):

    f = 2
    T = 1
    N = int(fs * T)

    t = np.arange(N) / fs
    x = np.sin(2 * np.pi * f * t)

    signal_plot(t, x, both=True)    

def discrete_time_demo1():
    interact(discrete_time_plot, fs=(5, 100, 10), continuous_update=False)
    
    

    

