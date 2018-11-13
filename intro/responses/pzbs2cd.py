from lcapy import s, sympify, j, sqrt

zeta = sympify('zeta_', real=True)
omega0 = sympify('omega0', real=True)
p1a = -omega0
p1b = -omega0

H = (s*2 + omega0**2) / ((s - p1a) * (s - p1b))

G = H / s

#g = G.partfrac().inverse_laplace(causal=True).simplify()
#h = H.partfrac().inverse_laplace(causal=True).simplify()
g = G.inverse_laplace(causal=True)
h = H.inverse_laplace(causal=True)

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)').replace('/', ' / ')    
    return s

print(topy(g))

print(topy(h))
