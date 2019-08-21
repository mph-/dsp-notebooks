# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import create_axes
from .lib.signal import Signal, signals

def convolution_demo3_plot(h='exp(-t) u(t)', T=0.2, steps=4):

    x = 'u(t)'

    N = 500
    tmax = 4
    t1 = np.linspace(-1, tmax, N)    

    dt = t1[1] - t1[0]    
    offset = int(-t1[0] / dt)
    
    x1 = Signal(x)(t1)
    h1 = Signal(h)(t1)

    y1 = np.convolve(x1, h1)[offset:offset + len(t1)] * dt

    #axes, foo = create_axes(steps + 2)
    fig, axes = subplots(steps + 2, 2, figsize=(8, 6))

    axes[0, 0].plot(t1, t1 * 0)    
    axes[0, 0].arrow(0, 0, 0, 1, lw=1.5,  fc='k', ec='k',
                     head_width=0.1, head_length=0.2, overhang=0.1,
                     length_includes_head=True, clip_on=False)
    axes[0, 1].plot(t1, h1, 'k')

    ys = y1 * 0
    xs = x1 * 0    

    for step in range(steps):
        x2 = x1 * (t1 >= step * T) * (t1 <= (step + 1) * T)
        y2 = np.convolve(x2, h1)[offset:offset + len(t1)] * dt
        axes[step + 1, 0].plot(t1, x2, color='orange')
        axes[step + 1, 1].plot(t1, y2, color='orange')

        xs += x2        
        ys += y2

    axes[steps + 1, 0].plot(t1, x1, '--')
    axes[steps + 1, 0].plot(t1, xs, color='purple')
    axes[steps + 1, 1].plot(t1, y1, '--')
    axes[steps + 1, 1].plot(t1, ys, color='purple')    
    axes[steps + 1, 0].set_xlabel('$t$')    
    axes[steps + 1, 1].set_xlabel('$t$')

    for ax in axes.flat:
        ax.set_xticklabels([])
        ax.set_yticks([0, 1])
        ax.set_ylim(0, 1.1)
        

    #fig.tight_layout()

def convolution_demo3():
    interact(convolution_demo3_plot, x=signals, h=signals,
             T=(0.05, 0.8, 0.05),             
             steps=(1, 10, 1),
             continuous_update=False)
    
