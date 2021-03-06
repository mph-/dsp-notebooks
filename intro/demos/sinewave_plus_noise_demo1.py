# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def sinewave_plus_noise_plot(A=1, sigma=0.2, f=4, N=100, fs=100, lollipop=True):

    mu = 0
    np.random.seed(42)
    n = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + n

    signal_plot(t, x, lollipop=lollipop)    

def sinewave_plus_noise_demo1():
    interact(sinewave_plus_noise_plot, A=(1.0, 10.0), sigma=(0.0, 2.0),
                    fs=(100, 1000, 100), N=(100, 1000, 100),                    
                    continuous_update=False)
    
    

    

