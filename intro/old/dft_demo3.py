# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot, signal_plot_with_dft

def dft_demo3_plot(N=100, f0=2, fs=100, lollipop=True):

    t = np.arange(N) / fs
    x = np.cos(2 * np.pi * f0 * t)
    X = np.fft.rfft(x) / N

    f = np.arange(len(X)) / N * fs

    signal_plot_with_dft(t, x, f, X, lollipop=lollipop)

def dft_demo3():
    interact(dft_demo3_plot, N=(64, 512), f0=(1, 10, 0.1), fs=(10, 200, 10),
             continuous_update=False)
    
    

    




    

