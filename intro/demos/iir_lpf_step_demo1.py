# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def iir_lpf_step_demo1_plot(alpha=0.9, lollipop=True, filter=True):

    A = 1
    fs = 100

    n = np.arange(-20, 80)
    t = n / fs

    x = A * (n >= 0) * (n <= 50)

    y = signal.lfilter(b=(1 - alpha, ), a=(1, -alpha), x=x)
    
    colour = 'orange'
    if not filter:
        y = x
        colour = 'blue'        

    signal_plot(t, y, lollipop=lollipop, ylim=(-1.1, 1.1), color=colour)

def iir_lpf_step_demo1():
    interact(iir_lpf_step_demo1_plot,
             alpha=(0.0, 0.999, 0.01),
             continuous_update=False)
    
    

    

