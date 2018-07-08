# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, signal_plot_with_interpolated
import scipy.signal as signal

waveforms = [r'\(\sin(2\pi t)\)', r'\(\sin(6\pi t)\)', r'\(\sin(2\pi t) + \sin(3\pi t)\)']

def reconstruction_demo3_plot(fs=5, lollipop=True, waveform=waveforms[-1]):

    f0 = 1
    cycles = 5
    T = cycles / f0

    N = int(fs * T)
    
    t = np.arange(N) / fs
    x = np.zeros(N)
    if '1 Hz' in waveform:
        x += np.sin(2 * np.pi * f0 * t)
    if '3 Hz' in waveform:
        x += np.sin(2 * np.pi * 3 * f0 * t)

    Q = 20

    xz = signal.resample(x, N * Q)
    tz = np.arange(len(xz)) / (Q * fs)
    
    signal_plot_with_interpolated(t, x, tz, xz, lollipop=lollipop, ylim=(-2.1, 2.1))

def reconstruction_demo3():
    interact(reconstruction_demo3_plot, M=(0.2, 10, 0.2), waveform=waveforms,
             continuous_update=False)
    
    

    

