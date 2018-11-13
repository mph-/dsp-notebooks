from lcapy import s, sympify, j, sqrt

#zeta = sympify('zeta_', real=True)
#omega0 = sympify('omega0', real=True)
#p1a = -zeta * omega0 + j * omega0 * sqrt(1 - zeta**2)
#p1b = -zeta * omega0 - j * omega0 * sqrt(1 - zeta**2)
#H = s * 2 * zeta * omega0 / ((s - p1a) * (s - p1b))

a1 = sympify('alpha_1')
o1 = sympify('omega_1')
H = s**2 / ((s + a1 + j * o1) * (s + a1 - j * o1))

G = H / s

g = G.partfrac().inverse_laplace(causal=True).simplify()
h = H.partfrac().inverse_laplace(causal=True).simplify()

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)').replace('/', ' / ')    
    return s

print(topy(g))

print(topy(h))
