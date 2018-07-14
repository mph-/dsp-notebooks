# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def ma_lpf_demo2_plot(f=4, M=10, N=100, sigma=0.2, lollipop=True):

    A = 1
    fs = 100
    mu = 0
    np.random.seed(42)
    w = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + w

    h = np.ones(M) / M
    y = signal.lfilter(b=h, a=1, x=x)

    signal_plot(t, y, lollipop=lollipop)
    show()

def ma_lpf_demo2():
    interact(ma_lpf_demo2_plot, M=(1, 100, 1),
             N=(100, 1000, 100),
             sigma=(0.0, 2.0, 0.1),
             continuous_update=False)
