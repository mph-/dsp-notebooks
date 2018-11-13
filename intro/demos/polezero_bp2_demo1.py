# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes
from .lib.bandpass2 import Bandpass2

def polezero_bp2_demo1_plot(zeta=0.5, omega0=10, mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)    
    s = 1j * w

    obj = Bandpass2(zeta, omega0)

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
    eps = 0.01
    if zeta > (1 + eps):
        s = 'Over damped'
    elif zeta < (1 - eps):
        s = 'Under damped'
    else:
        s = 'Critically damped'
        
    axes[1].set_title('%s  $\zeta$=%.2f  $\omega_0$=%.1f' % (s, zeta, omega0))

def polezero_bp2_demo1():
    interact(polezero_bp2_demo1_plot,
             zeta=(0.1, 10), omega0=(0, 20),
             mode=response_modes, continuous_update=False)             
