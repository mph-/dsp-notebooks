# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot3
from .lib.signal import Signal, signals

def convolution_demo2_plot(x=signals[7], h=signals[9]):

    N = 800
    tmax = 5
    fmax = 5    
    t1 = np.linspace(-tmax, tmax, N)    

    dt = t1[1] - t1[0]    
    offset = int(-t1[0] / dt)
    
    x1 = Signal(x)(t1)
    h1 = Signal(h)(t1)

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
    
