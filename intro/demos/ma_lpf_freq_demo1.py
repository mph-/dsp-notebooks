# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def ma_lpf_freq_demo1_plot(f=0, M=4, lollipop=True, filter=False):

    N = 100
    A = 1
    fs = 100
    sigma = 0.2
    mu = 0
    np.random.seed(42)
    w = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + w    

    h = np.ones(M) / M
    y = signal.lfilter(b=h, a=1, x=x)

    colour = 'orange'
    if not filter:
        y = x
        colour = 'blue'            

    signal_plot(t, y, lollipop=lollipop, color=colour)


def ma_lpf_freq_demo1():
    interact(ma_lpf_freq_demo1_plot, M=(1, 100, 1),
             f=(0, 10, 0.25),             
             continuous_update=False)             
