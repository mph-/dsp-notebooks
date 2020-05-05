# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, dtft_plot, spectrum_modes

def ma_lpf_dtft_plot(M=10, fs=100, fmax=50, mode='magnitude',
                     log_frequency=False):

    N = 100
    t = np.arange(N) / fs

    u = np.zeros(N)
    u[0] = 1

    b = np.ones(M) / M
    a = 1
    x = signal.lfilter(b=b, a=a, x=u)
    
    f = np.arange(200) / 200 * fmax
    w, X = signal.freqz(b, a, 2 * np.pi * f / fs)
    
    dtft_plot(f, X, mode=mode, log_frequency=log_frequency)

def ma_lpf_dtft_demo1():
    interact(ma_lpf_dtft_plot, M=(2, 100),
             fs=(10, 200, 10), fmax=(50, 200, 10),
             mode=spectrum_modes, continuous_update=False)
    
    

    




    

