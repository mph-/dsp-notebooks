# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, signal_plot_with_interpolated
import scipy.signal as signal

def reconstruction_demo2_plot(M=5, lollipop=True, cpt1=True, cpt2=True):

    f0 = 1
    cycles = 5
    T = cycles / f0

    fs = f0 * M
    N = int(fs * T)
    
    t = np.arange(N) / fs
    x = np.zeros(N)
    if cpt1:
        x += 0.5 * np.sin(2 * np.pi * f0 * t)
    if cpt2:
        x += 0.5 * np.sin(2 * np.pi * 3 * f0 * t)

    Q = 20

    xz = signal.resample(x, N * Q)
    tz = np.arange(len(xz)) / (Q * fs)
    
    signal_plot_with_interpolated(t, x, tz, xz, lollipop=lollipop, ylim=(-1.1, 1.1))

def reconstruction_demo2():
    interact(reconstruction_demo2_plot, M=(0.2, 10, 0.2),
             continuous_update=False)
    
    

    

