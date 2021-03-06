from lcapy import s, sympify, j

a1 = sympify('alpha_1')
o1 = sympify('omega_1')
H = 2 * a1 * s / ((s + a1 + j * o1) * (s + a1 - j * o1))

G = H / s

g = G.partfrac().inverse_laplace(causal=True).simplify()
h = H.partfrac().inverse_laplace(causal=True).simplify()

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)').replace('/', ' / ')    
    return s

print(topy(g))

print(topy(h))
