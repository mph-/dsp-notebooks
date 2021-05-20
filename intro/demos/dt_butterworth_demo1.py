# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.dt_butterworth import DTButterworth, btypes, response_modes
from IPython.display import display, Math, Latex

# Ignore band-pass and band-stop for now since these need two
# break frequencies.
btypes = ['Low-pass', 'High-pass']

def dt_butterworth_demo1_plot(order=1, btype=btypes[0], fb=20, fs=100,
                              mode=response_modes[0]):

    if fb == 0:
        fb = 0.01
    elif fb >= fs / 2:
        fb = fs / 2 - 0.01    
        
    dtfilter = DTButterworth(order=order, fb=fb, fs=fs, btype=btype)

    dtfilter.polezero_plot_with_response(50, mode=mode)

    if True:
        a = dtfilter.a
        b = dtfilter.b

        def fmt(a):
            return '[' + ', '.join(['%.3f' % a1 for a1 in a]) + ']'
        
        print('a = %s, b = %s' % (fmt(a), fmt(b)))

def dt_butterworth_demo1():
    interact(dt_butterworth_demo1_plot,
             order=(1, 10), btype=btypes, fb=(1, 100, 1),
             fs=(100, 500, 100),
             mode=response_modes, continuous_update=False)             
