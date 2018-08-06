# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def hpf_response_demo1_plot(fb=100, f=50):

    N = 501
    t = np.linspace(0, 0.1, N)

    s = f * 2j * np.pi

    alpha = 2 * np.pi * fb

    H = s / (s + alpha)

    x = np.cos(2 * np.pi * f * t)
    y = abs(H) * np.cos(2 * np.pi * f * t + np.angle(H))

    fig = signal_plot(t, x)
    axes = fig.axes[0]
    axes.plot(t, y)

def hpf_response_demo1():
    interact(hpf_response_demo1_plot, fb=(10, 400, 10),
             f=(10, 400, 10),
             continuous_update=False)
    
    

    

