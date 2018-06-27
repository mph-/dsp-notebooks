# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual
from .signal_plot import signal_plot

def dc_demo1_plot(A=1, lollipop=True):

    fs = 50
    N = 50
    t = np.arange(N) / fs

    x = np.ones(N) * A
    signal_plot(t, x, lollipop=lollipop, ylim=(0, 1.1))

def dc_demo1():
    interact(dc_demo1_plot, A=(-5, 5), continuous_update=False)
    

def impulse_demo1_plot(A=1, lollipop=True):

    fs = 50
    N = 50
    t = np.arange(N) / fs

    x = np.zeros(N)
    x[0] = A
    signal_plot(t, x, lollipop=lollipop, ylim=(0, 1.1))

def impulse_demo1():
    interact(impulse_demo1_plot, A=(-5, 5), continuous_update=False)
    
    

    

