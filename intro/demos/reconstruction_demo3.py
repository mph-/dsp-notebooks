# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, signal_plot_with_interpolated
import scipy.signal as signal
from .lib.utils import rect, tri, triangle_wave

def reconstruction_demo3_plot(fs=5, lollipop=True):

    f0 = 1
    cycles = 5
    T = cycles / f0

    N = int(fs * T)
    
    t = np.arange(N) / fs
    x = triangle_wave(f0 * t)

    Q = 20

    xz = signal.resample(x, N * Q)
    
    #X = np.fft.rfft(x) / N
    # Need to fix next line
    #Xz = np.concatenate((X, np.zeros(len(X) * (Q - 1))))
    #xz = np.fft.irfft(Xz) * (Q * N)
    tz = np.arange(len(xz)) / (Q * fs)
    
    signal_plot_with_interpolated(t, x, tz, xz, lollipop=lollipop, ylim=(-1.1, 1.1))

def reconstruction_demo3():
    interact(reconstruction_demo3_plot, fs=(0.2, 10, 0.2),
             continuous_update=False)
    
    

    

