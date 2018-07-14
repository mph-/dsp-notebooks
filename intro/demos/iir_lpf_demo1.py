# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def iir_lpf_plot(f=4, alpha=0.5, lollipop=True):

    A = 1
    N = 100
    fs = 100
    sigma = 0.2
    mu = 0
    np.random.seed(42)
    w = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + w

    y = signal.lfilter(b=(1 - alpha, ), a=(1, -alpha), x=x)

    signal_plot(t, y, lollipop=lollipop)
    show()

def iir_lpf_demo1():
    interact(iir_lpf_plot, alpha=(0.0, 0.999, 0.01), continuous_update=False)
    
    

    

