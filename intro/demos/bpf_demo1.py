# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import spectrum_plot, spectrum_modes

def bpf_demo1_plot(f0=100, zeta=1, mode='magnitude dB', log_frequency=True):

    N = 501
    fmax = 1e3

    if log_frequency:
        f = np.logspace(np.log10(1), np.log10(fmax), N)
    else:
        f = np.linspace(0, fmax, N)
    s = f * 2j * np.pi

    alpha = 2 * np.pi * f0
    omega0 = 2 * np.pi * f0

    H = (2 * zeta * omega0 * s) / (s**2 + 2 * zeta * omega0 * s + omega0**2)

    spectrum_plot(f, H, mode=mode, log_frequency=log_frequency)


def bpf_demo1():
    interact(bpf_demo1_plot, f0=(10, 400, 10), zeta=(0.05, 10, 0.05),
             mode=spectrum_modes, continuous_update=False)
    
    

    

