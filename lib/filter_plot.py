import numpy as np
import scipy.signal as signal
from .signal_plot import one_axes

def filter_plot(b, a, fs, f=None, bode=True, N=400, **kwargs):

    if f is None:
        f = np.arange(N) / N * fs / 2
        
    w, X = signal.freqz(b, a, 2 * np.pi * f / fs)

    axes, kwargs = one_axes(**kwargs)

    if bode:
        P = abs(X)**2

        PdB = 10 * np.log10(P + 1e-12)
        
        axes.semilogx(f, PdB)
        axes.set_xlabel('Frequency (Hz)')
        axes.set_ylabel('dB')
        axes.set_ylim(-50, 0)

    else:
        axes.plot(f, abs(X))
        axes.set_xlabel('Frequency (Hz)')
        axes.set_ylabel('Magnitude')
        axes.set_ylim(0, 1.1)        
    
