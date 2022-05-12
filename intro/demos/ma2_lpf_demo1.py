# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_hist
from .lib.utils import gauss


def ma2_lpf_demo1_plot(N=100, sigma=0.2, seed=1, lollipop=True, filter=False):

    np.random.seed(seed)

    M = 2
    A = 1
    fs = 100
    mu = 0

    w = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A
    x = s + w

    h = np.ones(M) / M
    y = signal.lfilter(b=h, a=1, x=x)

    colour = 'orange'
    if not filter:
        y = x
        colour = 'blue'

    fig = signal_plot_with_hist(t, y, lollipop=lollipop, color=colour,
                                ylim=(0, 1.3))

    z = np.linspace(-5, 5, 401)
    fX = gauss(z, A + mu, sigma / np.sqrt(M))

    fig.axes[1].plot(fX, z)


def ma2_lpf_demo1():
    interact(ma2_lpf_demo1_plot, M=(1, 100, 1), N=(100, 1000, 100),
             sigma=(0.0, 0.5, 0.1),
             seed=(1, 100), continuous_update=False)
