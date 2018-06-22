# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot2

def interpolation_demo1_plot(N=100, cycles=25, Q=10, lollipop=False):

    fs = 100
    T = N / fs
    f0 = cycles / T
    
    t = np.arange(N) / fs
    x = np.cos(2 * np.pi * f0 * t)

    X = np.fft.rfft(x) / N
    Xz = np.concatenate((X, np.zeros(len(X) * (Q - 1))))
    xz = np.fft.irfft(Xz) * (Q * N)
    tz = np.arange(len(xz)) / (Q * fs)

    signal_plot2(t, x, tz, xz, lollipop=lollipop)

def interpolation_demo1():
    interact(interpolation_demo1_plot, N=(64, 512), cycles=(0, 64, 1),
             Q=(1, 20),
             continuous_update=False)
    
    

    




    

