from numpy import exp, sin, cos, sqrt

class Lowpass1(object):

    def __init__(self, alpha):
        self.alpha = alpha
        self.poles = (-alpha, )
        self.zeros = ()

    def frequency_response(self, s):
        alpha = self.alpha
        return alpha / (s + alpha)

    def step_response(self, t):
        alpha = self.alpha        
        return (1 - exp(-alpha * t)) * (t >= 0)

    def impulse_response(self, t):
        alpha = self.alpha                
        return alpha * exp(-alpha * t) * (t >= 0)
        
