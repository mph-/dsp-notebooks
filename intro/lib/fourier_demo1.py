# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot_with_dft, spectrum_modes
from .utils import rect, sinc

def rect_demo1_plot(T=1, mode='real-imag'):

    tmax = 5
    fmax = 5
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)    

    x = rect(t / T)
    X = T * sinc(f * T)
    
    signal_plot_with_dft(t, x, f, X, mode=mode)

def rect_demo1():
    interact(rect_demo1_plot, T=(0.1, 5, 0.1), mode=spectrum_modes,
             continuous_update=False)
    
def sinc_demo1_plot(T=1, mode='real-imag'):

    tmax = 5
    fmax = 5
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)    

    x = sinc(t / T)
    X = T * rect(f * T)
    
    signal_plot_with_dft(t, x, f, X, mode=mode)

def sinc_demo1():
    interact(sinc_demo1_plot, T=(0.1, 5, 0.1), mode=spectrum_modes,
             continuous_update=False)
    
    
    
    

