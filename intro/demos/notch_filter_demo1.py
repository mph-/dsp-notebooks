# M. P. Hayes UCECE
import numpy as np
from scipy.signal import butter, lfilter, freqz
from scipy.io import wavfile
from matplotlib.pyplot import figure
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_dtft, spectrum_modes, signal_plot
from .lib.utils import rect

def notch_filter(t, x, fn, alpha):

    dt = t[1] - t[0]
    omegan = 2 * np.pi * fn * dt
    beta = np.cos(omegan)
    
    K = 0.5 * (1 + alpha)
    
    b = (K, -2 * K * beta, K)
    a = (1, -2 * K * beta, alpha)
    
    return lfilter(b, a, x), b, a


def notch_filter_demo1_plot(f0=200, fn=50, alpha=0.8, enable=True):

    fs = 2000
    N = 400
    t = np.arange(N) / fs

    T = 100 / fs
    t1 = t - 300 / fs
    x = np.cos(2 * np.pi * f0 * t1) * rect(t1 / T)
    i = 5 * np.cos(2 * np.pi * 50 * t)
    x = x + i

    y, b, a = notch_filter(t, x, fn, alpha)

    f = np.arange(0, N // 2 + 1) / N * fs
    w, H = freqz(b, a, 2 * np.pi * f / fs)
    
    if enable:
        fig = signal_plot_with_dtft(t, y, f, H, mode='magnitude')
    else:
        fig = signal_plot_with_dtft(t, x, f, H, mode='magnitude')        
        
    axes = fig.axes
    axes[0].set_ylim(-6, 6)
    
    #Y = np.fft.rfft(np.fft.fftshift(y))
    #X = np.fft.rfft(np.fft.fftshift(x))        
    
    #axes[1].plot(f, abs(X))      
    #axes[1].plot(f, abs(Y))

    
def notch_filter_demo1():
    interact(notch_filter_demo1_plot, continuous_update=False,
             f0=(50, 500, 10), fn=(20,100,1), alpha=(0.5,0.99,0.01))
