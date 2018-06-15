from matplotlib.pyplot import subplots, setp
import numpy as np


def lollipop(ax, x, y, markersize=6, **kwargs):
    """Produce a lollipop (stem) plot."""

    markerline, stemlines, baseline = ax.stem(x, y, **kwargs)
    setp(baseline, 'linewidth', 0)
    setp(markerline, 'markersize', markersize)        

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
    lollipop(axes, n, x, **kwargs)
    axes.set_xlabel('Sample number')

def signal_plot_continuous(t, x, axes, **kwargs):

    axes.plot(t, x, **kwargs)
    axes.set_xlabel('Time (s)')

def signal_plot2(t, x, **kwargs):    

    axes = kwargs.pop('axes', None)        
    axes, kwargs = two_axes(**kwargs)
    
    signal_plot_discrete(t, x, axes=axes[0], **kwargs)
    signal_plot_continuous(t, x, axes=axes[1], **kwargs)    

def signal_plot(t, x, **kwargs):    

    if kwargs.pop('both', False):
        return signal_plot2(t, x, **kwargs)
    
    discrete = kwargs.pop('discrete', False)

    axes, kwargs = one_axes(**kwargs)

    if discrete:
        signal_plot_discrete(t, x, axes=axes, **kwargs)
    else:
        signal_plot_continuous(t, x, axes=axes, **kwargs)    

def hist_plot(t, x, **kwargs):

    bins = kwargs.pop('bins', 100)
    range = kwargs.pop('range', None)
    density = kwargs.pop('density', None)    
    
    axes, kwargs = one_axes(**kwargs)    
            
    axes.hist(x, density=density, bins=bins, range=range)
        
def signal_plot_with_hist(t, x, **kwargs):

    range = kwargs.pop('range', None)
    
    axes, kwargs = two_axes(**kwargs)

    signal_plot(t, x, axes=axes[0], **kwargs)
    hist_plot(t, x, axes=axes[1], range=range, **kwargs)
        
