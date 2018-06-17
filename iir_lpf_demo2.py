from __future__ import print_function
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import Audio

def iir_lpf_play(alpha=0.5):

    fs, x = scipy.io.wavfile.read('data/dalek-exterminate.wav')
    x = x[:, 0]

    y = signal.lfilter(b=(1 - alpha, ), a=(1, -alpha), x=x)

    # y = y / y.max()
    
    return Audio(y, rate=fs)
    #return Audio(filename='data/dalek-exterminate.wav')

def iir_lpf_demo2():
    interact(iir_lpf_play, alpha=(0.0, 1.0, 0.01), continuous_update=False)
    
    

    

