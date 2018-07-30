# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import spectrum_plot, spectrum_modes, signal_plot


def butterworth(f, K, omega_0, order=2):

    omega = 2 * np.pi * f
    s = 1j * omega

    H = K
    for k in range(1, order + 1):
        sk = omega_0 * np.exp(1j * (2 * k + order - 1) * np.pi / (2 * order))
        H *= omega_0 / (s - sk)

    return H

def butterworth_demo1_plot(fb=100, order=2, mode='magnitude dB', log_frequency=True):

    N = 501
    fmax = 1e3

    if log_frequency:
        f = np.logspace(np.log10(1), np.log10(fmax), N)
    else:
        f = np.linspace(0, fmax, N)
    s = f * 2j * np.pi

    H = butterworth(f, 1, 2 * np.pi * fb, order)

    fig = spectrum_plot(f, H, mode=mode, log_frequency=log_frequency)
    if 'magnitude dB' in mode:
        axes = fig.axes
        axes[0].set_ylim(-100, 0)

def butterworth_demo1():
    interact(butterworth_demo1_plot, fb=(10, 400, 10),
             order=(1, 10, 1),
             mode=spectrum_modes, continuous_update=False)
    
    

    

