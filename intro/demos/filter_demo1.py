# M. P. Hayes UCECE
from numpy import linspace, pi, exp, sin, cos
from numpy.random import randn
from scipy.signal import lfilter
from ipywidgets import interact
from .lib.signal_plot import signal_plot


def notch_filter(x, fc, alpha=0.9):
    """Second order IIR notch filter centred on fc"""

    if alpha >= 1.0:
        raise ValueError('Require alpha < 1 for stability')

    omega0 = 2 * pi * fc
    beta = cos(omega0)

    K = 0.5 * (1 + alpha)

    b = (K, -2 * K * beta, K)
    a = (1, -2 * K * beta, alpha)

    return lfilter(b, a, x)


def filter_demo1_plot(interference=True, noise=False,
                      filter_interference=False, filter_noise=False):

    t0 = 0.2
    t = linspace(-1, 1, 301)
    x = (t > t0) * exp(-(t - t0) * 10) * sin(2 * pi * 10 * (t - t0))

    dt = t[1] - t[0]

    if interference:
        x += cos(2 * pi * 50 * t) * 2

    if noise:
        x += randn(len(t)) * 0.1

    if filter_interference:
        x = notch_filter(x, 50 * dt, 0.8)

    if filter_noise:
        x = lfilter([1] * 8, [1], x)

    m = t >= 0

    signal_plot(t[m], x[m], lollipop=False)


def filter_demo1():
    interact(filter_demo1_plot, continuous_update=False)
