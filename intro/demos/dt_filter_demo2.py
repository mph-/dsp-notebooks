# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.dt_generic import DTGeneric, response_modes
from IPython.display import display, Math, Latex


def dt_filter_demo2_plot(a1=0.0, a2=0.0, b0=1.0, b1=0.0, b2=0.0,
                         mode=response_modes[2]):

    fs = 100
    a0 = 1.0
    a = (a0, a1, a2)
    b = (b0, b1, b2)
    dtfilter = DTGeneric(b, a, fs=fs)

    dtfilter.polezero_plot_with_response(50, mode=mode)

    if True:
        a = dtfilter.a
        b = dtfilter.b

        def fmt(a):
            return '[' + ', '.join(['%.3f' % a1 for a1 in a]) + ']'

        print('a = %s, b = %s' % (fmt(a), fmt(b)))


def dt_filter_demo2():
    interact(dt_filter_demo2_plot,
             a1=(-1.1, 1.1, 0.1),
             a2=(-1.1, 1.1, 0.1),
             b0=(-1.1, 1.1, 0.1),
             b1=(-1.1, 1.1, 0.1),
             b2=(-1.1, 1.1, 0.1),
             mode=response_modes, continuous_update=False)
