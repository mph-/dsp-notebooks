from .filter_base import FilterBase
from numpy import exp, sin, cos, sqrt

class Bandstop2Base(FilterBase):

    def __init__(self, zeta, omega0):
        self.zeta = zeta
        self.omega0 = omega0

    def frequency_response(self, s):

        zeta, omega0 = self.zeta, self.omega0
        return (s**2 + omega0**2) / (s**2 + 2 * zeta * omega0 * s + omega0**2)

class Bandstop2UnderDamped(Bandstop2Base):

    def __init__(self, zeta, omega0):
        if zeta >= 1.0:
            raise ValueError('System not under damped')
        super (Bandstop2UnderDamped, self).__init__(zeta, omega0)
        
        p1a = -zeta * omega0 + 1j * omega0 * sqrt(1 - zeta**2)
        p1b = -zeta * omega0 - 1j * omega0 * sqrt(1 - zeta**2)
        self.poles = (p1a, p1b)
        self.zeros = (1j * omega0, -1j * omega0)

        self.alpha1 = zeta * omega0
        self.omega1 = omega0 * sqrt(1 - zeta**2)        
    
    def step_response(self, t):
        alpha1, omega1 = self.alpha1, self.omega1
        return (alpha1 * (alpha1 * omega1 * cos(omega1 * t) - (alpha1**2 + 2 * omega1**2) * sin(omega1 * t)) + omega1**3 * exp(alpha1 * t)) * exp(-alpha1 * t) * (t >= 0) / (omega1 * (alpha1**2 + omega1**2))

    def impulse_response(self, t):
        alpha1, omega1 = self.alpha1, self.omega1
        return (alpha1 * (alpha1 * sin(omega1 * t) - 2 * omega1 * cos(omega1 * t)) * (t >= 0) + omega1 * exp(alpha1 * t) * DiracDelta(t)) * exp(-alpha1 * t) / omega1

    
class Bandstop2CriticallyDamped(Bandstop2Base):

    def __init__(self, zeta, omega0):
        if zeta != 1.0:
            raise ValueError('System not critically damped')
        super (Bandstop2CriticallyDamped, self).__init__(zeta, omega0)

        p1a = -omega0
        self.poles = (p1a, p1a)
        self.zeros = (1j * omega0, -1j * omega0)        

        self.alpha1 = -p1a

    def step_response(self, t):
        alpha1 = self.alpha1
        return (t * (-omega0 + 2) * exp(-omega0 * t) + 1 - exp(-omega0 * t)) * (t >= 0)

    def impulse_response(self, t):
        alpha1 = self.alpha1
        return (t * (omega0**2 - 2 * omega0) * exp(-omega0 * t) + 2 * exp(-omega0 * t)) * (t >= 0)
    
class Bandstop2OverDamped(Bandstop2Base):

    def __init__(self, zeta, omega0):
        if zeta <= 1.0:
            raise ValueError('System not over damped')
        super (Bandstop2OverDamped, self).__init__(zeta, omega0)
        
        p1a = -zeta * omega0 + omega0 * sqrt(zeta**2 - 1)
        p1b = -zeta * omega0 - omega0 * sqrt(zeta**2 - 1)
        self.poles = (p1a, p1b)
        self.zeros = (1j * omega0, -1j * omega0)        

        self.alpha1 = -p1a
        self.alpha2 = -p1b        
    
    def step_response(self, t):
        alpha1, alpha2 = self.alpha1, self.alpha2
        return (1 - (alpha1 + alpha2) * exp(-alpha2 * t) / (alpha1 - alpha2) + (alpha1 + alpha2) * exp(-alpha1 * t) / (alpha1 - alpha2)) * (t >= 0)

    def impulse_response(self, t):
        alpha1, alpha2 = self.alpha1, self.alpha2
        return None
        #return (-(alpha1**2 + alpha1 * alpha2) * exp(-alpha1 * t) / (alpha1 - alpha2) + (alpha1 * alpha2 + alpha2**2) * exp(-alpha2 * t) / (alpha1 - alpha2)) * (t >= 0) + DiracDelta(t)

    
def Bandstop2(zeta, omega0):
    if zeta > 1.0:
        return Bandstop2OverDamped(zeta, omega0)
    elif zeta < 1.0:
        return Bandstop2UnderDamped(zeta, omega0)
    else:
        return Bandstop2CriticallyDamped(zeta, omega0)
