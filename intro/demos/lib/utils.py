import numpy as np

def rect(t):
    """Rectangle function"""

    return (abs(t) <= 0.5) * 1

def tri(t):
    """Triangle function"""

    return (1 - abs(t)) * rect(t / 2)

def triangle_wave(t, period=1.0):
    """Triangle wave with symmetry of cosine"""

    t /= period
    cycles = np.round(t)
    y = t - cycles
    return 2 * (tri(2 * y) - 0.5)

def sinc(t):
    """Normalised cardinal sine function sin(pi t) / (pi t)"""
    return np.sinc(t)

def gauss(t, mu=0, sigma=1):
    """Gaussian function"""

    return np.exp(-0.5 * ((t - mu) / sigma)**2) / (np.sqrt(2 * np.pi) * sigma)

