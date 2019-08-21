# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import subplots, setp
import scipy.signal as signal
from .signal_plot import create_axes

def filter_plot(b, a, fs, f=None, bode=True, N=400, **kwargs):

    if f is None:
        f = np.arange(N) / N * fs / 2

    # Quietly ignore DC bin where can have problems
    mf = f != 0
    f = f[mf]
        
    w, X = signal.freqz(b, a, 2 * np.pi * f / fs)

    axes, kwargs = create_axes(1, **kwargs)

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

    return axes.figure

