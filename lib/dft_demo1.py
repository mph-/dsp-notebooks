# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot_with_dft

def dft_demo1_plot(N=100, cycles=2, lollipop=True):

    fs = 100
    T = N / fs
    f0 = cycles / T
    
    t = np.arange(N) / fs
    x = np.cos(2 * np.pi * f0 * t)
    X = np.fft.rfft(x) / N

    f = np.arange(len(X)) / N * fs

    signal_plot_with_dft(t, x, f, X, lollipop=lollipop)

def dft_demo1():
    interact(dft_demo1_plot, N=(64, 512), cycles=(0, 50, 1),
             continuous_update=False)
    
    

    




    

