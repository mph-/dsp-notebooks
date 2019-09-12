# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def ma_lpf_impulse_plot(M=10, fs=100, lollipop=True):

    N = 100
    t = np.arange(N) / fs

    u = np.zeros(N)
    u[0] = 1

    b = np.ones(M) / M
    a = 1
    x = signal.lfilter(b=b, a=a, x=u)
    
    signal_plot(t, x, lollipop=lollipop)

def ma_lpf_impulse_demo1():
    interact(ma_lpf_impulse_plot, M=(10, 100),
             fs=(10, 200, 10),
             continuous_update=False)
    
    

    




    

