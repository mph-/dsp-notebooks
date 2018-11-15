# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes
from .lib.p3z1 import P3Z1

def polezero_p3z1_demo1_plot(alpha1=5, omega1=10, alpha2=20, beta1=10,
                             mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)

    obj = P3Z1(alpha1, omega1, alpha2, beta1)
    t, h = obj.response(mode, t, w)
    if h is None:
        return Latex('Cannot compute Dirac delta for %s' % mode)    

    axes = polezero_plot_with_time(t, h, obj.poles, obj.zeros, mode=mode)    

def polezero_p3z1_demo1():
    interact(polezero_p3z1_demo1_plot,
             alpha1=(-2, 20), omega1=(1, 20), alpha2=(-2, 40),
             beta1=(1, 40), mode=response_modes,
             continuous_update=False)

