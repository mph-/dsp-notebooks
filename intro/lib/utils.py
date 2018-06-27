from numpy import round

def rect(t):
    """Rectangle function"""

    return (abs(t) <= 0.5) * 1

def tri(t):
    """Triangle function"""

    return (1 - abs(t)) * rect(t / 2)

def triangle_wave(t, period=1.0):
    """Triangle wave with symmetry of cosine"""

    t /= period
    cycles = round(t)
    y = t - cycles
    return 2 * (tri(2 * y) - 0.5)

