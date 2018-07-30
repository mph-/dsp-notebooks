# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import spectrum_plot, spectrum_modes, signal_plot

def lpf_demo2_plot(fb=100, zeta=1, mode='magnitude dB', log_frequency=True,
                   impulse_response=False):

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

    if impulse_response:
        t = np.linspace(-0.01, 0.1, N)
        sigma1 = omega0 * zeta
        if zeta == 1.0:
            h = omega0**2 * t * np.exp(-sigma1 * t) * (t >= 0)      
        elif zeta < 1.0:
            omega1 = omega0 * np.sqrt(1 - zeta**2)
            h = (omega0**2 / omega1) * np.exp(-sigma1 * t) * np.sin(omega1 * t) * (t >= 0)
        else:
            s1 = -omega0 * (zeta + np.sqrt(zeta**2 - 1))
            s2 = -omega0 * (zeta - np.sqrt(zeta**2 - 1))
            k1 = omega0**2 / (s1 - s2)
            k2 = -k1
            h = (k1 * np.exp(s1 * t) + k2 * np.exp(s2 * t)) * (t >= 0)
            
        signal_plot(t, h, color='orange')
    

def lpf_demo2():
    interact(lpf_demo2_plot, fb=(10, 400, 10), zeta=(0, 10, 0.1),
             mode=spectrum_modes, continuous_update=False)
    
    

    

