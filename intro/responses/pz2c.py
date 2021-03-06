from lcapy import s, sympify, j

a1 = sympify('alpha_1')
b1 = sympify('beta_1')
o1 = sympify('omega_1')
H = (a1**2 + o1**2) * (s + b1) / ((s + a1 + j * o1) * (s + a1 - j * o1)) / b1

G = H / s

g = G.partfrac().inverse_laplace(causal=True).simplify()
h = H.partfrac().inverse_laplace(causal=True).simplify()

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)').replace('/', ' / ')        
    return s

print(topy(g))

print(topy(h))
