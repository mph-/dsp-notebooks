# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def bsf_response_demo1_plot(f0=100, zeta=1, f=50):

    N = 501
    t = np.linspace(0, 0.1, N)

    s = f * 2j * np.pi

    omega0 = 2 * np.pi * f0

    H = (s**2 + omega0**2) / (s**2 + 2 * zeta * omega0 * s + omega0**2)    

    x = np.cos(2 * np.pi * f * t)
    y = abs(H) * np.cos(2 * np.pi * f * t + np.angle(H))

    fig = signal_plot(t, x)
    axes = fig.axes[0]
    axes.plot(t, y)

def bsf_response_demo1():
    interact(bsf_response_demo1_plot,  f0=(10, 400, 10), zeta=(0.05, 10, 0.05),
             f=(10, 400, 10),
             continuous_update=False)
    
    

    

