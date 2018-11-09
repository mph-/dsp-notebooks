# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time


def polezero_demo3_plot(alpha1=5, omega1=10, alpha2=20, step_response=True):

    t = np.linspace(0, 3, 201)
    f = np.linspace(-100, 100, 201)
    s = 2j * np.pi * f

    p1a = -alpha1 - 1j * omega1
    p1b = -alpha1 + 1j * omega1
    p2 = -alpha2

    H = -p2 * -p1a * -p1b / ((s - p1a) * (s - p1b) * (s - p2))
    if step_response:
        H = H / (s + 1e-12)

    #h = ((alpha1 - alpha2) * np.exp(alpha1 * t) * np.sin(omega1 * t) - omega1 * np.exp(alpha1 * t) + omega1 * np.exp(alpha2 * t)) / (omega1 * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2))

    h = alpha2 * (alpha1**2 + omega1**2) * (omega1 * (omega1**2 + (alpha1 - alpha2)**2) * np.exp(alpha1 * t) - (omega1 * np.cos(omega1 * t) + (alpha1 - alpha2) * np.sin(omega1 * t)) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * np.exp(alpha2 * t)) * np.exp(-t * (alpha1 + alpha2)) / (omega1 * (omega1**2 + (alpha1 - alpha2)**2) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2))
    
    if step_response:
        h = (alpha1**2 * alpha2 * np.exp(alpha2 * t) * np.sin(omega1 * t) - alpha1**2 * omega1 * np.exp(alpha1 * t) + alpha1**2 * omega1 * np.exp(t * (alpha1 + alpha2)) - alpha1 * alpha2**2 * np.exp(alpha2 * t) * np.sin(omega1 * t) + 2 * alpha1 * alpha2 * omega1 * np.exp(alpha2 * t) * np.cos(omega1 * t) - 2 * alpha1 * alpha2 * omega1 * np.exp(t * (alpha1 + alpha2)) - alpha2**2 * omega1 * np.exp(alpha2 * t) * np.cos(omega1 * t) + alpha2**2 * omega1 * np.exp(t * (alpha1 + alpha2)) - alpha2 * omega1**2 * np.exp(alpha2 * t) * np.sin(omega1 * t) - omega1 ** 3 * np.exp(alpha1 * t) + omega1 ** 3 * np.exp(t * (alpha1 + alpha2))) * np.exp(-t * (alpha1 + alpha2)) / (omega1 * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2))        

    poles = np.array((p1a, p1b, p2))

    axes = polezero_plot_with_time(t, h, poles, ylim=(-0.5, 2.1))
    

def polezero_demo3():
    interact(polezero_demo3_plot,
             alpha1=(-2, 20), omega1=(1, 20), alpha2=(-2, 40),
             continuous_update=False)

