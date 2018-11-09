# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots
from ipywidgets import interact, interactive, fixed, interact


def polezero_demo2_plot(alpha1=5, omega1=10, step_response=True):

    t = np.linspace(0, 3, 201)
    f = np.linspace(-100, 100, 201)
    s = 2j * np.pi * f

    p1a = -alpha1 - 1j * omega1
    p1b = -alpha1 + 1j * omega1

    H = 1 / ((s - p1a) * (s - p1b))
    if step_response:
        H = H / (s + 1e-12)

    alpha2 = 1000000

    h = (alpha1 ** 2 + omega1 ** 2) * np.exp(-alpha1 * t) * np.sin(omega1 * t) / omega1

    if step_response:
        h = -(alpha1 * np.sin(omega1 * t) - omega1 * np.exp(alpha1 * t) + omega1 * np.cos(omega1 * t)) * np.exp(-alpha1 * t) / omega1


    p = np.array((p1a, p1b))
    
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


def polezero_demo2():
    interact(polezero_demo2_plot,
             alpha1=(-2, 20), omega1=(1, 20),
             continuous_update=False)
