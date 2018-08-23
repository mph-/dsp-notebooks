# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_overplot2
from .lib.utils import rect

def iir_lpf_delay_demo1_plot(f0=2, alpha=0.5):

    A = 1
    T = 4
    fs = 100
    N = 550
    N0 = 50
    
    t = np.arange(-N0, N - N0) / fs
    t1 = t - T / 2
    x = A * np.cos(2 * np.pi * f0 * t) * rect(t1 / T)

    y = signal.lfilter(b=(1 - alpha, ), a=(1, -alpha), x=x)

    fig = signal_overplot2(t, x, t, y, ylim=(-1.3, 1.3), labels=('x', 'y'))


def iir_lpf_delay_demo1():
    interact(iir_lpf_delay_demo1_plot, f0=(0.5, 8, 0.25), 
             alpha=(0.0, 0.999, 0.01),             
             continuous_update=False)
    
    

    

