from lcapy import s, sympify, j, sqrt

a1 = sympify('alpha_1', real=True)
a2 = sympify('alpha_2', real=True)

H = a1 * a2 / ((s + a1) * (s + a2))

G = H / s

g = G.partfrac().inverse_laplace(causal=True)
h = H.partfrac().inverse_laplace(causal=True)

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)').replace('/', ' / ')    
    return s

print(topy(g))

print(topy(h))
