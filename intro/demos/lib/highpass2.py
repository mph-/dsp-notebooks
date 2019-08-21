from .filter_base import FilterBase
from numpy import exp, sin, cos, sqrt

class Highpass2Base(FilterBase):

    def __init__(self, zeta, omega0):
        self.zeta = zeta
        self.omega0 = omega0

    def transfer_function(self, s):

        zeta, omega0 = self.zeta, self.omega0
        return s**2 / (s**2 + 2 * zeta * omega0 * s + omega0**2)

class Highpass2UnderDamped(Highpass2Base):

    def __init__(self, zeta, omega0):
        if zeta >= 1.0:
            raise ValueError('System not under damped')
        super (Highpass2UnderDamped, self).__init__(zeta, omega0)
        
        p1a = -zeta * omega0 + 1j * omega0 * sqrt(1 - zeta**2)
        p1b = -zeta * omega0 - 1j * omega0 * sqrt(1 - zeta**2)
        self.poles = (p1a, p1b)
        self.zeros = (0, )

        self.alpha1 = zeta * omega0
        self.omega1 = omega0 * sqrt(1 - zeta**2)        
    
    def step_response(self, t):
        alpha1, omega1 = self.alpha1, self.omega1
        return -(alpha1 * sin(omega1 * t) - omega1 * cos(omega1 * t)) * exp(-alpha1 * t) * (t >= 0) / omega1

    def impulse_response(self, t):
        alpha1, omega1 = self.alpha1, self.omega1
        return None
        # return (omega1 * exp(alpha1 * t) * DiracDelta(t) - (2 * alpha1 * omega1 * cos(omega1 * t) + (-alpha1**2 + omega1**2) * sin(omega1 * t)) * (t >= 0)) * exp(-alpha1 * t) / omega1
    
class Highpass2CriticallyDamped(Highpass2Base):

    def __init__(self, zeta, omega0):
        if zeta != 1.0:
            raise ValueError('System not critically damped')
        super (Highpass2CriticallyDamped, self).__init__(zeta, omega0)

        p1a = -omega0
        self.poles = (p1a, p1a)
        self.zeros = (0, )        

        self.alpha1 = -p1a

    def step_response(self, t):
        alpha1 = self.alpha1
        return (-omega0 * t * exp(-omega0 * t) + exp(-omega0 * t)) * (t >= 0)

    def impulse_response(self, t):
        alpha1 = self.alpha1
        return None
        # return (omega0**2 * t * exp(-omega0 * t) - 2 * omega0 * exp(-omega0 * t)) * (t >= 0) + DiracDelta(t)
    
class Highpass2OverDamped(Highpass2Base):

    def __init__(self, zeta, omega0):
        if zeta <= 1.0:
            raise ValueError('System not over damped')
        super (Highpass2OverDamped, self).__init__(zeta, omega0)
        
        p1a = -zeta * omega0 + omega0 * sqrt(zeta**2 - 1)
        p1b = -zeta * omega0 - omega0 * sqrt(zeta**2 - 1)
        self.poles = (p1a, p1b)
        self.zeros = (0, )                

        self.alpha1 = -p1a
        self.alpha2 = -p1b        
    
    def step_response(self, t):
        alpha1, alpha2 = self.alpha1, self.alpha2
        return (alpha1 * exp(-alpha1 * t) / (alpha1 - alpha2) - alpha2 * exp(-alpha2 * t) / (alpha1 - alpha2)) * (t >= 0)

    def impulse_response(self, t):
        alpha1, alpha2 = self.alpha1, self.alpha2
        return None
        # (-alpha1**2 * exp(-alpha1 * t) / (alpha1 - alpha2) + alpha2**2 * exp(-alpha2 * t) / (alpha1 - alpha2)) * (t >= 0) + DiracDelta(t)

        
def Highpass2(zeta, omega0):
    if zeta > 1.0:
        return Highpass2OverDamped(zeta, omega0)
    elif zeta < 1.0:
        return Highpass2UnderDamped(zeta, omega0)
    else:
        return Highpass2CriticallyDamped(zeta, omega0)            
    

