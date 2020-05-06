# M. P. Hayes UCECE
import numpy as np
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import display, Math
from .lib.signal_plot import signal_plot3, signal_overplot2
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
        s = '%s' % val        
    return s


def equation(xseq, hseq, n):

    M = len(hseq)

    result = 0
    terms = []
    for m in range(M):
        h1 = hseq(m)
        x1 = xseq(n - m)        
        result += h1 * x1
        terms.append(numstr(h1) + r' \times ' + numstr(x1))
    return 'y[%d] = ' % n + ' + '.join(terms) + ' = ' + numstr(result)


def dt_convolution_demo1_plot(x='{_1, 2, 3}', h='{_0.5, 0.5}', n=0):

    xseq = Sequence(x)
    hseq = Sequence(h)

    x = np.array(xseq)
    h = np.array(hseq)    
    
    N = 13
    tmax = 5
    n1 = np.arange((1 - N) // 2, (N + 1) // 2, dtype=int)

    dt = 1    
    t1 = n1 * dt

    offset = -n1[0]

    x1 = xseq(n - n1)
    x2 = hseq(n1)
    y1 = xseq(n1)    

    z1 = x1 * x2
    z = np.convolve(y1, x2)[offset:offset + len(t1)]

    foo = np.sum(z1)
    
    valmin = min(min(x1), min(y1), min(z))
    valmax = max(max(x1), max(y1), max(z))

    display(Math(equation(hseq, xseq, n)))
    
    fig = signal_plot3(t1, x1, t1, z1, t1, z, lollipop=True)
    axes = fig.axes
    signal_overplot2(t1, x1, t1, x2, axes=axes[0], lollipop=True,
                     labels=[r'$x[%d-m]$' % n, r'$h[m]$'])
    axes[0].set_xlabel(r'$m$')
    axes[0].set_ylim(valmin, valmax)
    axes[0].grid(True)

    axes[1].legend((r'$x[%d-m] h[m]$' % n, ), loc='upper right')    
    axes[1].set_ylim(valmin, valmax)
    axes[1].set_xlabel(r'$m$')
    axes[1].grid(True)    
    
    axes[2].plot((n, n), (0, foo), 'r')
    axes[2].plot(n, foo, 'ro')
    axes[2].set_ylim(valmin, valmax)    
    axes[2].legend((r'$y[%d]$' % n, ), loc='upper right')    
    axes[2].set_xlabel('$n$')
    axes[2].grid(True)    

    fig.tight_layout()

def dt_convolution_demo1():
    interact(dt_convolution_demo1_plot, 
             n=(-10, 10, 1), continuous_update=False)
    
