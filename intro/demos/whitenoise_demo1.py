# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def whitenoise_plot(T=300, R=1e3, N=1000, B=100, seed=42, lollipop=True):

    np.random.seed(42)

    k = 1.38e-23

    sigma = np.sqrt(4 * k * T * R * B)

    fs = 2 * B
    t = np.arange(N) / fs
    x = np.random.standard_normal(N) * sigma

    if ASD:
        f = np.arange(N // 2) / (N * fs)
        m = f != 0
        X = f * 0
        X[m] = 4 * k * T * R

        axes, tmp = create_axes(2)
        
        axes[0].loglog(f[m], X[m])
        axes[0].set_ylabel('Voltage ASD (V/rtHz)')
        axes[0].set_xlabel('Frequency (Hz)')

        ax = axes[1]
        signal_plot(t, x * 1e6, lollipop=lollipop, axes=ax)

        
    else:
        fig = signal_plot(t, x * 1e6, lollipop=lollipop)
        ax = fig.axes[0]

    ax.set_ylim(-1, 1)
    ax.set_ylabel('Voltage (uV)')        

def whitenoise_demo1():
    interact(whitenoise_plot, T=(0, 300, 10),
             R=(0, 10e3, 100),
             B=(100, 1000, 100), N=(100, 1000, 100),                    
             continuous_update=False)
    
    

    

