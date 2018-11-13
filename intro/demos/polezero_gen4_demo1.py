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


def polezero_gen4_demo1_plot(zeta1=0.5, omega01=10, kind1=kinds[0],
                             zeta2=0.5, omega02=20, kind2=kinds[0],
                             mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    t2 = np.linspace(0, 3, 201)    
    w = np.logspace(-1, 3, 201)    
    s = 1j * w

    if kind1 == 'Low-pass':
        obj1 = Lowpass2(zeta1, omega01)
    elif kind1 == 'Band-pass':
        obj1 = Bandpass2(zeta1, omega01)        
    elif kind1 == 'High-pass':
        obj1 = Highpass2(zeta1, omega01)        
    elif kind1 == 'Band-stop':
        obj1 = Bandstop2(zeta1, omega01)

    if kind2 == 'Low-pass':
        obj2 = Lowpass2(zeta2, omega02)
    elif kind2 == 'Band-pass':
        obj2 = Bandpass2(zeta2, omega02)        
    elif kind2 == 'High-pass':
        obj2 = Highpass2(zeta2, omega02)        
    elif kind2 == 'Band-stop':
        obj2 = Bandstop2(zeta2, omega02)        

    if mode == 'Step response':
        h1 = obj1.step_response(t)
        h2 = obj2.step_response(t2)
        h = np.convolve(h1, h2)[0:len(t)] * (t[1] - t[0])
        ylim = (-0.5, 2.1)        
    elif mode == 'Impulse response':
        h1 = obj1.impulse_response(t)
        h2 = obj2.impulse_response(t2)        
        if h1 is None:
            return Latex('Cannot compute Dirac delta for %s' % mode)
        if h2 is None:
            return Latex('Cannot compute Dirac delta for %s' % mode)
        h = np.convolve(h1, h2)[0:len(t)] * (t[1] - t[0])
        ylim = (-5, 10)                    
    elif mode == 'Frequency response':
        H1 = obj1.frequency_response(s)
        H2 = obj2.frequency_response(s)
        h = H1 * H2
        ylim = (-40, 20)
        t = w
    else:
        raise ValueError('Unknown mode=%s', mode)        

    poles = np.array(obj1.poles + obj2.poles)
    zeros = np.array(obj1.zeros + obj2.zeros)    

    axes = polezero_plot_with_time(t, h, poles, zeros, ylim=ylim, mode=mode)

def polezero_gen4_demo1():
    interact(polezero_gen4_demo1_plot,
             zeta1=(0.1, 10), omega01=(0, 20), kind1=kinds,
             zeta2=(0.1, 10), omega02=(0, 20), kind2=kinds,
             mode=response_modes, continuous_update=False)             
