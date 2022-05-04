# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact
from .lib.signal_plot import signal_plot_with_dft
from .lib.utils import rect, sinc


def fourier_linearity_demo1_plot(a=1.0, b=0.0):

    mode = 'real-imag'

    tmax = 4
    fmax = 4
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)

    x = rect(t)
    y = sinc(t)

    z = a * x + b * y

    X = sinc(f)
    Y = rect(f)

    Z = a * X + b * Y

    fig = signal_plot_with_dft(t, z, f, Z, mode=mode)
    axes = fig.axes
    axes[0].set_ylim(-2, 2)
    axes[1].set_ylim(-2, 2)


def fourier_linearity_demo1():
    interact(fourier_linearity_demo1_plot, a=(0, 1.0, 0.1),
             b=(0, 1.0, 0.1),
             continuous_update=False)
