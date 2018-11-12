# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time, response_modes


def polezero_demo2c_plot(alpha1=5, omega1=10, beta1=10, mode=response_modes[0]):

    t = np.linspace(-0.1, 3, 201)
    f = np.logspace(-1, 3, 201)    
    s = 2j * np.pi * f

    p1a = -alpha1 - 1j * omega1
    p1b = -alpha1 + 1j * omega1

    if mode == 'Step response':
        h = (alpha1**2 * sin(omega1 * t) - alpha1 * beta1 * sin(omega1 * t) + beta1 * omega1 * exp(alpha1 * t) - beta1 * omega1 * cos(omega1 * t) + omega1**2 * sin(omega1 * t)) * exp(-alpha1 * t) * (t >= 0) / (omega1 * beta1)
        ylim = (-0.5, 2.1)
    elif mode == 'Impulse response':        
        h = (omega1 * (alpha1**2 + omega1**2) * cos(omega1 * t) + (-alpha1**3 + alpha1**2 * beta1 - alpha1 * omega1**2 + beta1 * omega1**2) * sin(omega1 * t)) * exp(-alpha1 * t) * (t >= 0) / (omega1 * beta1)
        ylim = (-5, 10)
    else:
        H = p1a * p1b * (s + beta1) / ((s - p1a) * (s - p1b)) / beta1
        h = H
        t = f
        ylim = (-40, 20)                    

    poles = np.array((p1a, p1b))
    zeros = np.array((-beta1, ))

    axes = polezero_plot_with_time(t, h, poles, zeros, ylim=ylim, mode=mode)       

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

def polezero_demo2c():
    interact(polezero_demo2c_plot,
             alpha1=(-2, 20), omega1=(0, 20), beta1=(1, 40),
             mode=response_modes, continuous_update=False)             
