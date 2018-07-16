# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual
from .lib.signal_plot import signal_plot

def dc_demo1_plot(A=1, discrete_time=False):

    fs = 50
    N = 50
    t = np.arange(-N //2, N // 2) / fs

    x = np.ones(N) * A
    signal_plot(t, x, lollipop=discrete_time, ylim=(-5.1, 5.1))

def dc_demo1():
    interact(dc_demo1_plot, A=(-5, 5), continuous_update=False)
