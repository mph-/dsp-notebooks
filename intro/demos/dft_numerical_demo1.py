# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import display, Math
from .lib.signal_plot import signal_plot_with_dft, spectrum_modes
from .lib.sequence import Sequence


def numstr(val):
    s = ''
    sign = '+'
    if val < 0:
        sign = '-'
        val = -val

    if isinstance(val, int) or val.is_integer():
        s = '%d' % val
    else:
        s = '%.3g' % val
    return s

def cnumstr(val):

    if val.real == 0 and val.imag == 0:
        return '0'

    if val.imag == 0:
        return numstr(val.real)

    if val.real == 0:
        return r'\mathrm{j}' + numstr(val.imag)

    return numstr(val.real) + ' + ' + r'\mathrm{j}' + numstr(val.imag)


def dft_numerical_demo1_plot(x='{_1, 0, 0, 0}', mode='real-imag'):

    xseq = Sequence(x)
    x = np.array(xseq)

    N = len(x)
    X = np.fft.fft(x)

    terms = []
    for n in range(N):
        terms.append(cnumstr(X[n]))
        
    display(Math(r'X = \left\{' + ', '.join(terms) + r'\right\}'))

    fs = 1
    f = np.arange(N) / N * fs
    t = np.arange(N) / fs
    
    signal_plot_with_dft(t, x, f, X, lollipop=True, mode=mode)
    

def dft_numerical_demo1():
    interact(dft_numerical_demo1_plot, mode=spectrum_modes,
             continuous_update=False)
    
