# M. P. Hayes UCECE
import numpy as np
from numpy import exp, sin, cos
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time


def polezero_demo4_plot(alpha1=5, omega1=10, alpha2=20, beta1=10,
                        step_response=True):

    t = np.linspace(0, 3, 201)
    f = np.linspace(-100, 100, 201)
    s = 2j * np.pi * f

    p1a = -alpha1 - 1j * omega1
    p1b = -alpha1 + 1j * omega1
    p2 = -alpha2
    z1 = -beta1

    H = -p2 * -p1a * -p1b * (s + beta1) / ((s - p1a) * (s - p1b) * (s - p2))
    if step_response:
        H = H / (s + 1e-12)
    
    if step_response:
        h = (alpha2 * (-omega1 * ((2 * alpha1 - alpha2) * (alpha1**3 - alpha1**2 * beta1 + alpha1 * omega1**2 - beta1 * omega1**2) + (alpha1**2 + omega1**2) * (-alpha1**2 + alpha1 * alpha2 + omega1**2)) * cos(omega1 * t) + (-omega1**2 * (2 * alpha1 - alpha2) * (alpha1**2 + omega1**2) + (-alpha1**2 + alpha1 * alpha2 + omega1**2) * (alpha1**3 - alpha1**2 * beta1 + alpha1 * omega1**2 - beta1 * omega1**2)) * sin(omega1 * t)) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * exp(alpha2 * t) + beta1 * omega1 * (omega1**2 * (2 * alpha1 - alpha2)**2 + (-alpha1**2 + alpha1 * alpha2 + omega1**2)**2) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * exp(t * (alpha1 + alpha2)) + omega1 * (omega1**2 * (2 * alpha1 - alpha2)**2 + (-alpha1**2 + alpha1 * alpha2 + omega1**2)**2) * (alpha1**2 * alpha2 - alpha1**2 * beta1 + alpha2 * omega1**2 - beta1 * omega1**2) * exp(alpha1 * t)) * exp(-t * (alpha1 + alpha2)) * (t >= 0)/(beta1 * omega1 * (omega1**2 * (2 * alpha1 - alpha2)**2 + (-alpha1**2 + alpha1 * alpha2 + omega1**2)**2) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2))
    else:
        h = alpha2 * (-omega1 * (omega1**2 + (alpha1 - alpha2)**2)**2 * (alpha1**2 * alpha2 - alpha1**2 * beta1 + alpha2 * omega1**2 - beta1 * omega1**2) * exp(2 * alpha1 * t) - omega1 * (omega1**2 + (alpha1 - alpha2)**2) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * (-alpha1**3 + alpha1**2 * beta1 - alpha1 * omega1**2 + beta1 * omega1**2 + (alpha1 - alpha2) * (alpha1**2 + omega1**2)) * exp(t * (alpha1 + alpha2)) * cos(omega1 * t) + (omega1**2 + (alpha1 - alpha2)**2) * (omega1**2 * (alpha1**2 + omega1**2) + (alpha1 - alpha2) * (alpha1**3 - alpha1**2 * beta1 + alpha1 * omega1**2 - beta1 * omega1**2)) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * exp(t * (alpha1 + alpha2)) * sin(omega1 * t)) * exp(-t * (2 * alpha1 + alpha2)) * (t >= 0)/(beta1 * omega1 * (omega1**2 + (alpha1 - alpha2)**2)**2 * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2))        

    poles = np.array((p1a, p1b, p2))
    zeros = np.array((z1, ))    

    axes = polezero_plot_with_time(t, h, poles, zeros, ylim=(-0.5, 2.1))
    

def polezero_demo4():
    interact(polezero_demo4_plot,
             alpha1=(-2, 20), omega1=(1, 20), alpha2=(-2, 40),
             beta1=(-2, 40),
             continuous_update=False)

