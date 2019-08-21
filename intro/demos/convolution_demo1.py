# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot3
from .lib.signal import Signal, signals

def convolution_demo1_plot(x='fang(t)', h='exp(-t) u(t)', t=0.5):

    N = 500
    tmax = 5
    fmax = 5    
    t1 = np.linspace(-tmax, tmax, N)    

    dt = t1[1] - t1[0]    
    offset = int(-t1[0] / dt)
    
    x1 = Signal(x)(t - t1)
    x2 = Signal(h)(t1)
    y1 = Signal(x)(t1)    

    bar = [max(x2 * Signal(x)(tau - t1)) for tau in t1]
    
    z1 = x1 * x2
    z = np.convolve(y1, x2)[offset:offset + len(t1)] * dt

    foo = np.trapz(z1, t1)
    
    fig = signal_plot3(t1, x1, t1, z1, t1, z)
    axes = fig.axes
    axes[0].plot(t1, x2)
    axes[0].legend((r'$x(%s-\tau)$' % t, r'$h(\tau)$'))
    axes[0].set_xlabel(r'$\tau$')
    axes[1].fill_between(t1, 0, z1, facecolor='none', edgecolor='b', hatch='///')
    axes[1].legend((r'$x(%s-\tau) h(\tau)$' % t, ))    
    axes[1].set_ylim(0, max(bar))
    axes[1].set_xlabel(r'$\tau$')    
    axes[2].plot((t, t), (0, foo), 'r')
    axes[2].plot(t, foo, 'ro')    
    axes[2].legend((r'$y(t)$', ))
    axes[2].set_xlabel('$t$')    

    fig.tight_layout()

def convolution_demo1():
    interact(convolution_demo1_plot, x=signals, h=signals,
             t=(-5, 5, 0.1), continuous_update=False)
    
