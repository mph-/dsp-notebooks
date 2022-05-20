from numpy import exp, sin, cos, sqrt, pi, angle


class FilterBase(object):

    def dc_response(self, t):

        H = self.frequency_response(0)
        return 0 * t + H.real

    def ac_response(self, t, omega):

        H = self.frequency_response(omega)

        phase = angle(H)
        mag = abs(H)

        return mag * cos(omega * t + phase)

    def frequency_response(self, omega):
        return self.transfer_function(1j * omega)

    def response(self, mode, t, omega):

        if mode == 'Step response':
            return t, self.step_response(t)
        elif mode == 'Impulse response':
            return t, self.impulse_response(t)
        elif mode == 'Frequency response':
            return omega, self.frequency_response(omega)
        elif mode == 'DC response':
            return t, self.dc_response(t)
        elif mode == 'AC response omega=1':
            return t, self.ac_response(t, 1)
        elif mode == 'AC response omega=10':
            return t, self.ac_response(t, 10)
        raise ValueError('Unknown mode=%s', mode)
