from .filter_base import FilterBase
from numpy import exp, sin, cos, sqrt

class LeadCompensator1(FilterBase):

    def __init__(self, alpha, tau):
        self.alpha = alpha
        self.tau = tau
        self.poles = (-1 / tau, )
        self.zeros = (-1 / (alpha * tau), )

    def transfer_function(self, s):
        alpha, tau = self.alpha, self.tau
        return (s + 1 / (alpha * tau)) / (s + 1 / tau)

    def step_response(self, t):
        alpha, tau = self.alpha, self.tau
        return ((alpha - 1) * exp(-t / tau) / alpha + 1 / alpha) * (t >= 0)

    def impulse_response(self, t):
        return None
        # DiracDelta(t) + (-alpha + 1) * exp(-t / tau) * (t >= 0) / (alpha * tau)


