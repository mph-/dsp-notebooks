from __future__ import print_function
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from signal_plot import signal_plot_with_hist

def noise_plot(sigma=1, mu=0, N=1000, fs=50):

    t = np.arange(N) / fs
    x = np.random.standard_normal(N) * sigma + mu

    signal_plot_with_hist(t, x, discrete=True, range=(-5, 5))    

def noise_demo1():
    interact(noise_plot, sigma=(1, 10), mu=(-10, 10), N=(10, 1000, 10), fs=(5, 100, 10), continuous_update=False)
    
    

    

