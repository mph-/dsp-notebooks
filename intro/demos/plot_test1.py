# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
import sys
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot

def plot_test1_plot():

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

def plot_test1():
    interact(plot_test1_plot, continuous_update=False)
    
    

    

