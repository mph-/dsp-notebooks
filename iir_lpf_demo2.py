from __future__ import print_function
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import Audio

def iir_lpf_play(alpha=0.5, name='dalek-exterminate'):

    fs, x = scipy.io.wavfile.read('data/%s.wav' % name)
    try:
        x = x[:, 0]
    except:
        pass

    y = signal.lfilter(b=(1 - alpha, ), a=(1, -alpha), x=x)

    # y = y / y.max()
    
    return Audio(y, rate=fs)
    #return Audio(filename='data/dalek-exterminate.wav')

def iir_lpf_demo2():
    interact(iir_lpf_play, alpha=(0.0, 0.999, 0.01),
             name = ['dalek-exterminate', 'dalek-gun', 'dalek-groan'],
             continuous_update=False)
    
    

    

