# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes
from IPython.display import display, Math, Latex

def polezero_ll1_demo1_plot(alpha=5, beta=10, mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)        
    s = 1j * w

    if mode == 'Step response':
        h = (alpha + beta * exp(alpha * t) - beta) * exp(-alpha * t) * (t >= 0) / beta

        ylim = (-0.5, 2.1)
    elif mode == 'Impulse response':
        return Latex('Cannot draw Dirac delta')
        #h = alpha * (-(alpha - beta) * (t >= 0) + exp(alpha * t) * DiracDelta(t)) * exp(-alpha * t) / beta
        ylim = (-5, 10)
    else:
        H = alpha * (s + beta) / (beta * (s + alpha))
        h = H
        t = w
        ylim = (-40, 20)
        
    poles = np.array((-alpha, ))
    zeros = np.array((-beta, ))

    axes = polezero_plot_with_time(t, h, poles, zeros, ylim=ylim, mode=mode)           


def polezero_ll1_demo1():
    interact(polezero_ll1_demo1_plot,
             alpha=(-2, 20), beta=(1, 20),
             mode=response_modes, continuous_update=False)
