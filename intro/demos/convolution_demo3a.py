# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import create_axes
from .lib.signal import Signal, signals

def convolution_demo3_plot(h='exp(-t) u(t)', steps=4):

    x = 'u(t)'
    
    N = 800
    tmax = 5
    fmax = 5    
    t1 = np.linspace(-tmax, tmax, N)    

    dt = t1[1] - t1[0]    
    offset = int(-t1[0] / dt)
    
    x1 = Signal(x)(t1)
    h1 = Signal(h)(t1)

    y1 = np.convolve(x1, h1)[offset:offset + len(t1)] * dt

    #axes, foo = create_axes(steps + 2)
    fig, axes = subplots(steps + 3, figsize=(8, 6))

    axes[0].plot(t1, x1)
    #axes[0].set_xlabel('$t$')
    axes[0].set_ylabel('$x(t)$')

    axes[1].plot(t1, h1)
    #axes[1].set_xlabel('$t$')
    axes[1].set_ylabel('$h(t)$')    

    ys = y1 * 0
    
    T = 0.1
    for step in range(steps):
        x2 = x1 * (t1 >= step * T) * (t1 <= (step + 1) * T)
        y2 = np.convolve(x2, h1)[offset:offset + len(t1)] * dt
        axes[step + 2].plot(t1, y2)
        axes[step + 2].set_ylim(0, 1)
        ys += y2

    axes[steps + 2].plot(t1, ys)            
    axes[steps + 2].plot(t1, y1)    
    axes[steps + 2].set_xlabel('$t$')
    axes[steps + 2].set_ylabel('$y(t)$')

    for ax in axes:
        ax.set_xticklabels([])    
    
    fig = axes[0].figure
    #fig.tight_layout()

def convolution_demo3():
    interact(convolution_demo3_plot, x=signals, h=signals,
             steps=(1, 4, 1),
             continuous_update=False)
    
