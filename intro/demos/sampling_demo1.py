# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, signal_plot_with_interpolated
import scipy.signal as signal

def sampling_demo1_plot(fs=5, lollipop=True, reconstruct=False):

    f0 = 1
    cycles = 2
    T = cycles / f0

    N = int(fs * T)
    
    t = np.arange(N) / fs
    x = np.sin(2 * np.pi * f0 * t)

    fs1 = fs * 100
    N1 = int(fs1 * T)
    t1 = np.arange(N1) / fs1
    x1 = np.sin(2 * np.pi * f0 * t1)

    fig = signal_plot_with_interpolated(t, x, t1, x1,
                                        lollipop=True, ylim=(-1.1, 1.1))
    fig.axes[0].set_xlim(t1[0], t1[-1])
    print(t[-1], t1[-1])
    
    if reconstruct:
        Q = 20
        xz = signal.resample(x, N * Q)
        tz = np.arange(len(xz)) / (Q * fs)
        fig.axes[0].plot(tz, xz, zorder=1, color='green')
        #fig.axes[0].set_xlim(tz[0], tz[-1])
        

def sampling_demo1():
    interact(sampling_demo1_plot, fs=(0.2, 10, 0.2),
             continuous_update=False)
    
    

    

