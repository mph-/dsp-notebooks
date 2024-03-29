# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
from ipywidgets import interact
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

    ylim2 = None
    if mode in ('real-imag', 'magnitude'):
        ylim2 = (-1, 5)

    print('a = %s' % round(1 / T, 2))
    signal_plot_with_dft(t, x, f, X, mode=mode, ylim2=ylim2)
    show()


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

    ylim2 = None
    if mode in ('real-imag', 'magnitude'):
        ylim2 = (-1, 5)

    signal_plot_with_dft(t, x, f, X, mode=mode, ylim2=ylim2)


def sinc_demo1():
    interact(sinc_demo1_plot, T=(0.1, 5, 0.1), mode=spectrum_modes,
             continuous_update=False)


def toneburst_fourier_demo1_plot(T=1, f0=5, phase=0, mode='real-imag'):

    tmax = 5
    fmax = 20
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)

    x = rect(t / T) * np.cos(2 * np.pi * f0 * t + np.radians(phase))

    X = 0.5 * T * sinc((f - f0) * T) * np.exp(1j * np.radians(phase)) + \
        0.5 * T * sinc((f + f0) * T) * np.exp(-1j * np.radians(phase))

    ylim2 = (-1, 1)
    signal_plot_with_dft(t, x, f, X, mode=mode, ylim2=ylim2)


def toneburst_fourier_demo1():
    interact(toneburst_fourier_demo1_plot, T=(0.1, 8, 0.1),
             f0=(0, 10),
             phase=(-180, 180, 15),
             mode=spectrum_modes,
             continuous_update=False)


def fourier_hermitian_symmetry_demo1_plot(phase=0):
    return toneburst_fourier_demo1_plot(T=1, f0=5, phase=phase,
                                        mode='real-imag')


def fourier_hermitian_symmetry_demo1():
    interact(fourier_hermitian_symmetry_demo1_plot,
             phase=(-180, 180, 15),
             continuous_update=False)


def dirac_delta_demo1_plot(alpha=0.05, mode='real-imag'):

    tmax = 20
    fmax = 0.5
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)

    x = np.exp(-alpha * abs(t))
    X = 2 * alpha / (alpha**2 + (2 * np.pi * f)**2)

    fig = signal_plot_with_dft(t, x, f, X, mode=mode)
    axes = fig.axes
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

    W = np.exp(-1j * 2 * np.pi * f * delay)
    X = (0.5 * T * sinc((f - f0) * T) *
         np.exp(1j * np.radians(phase)) +
         0.5 * T * sinc((f + f0) * T) * np.exp(-1j * np.radians(phase))) * W

    signal_plot_with_dft(t, x, f, X, mode=mode)


def time_shift_demo1():
    interact(time_shift_demo1_plot, delay=(-2, 2, 0.1),
             mode=spectrum_modes,
             continuous_update=False)


def delayed_toneburst_fourier_demo1_plot(T=1, f0=5, tau=0, mode='real-imag'):

    tmax = 5
    fmax = 20
    N = 1000

    t = np.linspace(-tmax, tmax, N)
    f = np.linspace(-fmax, fmax, N)

    t1 = t - tau
    x = rect(t1 / T) * np.cos(2 * np.pi * f0 * t1)

    X = (0.5 * T * sinc((f - f0) * T) + 0.5 * T *
         sinc((f + f0) * T)) * np.exp(-2j * np.pi * f * tau)

    signal_plot_with_dft(t, x, f, X, mode=mode)


def delayed_toneburst_fourier_demo1():
    interact(delayed_toneburst_fourier_demo1_plot, T=(0.1, 8, 0.1),
             f0=(0, 10),
             tau=(0, 5, 0.1),
             mode=spectrum_modes,
             continuous_update=False)
