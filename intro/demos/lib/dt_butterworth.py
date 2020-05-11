from .dt_filter_base import DTFilterBase
from scipy.signal import butter, dlti
from numpy import exp, sin, cos, sqrt
from .dt_filter_base import response_modes

btypes = ['Low-pass', 'High-pass', 'Band-pass', 'Band-stop']

class DTButterworth(DTFilterBase):

    def __init__(self, fs=1, fb=None, btype='low', order=1):

        dt = 1 / fs

        if fb is None:
            fb = 0.25 / dt

        btype = {'Low-pass':'lowpass', 'High-pass':'highpass',
                 'Band-pass':'bandpass', 'Band-stop':'bandstop'}[btype]
        self.dt = dt
        self.fb = fb
        self.order = order
        self.btype = btype

        self.b, self.a = butter(order, 2 * fb * dt, btype)
        
        self.tf = dlti(self.b, self.a, dt=dt)
