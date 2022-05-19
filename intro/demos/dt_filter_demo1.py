# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.dt_generic import DTGeneric, response_modes
from IPython.display import display, Math, Latex


def dt_filter_demo1_plot(a0=1.0, a1=0.0, b0=1.0, b1=0.0, fs=100,
                         mode=response_modes[0]):

    a = (a0, a1)
    b = (b0, b1)
    dtfilter = DTGeneric(a, b, fs=fs)

    dtfilter.polezero_plot_with_response(50, mode=mode)

    if True:
        a = dtfilter.a
        b = dtfilter.b

        def fmt(a):
            return '[' + ', '.join(['%.3f' % a1 for a1 in a]) + ']'

        print('a = %s, b = %s' % (fmt(a), fmt(b)))


def dt_filter_demo1():
    interact(dt_filter_demo1_plot,
             fs=(100, 500, 100),
             mode=response_modes, continuous_update=False)
