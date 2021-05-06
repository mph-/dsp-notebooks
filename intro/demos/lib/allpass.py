from .filter_base import FilterBase
from numpy import exp, sin, cos, sqrt

class Allpass(FilterBase):

    def __init__(self):
        self.poles = ()
        self.zeros = ()

    def transfer_function(self, s):
        return s * 0 + 1

    def step_response(self, t):
        return (t >= 0)

    def impulse_response(self, t):
        raise ValueError('Have Dirac delta')
