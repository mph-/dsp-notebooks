from numpy import exp, sin, cos, sqrt

class FilterBase(object):

    def ac_response(self, t, omega):

        H = self.frequency_response(omega)

        phase = np.angle(H)
        mag = abs(H)

        return mag * cos(omega * t + phase)
    
        

        
        
