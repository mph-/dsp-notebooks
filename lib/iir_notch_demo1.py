from __future__ import print_function
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import Audio
from .filter_plot import filter_plot
from .signal_plot import signal_plot

def iir_notch_play(fnotch=50, alpha=0.5, bode=True):

    N = 40000
    fs = 20e3

    t = np.arange(N) / fs
    hum = 0.5 * np.cos(2 * np.pi * 50 * t)
    s = 0.2 * np.cos(2 * np.pi * 220 * t)
    x = hum + s

    omega0 = 2 * np.pi * fnotch / fs
    beta = np.cos(omega0)
    
    K = 0.5 * (1 + alpha)
    
    b = (K, -2 * K * beta, K)
    a = (1, -2 * K * beta, alpha)

    f = np.logspace(0, 4, 200)
    
    filter_plot(b, a, fs, f=f, bode=bode)
    
    y = signal.lfilter(b=b, a=a, x=x)

    signal_plot(t[0:2000:10], y[0:2000:10])
    
    return Audio(y, rate=fs)

def iir_notch_demo1():
    interact(iir_notch_play, fnotch=(30, 70, 1), alpha=(0.0, 0.999, 0.01),
             continuous_update=False)
    
    

    

