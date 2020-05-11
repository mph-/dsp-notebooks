# M. P. Hayes UCECE
import numpy as np
from matplotlib.pyplot import show
import scipy.io.wavfile
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import Audio, display
from .lib.filter_plot import filter_plot

filters = ['High-pass', 'Low-pass', 'All-pass', 'Differentiator', 'Integrator']


def dalek_filter_play(alpha=0.5, signal_name='dalek-exterminate', filter='High-pass', bode=True):

    fs, x = scipy.io.wavfile.read('data/%s.wav' % signal_name)
    try:
        x = x[:, 0]
    except:
        pass

    #dt = 1 / fs
    # Normalise response
    dt = 1

    ymin = -30
    ymax = 5
    if filter == 'High-pass':
        a = (1.0, -alpha)        
        b = (alpha, -alpha )
    elif filter == 'Low-pass':
        a = (1.0, -alpha)
        b = (1.0 - alpha, )        
    elif filter == 'All-pass':
        a = (1.0, )
        b = (1.0, )        
    elif filter == 'Differentiator':
        a = (1.0, )
        b = (1.0 / dt, -1.0 / dt)
    elif filter == 'Integrator':
        a = (1.0, -1.0)
        b = (dt, )
        ymin = -5
        ymax = 30
    
    fig = filter_plot(b, a, fs, bode=bode)
    axes = fig.axes
    if bode:
        axes[0].set_ylim(ymin, ymax)
    show()
    
    y = signal.lfilter(b=b, a=a, x=x)

    display(Audio(y, rate=fs))

def dalek_filter_demo1():
    interact(dalek_filter_play, alpha=(0.0, 0.999, 0.01),
             signal_name=['dalek-exterminate', 'dalek-gun', 'dalek-groan'],
             filter=filters,
             continuous_update=False)

