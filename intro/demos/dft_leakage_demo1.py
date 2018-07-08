# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_dft, spectrum_modes

def dft_leakage_demo1_plot(N=100, cycles=2.5, phase=0, mode='real-imag', lollipop=True):

    fs = 100
    T = N / fs
    f0 = cycles / T
    phi = np.radians(phase)

    t = np.arange(N) / fs
    x = np.cos(2 * np.pi * f0 * t + phi)
    X = np.fft.rfft(x, N) / N

    f = np.arange(len(X)) / N * fs
    
    signal_plot_with_dft(t, x, f, X, lollipop=lollipop, mode=mode)

def dft_leakage_demo1():
    interact(dft_leakage_demo1_plot, N=(64, 512), cycles=(1, 3, 0.1),
             phase=(-180, 180, 15),
             mode=spectrum_modes,
             continuous_update=False)
    
    

    




    

