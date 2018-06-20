# M. P. Hayes UCECE
from matplotlib.pyplot import subplots, setp
import numpy as np

spectrum_modes = ['real-imag', 'magnitude', 'magnitude dB', 'phase', 'magnitude-phase', 'magnitude dB-phase']

def lollipop_plot(n, x, axes=None, markersize=6, **kwargs):
    """Produce a lollipop (stem) plot."""

    # TODO, use color cycler
    color = kwargs.pop('color', 'blue')
    
    markerline, stemlines, baseline = axes.stem(n, x, **kwargs)
    setp(baseline, 'linewidth', 0, 'color', color)
    setp(markerline, 'markersize', markersize, 'color', color)
    setp(stemlines, 'color', color)    


class Plotter(object):

    def plot_lines(self, x, y, **kwargs):
        axes = kwargs.pop('axes', self.axes)
        axes.plot(x, y, **kwargs)
        axes.set_xlabel(self.xlabel)

    def plot_lollipop(self, x, y, **kwargs):
        axes = kwargs.pop('axes', self.axes)        
        lollipop_plot(x, y, axes=axes, **kwargs)
        axes.set_xlabel(self.xlabel)        

    def __init__(self, axes, mode='time', lollipop=True):
        self.axes = axes
        self.mode = mode
        self.lollipop = lollipop
        self.plot_method = self.plot_lollipop if lollipop else self.plot_lines
        if mode == 'time':
            xlabel = 'Time'
            if lollipop:
                xlabel += ' (samples)'
            else:
                xlabel += ' (s)'
        else:
            xlabel = 'Frequency'
            if lollipop:
                xlabel += ' (samples)'
            else:
                xlabel += ' (Hz)'
        self.xlabel = xlabel
                

    def plot(self, x, y, **kwargs):
        if self.mode == 'time':
            self.plot_method(x, y, **kwargs)
            xlabel = 'Time (s)'
            if self.lollipop:
                xlabel = 'Time (samples)'                
            self.axes.set_xlabel(xlabel)

        elif self.mode == 'real-imag':
            self.plot_method(x, y.real, label='real', **kwargs)
            self.plot_method(x, y.imag, label='imag', color='orange', **kwargs)
            self.axes.legend()
            
        elif self.mode == 'magnitude':
            self.plot_method(x, abs(y), label='magnitude', **kwargs)
            self.axes.set_ylabel('Magnitude')

        elif self.mode == 'magnitude dB':
            dB = 20 * np.log10(abs(y))
            dB[dB < -100] = -100
            self.plot_method(x, dB, label='magnitude', **kwargs)
            self.axes.set_ylabel('Magnitude (dB)')

        elif self.mode == 'phase':
            self.plot_method(x, np.degrees(np.arctan2(y.imag, y.real)), label='phase', color='orange', **kwargs)
            self.axes.set_ylabel('Phase (deg)')

        elif self.mode == 'magnitude-phase':
            axes2 = self.axes.twinx()
            self.plot_method(x, abs(y), label='magnitude', **kwargs)
            self.axes.set_ylabel('Magnitude')
            self.plot_method(x, np.degrees(np.arctan2(y.imag, y.real)), label='phase', axes=axes2, color='orange', **kwargs)
            axes2.set_ylabel('Phase (deg)')
            self.axes.legend()
            axes2.legend()            
            
        elif self.mode == 'magnitude dB-phase':
            axes2 = self.axes.twinx()
            dB = 20 * np.log10(abs(y))
            dB[dB < -100] = -100            
            self.plot_method(x, dB, label='magnitude', **kwargs)
            self.axes.set_ylabel('Magnitude (dB)')
            self.plot_method(x, np.degrees(np.arctan2(y.imag, y.real)), label='phase', axes=axes2, color='orange', **kwargs)
            axes2.set_ylabel('Phase (deg)')
            self.axes.legend()
            axes2.legend()            
            
        else:
            raise ValueError('Unknown mode %s' % mode)
        
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
        fig.subplots_adjust(hspace=0.4)
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

def dtft_plot(f, X, mode='real-imag', **kwargs):

    axes, kwargs = one_axes(**kwargs)

    Plotter(axes, mode, lollipop=False).plot(f, X)
    
def signal_plot_with_dtft(t, x, f, X, **kwargs):

    axes, kwargs = two_axes(**kwargs)

    lollipop = kwargs.pop('lollipop', False)
    
    signal_plot(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    dtft_plot(f, X, axes=axes[1], **kwargs)    
        
    return axes[0].figure

def dft_plot(f, X, lollipop=False, mode='real-imag', **kwargs):
    axes, kwargs = one_axes(**kwargs)

    Plotter(axes, mode, lollipop).plot(f, X)

def signal_plot_with_dft(t, x, f, X, **kwargs):

    axes, kwargs = two_axes(**kwargs)

    lollipop = kwargs.pop('lollipop', False)
    mode = kwargs.pop('mode', 'real-imag')    
    
    signal_plot(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    dft_plot(f, X, axes=axes[1], lollipop=lollipop, mode=mode, **kwargs)    
        
    return axes[0].figure
