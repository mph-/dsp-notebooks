# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from scipy.signal import remez
from .lib.dt_generic import DTGeneric, response_modes
from IPython.display import display, Math, Latex


def parks_mcclellan_demo1_plot(order=20, cutoff=100, trans_width=20, fs=400,
                               mode=response_modes[2]):

    b = remez(order, [0, cutoff, cutoff + trans_width,
                      0.5 * fs], [1, 0], fs=fs)
    dtfilter = DTGeneric(b, [1], fs=fs)

    dtfilter.polezero_plot_with_response(50, mode=mode)

    if True:
        a = dtfilter.a
        b = dtfilter.b

        def fmt(a):
            return '[' + ', '.join(['%.3f' % a1 for a1 in a]) + ']'

        print('a = %s, b = %s' % (fmt(a), fmt(b)))


def parks_mcclellan_demo1():
    interact(parks_mcclellan_demo1_plot,
             order=(5, 100, 5), cutoff=(10, 200, 10),
             trans_width=(10, 100, 10),
             fs=(200, 500, 50),
             mode=response_modes, continuous_update=False)
