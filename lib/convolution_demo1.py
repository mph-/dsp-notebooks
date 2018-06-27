# M. P. Hayes UCECE
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .signal_plot import signal_plot3

seq1 = '{_1, 0, 0, 0, 0, 0}'
seq2 = '{_1, 2, 3, 0, 0, 0}'
seq3 = '{_1, 1, 1, 0, 0, 0}'
seq4 = '{_0, 1, 0, 0, 0, 0}'
seq5 = '{_0, 0, 1, 0, 0, 0}'
seq6 = '{_0, 0, 0, 1, 0, 0}'
seq7 = '{_1, 1, 1, 1, 1, 1}'
seq8 = '{_1, 2, 3, 2, 1, 0}'
seq9 = '{_1, -1, 0, 0, 0, 0}'

sequences = [seq1, seq2, seq3, seq4, seq5, seq6, seq7, seq8, seq9]

def convert(seq):

    seq = seq[1:-1]
    seq = seq.replace('_', '')
    parts = seq.split(',')
    x = np.array(parts, dtype=float)
    nx = np.arange(len(x))
    return x, nx

def zeropad(x, N):

    return np.concatenate((x, np.zeros(N - len(x))))


def convolution_demo1_plot(x, h):

    x, nx = convert(x)
    h, nh = convert(h)

    y = signal.convolve(x, h)
    ny = np.arange(len(y))

    x = zeropad(x, len(y))
    h = zeropad(h, len(y))    
    
    signal_plot3(ny, x, ny, h, ny, y, lollipop=True, markersize=8)

def convolution_demo1():
    interact(convolution_demo1_plot,
             x=sequences, h=sequences,             
             continuous_update=False)
    
    

    

