# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot

def exp_demo1_plot(A=1, alpha=2, discrete_time=False):

    if discrete_time:
        N = 50
        fs = 50
    else:
        N = 800
        fs = 800
        
    t = np.arange(-N // 2, N // 2) / fs
    x = A * np.exp(-alpha * t)

    signal_plot(t, x, lollipop=discrete_time)
    show()

def exp_demo1():
    interact(exp_demo1_plot, A=(1, 10), alpha=(1, 10), continuous_update=False)
    
    

    

