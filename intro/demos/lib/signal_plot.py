# M. P. Hayes UCECE
from matplotlib.pyplot import subplots, setp
import numpy as np

spectrum_modes = ['real-imag', 'magnitude', 'magnitude dB', 'phase', 'magnitude-phase', 'magnitude dB-phase']

def lollipop_plot(x, y, axes=None, markersize=4, **kwargs):
    """Produce a lollipop (stem) plot."""

    # TODO, use color cycler
    color = kwargs.pop('color', 'blue')

    x = np.arange(len(x))
    
    markerline, stemlines, baseline = axes.stem(x, y, **kwargs)
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

        ylim = kwargs.pop('ylim', None)
        
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

        if ylim is not None:
           self.axes.set_ylim(ylim)

            
def create_axes(num_axes, **kwargs):

    axes = kwargs.pop('axes', None)
    figsize = kwargs.pop('figsize', (8, 4))    

    if axes is None:    
        fig, axes = subplots(num_axes, 1, figsize=figsize)
        if num_axes > 1:
            fig.subplots_adjust(hspace=0.4)
    return axes, kwargs

def signal_plot_func(t, x, **kwargs):    

    if kwargs.pop('both', False):
        axes, kwargs = create_axes(2, **kwargs)
        Plotter(axes[0], 'time', lollipop=True).plot(t, x)
        Plotter(axes[1], 'time', lollipop=False).plot(t, x)                
        return axes[0].figure

    axes, kwargs = create_axes(1, **kwargs)    
    lollipop = kwargs.pop('lollipop', False)
    Plotter(axes, 'time', lollipop=lollipop).plot(t, x, **kwargs)
    return axes

def dft_plot_func(f, X, lollipop=False, mode='real-imag', **kwargs):
    axes, kwargs = create_axes(1, **kwargs)

    Plotter(axes, mode, lollipop).plot(f, X)
    return axes

def dtft_plot_func(f, X, mode='real-imag', **kwargs):

    axes, kwargs = create_axes(1, **kwargs)

    Plotter(axes, mode, lollipop=False).plot(f, X)
    return axes

def fourier_series_plot_func(n, X, mode='real-imag', **kwargs):

    axes, kwargs = create_axes(1, **kwargs)

    Plotter(axes, mode, lollipop=True).plot(n, X)
    return axes

def hist_plot_func(t, x, **kwargs):

    bins = kwargs.pop('bins', 100)
    range = kwargs.pop('range', None)
    density = kwargs.pop('density', None)    
    
    axes, kwargs = create_axes(1, **kwargs)    
            
    axes.hist(x, density=density, bins=bins, range=range)
    return axes

def signal_plot(t, x, **kwargs):

    axes, kwargs = create_axes(1, **kwargs)
    signal_plot_func(t, x, axes=axes, **kwargs)
    return axes.figure
    
def signal_plot2(t1, x1, t2, x2, **kwargs):    

    axes, kwargs = create_axes(2, **kwargs)
    
    signal_plot_func(t1, x1, axes=axes[0], **kwargs)
    if 'color' not in kwargs:
        kwargs['color'] = 'orange'
    signal_plot_func(t2, x2, axes=axes[1], **kwargs)
    return axes[0].figure

def signal_plot_with_interpolated(t1, x1, t2, x2, **kwargs):

    axes, kwargs = create_axes(1, **kwargs)    
    lollipop = kwargs.pop('lollipop', False)
    p1 = Plotter(axes, 'time', lollipop=lollipop)
    p1.plot(t1, x1, **kwargs)

    if lollipop:
        t2 = np.arange(len(t2)) / len(t2) * len(t1)
    kwargs.pop('ylim')
    p1.axes.plot(t2, x2, color='orange', **kwargs)
    return axes.figure
    
def signal_plot3(t1, x1, t2, x2, t3, x3, **kwargs):    

    axes, kwargs = create_axes(3, **kwargs)

    signal_plot_func(t1, x1, axes=axes[0], **kwargs)
    signal_plot_func(t2, x2, axes=axes[1], **kwargs)
    signal_plot_func(t3, x3, axes=axes[2], **kwargs)
    return axes[0].figure    

def hist_plot(t, x, **kwargs):

    axes = hist_plot_func(t, x, **kwargs)
    return axes.figure
        
def signal_plot_with_hist(t, x, **kwargs):

    range = kwargs.pop('range', None)
    lollipop = kwargs.pop('lollipop', False)    
    
    axes, kwargs = create_axes(2, **kwargs)

    signal_plot_func(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    hist_plot_func(t, x, axes=axes[1], range=range, **kwargs)
    return axes[0].figure

def dtft_plot(f, X, **kwargs):

    axes = dtft_plot_func(f, X, **kwargs)
    return axes.figure

def signal_plot_with_dtft(t, x, f, X, **kwargs):

    axes, kwargs = create_axes(2, **kwargs)

    lollipop = kwargs.pop('lollipop', False)
    
    signal_plot_func(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    dtft_plot_func(f, X, axes=axes[1], **kwargs)
    return axes[0].figure

def dft_plot(f, X, **kwargs):
    axes = dft_plot_func(f, X, **kwargs)
    return axes.figure

def signal_plot_with_dft(t, x, f, X, **kwargs):

    axes, kwargs = create_axes(2, **kwargs)

    lollipop = kwargs.pop('lollipop', False)
    mode = kwargs.pop('mode', 'real-imag')    
    
    signal_plot_func(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    dft_plot_func(f, X, axes=axes[1], lollipop=lollipop, mode=mode, **kwargs)
    return axes[0].figure

def signal_plot_with_fourier_series(t, x, n, X, **kwargs):

    axes, kwargs = create_axes(2, **kwargs)

    lollipop = kwargs.pop('lollipop', False)
    
    signal_plot_func(t, x, axes=axes[0], lollipop=lollipop, **kwargs)
    fourier_series_plot_func(n, X, axes=axes[1], **kwargs)
    return axes[0].figure
