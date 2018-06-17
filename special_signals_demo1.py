from __future__ import print_function
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual
from signal_plot import signal_plot

def dc_plot(A=1):

    fs = 50
    N = 50
    t = np.arange(N) / fs

    x = np.ones(N) * A
    signal_plot(t, x, both=True)    

def dc_demo1():
    interact(dc_plot, A=(-5, 5), continuous_update=False)
    
    

    

