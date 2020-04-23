# M. P. Hayes UCECE
import numpy as np
import scipy.signal as signal
from ipywidgets import interact, interactive, fixed, interact
from IPython.display import display, Math
from .lib.signal_plot import signal_plot

def foo(join, val, index):

    if val == 0:
        return ''
    
    num = ''
    sign = '+'
    if val < 0:
        sign = '-'
        val = -val
    if val.is_integer:
        if val == 1:
            num = ''
        else:
            num = '%d' % val
    else:
        num = '%s' % val        
        
    if index == 0:
        term = r'%s \delta[n]' % num
    elif index < 0:
        term = r'%s \delta[n + %d]' % (num, -index)
    else:
        term = r'%s \delta[n - %d]' % (num, index)        

    if not join:
        if sign == '+':
            return term
        else:
            return '-' + term            
    return sign + ' ' + term

def sumimpulses(seq, offset=0):

    string = 'x[n] = '
    for m, val in enumerate(seq):
        string += foo(m != 0, val, m - offset)
    return string

def plotseq_demo1_plot(sequence='{1, _2, 3, 4, 5}'):

    s = sequence.strip()
    if s == '':
        return

    # Be generous with the sequence formatting.
    if s.startswith('{'):
        s = s[1:]
    if s.endswith('}'):
        s = s[:-1]

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

    display(Math(sumimpulses(seq, underscore)))    
    
    fig = signal_plot(t - underscore, seq, lollipop=True)
    fig.axes[0].grid(True)
    
def plotseq_demo1():
    interact(plotseq_demo1_plot, continuous_update=False)             
