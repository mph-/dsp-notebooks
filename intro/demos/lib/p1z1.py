from numpy import exp, sin, cos, sqrt
from .filter_base import FilterBase


class P1Z1(FilterBase):

    def __init__(self, z, p):
        self.z = z
        self.p = p
        self.poles = (p, )
        self.zeros = (z, )

        self.title = 'Lag-compensator with gain'
        if abs(z) > abs(p):
            self.title = 'Lead-compensator'
        elif abs(z) == abs(p):
            self.title = 'All-pass'

    def frequency_response(self, s):
        z, p = self.z, self.p
        
        return (s - p) / (s - z)

    def step_response(self, t):
        z, p = self.z, self.p
        return (p / z - (p - z) * exp(z * t) / z) * (t >= 0)

    def impulse_response(self, t):
        return None
        # (z - p) * exp(z * t) * (t >= 0) + DiracDelta(t)
        
