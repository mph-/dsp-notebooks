# M. P. Hayes UCECE
import numpy as np
from scipy.signal import butter, lfilter
from ipywidgets import interact, interactive, fixed
from .lib.signal_plot import signal_plot2
from .lib.utils import rect

rmin = 0.05
rmax = 0.5

def sonar_tof_demo2_plot(tx_filter=False, rx_filter=False):

    r = 0.1
    f0 = 40e3
    fs = f0 * 25

    Tp = 8 / f0

    c = 340
    tau = 2 * r / c

    tau_max = 2 * rmax / c / 4
        
    N = int(fs * (tau_max + Tp))
    t = np.arange(0, N) / fs

    # TODO, fix withought kludge...
    s = np.sin(2 * np.pi * f0 * t) * rect(t / Tp - 0.5 + 0.01)
    s[s > 0] = 1
    s[s < 0] = -1

    BW = 4e3
    fb = np.array((40e3 - BW / 2, 40e3 + BW / 2))
    b, a = butter(2, 2 * fb / fs, 'bandpass')

    sf = s
    if tx_filter:
        sf = lfilter(b, a, s)
    if rx_filter:
        sf = lfilter(b, a, sf)        

    fig = signal_plot2(t, s, t, sf, ylim=(-1.1, 1.1))
    

def sonar_tof_demo2():
    interact(sonar_tof_demo2_plot, continuous_update=False)
    
    
