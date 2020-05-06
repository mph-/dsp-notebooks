# M. P. Hayes UCECE

import numpy as np
from .utils import rect, sinc, gauss, tri

dtsignals = ['rect(t)', 'rect(t/2)', 'fang(t)',
           'tri(t)', 'tri(t/0.1)', 'tri(t/0.01)',
           'gauss(t)', 'gauss(t/0.1)', 'gauss(t/0.01)',
           'exp(-t) u(t)', 'u(t)']

class Dtsignal(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, t):
        name = self.name

        if name == 'gauss(t)':
            return gauss(t, 0, 1)
        elif name == 'gauss(t/0.1)':
            x = gauss(t / 0.1)    
            return x / max(x)
        elif name == 'gauss(t/0.01)':
            x = gauss(t / 0.01)    
            return x / max(x)    
        elif name == 'rect(t)':
            return rect(t)
        elif name == 'rect(t/2)':
            return rect(t / 2)
        elif name == 'tri(t)':
            return tri(t)
        elif name == 'tri(t/0.1)':
            return tri(t / 0.1)
        elif name == 'tri(t/0.01)':
            return tri(t / 0.01)            
        elif name == 'fang(t)':
            return t * rect(t - 0.5)
        elif name == 'exp(-t) u(t)':
            return np.exp(-t) * (t >= 0)
        elif name == 'u(t)':
            return 1 * (t >= 0)    
        raise ValueError('Unknown signal ' + name)
    
