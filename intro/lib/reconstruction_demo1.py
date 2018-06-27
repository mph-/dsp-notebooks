# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot, signal_plot_with_interpolated
import scipy.signal as signal

def reconstruction_demo1_plot(fs=5, lollipop=True):

    f0 = 1
    cycles = 5
    T = cycles / f0

    N = int(fs * T)
    
    t = np.arange(N) / fs
    x = np.sin(2 * np.pi * f0 * t)

    Q = 20

    xz = signal.resample(x, N * Q)
    
    #X = np.fft.rfft(x) / N
    # Need to fix next line
    #Xz = np.concatenate((X, np.zeros(len(X) * (Q - 1))))
    #xz = np.fft.irfft(Xz) * (Q * N)
    tz = np.arange(len(xz)) / (Q * fs)
    
    signal_plot_with_interpolated(t, x, tz, xz, lollipop=lollipop, ylim=(-1.1, 1.1))

def reconstruction_demo1():
    interact(reconstruction_demo1_plot, fs=(0.2, 10, 0.2),
             continuous_update=False)
    
    

    

