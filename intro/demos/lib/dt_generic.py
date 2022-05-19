from .dt_filter_base import DTFilterBase
from scipy.signal import butter, dlti
from numpy import exp, sin, cos, sqrt, trim_zeros
from .dt_filter_base import response_modes


class DTGeneric(DTFilterBase):

    def __init__(self, b, a, fs):

        dt = 1 / fs

        self.a = a
        self.b = b
        self.dt = dt

        # Remove trailing zeros otherwise get additional poles/zeros
        a = trim_zeros(a, 'b')
        b = trim_zeros(b, 'b')

        self.tf = dlti(b, a, dt=dt)
