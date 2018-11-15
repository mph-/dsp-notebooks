from .filter_base import FilterBase
from numpy import exp, sin, cos, sqrt

class Highpass1(FilterBase):

    def __init__(self, alpha):
        self.alpha = alpha
        self.poles = (-alpha, )
        self.zeros = (0, )        

    def frequency_response(self, s):
        alpha = self.alpha
        return s / (s + alpha)

    def step_response(self, t):
        alpha = self.alpha
        return exp(-alpha * t) * (t >= 0)

    def impulse_response(self, t):
        return False
        #return -alpha * exp(-alpha * t) * (t >= 0) + DiracDelta(t)
        
