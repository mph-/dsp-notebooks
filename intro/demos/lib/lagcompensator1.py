from .filter_base import FilterBase
from numpy import exp, sin, cos, sqrt

class LagCompensator1(FilterBase):

    def __init__(self, alpha, tau):
        self.alpha = alpha
        self.tau = tau
        self.poles = (-1 / (alpha * tau), )
        self.zeros = (-1 / tau, )

    def transfer_function(self, s):
        alpha, tau = self.alpha, self.tau
        return (s + 1 / tau) / (s + 1 / (alpha * tau)) / alpha

    def step_response(self, t):
        alpha, tau = self.alpha, self.tau
        return (1 - (alpha - 1) * exp(-t / (alpha * tau)) / alpha) * (t >= 0)

    def impulse_response(self, t):
        return None
        # DiracDelta(t) / alpha + (alpha - 1) * exp(-t / (alpha * tau)) * (t >= 0) / (alpha**2 * tau)


