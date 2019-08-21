# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot3
from .lib.utils import rect, sinc, gauss, tri

signals = ['rect(t)', 'rect(t/2)', 'fang(t)',
           'tri(t)', 'tri(t/0.1)', 'tri(t/0.01)',
           'gauss(t)', 'gauss(t/0.1)', 'gauss(t/0.01)',
           'exp(-t) u(t)', 'u(t)']


def make_signal(t, name):

    if name == 'gauss(t)':
        return gauss(t, 0, 1)
    elif name == 'gauss(t/0.1)':
        x = gauss(t / 0.1)    
        return x / max(x)
    elif name == 'gauss(t/0.01)':
        x = gauss(t / 0.01)    
        return x / max(x)    
    elif name == 'rect(t)':
        return rect(t)
    elif name == 'rect(t/2)':
        return rect(t / 2)
    elif name == 'tri(t)':
        return tri(t)
    elif name == 'tri(t/0.1)':
        return tri(t / 0.1)
    elif name == 'tri(t/0.01)':
        return tri(t / 0.01)            
    elif name == 'fang(t)':
        return t * rect(t - 0.5)
    elif name == 'exp(-t) u(t)':
        return np.exp(-t) * (t >= 0)
    elif name == 'u(t)':
        return 1 * (t >= 0)    
    raise ValueError('Unknown signal ' + name)
    

def convolution_demo2_plot(x=signals[7], h=signals[9]):

    N = 800
    tmax = 5
    fmax = 5    
    t1 = np.linspace(-tmax, tmax, N)    

    dt = t1[1] - t1[0]    
    offset = int(-t1[0] / dt)
    
    x1 = make_signal(t1, x)
    h1 = make_signal(t1, h)

    y1 = np.convolve(x1, h1)[offset:offset + len(t1)] * dt

    fig = signal_plot3(t1, x1, t1, h1, t1, y1)
    axes = fig.axes
    axes[0].set_xlabel('$t$')
    axes[0].set_ylabel('$x(t)$')
    axes[1].set_xlabel('$t$')
    axes[1].set_ylabel('$h(t)$')
    axes[2].set_xlabel('$t$')        
    axes[2].set_ylabel('$y(t)$')

    fig.tight_layout()

def convolution_demo2():
    interact(convolution_demo2_plot, x=signals, h=signals,
             continuous_update=False)
    
