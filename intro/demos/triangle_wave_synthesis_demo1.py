# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot, signal_plot_with_fourier_series

def triangle_wave_synthesis_plot(K=10, f0=2, fs=100, N=100, lollipop=False):

    t = np.arange(N) / fs
    omega0 = 2 * np.pi * f0

    A = np.zeros(K)
    
    x = np.zeros(N)
    for k in range(0, K):
        if k % 2 == 0:
            continue
        m = k // 2
        
        A[k] = 8 * ((-1.0) ** m) / np.pi**2 / k ** 2  
        x += A[k] * np.sin(k * omega0 * t)
    signal_plot_with_fourier_series(t, x, np.arange(len(A)), A, lollipop=lollipop)

def triangle_wave_synthesis_demo1():
    interact(triangle_wave_synthesis_plot,  K=(1, 100), f0=(1, 10),
                    fs=(100, 1000, 100), N=(100, 1000, 100),
                    continuous_update=False)
    
    

    

