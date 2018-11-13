# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes
from .lib.lowpass1 import Lowpass1

def polezero_lp1_demo1_plot(alpha=5, mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)        
    s = 1j * w

    obj = Lowpass1(alpha)

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
    

def polezero_lp1_demo1():
    interact(polezero_lp1_demo1_plot,
             alpha=(-2, 20),
             mode=response_modes, continuous_update=False)
