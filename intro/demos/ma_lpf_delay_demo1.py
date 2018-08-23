# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_overplot2
from .lib.utils import rect

def ma_lpf_delay_demo1_plot(f0=2, M=10):

    A = 1
    T = 4
    fs = 100
    N = 550
    N0 = 50
    
    t = np.arange(-N0, N - N0) / fs
    t1 = t - T / 2
    x = A * np.cos(2 * np.pi * f0 * t) * rect(t1 / T)

    h = np.ones(M) / M
    y = signal.lfilter(b=h, a=1, x=x)

    fig = signal_overplot2(t, x, t, y, ylim=(-1.3, 1.3), labels=('x', 'y'))


def ma_lpf_delay_demo1():
    interact(ma_lpf_delay_demo1_plot, M=(1, 100, 1),
             fs=(10,200, 10),  f0=(0.5, 8, 0.5), T=(0.5, 8, 0.5),             
             continuous_update=False)
    
    

    

