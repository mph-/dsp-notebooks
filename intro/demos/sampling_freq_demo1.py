# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import spectrum_plot
import scipy.signal as signal
from .lib.utils import butterworth_lowpass


def sampling_freq_demo1_plot(fb=2, fs=5, order=2, bode=False):

    mode = 'magnitude'
    log_frequency = False
    if bode:
        mode = 'magnitude dB'
        log_frequency = True        
    
    # Calculate frequency response
    N = 1000
    if log_frequency:
        fs1 = 50        
        f = np.arange(0, N) * fs1 / N        
    else:
        fs1 = 16
        f = np.arange(-N//2, N//2) * fs1 / N        
        
    S = butterworth_lowpass(f, fb, order)

    fig = spectrum_plot(f, S, mode=mode, log_frequency=log_frequency)
    axes = fig.axes[0]
    
    if log_frequency:
        plot = axes.semilogx
        axes.set_ylim(-60, 2)
        M = 20
    else:
        plot = axes.plot
        M = 4

    for m in range(0, M):

        k = m // 2 + 1
        s = (m % 2) * 2 - 1
        
        Simage = butterworth_lowpass(f + s * k * fs, fb, order)
        Simage = abs(Simage)
        
        if bode:
            Simage = 20 * np.log10(abs(Simage))
        
        plot(f, Simage, linestyle='--')

    if log_frequency:
        axes.set_xticks((0.01 * fs, 0.1 * fs, fs, 2 * fs, 3 * fs, 4 * fs))
        axes.set_xticklabels(('0.001 fs', '0.1 fs', 'fs', '2fs', '3fs'))
    else:
        axes.set_xticks((-2 * fs, -fs, 0, fs, 2 * fs))
        axes.set_xticklabels(('-2 fs', '-fs', '0', 'fs', '2fs'))
        
        
def sampling_freq_demo1():
    interact(sampling_freq_demo1_plot, fb=(1, 5, 0.5),
             fs=(4, 20, 0.5),             
             order=(1, 10, 1),
             continuous_update=False)
    
