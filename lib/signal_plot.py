# M. P. Hayes UCECE
from matplotlib.pyplot import subplots, setp
import numpy as np

def lollipop_plot(n, x, axes=None, markersize=6, **kwargs):
    """Produce a lollipop (stem) plot."""

    # TODO, use color cycler
    color = kwargs.pop('color', 'blue')
    
    markerline, stemlines, baseline = axes.stem(n, x, **kwargs)
    setp(baseline, 'linewidth', 0, 'color', color)
    setp(markerline, 'markersize', markersize, 'color', color)
    setp(stemlines, 'color', color)    

def one_axes(**kwargs):

    axes = kwargs.pop('axes', None)
    figsize = kwargs.pop('figsize', (8, 4))

    if axes is None:
        fig, axes = subplots(1, figsize=figsize)
    return axes, kwargs

def two_axes(**kwargs):

    axes = kwargs.pop('axes', None)
    figsize = kwargs.pop('figsize', (8, 4))    

    if axes is None:    
        fig, axes = subplots(2, 1, figsize=figsize)
    return axes, kwargs

def signal_plot_discrete(t, x, axes, **kwargs):

    n = np.arange(len(t))
    lollipop_plot(n, x, axes=axes, **kwargs)
    axes.set_xlabel('Sample number')

def signal_plot_continuous(t, x, axes, **kwargs):

    axes.plot(t, x, **kwargs)
    axes.set_xlabel('Time (s)')

def signal_plot2(t1, x1, t2, x2, **kwargs):    

    axes, kwargs = two_axes(**kwargs)
    
    signal_plot(t1, x1, axes=axes[0], **kwargs)
    signal_plot(t2, x2, axes=axes[1], **kwargs)    

def signal_plot(t, x, **kwargs):    

    if kwargs.pop('both', False):
        axes, kwargs = two_axes(**kwargs)
        signal_plot_discrete(t, x, axes=axes[0], **kwargs)
        signal_plot_continuous(t, x, axes=axes[1], **kwargs)
        return axes[0].figure
    
    lollipop = kwargs.pop('lollipop', False)

    axes, kwargs = one_axes(**kwargs)

    if lollipop:
        signal_plot_discrete(t, x, axes=axes, **kwargs)
    else:
        signal_plot_continuous(t, x, axes=axes, **kwargs)

    return axes.figure        

def hist_plot(t, x, **kwargs):

    bins = kwargs.pop('bins', 100)
    range = kwargs.pop('range', None)
    density = kwargs.pop('density', None)    
    
    axes, kwargs = one_axes(**kwargs)    
            
    axes.hist(x, density=density, bins=bins, range=range)
        
def signal_plot_with_hist(t, x, **kwargs):

    range = kwargs.pop('range', None)
    lollipop = kwargs.pop('lollipop', False)    
    
    axes, kwargs = two_axes(**kwargs)

    signal_plot(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    hist_plot(t, x, axes=axes[1], range=range, **kwargs)

    return axes[0].figure    

def dtft_plot(f, X, **kwargs):

    axes, kwargs = one_axes(**kwargs)
    axes.plot(f, X.real, label='real', **kwargs)
    axes.plot(f, X.imag, label='imag', **kwargs)    
    axes.set_xlabel('Frequency (Hz)')
    axes.legend()    
    
def signal_plot_with_dtft(t, x, f, X, **kwargs):

    axes, kwargs = two_axes(**kwargs)

    lollipop = kwargs.pop('lollipop', False)
    
    signal_plot(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    dtft_plot(f, X, axes=axes[1], **kwargs)    
        
    return axes[0].figure

def dft_plot(f, X, lollipop=False, **kwargs):
    axes, kwargs = one_axes(**kwargs)

    if lollipop:
        lollipop_plot(f, X.real, label='real', axes=axes, **kwargs)
        lollipop_plot(f, X.imag, label='imag', axes=axes, **kwargs, color='orange')
        axes.set_xlabel('Sample')
    else:
        axes.plot(f, X.real, label='real', **kwargs)
        axes.plot(f, X.imag, label='imag', **kwargs)    
        axes.set_xlabel('Frequency (Hz)')
    axes.legend()

def signal_plot_with_dft(t, x, f, X, **kwargs):

    axes, kwargs = two_axes(**kwargs)

    lollipop = kwargs.pop('lollipop', False)
    
    signal_plot(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    dft_plot(f, X, axes=axes[1], lollipop=lollipop, **kwargs)    
        
    return axes[0].figure
