import numpy as np

def noise_asd(An, f):
    """Calculate Gaussian noise with a one-sided amplitude spectral
    density described by An at the evenly spaced frequencies given by f."""    

    fmax = f[-1]
    N = (len(An) - 1) * 2
    # Zero mean, unit variance Gaussian random vector.
    x = np.random.randn(N)
    # Could avoid the FFT since the FFT of Gaussian noise is also Gaussian.
    X = np.fft.rfft(x) * np.sqrt(fmax)
    Y = X * An
    y = np.fft.irfft(Y)
    return y


def noise_psd(Sn, f):
    """Calculate Gaussian noise with a one-sided power spectral
    density described by Sn at the evenly spaced frequencies given by f."""

    return noise_asd(np.sqrt(Sn), f)


class FlickerNoise(object):

    def __init__(self, N, fs, alpha=None, eta=None, gamma=None,
                 over=16, fc=None, N0=None, beta=None, verbose=False):
        """Gaussian 1/f noise having a one-sided power spectral density

        The one-sided PSD is given by:

        S = alpha**2 / f**beta + N0

        where N0 = gamma**2 is the PSD of the white-noise.

        eta = beta / 2 is the exponent for the ASD

        The corner frequency occurs at
        fc = (alpha / gamma)**(1 / eta)

        If alpha=0 white noise is produced with a variance
        sigma**2 = gamma**2 * fs / 2.

        The signal is truncated from a signal many times the desired
        length to reduce the periodicity effects imposed by a DFT.
        This is controlled by the parameter over.

        The expected value of a sample is 0.

        Note, if desire white noise need to make fc small but do
        not make beta=0 otherwise get 2 * N_0

        """

        if gamma is None and N0 is None:
            raise ValueError('Must specify N0 or gamma')
        if gamma is None:
            gamma = np.sqrt(N0)
        
        if eta is None and beta is None:
            raise ValueError('Must specify eta or beta')
        if beta is None:
            beta = eta * 2
        eta = beta / 2

        if fc is None and alpha is None:
            raise ValueError('Must specify alpha or fc')
        if alpha is None:
            alpha = gamma * fc ** eta
        else:
            fc = (alpha / gamma) ** (1.0 / eta)

        N0 = gamma**2
        self.N0 = N0
            
        if verbose:
            print('beta=%.2f, N_0=%.2f nV^2/Hz, f_c=%.1f Hz' % (beta, N0 * 1e18, fc))
            print('eta=%.2f, gamma=%.2f nV/rtHz, alpha=%.2e' % (eta, gamma * 1e9, alpha))            
        
        self.N = N
        self.fs = fs
        self.f = np.arange(N // 2 + 1) / N * fs
        self._f = np.arange(N * over // 2 + 1) / (N * over) * fs        
        self.alpha = alpha
        self.eta = eta
        self.beta = beta        
        self.gamma = gamma
        self.fc = fc

        self.Sn = alpha**2 * (abs(self.f) + 1e-20)**(-beta) + gamma**2
        self.Sn[0] = self.Sn[1]        
        # This needs to be infinite..., let the user beware when plotting.
        #self.Sn[0] = self.Sn[1] * 10

        self._Sn = alpha**2 * (abs(self._f) + 1e-20)**(-beta) + gamma**2
        # This needs to be infinite so zero is good enough!  Moreover,
        # since the input noise is zero mean, the generated noise is
        # zero mean whatever this value.  Note, the time-average of a
        # sequence may not be zero.
        self._Sn[0] = self._Sn[1]

    def psd(self):
        return self.Sn

    def asd(self):
        return np.sqrt(self.psd())

    def realisation(self):
        return noise_psd(self._Sn, self._f)[0:self.N]

    def realisation_all(self):
        return noise_psd(self._Sn, self._f)
