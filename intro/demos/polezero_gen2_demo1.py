# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos, sqrt
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes

kinds = ['Low-pass', 'Band-pass', 'High-pass', 'Band-stop']

class Lowpass2(object):

    def __init__(self, zeta, omega0):
        self.zeta = zeta
        self.omega0 = omega0

    def frequency_response(self, s):

        zeta, omega0 = self.zeta, self.omega0
        return omega0**2 / (s**2 + 2 * zeta * omega0 * s + omega0**2)

class Lowpass2UnderDamped(Lowpass2):

    def __init__(self, zeta, omega0):
        if zeta >= 1.0:
            raise ValueError('System not under damped')
        super (Lowpass2UnderDamped, self).__init__(zeta, omega0)
        
        p1a = -zeta * omega0 + 1j * omega0 * sqrt(1 - zeta**2)
        p1b = -zeta * omega0 - 1j * omega0 * sqrt(1 - zeta**2)
        self.poles = (p1a, p1b)
        self.zeros = ()

        self.alpha1 = zeta * omega0
        self.omega1 = omega0 * sqrt(1 - zeta**2)        
    
    def step_response(self, t):
        alpha1, omega1 = self.alpha1, self.omega1        
        return (1 - (alpha1 /omega1 * sin(omega1 * t) + cos(omega1 * t)) * exp(-alpha1 * t)) * (t >= 0)

    def impulse_response(self, t):
        alpha1, omega1 = self.alpha1, self.omega1
        return ((alpha1 ** 2 + omega1 ** 2) * exp(-alpha1 * t) * sin(omega1 * t) / omega1) * (t >= 0)                

class Lowpass2CriticallyDamped(Lowpass2):

    def __init__(self, zeta, omega0):
        if zeta != 1.0:
            raise ValueError('System not critically damped')
        super (Lowpass2CriticallyDamped, self).__init__(zeta, omega0)

        p1a = -omega0
        self.poles = (p1a, p1a)
        self.zeros = ()

        self.alpha1 = -p1a

    def step_response(self, t):
        alpha1 = self.alpha1
        return (-alpha1 * t * exp(-alpha1 * t) + 1 - exp(-alpha1 * t)) * (t >= 0)

    def impulse_response(self, t):
        alpha1 = self.alpha1        
        return alpha1**2 * t * exp(-alpha1 * t) * (t >= 0)
    
class Lowpass2OverDamped(Lowpass2):

    def __init__(self, zeta, omega0):
        if zeta <= 1.0:
            raise ValueError('System not over damped')
        super (Lowpass2UnderDamped, self).__init__(zeta, omega0)
        
        p1a = -zeta * omega0 + omega0 * sqrt(zeta**2 - 1)
        p1b = -zeta * omega0 - omega0 * sqrt(zeta**2 - 1)
        self.poles = (p1a, p1b)
        self.zeros = ()

        self.alpha1 = -p1a
        self.alpha2 = -p1b        
    
    def step_response(self, t):
        alpha1, alpha2 = self.alpha1, self.alpha2
        return (-alpha1 * exp(-alpha2 * t) / (alpha1 - alpha2) + alpha2 * exp(-alpha1 * t) / (alpha1 - alpha2) + 1) * (t >= 0)

    def impulse_response(self, t):
        alpha1, alpha2 = self.alpha1, self.alpha2        
        return (alpha1 * alpha2 * exp(-alpha2 * t) / (alpha1 - alpha2) - alpha1 * alpha2 * exp(-alpha1 * t) / (alpha1 - alpha2)) * (t >= 0)        


def lowpass2(zeta, omega0):
    if zeta > 1.0:
        return Lowpass2OverDamped(zeta, omega0)
    elif zeta < 1.0:
        return Lowpass2UnderDamped(zeta, omega0)
    else:
        return Lowpass2CriticallyDamped(zeta, omega0)


class Bandpass2(object):

    def __init__(self, zeta, omega0):
        self.zeta = zeta
        self.omega0 = omega0

    def frequency_response(self, s):

        zeta, omega0 = self.zeta, self.omega0
        return 2 * zeta * omega0 * s / (s**2 + 2 * zeta * omega0 * s + omega0**2)

