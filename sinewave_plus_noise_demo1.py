from __future__ import print_function
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual
from signal_plot import signal_plot

def sinewave_plus_noise_plot(A=1, sigma=0.2, f=4, N=100, fs=100):

    mu = 0
    np.random.seed(42)
    n = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + n

    signal_plot(t, x, both=True)    

def sinewave_plus_noise_demo1():
    interact_manual(sinewave_plus_noise_plot, A=(1.0, 10.0), sigma=(0.0, 2.0),
                    fs=(100, 1000, 100), N=(100, 1000, 100),                    
                    manual_name='Update')
    
    

    

