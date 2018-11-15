from numpy import exp, sin, cos, sqrt
from .filter_base import FilterBase


class P3Z1(FilterBase):

    def __init__(self, alpha1, omega1, alpha2, beta1):
        self.params = (alpha1, omega1, alpha2, beta1)
        p1a = -alpha1 - 1j * omega1
        p1b = -alpha1 + 1j * omega1
        p2 = -alpha2
        z1 = -beta1        
        self.poles = (p1a, p1b, p2)
        self.zeros = (z1, )

    def frequency_response(self, s):
        alpha1, alpha2, omega1, beta1 = self.params
        p1a, p1b, p2 = self.poles
        z1, = self.zeros
        return -p2 * -p1a * -p1b * (s - z1) / ((s - p1a) * (s - p1b) * (s - p2)) / beta1

    def step_response(self, t):
        alpha1, alpha2, omega1, beta1 = self.params        
        return ((alpha2 * (-omega1 * ((2 * alpha1 - alpha2) * (alpha1**3 - alpha1**2 * beta1 + alpha1 * omega1**2 - beta1 * omega1**2) + (alpha1**2 + omega1**2) * (-alpha1**2 + alpha1 * alpha2 + omega1**2)) * cos(omega1 * t) + (-omega1**2 * (2 * alpha1 - alpha2) * (alpha1**2 + omega1**2) + (-alpha1**2 + alpha1 * alpha2 + omega1**2) * (alpha1**3 - alpha1**2 * beta1 + alpha1 * omega1**2 - beta1 * omega1**2)) * sin(omega1 * t)) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * exp(alpha2 * t) + beta1 * omega1 * (omega1**2 * (2 * alpha1 - alpha2)**2 + (-alpha1**2 + alpha1 * alpha2 + omega1**2)**2) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * exp(t * (alpha1 + alpha2)) + omega1 * (omega1**2 * (2 * alpha1 - alpha2)**2 + (-alpha1**2 + alpha1 * alpha2 + omega1**2)**2) * (alpha1**2 * alpha2 - alpha1**2 * beta1 + alpha2 * omega1**2 - beta1 * omega1**2) * exp(alpha1 * t)) * exp(-t * (alpha1 + alpha2)) * (t >= 0) / (beta1 * omega1 * (omega1**2 * (2 * alpha1 - alpha2)**2 + (-alpha1**2 + alpha1 * alpha2 + omega1**2)**2) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2))) * (t >= 0)

    def impulse_response(self, t):
        alpha1, alpha2, omega1, beta1 = self.params                
        return alpha2 * (-omega1 * (omega1**2 + (alpha1 - alpha2)**2)**2 * (alpha1**2 * alpha2 - alpha1**2 * beta1 + alpha2 * omega1**2 - beta1 * omega1**2) * exp(2 * alpha1 * t) - omega1 * (omega1**2 + (alpha1 - alpha2)**2) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * (-alpha1**3 + alpha1**2 * beta1 - alpha1 * omega1**2 + beta1 * omega1**2 + (alpha1 - alpha2) * (alpha1**2 + omega1**2)) * exp(t * (alpha1 + alpha2)) * cos(omega1 * t) + (omega1**2 + (alpha1 - alpha2)**2) * (omega1**2 * (alpha1**2 + omega1**2) + (alpha1 - alpha2) * (alpha1**3 - alpha1**2 * beta1 + alpha1 * omega1**2 - beta1 * omega1**2)) * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2) * exp(t * (alpha1 + alpha2)) * sin(omega1 * t)) * exp(-t * (2 * alpha1 + alpha2)) * (t >= 0) / (beta1 * omega1 * (omega1**2 + (alpha1 - alpha2)**2)**2 * (alpha1**2 - 2 * alpha1 * alpha2 + alpha2**2 + omega1**2)) * (t >= 0)        
        return False
        # (z - p) * exp(z * t) * (t >= 0) + DiracDelta(t)
        
