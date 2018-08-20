# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_hist

def iir_lpf_demo1_plot(f=0, N=100, alpha=0.9, lollipop=True, filter=True):

    A = 1
    fs = 100
    sigma = 0.2
    mu = 0
    np.random.seed(42)
    w = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + w

    y = signal.lfilter(b=(1 - alpha, ), a=(1, -alpha), x=x)

    colour = 'orange'
    if not filter:
        y = x
        colour = 'blue'        

    signal_plot_with_hist(t, y, lollipop=lollipop, ylim=(-1.1, 1.1),
                          color=colour)

def iir_lpf_demo1():
    interact(iir_lpf_demo1_plot,
             f=(0, 10, 1),
             N=(100, 1000, 100),             
             alpha=(0.0, 0.999, 0.01),
             continuous_update=False)
    
    

    

