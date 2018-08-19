# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_hist
from .lib.utils import gauss

def ma_lpf_demo1_plot(M=10, N=100, sigma=0.2, lollipop=True):

    A = 1
    fs = 100
    mu = 0
    np.random.seed(42)
    w = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A
    x = s + w

    h = np.ones(M) / M
    y = signal.lfilter(b=h, a=1, x=x)

    fig = signal_plot_with_hist(t, y, lollipop=lollipop)

    z = np.linspace(-5, 5, 401)
    fX = gauss(z, A + mu, sigma / np.sqrt(M))
    
    fig.axes[1].plot(fX, z)    
    signal_plot_with_hist(t, y, lollipop=lollipop, ylim=(-1.1, 1.1))


def ma_lpf_demo1():
    interact(ma_lpf_demo1_plot, M=(1, 100, 1), N=(100, 1000, 100),
             sigma=(0.0, 2.0, 0.1),
             continuous_update=False)
    
    

    

