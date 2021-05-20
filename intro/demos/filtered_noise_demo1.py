# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
import scipy.signal as sig
from .lib.signal_plot import create_axes, signal_plot
from .lib.lowpass1 import Lowpass1
from .lib.highpass1 import Highpass1
from .lib.allpass import Allpass

filter_names = ['All-pass', 'Low-pass', 'High-pass']


def filter_noise(x, H, f):
    
    X = np.fft.rfft(x)
    Y = X * H
    y = np.fft.irfft(Y)

    return y


def filtered_noise_demo1_plot(filter_name=filter_names[0], alpha=5, seed=1):

    if filter_name == 'Low-pass':
        obj = Lowpass1(alpha)
    elif filter_name == 'High-pass':
        obj = Highpass1(alpha)
    elif filter_name == 'All-pass':
        obj = Allpass()                
    else:
        raise ValueError('Unknown filter %s' % filter_name)

    A0 = 4e-9
    N0 = A0**2
    
    fs = 2000

    sigmasq = N0 / 2 * fs
    sigma = np.sqrt(sigmasq) 

    Nplot = 400
    N = Nplot * 256
    N = Nplot * 2    
    
    t = np.arange(N) / fs
    f = np.arange(N) / N * fs    

    np.random.seed(seed)
    x = np.random.standard_normal(N) * sigma

    fp = f[0: N // 2 + 1]
    H = obj.frequency_response(fp)

    y = filter_noise(x, H, f)

    # f_e, S_Ye = sig.welch(y, fs)
    # A_Ye = np.sqrt(S_Ye)

    A_X = A0
    A_Y = A_X * abs(H)
    
    axes, tmp = create_axes(2)

    axes[0].loglog(fp, A_Y * 1e9)
    axes[0].set_ylabel('Voltage ASD (nV/rtHz)')
    axes[0].set_xlabel('Frequency (Hz)')
    axes[0].set_ylim(0.01, 10)

    m = np.arange(N) < Nplot
    
    signal_plot(t[m], y[m] * 1e6, lollipop=False, axes=axes[1], ylim=(-0.5, 0.5))
    axes[1].set_ylabel('Voltage (uV)')    

    
def filtered_noise_demo1():
    interact(filtered_noise_demo1_plot, filter_name=filter_names,
             alpha=(1, 100, 5), seed=(1, 100), continuous_update=False)
