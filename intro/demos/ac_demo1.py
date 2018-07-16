# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot

def ac_demo1_plot(A=1, f=2, phi=0, discrete_time=False):

    if discrete_time:
        N = 50
        fs = 50
    else:
        N = 800
        fs = 800
        
    t = np.arange(-N // 2, N // 2) / fs
    x = A * np.cos(2 * np.pi * f * t + np.radians(phi))

    signal_plot(t, x, lollipop=discrete_time)
    show()

def ac_demo1():
    interact(ac_demo1_plot, A=(1, 10), f=(1, 10), phi=(-180, 180, 10), continuous_update=False)
    
    

    

