# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from .lib.signal_plot import signal_plot

def plotseq_demo1_plot(sequence='{1, _2, 3, 4, 5}'):

    s = sequence.strip()
    if s == '':
        return
    if s[0] == '{' and s[-1] == '}':
        s = s[1:-1]
    parts = s.split(',')

    count = s.count('_')
    if count > 1:
        raise ValueError('More than one _ in %s' % sequence)

    vals = []
    underscore = 0
    for m, elt in enumerate(parts):
        elt = elt.strip()
        if elt == '':
            vals.append(0)
        else:
            if elt[0] == '_':
                underscore = m
                elt = elt[1:]
            vals.append(float(elt))
            
    seq = np.array(vals)
    t = np.arange(len(seq))
        
    fig = signal_plot(t - underscore, seq, lollipop=True)
    fig.axes[0].grid(True)
    

def plotseq_demo1():
    interact(plotseq_demo1_plot, continuous_update=False)             
