# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot, signal_plot_with_dtft

def iir_lpf_dtft_plot(alpha=0.5, fs=100, fmax=50, lollipop=True):

    N = 100
    t = np.arange(N) / fs

    u = np.zeros(N)
    u[0] = 1

    b = (1 - alpha, )
    a = (1, -alpha)
    x = signal.lfilter(b=b, a=a, x=u)
    
    f = np.arange(200) / 200 * fmax
    w, X = signal.freqz(b, a, 2 * np.pi * f / fs)
    
    signal_plot_with_dtft(t, x, f, X, lollipop=lollipop)

def iir_lpf_dtft_demo1():
    interact(iir_lpf_dtft_plot, alpha=(0.0, 1.0, 0.01),
                    fs=(10, 200, 10), fmax=(10, 200, 10),
                    continuous_update=False)
    
    

    




    

