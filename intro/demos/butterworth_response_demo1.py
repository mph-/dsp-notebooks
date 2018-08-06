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

def butterworth_response_demo1_plot(fb=100, order=2, f=40):

    N = 501
    t = np.linspace(0, 0.1, N)

    s = f * 2j * np.pi

    H = butterworth(f, 1, 2 * np.pi * fb, order)

    x = np.cos(2 * np.pi * f * t)
    y = abs(H) * np.cos(2 * np.pi * f * t + np.angle(H))

    fig = signal_plot(t, x)
    axes = fig.axes[0]
    axes.plot(t, y)

def butterworth_response_demo1():
    interact(butterworth_response_demo1_plot, fb=(10, 400, 10),
             order=(1, 10, 1),  f=(10, 400, 10),
             continuous_update=False)
    
    

    

