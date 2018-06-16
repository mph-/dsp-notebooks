from __future__ import print_function
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual
from signal_plot import signal_plot

def ma_lpf_plot(M=10, N=100, sigma=0.2):

    A = 1
    fs = 100
    mu = 0
    np.random.seed(42)
    n = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A
    x = s + n

    h = np.ones(M) / M
    y = signal.lfilter(b=h, a=1, x=x)

    signal_plot(t, y, both=True)    

def ma_lpf_demo1():
    interact_manual(ma_lpf_plot, M=(1, 100, 1), N=(100, 1000, 100),
                    sigma=(0.0, 2.0, 0.1),
                    manual_name='Update')
    
    

    

