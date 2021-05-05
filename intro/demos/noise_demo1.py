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

    # Could scale by sigma but do not see change.
    ymin = -10
    ymax = 10

    fig = signal_plot_with_hist(t, x, range=(ymin, ymax), lollipop=lollipop,
                                density=True, ylim2=(0, 0.6), ylim=(ymin, ymax))

    vx = np.linspace(ymin, ymax, 201)    
    fX = gauss(vx, mu, sigma)
    
    fig.axes[1].plot(fX, vx)

def noise_demo1():
    interact(noise_demo1_plot, sigma=(1, 5), mu=(-5, 5),
             N=(50, 1000, 10), fs=(5, 100, 10),
             seed=(1, 100), continuous_update=False)
    
    

    

