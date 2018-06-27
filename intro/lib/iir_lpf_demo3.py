# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual
from .signal_plot import signal_plot
from .filter_plot import filter_plot

def iir_lpf_plot(f=4, alpha=0.5):

    A = 1
    N = 100
    fs = 100
    sigma = 0.5
    mu = 0
    n = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + n

    b = (1 - alpha,)
    a = (1, -alpha)
    
    filter_plot(b, a, fs)
    y = signal.lfilter(b=b, a=a, x=x)

    signal_plot(t, y, lollipop=lollipop)    

def iir_lpf_demo3():
    interact_manual(iir_lpf_plot, alpha=(0.0, 1.0, 0.01), manual_name='Update')
    
    

    

