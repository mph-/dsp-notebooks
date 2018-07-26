# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot
from .lib.utils import rect

def toneburst_plot(A=1, f0=2, T=1, discrete_time=False):

    fs = 800
    if discrete_time:
        fs = 20

    Td = 8
        
    N = int(fs * Td)

    t = np.arange(-N // 2, N // 2) / fs
    x = A * np.cos(2 * np.pi * f0 * t) * rect(t / T)

    signal_plot(t, x, lollipop=discrete_time)

def toneburst_demo1():
    interact(toneburst_plot, A=(0.5, 4, 0.5), f0=(0.5, 8, 0.5), T=(0.5, 8, 0.5),
             continuous_update=False)
    
    
