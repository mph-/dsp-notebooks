# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes


def polezero_demo1_plot(alpha=5, mode=response_modes[0]):

    t = np.linspace(0, 3, 201)
    f = np.logspace(-1, 3, 201)        
    s = 2j * np.pi * f

    p1 = -alpha

    if mode == 'Step response':
        h = 1 - exp(p1 * t)
        ylim = (-0.5, 2.1)
    elif mode == 'Impulse response':
        h = -p1 * exp(p1 * t)
        ylim = (-5, 10)
    else:
        H = -p1 / (s - p1)
        h = H
        t = f
        ylim = (-40, 20)
        
    poles = np.array((p1, ))

    axes = polezero_plot_with_time(t, h, poles, ylim=ylim, mode=mode)           


def polezero_demo1():
    interact(polezero_demo1_plot,
             alpha=(-2, 20),
             mode=response_modes, continuous_update=False)
