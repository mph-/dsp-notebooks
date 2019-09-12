# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def iir_lpf_impulse_plot(alpha=0.5, fs=100, lollipop=True):

    N = 100
    t = np.arange(N) / fs

    u = np.zeros(N)
    u[0] = 1

    b = (1 - alpha, )
    a = (1, -alpha)
    x = signal.lfilter(b=b, a=a, x=u)
    
    signal_plot(t, x, lollipop=lollipop)

def iir_lpf_impulse_demo1():
    interact(iir_lpf_impulse_plot, alpha=(0.0, 1.0, 0.01),
             fs=(10, 200, 10),
             continuous_update=False)
    
    

    




    

