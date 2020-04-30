# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, create_axes
from .lib.flickernoise import FlickerNoise

def flickernoise_plot(alpha=3, B=100, N=1000, seed=42, ASD=True,
                      lollipop=False):
                      
    np.random.seed(seed)

    fs = 2 * B
    
    noise = FlickerNoise(N, fs, beta=0.5, alpha=alpha * 1e-8, N0=1e-40)

    M = 4
    t = np.arange(N) / fs
    x = noise.realisation()

    if ASD:
        f = np.arange(N // 2) / (N * fs)
        m = f != 0
        X = f * 0
        X[m] = alpha * 1e-8 * f[m]**-0.5

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

def flickernoise_demo1():
    interact(flickernoise_plot, alpha=(0.0, 5),
             B=(100, 1000, 100), N=(100, 1000, 100),                    
             continuous_update=False)
    
    

    

