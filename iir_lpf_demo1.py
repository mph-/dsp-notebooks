from __future__ import print_function
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual
from signal_plot import signal_plot

def iir_lpf_filter_plot(f=4, alpha=0.5):

    A = 1
    N = 100
    fs = 100
    sigma = 0.2
    mu = 0
    np.random.seed(42)
    n = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + n

    y = signal.lfilter(b=(1 - alpha, ), a=(1, -alpha), x=x)

    signal_plot(t, y, both=True)    

def iir_lpf_filter_demo1():
    interact_manual(iir_lpf_filter_plot, alpha=(0.0, 1.0, 0.01), manual_name='Update')
    
    

    

