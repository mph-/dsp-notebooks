# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, signal_plot_with_interpolated
import scipy.signal as signal

def reconstruction_demo1_plot(fs=5, interpolator='linear', original=True):

    f0 = 1
    cycles = 5
    T = cycles / f0

    N = int(fs * T)
    
    t = np.arange(N) / fs
    x = np.sin(2 * np.pi * f0 * t)

    if interpolator == 'linear':
        Q = 1
    elif interpolator == 'sinc':
        # Not really sinc; oversampled with linear.
        Q = 20
    else:
        raise ValueError('Unhandled interpolator ' + interpolator)

    xz = signal.resample(x, N * Q)
    
    tz = np.arange(len(xz)) / (Q * fs)
    
    fig = signal_plot_with_interpolated(t, x, tz, xz,
                                        lollipop=True, ylim=(-1.1, 1.1))

    P = 1000
    fs = P / T
    t = np.arange(P) / fs
    x = np.sin(2 * np.pi * f0 * t)

    t = np.arange(P) / P * N
    if original:
        fig.axes[0].plot(t, x, zorder=1, color='green')
    fig.axes[0].set_xlim(t[0], t[-1])
        

def reconstruction_demo1():
    interact(reconstruction_demo1_plot, fs=(0.2, 10, 0.2),
             interpolator=['linear', 'sinc'],
             continuous_update=False)
    
    

    

