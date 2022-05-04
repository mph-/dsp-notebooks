# M. P. Hayes UCECE
from numpy import pi, exp, sin, cos, linspace
from ipywidgets import interact
from .lib.signal_plot import signal_plot_with_dft
from .lib.utils import rect, sinc

funcs = ['exp(-0.1 |t|) cos(2 pi t)',
         'exp(-0.1 |t|) sin(4 pi t)',
         'exp(-0.1 |t|',
         '0']


def calc_signal(func, t):

    alpha = 0.1

    if func == funcs[0]:
        return exp(-alpha * abs(t)) * cos(2 * pi * t)
    elif func == funcs[1]:
        return exp(-alpha * abs(t)) * cos(4 * pi * t)
    elif func == funcs[2]:
        return exp(-alpha * abs(t))
    return 0


def calc_spectrum(func, f):

    alpha = 0.1

    if func == funcs[0]:
        f0 = 1
        return 2*alpha*(alpha**2 + 4*pi**2*f**2 + 4*pi**2*f0**2)/(alpha**4 + 8*pi**2*alpha**2*f**2 + 8*pi**2*alpha**2*f0**2 + 16*pi**4*f**4 - 32*pi**4*f**2*f0**2 + 16*pi**4*f0**4)
    elif func == funcs[1]:
        f0 = 2
        return -16*1j*pi**2*alpha*f*f0/(alpha**4 + 8*pi**2*alpha**2*f**2 + 8*pi**2*alpha**2*f0**2 + 16*pi**4*f**4 - 32*pi**4*f**2*f0**2 + 16*pi**4*f0**4)
    elif func == funcs[2]:
        return 2*alpha/(alpha**2 + 4*pi**2*f**2)
    return 0


def fourier_linearity_demo2_plot(x=funcs[0], y=funcs[-1]):

    mode = 'real-imag'

    tmax = 4
    fmax = 4
    N = 1000

    t = linspace(-tmax, tmax, N)
    f = linspace(-fmax, fmax, N)

    xs = calc_signal(x, t)
    Xs = calc_spectrum(x, f)

    ys = calc_signal(y, t)
    Ys = calc_spectrum(y, f)

    z = xs + ys
    Z = Xs + Ys

    print('z = %s + %s' % (x, y))

    fig = signal_plot_with_dft(t, z, f, Z, mode=mode)
    axes = fig.axes
    axes[0].set_ylim(-2, 2)
    axes[1].set_ylim(-20, 20)


def fourier_linearity_demo2():
    interact(fourier_linearity_demo2_plot, x=funcs, y=funcs,
             continuous_update=False)
