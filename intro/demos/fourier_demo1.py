# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_dft, spectrum_modes
from .lib.utils import rect, sinc

def rect_demo1_plot(T=1, mode='real-imag'):

    tmax = 5
    fmax = 5
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)    

    x = rect(t / T)
    X = T * sinc(f * T)
    
    signal_plot_with_dft(t, x, f, X, mode=mode)

def rect_demo1():
    interact(rect_demo1_plot, T=(0.1, 5, 0.1), mode=spectrum_modes,
             continuous_update=False)
    
def sinc_demo1_plot(T=1, mode='real-imag'):

    tmax = 5
    fmax = 5
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)    

    x = sinc(t / T)
    X = T * rect(f * T)
    
    signal_plot_with_dft(t, x, f, X, mode=mode)

def sinc_demo1():
    interact(sinc_demo1_plot, T=(0.1, 5, 0.1), mode=spectrum_modes,
             continuous_update=False)
    

def modulated_pulse_demo1_plot(T=1, f0=5, phase=0, mode='real-imag'):

    tmax = 5
    fmax = 20
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)    

    x = rect(t / T) * np.cos(2 * np.pi * f0 * t + np.radians(phase))

    X = 0.5 * T * sinc((f - f0) * T) * np.exp(-1j * np.radians(phase)) + 0.5 * T * sinc((f + f0) * T) * np.exp(1j * np.radians(phase))
    
    signal_plot_with_dft(t, x, f, X, mode=mode)

def modulated_pulse_demo1():
    interact(modulated_pulse_demo1_plot, T=(0.1, 8, 0.1),
             f0=(0, 10),
             phase=(-180, 180, 15),
             mode=spectrum_modes,
             continuous_update=False)

def dirac_delta_demo1_plot(alpha=0.05, mode='real-imag'):

    tmax = 20
    fmax = 0.5
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)    

    x = np.exp(-alpha * abs(t))
    X = 2 * alpha / (alpha**2 + (2 * np.pi *f)**2)
    
    axes = signal_plot_with_dft(t, x, f, X, mode=mode)
    ylim = axes[0].get_ylim()
    axes[0].set_ylim(0, ylim[1])

def dirac_delta_demo1():
    interact(dirac_delta_demo1_plot, alpha=(0.01, 0.1, 0.01),
             mode=spectrum_modes,
             continuous_update=False)
    

def time_shift_demo1_plot(delay=0, mode='real-imag'):

    tmax = 5
    fmax = 5
    N = 1000

    T = 4
    f0 = 2
    phase = 0

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)    

    t1 = t - delay
    x = rect(t1 / T) * np.cos(2 * np.pi * f0 * t1 + np.radians(phase))

    X = (0.5 * T * sinc((f - f0) * T) * np.exp(-1j * np.radians(phase)) + 0.5 * T * sinc((f + f0) * T) * np.exp(1j * np.radians(phase))) * np.exp(-1j * 2 * np.pi * f * delay)
    
    signal_plot_with_dft(t, x, f, X, mode=mode)

def time_shift_demo1():
    interact(time_shift_demo1_plot, delay=(-2, 2, 0.1),
             mode=spectrum_modes,
             continuous_update=False)
    
