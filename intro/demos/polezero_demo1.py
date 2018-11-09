# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact


def polezero_demo1_plot(alpha1=-5, step_response=True):

    t = np.linspace(0, 3, 201)
    f = np.linspace(-100, 100, 201)
    s = 2j * np.pi * f

    p1 = alpha1

    H = 1 / (s - p1)
    if step_response:
        H = H / (s + 1e-12)

    h = np.exp(p1 * t)

    if step_response:
        h = np.cumsum(h) * (t[1] - t[0])

    p = np.array((p1, ))
    
    fig, axes = subplots(1, 2, figsize=(12, 6))

    hmax = max(abs(h)) * 1.1
    
    axes[0].grid(True)
    axes[0].set_xlim(-20, 20)
    axes[0].set_ylim(-20, 20)
    axes[0].set_xlabel('Real')
    axes[0].set_ylabel('Imag')    

    #axes[0].plot(z.real, z.imag, 'bo', ms=20)
    axes[0].plot(p.real, p.imag, 'bx', ms=20)

    axes[1].plot(t, h)
    axes[1].set_ylim(-hmax, hmax)
    axes[1].grid(True)
    axes[1].set_xlabel('Time (s)')
    #axes[1].set_ylabel('Amplitude')


def polezero_demo1():
    interact(polezero_demo1_plot,
             alpha1=(-20, 2), 
             continuous_update=False)