class Bandpass2UnderDamped(Bandpass2):

    def __init__(self, zeta, omega0):
        if zeta >= 1.0:
            raise ValueError('System not under damped')
        super (Bandpass2UnderDamped, self).__init__(zeta, omega0)
        
        p1a = -zeta * omega0 + 1j * omega0 * sqrt(1 - zeta**2)
        p1b = -zeta * omega0 - 1j * omega0 * sqrt(1 - zeta**2)
        self.poles = (p1a, p1b)
        self.zeros = (0, )

        self.alpha1 = zeta * omega0
        self.omega1 = omega0 * sqrt(1 - zeta**2)        
    
    def step_response(self, t):
        alpha1, omega1 = self.alpha1, self.omega1
        return 2 * alpha1 * exp(-alpha1 * t) * sin(omega1 * t) * (t >= 0) / omega1

    def impulse_response(self, t):
        alpha1, omega1 = self.alpha1, self.omega1
        return -2 * alpha1 * (alpha1 * sin(omega1 * t) - omega1 * cos(omega1 * t)) * exp(-alpha1 * t) * (t >= 0) / omega1

    
class Bandpass2CriticallyDamped(Bandpass2):

    def __init__(self, zeta, omega0):
        if zeta != 1.0:
            raise ValueError('System not critically damped')
        super (Bandpass2CriticallyDamped, self).__init__(zeta, omega0)

        p1a = -omega0
        self.poles = (p1a, p1a)
        self.zeros = (0, )        

        self.alpha1 = -p1a

    def step_response(self, t):
        alpha1 = self.alpha1
        return 2 * alpha1 * t * exp(-alpha1 * t) * (t >= 0)                    

    def impulse_response(self, t):
        alpha1 = self.alpha1
        return  (-2 * alpha1**2 * t * exp(-alpha1 * t) + 2 * alpha1 * exp(-alpha1 * t)) * (t >= 0)            
    
class Bandpass2OverDamped(Bandpass2):

    def __init__(self, zeta, omega0):
        if zeta <= 1.0:
            raise ValueError('System not over damped')
        super (Bandpass2UnderDamped, self).__init__(zeta, omega0)
        
        p1a = -zeta * omega0 + omega0 * sqrt(zeta**2 - 1)
        p1b = -zeta * omega0 - omega0 * sqrt(zeta**2 - 1)
        self.poles = (p1a, p1b)
        self.zeros = (0, )                

        self.alpha1 = -p1a
        self.alpha2 = -p1b        
    
    def step_response(self, t):
        alpha1, alpha2 = self.alpha1, self.alpha2
        return ((alpha1 + alpha2) * exp(-alpha2 * t) / (alpha1 - alpha2) - (alpha1 + alpha2) * exp(-alpha1 * t) / (alpha1 - alpha2)) * (t >= 0)        

    def impulse_response(self, t):
        alpha1, alpha2 = self.alpha1, self.alpha2
        return ((alpha1**2 + alpha1 * alpha2) * exp(-alpha1 * t) / (alpha1 - alpha2) - (alpha1 * alpha2 + alpha2**2) * exp(-alpha2 * t) / (alpha1 - alpha2)) * (t >= 0)

    
def bandpass2(zeta, omega0):
    if zeta > 1.0:
        return Bandpass2OverDamped(zeta, omega0)
    elif zeta < 1.0:
        return Bandpass2UnderDamped(zeta, omega0)
    else:
        return Bandpass2CriticallyDamped(zeta, omega0)        
    

def polezero_gen2_demo1_plot(zeta=0.5, omega0=10, kind=kinds[0],
                             mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)    
    s = 1j * w

    if kind == 'Low-pass':
        obj = lowpass2(zeta, omega0)
    elif kind == 'Band-pass':
        obj = bandpass2(zeta, omega0)        
    elif kind == 'High-pass':
        obj = highpass2(zeta, omega0)        
    elif kind == 'Band-stop':
        obj = bandstop2(zeta, omega0)

    if mode == 'Step response':
        h = obj.step_response(t)
        ylim = (-0.5, 2.1)        
    elif mode == 'Impulse response':
        h = obj.impulse_response(t)
        if h is None:
            return Latex('Cannot compute Dirac delta')
        ylim = (-5, 10)                    
    elif mode == 'Frequency response':
        h = obj.frequency_response(s)
        ylim = (-40, 20)
        t = w
    else:
        raise ValueError('Unknown mode=%s', mode)        

    poles = np.array(obj.poles)
    zeros = np.array(obj.zeros)    

    axes = polezero_plot_with_time(t, h, poles, zeros, ylim=ylim, mode=mode)

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
