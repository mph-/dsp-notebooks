# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot_with_hist

def noise_plot(sigma=1, mu=0, N=1000, fs=50, lollipop=True):

    t = np.arange(N) / fs
    x = np.random.standard_normal(N) * sigma + mu

    signal_plot_with_hist(t, x, range=(-5, 5), lollipop=lollipop)

def noise_demo1():
    interact(noise_plot, sigma=(1, 10), mu=(-10, 10), N=(10, 1000, 10), fs=(5, 100, 10), continuous_update=False)
    
    

    

