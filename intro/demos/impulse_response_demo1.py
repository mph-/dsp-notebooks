# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots
from scipy.signal import butter, lfilter
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import create_axes
from .lib.signal import Signal, signals

def impulse_response_demo1_plot(h='exp(-t) u(t)', alpha=0.04):

    x = 'u(t)'

    N = 500
    tmax = 4
    t1 = np.linspace(-1, tmax, N)    

    dt = t1[1] - t1[0]    
    offset = int(-t1[0] / dt)
    
    x1 = Signal(x)(t1)

    fb = alpha / (2 * dt)

    dt = t1[1] - t1[0]
    b, a = butter(1, 2 * fb * dt, 'lowpass')
    x = np.zeros(N)
    x[offset] = 1
    x1 = lfilter(b, a, x)
    
    h1 = Signal(h)(t1)

    y1 = np.convolve(x1, h1)[offset:offset + len(t1)] * dt

    fig, axes = subplots(2, 2, figsize=(8, 4))

    scale = max(h1) / max(y1)
    y1 *= scale
    x1 *= scale

    X1 = np.fft.rfft(x1)
    Y1 = np.fft.rfft(y1)
    H1 = np.fft.rfft(h1)    
    
    axes[0, 0].plot(t1, x1)
    axes[0, 0].set_xlabel('Time')    
    axes[1, 0].plot(t1, y1)
    axes[1, 0].plot(t1, h1)
    axes[1, 0].set_xlabel('Time')        

    axes[0, 1].plot(abs(X1))
    axes[0, 1].set_xlabel('Frequency')
    axes[1, 1].plot(abs(Y1))
    axes[1, 1].plot(abs(H1))
    axes[1, 1].set_xlabel('Frequency')    

    for ax in axes.flat:
        ax.set_xticklabels([])
        
def impulse_response_demo1():
    interact(impulse_response_demo1_plot, h=signals,
             alpha=(0.02, 0.5, 0.02),
             continuous_update=False)
    
