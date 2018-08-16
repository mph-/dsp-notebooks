# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_dft
from .lib.utils import gauss

def noise_demo2_plot(sigma=1, mu=0, N=100, seed=1, lollipop=True):

    fs = 10
    np.random.seed(seed)
    
    t = np.arange(N) / fs
    x = np.random.standard_normal(N) * sigma + mu

    f = np.arange(-N // 2, N // 2) * fs / N
    
    X = np.fft.fft(x) / N
    
    fig = signal_plot_with_dft(t, x, f, X, lollipop=lollipop)

def noise_demo2():
    interact(noise_demo2_plot, sigma=(1, 10), mu=(-10, 10), N=(50, 1000, 10), fs=(5, 100, 10), seed=(1, 100), continuous_update=False)
    
    

    

