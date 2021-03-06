from lcapy import s, sympify, j

a1 = sympify('alpha')
b1 = sympify('beta_')
H = a1 * (s + b1) / (b1 * (s + a1))

G = H / s

g = G.partfrac().inverse_laplace(causal=True)
h = H.partfrac().inverse_laplace(causal=True)

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)')
    return s

print(topy(g))

print(topy(h))
