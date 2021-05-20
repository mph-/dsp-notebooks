# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import spectrum_plot
import scipy.signal as signal
from .lib.utils import butterworth_lowpass


def aliasing_demo1_plot(fm=0, fs=24, Nimages=0):

    fs = 24
    
    # Calculate frequency response
    N = 1000
    fs1 = 100
    f = np.arange(-N//2, N//2) * fs1 / N        

    fb = 1
    order = 2
    S = butterworth_lowpass(f + fm, fb, order) + butterworth_lowpass(f - fm, fb, order)

    mode = 'magnitude'    
    fig = spectrum_plot(f, S, mode=mode)
    axes = fig.axes[0]
    
    plot = axes.plot
    M = 4

    for m in range(0, Nimages):

        k = m // 2 + 1
        s = (m % 2) * 2 - 1
        
        Simage = butterworth_lowpass(f + fm + s * k * fs, fb, order) + butterworth_lowpass(f - fm + s * k * fs, fb, order)
        Simage = abs(Simage)
        
        plot(f, Simage, linestyle='--')

    axes.set_xticks((-2 * fs, -fs, 0, fs, 2 * fs))
    #axes.set_xticklabels(('-2 fs', '-fs', '0', 'fs', '2fs'))
        
def aliasing_demo1():
    interact(aliasing_demo1_plot, fm=(0, 25, 1), fs=(0, 25, 1),
             Nimages=(0, 4, 1),
             continuous_update=False)
