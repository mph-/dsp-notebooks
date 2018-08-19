# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import spectrum_plot,  spectrum_plot_func
import scipy.signal as signal
from .lib.utils import butterworth_lowpass


def sampling_freq_demo1_plot(fb=2, fs=5, order=2):

    fs1 = 16

    # Calculate frequency response
    N = 1000
    f = np.arange(-N//2, N//2) * fs1 / N
    S = butterworth_lowpass(f, fb, order)

    fig = spectrum_plot(f, S, mode='magnitude')
    axes = fig.axes[0]
    axes.set_xticks((-2 * fs, -fs, 0, fs, 2 * fs))
    axes.set_xticklabels(('-2 fs', '-fs', '0', 'fs', '2fs'))    

    for m in range(0, 4):

        k = m // 2 + 1
        s = (m % 2) * 2 - 1
        
        Simage = butterworth_lowpass(f + s * k * fs , fb, order)
        axes.plot(f, abs(Simage), linestyle='--')

        
def sampling_freq_demo1():
    interact(sampling_freq_demo1_plot, fb=(1, 5, 0.5),
             fs=(4, 10, 0.5),             
             order=(1, 10, 1),
             continuous_update=False)
    
    

    

