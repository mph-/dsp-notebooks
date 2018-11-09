# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots, setp

def polezero_plot_with_time(t, h, poles=None, zeros=None, ylim=None, **kwargs):

    fig, axes = subplots(1, 2, figsize=(12, 6))
    
    axes[0].grid(True)
    axes[0].set_xlim(-20, 20)
    axes[0].set_ylim(-20, 20)
    axes[0].set_xlabel('Real')
    axes[0].set_ylabel('Imaginary')    

    if poles is not None:
        axes[0].plot(poles.real, poles.imag, 'bx', ms=20)
    if zeros is not None:        
        axes[0].plot(zeros.real, zeros.imag, 'bo', ms=20)

    axes[1].plot(t, h)
    if ylim is not None:
        axes[1].set_ylim(ylim)
    axes[1].grid(True)
    axes[1].set_xlabel('Time (s)')
    #axes[1].set_ylabel('Amplitude')

    return axes
