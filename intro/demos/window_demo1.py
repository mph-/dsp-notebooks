# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot


# fixed does not generate a widget
def window_plot(N=100, window='hamming', lollipop=False):

    fs = 100
    t = np.arange(N) / fs

    x = signal.get_window(window, N)
    
    signal_plot(t, x, lollipop=lollipop)    

def window_demo1():
    interact(window_plot, N=(20, 200, 20),
             window=['rect', 'hamming', 'blackman'], continuous_update=False)
    
    

    

