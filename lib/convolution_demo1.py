from __future__ import print_function
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import Audio, display, display
from .filter_plot import filter_plot

def convolution_play(signal_name='dalek-exterminate',
                     impulse_name='york-minster'):

    if impulse_name is None:
        h = np.ones(1)
    else:
        fs, h = scipy.io.wavfile.read('data/%s.wav' % impulse_name)
        try:
            h = h[:, 0]
        except:
            pass
        h = np.asarray(h, float)
    
    fs, x = scipy.io.wavfile.read('data/%s.wav' % signal_name)
    try:
        x = x[:, 0]
    except:
        pass

    b = h
    a = (1, )
    
    #filter_plot(b, a, fs, bode=bode)

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

def convolution_demo1():
    interact(convolution_play,
             signal_name=['dalek-exterminate', 'dalek-gun', 'dalek-groan', 'york-minster'],
             impulse_name=[None, 'york-minster', 'living-room', 'stairwell'],             
             continuous_update=False)
    
    

    

