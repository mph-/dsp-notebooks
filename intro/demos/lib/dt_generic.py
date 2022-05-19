from .dt_filter_base import DTFilterBase
from scipy.signal import butter, dlti
from numpy import exp, sin, cos, sqrt
from .dt_filter_base import response_modes


class DTGeneric(DTFilterBase):

    def __init__(self, a, b, fs):

        dt = 1 / fs

        self.a = a
        self.b = b
        self.dt = dt

        self.tf = dlti(self.b, self.a, dt=dt)
