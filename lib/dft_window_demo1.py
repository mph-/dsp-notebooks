# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot_with_dft

def dft_window_demo1_plot(N=100, P=2, window='hamming', cycles=2,
                           phase=0, lollipop=True):

    fs = 100
    T = N / fs
    f0 = cycles / T
    phi = np.radians(phase)

    w = signal.get_window(window, N)
    
    t = np.arange(N) / fs
    x = np.cos(2 * np.pi * f0 * t + phi) * w
    xz = np.concatenate((x, np.zeros((P - 1) * N)))

    tz = np.arange(N * P) / fs
    
    Xz = np.fft.rfft(xz) / N

    f = np.arange(len(Xz)) / N * fs

    signal_plot_with_dft(tz, xz, f, Xz, lollipop=lollipop)

def dft_window_demo1():
    interact(dft_window_demo1_plot, P=(1, 8),
             window=['rect', 'hamming', 'blackman'],
             N=(64, 512), cycles=(1, 3, 0.1),
             phase=(-180, 180, 15), continuous_update=False)
    
    

    




    

