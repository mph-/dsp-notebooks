# M. P. Hayes UCECE
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import Audio, display
from .lib.signal_plot import signal_plot

def convolution_audio_demo1_play(signal_name='dalek-exterminate',
                                 impulse_name='york-minster',
                                 show_impulse=True, show_log=False):

    if impulse_name is None:
        if signal_name is None:
            raise ValueError('Need to have a signal and/or an impulse response')
        h = np.ones(1)
    else:
        fs, h = scipy.io.wavfile.read('data/%s.wav' % impulse_name)
        try:
            h = h[:, 0]
        except:
            pass
        h = np.asarray(h, float)

    if signal_name is None:
        x = np.array([1])
    else:
        fs, x = scipy.io.wavfile.read('data/%s.wav' % signal_name)
        try:
            x = x[:, 0]
        except:
            pass

    b = h
    a = (1, )

    if show_impulse:
        h = h / 32767
        if show_log:
            h = np.log10(abs(h) + 1e-12)
            h[h < -4] = -4
        signal_plot(np.arange(len(h)) / fs, h)

    if False:
        # Too slow
        y = signal.lfilter(b=b, a=a, x=x)
    else:
        h = h / h.max()
        N = len(x) + len(h) - 1
        # Round to power of 2 for FFT efficiency
        Nz = 2 << (N - 1).bit_length()        
        X = np.fft.rfft(x, Nz)
        H = np.fft.rfft(h, Nz)
        Y = X * H
        y = np.fft.irfft(Y)[0:N]

    display(Audio(y, rate=fs))

def convolution_audio_demo1():
    interact(convolution_audio_demo1_play,
             signal_name=[None, 'dalek-exterminate', 'dalek-gun', 'dalek-groan', 'york-minster'],
             impulse_name=[None, 'york-minster', 'living-room', 'stairwell', 'bunker'],             
             continuous_update=False)
