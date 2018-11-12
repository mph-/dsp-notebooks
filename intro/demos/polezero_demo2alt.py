# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos, sqrt
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes


def polezero_demo2alt_plot(zeta=0.5, omega0=10, mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    f = np.logspace(-1, 3, 201)    
    s = 2j * np.pi * f

    if zeta > 1:
        # Over damped
        p1a = -zeta * omega0 + omega0 * sqrt(zeta**2 - 1)
        p1b = -zeta * omega0 - omega0 * sqrt(zeta**2 - 1)
        alpha1 = -p1a
        alpha2 = -p1b

        if mode == 'Step response':
            h = (-alpha1 * exp(-alpha2 * t) / (alpha1 - alpha2) + alpha2 * exp(-alpha1 * t) / (alpha1 - alpha2) + 1) * (t >= 0)
        elif mode == 'Impulse response':
            h = (alpha1 * alpha2 * exp(-alpha2 * t) / (alpha1 - alpha2) - alpha1 * alpha2 * exp(-alpha1 * t) / (alpha1 - alpha2)) * (t >= 0)
        
    elif zeta < 1:
        # Under damped
        p1a = -zeta * omega0 + 1j * omega0 * sqrt(1 - zeta**2)
        p1b = -zeta * omega0 - 1j * omega0 * sqrt(1 - zeta**2)

        alpha1 = zeta * omega0
        omega1 = omega0 * sqrt(1 - zeta**2)
        
        if mode == 'Step response':
            h = (1 - (alpha1 /omega1 * sin(omega1 * t) + cos(omega1 * t)) * exp(-alpha1 * t)) * (t >= 0)
        elif mode == 'Impulse response':
            h = ((alpha1 ** 2 + omega1 ** 2) * exp(-alpha1 * t) * sin(omega1 * t) / omega1) * (t >= 0)
        
    else:
        # Critically damped
        p1a = -omega0
        p1b = -omega0
        if mode == 'Step response':
            h = (-omega0 * t * exp(-omega0 * t) + 1 - exp(-omega0 * t)) * (t >= 0)
            ylim = (-0.5, 2.1)            
        elif mode == 'Impulse response':
            h = omega0**2 * t * exp(-omega0 * t) * (t >= 0)
            ylim = (-5, 10)            

    if mode == 'Step response':    
        ylim = (-0.5, 2.1)
    elif mode == 'Impulse response':
        ylim = (-5, 10)            
    else:
        H = p1a * p1b / ((s - p1a) * (s - p1b))
        h = H
        t = f
        ylim = (-40, 20)                            

    poles = np.array((p1a, p1b))

    axes = polezero_plot_with_time(t, h, poles, ylim=ylim, mode=mode)       

    eps = 0.01
    if zeta > (1 + eps):
        s = 'Over damped'
    elif zeta < (1 - eps):
        s = 'Under damped'
    else:
        s = 'Critically damped'
        
    axes[1].set_title('%s  $\zeta$=%.2f  $\omega_0$=%.1f' % (s, zeta, omega0))

def polezero_demo2alt():
    interact(polezero_demo2alt_plot,
             zeta=(0.1, 10), omega0=(0, 20),
             mode=response_modes, continuous_update=False)             
