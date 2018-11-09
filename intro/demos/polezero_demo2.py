# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time


def polezero_demo2_plot(alpha1=5, omega1=10, step_response=True):

    t = np.linspace(0, 3, 201)
    f = np.linspace(-100, 100, 201)
    s = 2j * np.pi * f

    p1a = -alpha1 - 1j * omega1
    p1b = -alpha1 + 1j * omega1

    H = p1a * p1b / ((s - p1a) * (s - p1b))
    if step_response:
        H = H / (s + 1e-12)

    alpha2 = 1000000

    if omega1 == 0:
        h = t * np.exp(-alpha1 * t)
    else:
        h = (alpha1 ** 2 + omega1 ** 2) * np.exp(-alpha1 * t) * np.sin(omega1 * t) / omega1

    if step_response:
        if omega1 == 0:
            h = -alpha1 * t * np.exp(-alpha1 * t) + 1 - np.exp(-alpha1 * t)
        else:
            h = -(alpha1 * np.sin(omega1 * t) - omega1 * np.exp(alpha1 * t) + omega1 * np.cos(omega1 * t)) * np.exp(-alpha1 * t) / omega1        


    poles = np.array((p1a, p1b))

    axes = polezero_plot_with_time(t, h, poles, ylim=(-0.5, 2.1))

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

        axes[1].set_title('%s  zeta=%.2f  omega0=%.1f' % (s, zeta, omega0))

def polezero_demo2():
    interact(polezero_demo2_plot,
             alpha1=(-2, 20), omega1=(0, 20),
             continuous_update=False)
