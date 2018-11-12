from lcapy import s, sympify, j, sqrt

zeta = sympify('zeta_', real=True)
omega0 = sympify('omega0', real=True)
p1a = -zeta * omega0 + j * omega0 * sqrt(1 - zeta**2)
p1b = -zeta * omega0 - j * omega0 * sqrt(1 - zeta**2)

H = p1a * p1b / ((s - p1a) * (s - p1b))

G = H / s

g = G.partfrac().inverse_laplace(causal=True).simplify()
h = H.partfrac().inverse_laplace(causal=True).simplify()

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)').replace('/', ' / ')    
    return s

print(topy(g))

print(topy(h))
