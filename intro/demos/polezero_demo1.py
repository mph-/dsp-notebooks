# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.polezero_plot import polezero_plot_with_time


def polezero_demo1_plot(alpha=5, step_response=True):

    t = np.linspace(0, 3, 201)
    f = np.linspace(-100, 100, 201)
    s = 2j * np.pi * f

    p1 = -alpha

    H = -p1 / (s - p1)
    if step_response:
        H = H / (s + 1e-12)

    h = -p1 * np.exp(p1 * t)

    if step_response:
        #h = np.cumsum(h) * (t[1] - t[0])
        h = 1 - np.exp(p1 * t)

    poles = np.array((p1, ))

    polezero_plot_with_time(t, h, poles, ylim=(-0.5, 2.1))


def polezero_demo1():
    interact(polezero_demo1_plot,
             alpha=(-2, 20), 
             continuous_update=False)
