# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes
from IPython.display import display, Math, Latex
from .lib.p1z1 import P1Z1

def polezero_p1z1_demo1_plot(p=-10, z=-5,
                             mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)        

    obj = P1Z1(p, z)
    t, h = obj.response(mode, t, w)
    if h is None:
        return Latex('Cannot compute Dirac delta for %s' % mode)    

    axes = polezero_plot_with_time(t, h, obj.poles, obj.zeros, mode=mode)
    axes[1].set_title(obj.title)


def polezero_p1z1_demo1():
    interact(polezero_p1z1_demo1_plot,
             p=(-30, 0), z=(-30, 0), 
             mode=response_modes, continuous_update=False)
