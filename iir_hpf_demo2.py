from __future__ import print_function
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import Audio
from filter_plot import filter_plot

def iir_hpf_play(alpha=0.5, name='dalek-exterminate', bode=True):

    fs, x = scipy.io.wavfile.read('data/%s.wav' % name)
    try:
        x = x[:, 0]
    except:
        pass

    b = (alpha, -alpha)
    a = (1, -alpha)
    
    filter_plot(b, a, fs, bode=bode)
    
    y = signal.lfilter(b=b, a=a, x=x)

    # y = y / y.max()
    
    return Audio(y, rate=fs)
    #return Audio(filename='data/dalek-exterminate.wav')

def iir_hpf_demo2():
    interact(iir_hpf_play, alpha=(0.001, 1.0, 0.01),
             name = ['dalek-exterminate', 'dalek-gun', 'dalek-groan'],
             continuous_update=False)
    
    

    

