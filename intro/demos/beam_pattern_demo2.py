# M. P. Hayes UCECE
import numpy as np
from scipy.interpolate import interp1d
from matplotlib.pyplot import figure
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot_with_dft, spectrum_modes
from .lib.utils import rect, sinc

def beam_pattern_demo2_plot(lambdamm=5.0, Dmm=50.0):

    lam = lambdamm / 1e3
    D = Dmm / 1e3

    Dmax = 0.2
    
    dx = min(D / 64, lam / 2)
    
    N = max(4000, int(2 * D / dx))

    dfx = 1 / (N * dx)
    x = np.arange(-N // 2, N // 2) * dx
    fx = np.arange(-N // 2, N // 2) * dfx
    
    a = rect(x / D)
    
    A = abs(np.fft.fftshift(np.fft.fft(np.fft.fftshift(a))))
    A /= max(A)

    theta = np.linspace(-np.pi / 2, np.pi / 2, 501)

    interp = interp1d(fx, A, kind='linear', bounds_error=False,
                      fill_value=0)

    B = interp(np.sin(theta) / lam)

    Bx = abs(B) * np.cos(theta) * Dmax * 2
    By = abs(B) * np.sin(theta) * Dmax * 2

    W = 0.025
    H = D
    lower_left = (0, - H / 2)

    fig = figure()
    ax = fig.add_subplot(111)
    ax.axis('equal')
    ax.set_xlim(0, Dmax * 2)
    ax.set_ylim(-Dmax, Dmax)    
    
    ax.plot(Bx + W, By)
    ax.set_xlim(0, Dmax * 2)    
    
    ax.add_patch(patches.Rectangle(lower_left, W, D, fill=True,
                                   color='black'))
    ax.set_xticks([])
    ax.xaxis.set_ticks_position('none')
    ax.set_yticks([])
    ax.yaxis.set_ticks_position('none')    
    ax.set_title('$D/\lambda$ = %.2f' % (D / lam))


def beam_pattern_demo2():
    interact(beam_pattern_demo2_plot, continuous_update=False,
             lambdamm=(1, 50, 1),
             Dmm=(10, 100, 5))
    
