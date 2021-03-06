# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, signal_plot_with_fourier_series

def synthesis_plot(f0=2, B1=10, B2=5, B3=1, N=100, fs=100, lollipop=True):

    t = np.arange(N) / fs
    omega0 = 2 * np.pi * f0
    
    x = B1 * np.sin(omega0 * t) + B2 * np.sin(2 * omega0 * t) + B3 * np.sin(3 * omega0 * t)


    X = np.array((0, B1, B2, B3)) * 1j

    signal_plot_with_fourier_series(t, x, np.arange(len(X)), X, lollipop=lollipop)                 

def synthesis_demo1():
    interact(synthesis_plot, f0=(1, 10), B1=(-5, 5), B2=(-5, 5), B3=(-5, 5), continuous_update=False)
    
    

    

