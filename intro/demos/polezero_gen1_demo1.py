# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes
from .lib.lowpass1 import Lowpass1
from .lib.highpass1 import Highpass1
from IPython.display import display, Math, Latex

kinds = ['Low-pass', 'High-pass']


def polezero_gen1_demo1_plot(alpha=1, kind=kinds[0],
                             mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)    
    s = 1j * w

    if kind == 'Low-pass':
        obj = Lowpass1(alpha)
    elif kind == 'High-pass':
        obj = Highpass1(alpha)        
    else:
        raise ValueError('Unknown kind %s' % kind)

    if mode == 'Step response':
        h = obj.step_response(t)
        ylim = (-0.5, 2.1)        
    elif mode == 'Impulse response':
        h = obj.impulse_response(t)
        if h is None:
            return Latex('Cannot compute Dirac delta for %s' % mode)
        ylim = (-5, 10)                    
    elif mode == 'Frequency response':
        h = obj.frequency_response(s)
        ylim = (-40, 20)
        t = w
    else:
        raise ValueError('Unknown mode=%s', mode)        

    axes = polezero_plot_with_time(t, h, obj.poles, obj.zeros,
                                   ylim=ylim, mode=mode)

def polezero_gen1_demo1():
    interact(polezero_gen1_demo1_plot,
             alpha=(0, 20), kind=kinds,
             mode=response_modes, continuous_update=False)             
