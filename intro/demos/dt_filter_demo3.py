# M. P. Hayes UCECE
from numpy import fromstring
from ipywidgets import interact, interactive, fixed, interact
from .lib.dt_generic import DTGeneric, response_modes
from IPython.display import display, Math, Latex


def dt_filter_demo3_plot(a='1', b='0.5, 0.5',
                         mode=response_modes[2]):

    fs = 100
    a0 = 1.0

    a = fromstring(a, sep=',')
    b = fromstring(b, sep=',')

    dtfilter = DTGeneric(b, a, fs=fs)

    dtfilter.polezero_plot_with_response(50, mode=mode)

    if True:
        a = dtfilter.a
        b = dtfilter.b

        def fmt(a):
            return '[' + ', '.join(['%.3f' % a1 for a1 in a]) + ']'

        print('a = %s, b = %s' % (fmt(a), fmt(b)))


def dt_filter_demo3():
    interact(dt_filter_demo3_plot,
             mode=response_modes, continuous_update=False)
