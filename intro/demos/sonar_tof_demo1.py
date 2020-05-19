# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot2
from .lib.utils import rect

rmin = 0.05
rmax = 0.5

def sonar_tof_demo1_plot(r=0.1, spreading_loss=False, noise=False):

    f0 = 40e3
    fs = f0 * 10

    Tp = 8 / f0

    c = 340
    tau = 2 * r / c

    tau_max = 2 * rmax / c
        
    N = int(fs * (tau_max + Tp))
    t = np.arange(0, N) / fs
    
    A = 1
    if spreading_loss:
        A = 1 / (r / rmin)**2

    s = np.sin(2 * np.pi * f0 * t) * rect(t / Tp - 0.5)
    e = A * np.sin(2 * np.pi * f0 * (t - tau)) * rect((t - tau) / Tp - 0.5)

    if noise:
        e += np.random.standard_normal(N) * 0.02

    fig = signal_plot2(t, s, t, e, ylim=(-1.1, 1.1))
    

def sonar_tof_demo1():
    interact(sonar_tof_demo1_plot, r = (rmin, rmax, 0.025),
             continuous_update=False)
    
    
