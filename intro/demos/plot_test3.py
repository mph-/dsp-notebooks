# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
import sys
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot

@interact()
def plot_test3():

    fs = 800
    f = 2
    T = 1
    N = int(fs * T)

    t = np.arange(N) / fs
    x = 4 * np.sin(2 * np.pi * f * t)

    signal_plot(t, x)

    print('matplotlib' in sys.modules)
    import matplotlib as mpl
    print(mpl.get_backend())
    show()
