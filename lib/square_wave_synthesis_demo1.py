from __future__ import print_function
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot

def square_wave_synthesis_plot(M=10, f0=2, fs=100, N=100, lollipop=False):

    t = np.arange(N) / fs
    omega0 = 2 * np.pi * f0

    x = np.zeros(N)
    for m in range(0, M):
        k = (2 * m) + 1
        
        x += np.sin(k * omega0 * t) / k
    signal_plot(t, x, lollipop=lollipop)

def square_wave_synthesis_demo1():
    interact(square_wave_synthesis_plot,  M=(1, 100), f0=(1, 10),
                    fs=(100, 1000, 100), N=(100, 1000, 100),
                    continuous_update=False)
    
    

    

