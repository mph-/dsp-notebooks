# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes
from .lib.lowpass2 import Lowpass2
from .lib.highpass2 import Highpass2
from .lib.bandpass2 import Bandpass2
from .lib.bandstop2 import Bandstop2
from IPython.display import display, Math, Latex

kinds = ['Low-pass', 'Band-pass', 'High-pass', 'Band-stop']


def polezero_gen2_demo1_plot(zeta=0.5, omega0=10, kind=kinds[0],
                             mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)    

    if kind == 'Low-pass':
        obj = Lowpass2(zeta, omega0)
    elif kind == 'Band-pass':
        obj = Bandpass2(zeta, omega0)        
    elif kind == 'High-pass':
        obj = Highpass2(zeta, omega0)        
    elif kind == 'Band-stop':
        obj = Bandstop2(zeta, omega0)
    else:
        raise ValueError('Unknown kind %s' % kind)

    t, h = obj.response(mode, t, w)
    if h is None:
        return Latex('Cannot compute Dirac delta for %s' % mode)    

    axes = polezero_plot_with_time(t, h, obj.poles, obj.zeros, mode=mode)    

    eps = 0.01
    if zeta > (1 + eps):
        s = 'Over damped'
    elif zeta < (1 - eps):
        s = 'Under damped'
    else:
        s = 'Critically damped'
        
    axes[1].set_title('%s  $\zeta$=%.2f  $\omega_0$=%.1f' % (s, zeta, omega0))

def polezero_gen2_demo1():
    interact(polezero_gen2_demo1_plot,
             zeta=(0.1, 10), omega0=(0, 20), kind=kinds,
             mode=response_modes, continuous_update=False)             
