from numpy import exp, sin, cos, sqrt

class LeadCompensator1(FilterBase):

    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        self.poles = (-alpha, )
        self.zeros = (-beta, )

        if abs(beta) < abs(alpha):
            self.name = 'Lead compensator'
        else:
            self.name = 'Lag compensator'            

    def frequency_response(self, s):
        alpha = self.alpha
        beta = self.beta        
        return (s + beta) / (s + alpha) * (alpha / beta)

    def step_response(self, t):
        alpha = self.alpha
        return (alpha / beta + exp(alpha * t) - 1) * exp(-alpha * t) * (t >= 0)
    def impulse_response(self, t):
        return None
        
