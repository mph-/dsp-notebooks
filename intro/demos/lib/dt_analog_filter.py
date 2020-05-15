from .dt_filter_base import DTFilterBase
from scipy.signal import butter, bessel, cheby1, cheby2, ellip, dlti
from numpy import exp, sin, cos, sqrt
from .dt_filter_base import response_modes

btypes = ['Low-pass', 'High-pass', 'Band-pass', 'Band-stop']
ftypes = ['Butterworth', 'Bessel', 'Chebyshev I', 'Chebyshev II', 'Elliptical']

class DTAnalogFilter(DTFilterBase):

    def __init__(self, fs=1, fb=None, ftype='Butterworth',
                 btype='low', order=1, rp=3, rs=40):
        """Passband ripple rp and stopband ripple rs in dB.
        These parameters are not used for all filters."""

        dt = 1 / fs

        if fb is None:
            fb = 0.25 / dt

        btype = {'Low-pass':'lowpass', 'High-pass':'highpass',
                 'Band-pass':'bandpass', 'Band-stop':'bandstop'}[btype]
        self.dt = dt
        self.fb = fb
        self.order = order
        self.btype = btype

        if ftype == 'Butterworth':
            self.b, self.a = butter(order, 2 * fb * dt, btype)
        elif ftype == 'Bessel':
            self.b, self.a = bessel(order, 2 * fb * dt, btype)
        elif ftype == 'Chebyshev I':
            self.b, self.a = cheby1(order, rp, 2 * fb * dt, btype)
        elif ftype == 'Chebyshev II':
            self.b, self.a = cheby2(order, rs, 2 * fb * dt, btype)
        elif ftype == 'Elliptical':
            self.b, self.a = ellip(order, rp, rs, 2 * fb * dt, btype)
        else:
            raise ValueError('Unknown filter ' + ftype)
        
        self.tf = dlti(self.b, self.a, dt=dt)
