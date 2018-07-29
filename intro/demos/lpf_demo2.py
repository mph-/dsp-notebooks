# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import spectrum_plot, spectrum_modes

def lpf_demo2_plot(fb=100, zeta=1, mode='magnitude dB', log_frequency=True):

    N = 501
    fmax = 1e3

    if log_frequency:
        f = np.logspace(np.log10(1), np.log10(fmax), N)
    else:
        f = np.linspace(0, fmax, N)
    s = f * 2j * np.pi

    alpha = 2 * np.pi * fb
    omega0 = 2 * np.pi * fb

    H = omega0**2 / (s**2 + 2 * zeta * omega0 * s + omega0**2)

    spectrum_plot(f, H, mode=mode, log_frequency=log_frequency)


def lpf_demo2():
    interact(lpf_demo2_plot, fb=(10, 400, 10), zeta=(0, 10, 0.1),
             mode=spectrum_modes, continuous_update=False)
    
    

    

