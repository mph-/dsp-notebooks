# M. P. Hayes UCECE
import numpy as np
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact
from IPython.display import Audio
from .lib.filter_plot import filter_plot


def adt_play(M=5000, alpha=0.5, signal_name='dalek-exterminate', bode=True):

    fs, x = scipy.io.wavfile.read('data/%s.wav' % signal_name)
    try:
        x = x[:, 0]
    except:
        pass

    b = np.zeros(M + 1)
    b[M] = alpha
    b[0] = 1 - alpha
    a = (1, )

    filter_plot(b, a, fs, bode=bode)

    y = signal.lfilter(b=b, a=a, x=x)

    audio = Audio(y, rate=fs, embed=True)
    return audio


def adt_demo1():
    interact(adt_play, alpha=(0.0, 0.999, 0.01),
             M=(0, 10000, 100),
             signal_name=['dalek-exterminate', 'dalek-gun', 'dalek-groan'],
             continuous_update=False)
