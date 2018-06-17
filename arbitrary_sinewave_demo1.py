from __future__ import print_function
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from signal_plot import signal_plot

def arbitrary_sinewave_plot(A=1, f=2, phi=0, N=50, fs=50):
    t = np.arange(N) / fs
    x = A * np.sin(2 * np.pi * f * t + np.radians(phi))

    signal_plot(t, x, both=True)    

def arbitrary_sinewave_demo1():
    interact(arbitrary_sinewave_plot, A=(1, 10), f=(1, 10), phi=(-180, 180, 10), N=(10, 100, 10), fs=(5, 100, 10), continuous_update=False)
    
    

    

