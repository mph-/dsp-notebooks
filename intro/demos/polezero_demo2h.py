# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes


def polezero_demo2h_plot(alpha1=5, omega1=10, mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    w = np.logspace(-1, 3, 201)    
    s = 1j * w

    p1a = -alpha1 - 1j * omega1
    p1b = -alpha1 + 1j * omega1

    if mode == 'Step response':
        if omega1 == 0:
            h = 2 * alpha1 * exp(-alpha1 * t) * (t >= 0)
        else:
            h = 2 * alpha1 * exp(-alpha1 * t) * sin(omega1 * t) * (t >= 0) / omega1
        ylim = (-0.5, 1.1)
    elif mode == 'Impulse response':        
        if omega1 == 0:
            h = -2 * alpha1 * (alpha1 - 1) * exp(-alpha1 * t) * (t >= 0)
        else:
            h = -2 * alpha1 * (alpha1 * sin(omega1 * t) - omega1 * cos(omega1 * t)) * exp(-alpha1 * t) * (t >= 0)

        ylim = (-50, 100)
    else:
        H = s**2 / ((s - p1a) * (s - p1b))
        h = H
        t = w
        ylim = (-40, 20)                    

    poles = np.array((p1a, p1b))

    axes = polezero_plot_with_time(t, h, poles, ylim=ylim, mode=mode)       

    omega0 = np.sqrt(alpha1**2 + omega1**2)    
    if omega0 != 0:
        zeta = alpha1 / omega0
        eps = 1e-2
        if zeta > (1 + eps):
            s = 'Over damped'
        elif zeta < (1 - eps):
            s = 'Under damped'
        else:
            s = 'Critically damped'

        axes[1].set_title('%s  $\zeta$=%.2f  $\omega_0$=%.1f' % (s, zeta, omega0))

def polezero_demo2h():
    interact(polezero_demo2h_plot,
             alpha1=(-2, 20), omega1=(0, 20),
             mode=response_modes, continuous_update=False)             
