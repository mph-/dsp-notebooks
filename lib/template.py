# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact_manual
from .signal_plot import signal_plot

# x = widgets.IntSlider(min=-10, max=30, step=1, value=10));


# fixed does not generate a widget
def template_plot(f=4, alpha=0.5, beta=fixed(1)):

    A = 1
    N = 100
    fs = 100
    sigma = 0.2
    mu = 0
    np.random.seed(42)
    n = np.random.standard_normal(N) * sigma + mu
    t = np.arange(N) / fs

    s = A * np.sin(2 * np.pi * f * t)
    x = s + n

    y = signal.lfilter(b=(1 - alpha, ), a=(1, -alpha), x=x)

    signal_plot(t, y, lollipop=lollipop)    

def template_demo1():
    interact(template_plot, alpha=(0.0, 1.0, 0.01), continuous_update=False)
    
    

    

