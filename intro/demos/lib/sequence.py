import numpy as np

class Sequence(list):

    def init_from_string(self, string):
        
        s = string.strip()
        if s == '':
            return [], 0

        # Be generous with the sequence formatting.
        if s.startswith('{'):
            s = s[1:]
        if s.endswith('}'):
            s = s[:-1]

        parts = s.split(',')

        count = s.count('_')
        if count > 1:
            raise ValueError('More than one _ in %s' % sequence)

        vals = []
        origin = 0
        for m, elt in enumerate(parts):
            elt = elt.strip()
            if elt == '':
                vals.append(0)
            else:
                if elt[0] == '_':
                    origin = m
                    elt = elt[1:]
                vals.append(float(elt))
            
        return vals, origin
    
    def __init__(self, arg):

        origin = 0
        if isinstance(arg, str):
            arg, origin = self.init_from_string(arg)

        super (Sequence, self).__init__(arg)
        self.origin = origin

        self.n = np.arange(len(self)) - self.origin


    def __call__(self, n):

        if isinstance(n, (np.ndarray, list, tuple)):
            vals = [self(n1) for n1 in list(n)]
            if isinstance(n, np.ndarray):
                return np.array(vals)
            return vals
        
        if n not in self.n:
            return 0
        m = list(self.n).index(n)
        return self[m]
    
