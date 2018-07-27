# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot3
from .lib.utils import rect, sinc, gauss

signals = ['rect(t)', 'rect(t/2)', 'gauss(t)', 'fang(t)', 'gauss(t/0.01)']


def make_signal(t, name):

    if name == 'gauss(t)':
        return gauss(t, 0, 1)
    elif name == 'gauss(t/0.01)':
        x = gauss(t / 0.01)    
        return x / max(x)
    elif name == 'rect(t)':
        return rect(t)
    elif name == 'rect(t/2)':
        return rect(t / 2)
    elif name == 'fang(t)':
        return t * rect(t - 0.5)
    raise ValueError('Unknown signal ' + name)
    

def convolution_demo1_plot(x=signals[0], h=signals[0], t=0.5):

    N = 500
    tmax = 5
    fmax = 5    
    t1 = np.linspace(-tmax, tmax, N)    

    dt = t1[1] - t1[0]    
    offset = int(-t1[0] / dt)
    
    x1 = make_signal(t - t1, x)
    x2 = make_signal(t1, h)
    y1 = make_signal(t1, x)    

    bar = [max(x2 * make_signal(tau - t1, x)) for tau in t1]
    
    z1 = x1 * x2
    z = np.convolve(y1, x2)[offset:offset + len(t1)] * dt

    foo = np.trapz(z1, t1)
    
    fig = signal_plot3(t1, x2, t1, z1, t1, z)
    axes = fig.axes
    axes[0].plot(t1, x1)
    axes[0].legend((r'$x(t-\tau)$', r'$h(\tau)$'))
    axes[1].fill_between(t1, 0, z1, facecolor='none', edgecolor='b', hatch='///')
    axes[1].legend((r'$x(t-\tau) h(\tau)$', ))    
    axes[1].set_ylim(0, max(bar))
    axes[2].plot((t, t), (0, foo), 'r')
    axes[2].plot(t, foo, 'ro')    
    axes[2].legend((r'$y(t)$', ))        

def convolution_demo1():
    interact(convolution_demo1_plot, x=signals, h=signals,
             t=(-5, 5, 0.1),  continuous_update=False)
    
