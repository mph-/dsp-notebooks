# M. P. Hayes UCECE
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import Audio, display
from .lib.filter_plot import filter_plot
from .lib.signal_plot import signal_plot_with_dft

def mystery_audio_demo1_play(signal_name='mystery1',
                             fmin=200, fmax=220):

    if fmax < fmin:
        fmax = fmin
        return

    fs, x = scipy.io.wavfile.read('data/%s.wav' % signal_name)
    try:
        x = x[:, 0]
    except:
        pass
    
    N = len(x)
    # Round to power of 2 for FFT efficiency
    Nz = 2 << (N - 1).bit_length()
    f = np.arange(Nz // 2 + 1) / Nz * fs / 2
    H = (f > fmin) & (f < fmax)
    
    X = np.fft.rfft(x, Nz)
    Y = X * H
    y = np.fft.irfft(Y)[0:N]
    y = y / y.max()

    t = np.arange(N) / fs
    signal_plot_with_dft(t, x, f, X, lollipop=False, mode='magnitude')
    
    display(Audio(y, rate=fs))

def mystery_audio_demo1():
    interact(mystery_audio_demo1_play,
             fmin=(0, 2000, 100),
             fmax=(0, 2000, 100),
             signal_name=['mystery1', 'mystery2'],
             continuous_update=False)
