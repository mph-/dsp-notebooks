# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def ma_lpf_step_demo1_plot(M=4, lollipop=True, filter=True):

    A = 1
    fs = 100

    n = np.arange(-20, 80)
    t = n / fs

    x = A * (n >= 0) * (n <= 50)

    h = np.ones(M) / M
    y = signal.lfilter(b=h, a=1, x=x)

    colour = 'orange'
    if not filter:
        y = x
        colour = 'blue'            

    signal_plot(t, y, lollipop=lollipop, color=colour)


def ma_lpf_step_demo1():
    interact(ma_lpf_step_demo1_plot, M=(1, 100, 1),
             continuous_update=False)             
    
    

    

