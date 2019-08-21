# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_hist
from .lib.utils import gauss

def noise_demo1_plot(sigma=1, mu=0, N=100, seed=1, lollipop=True):

    fs = 10
    np.random.seed(seed)
    
    t = np.arange(N) / fs
    x = np.random.standard_normal(N) * sigma + mu

    fig = signal_plot_with_hist(t, x, range=(-5, 5), lollipop=lollipop,
                                density=True, ylim2=(0, 0.6))

    vx = np.linspace(-5, 5, 201)    
    fX = gauss(vx, mu, sigma)
    
    fig.axes[1].plot(fX, vx)

def noise_demo1():
    interact(noise_demo1_plot, sigma=(1, 10), mu=(-10, 10),
             N=(50, 1000, 10), fs=(5, 100, 10),
             seed=(1, 100), continuous_update=False)
    
    

    

