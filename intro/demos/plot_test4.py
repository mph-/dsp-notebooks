# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import plot, show
from ipywidgets import interact, interactive, fixed

@interact()
def plot_test4():

    fs = 800
    f = 2
    T = 1
    N = int(fs * T)

    t = np.arange(N) / fs
    x = 4 * np.sin(2 * np.pi * f * t)

    plot(t, x)

