from numpy import exp, sin, cos, sqrt, pi

class FilterBase(object):

    def ac_response(self, t, omega):

        H = self.frequency_response(omega)

        phase = np.angle(H)
        mag = abs(H)

        return mag * cos(omega * t + phase)

    def response(self, mode, t, omega):

        if mode == 'Step response':
            return t, self.step_response(t)
        elif mode == 'Impulse response':
            return t, self.impulse_response(t)
        elif mode == 'Frequency response':
            return omega, self.frequency_response(omega * 2 * pi)
        raise ValueError('Unknown mode=%s', mode)                
