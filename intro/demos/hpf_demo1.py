# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import spectrum_plot, spectrum_modes, signal_plot

def hpf_demo1_plot(fb=100, mode='magnitude dB', log_frequency=True,
                   impulse_response=False):

    N = 501
    fmax = 1e3

    if log_frequency:
        f = np.logspace(np.log10(1), np.log10(fmax), N)
    else:
        f = np.linspace(0, fmax, N)
    s = f * 2j * np.pi

    alpha = 2 * np.pi * fb

    H = s / (s + alpha)

    spectrum_plot(f, H, mode=mode, log_frequency=log_frequency)

    if impulse_response:
        t = np.linspace(-0.01, 0.1, N)
        h = (1 - np.exp(-alpha * t)) * (t >= 0)
        signal_plot(t, h, color='orange')    


def hpf_demo1():
    interact(hpf_demo1_plot, fb=(10, 400, 10),
             mode=spectrum_modes, continuous_update=False)
    
    

    

