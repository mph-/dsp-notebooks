from lcapy import s, sympify, j

a1 = sympify('alpha_1')
a2 = sympify('alpha_2')
b1 = sympify('beta_1')
o1 = sympify('omega_1')

H = a2 * (a1**2 + o1**2) / ((s + a1 + j * o1) * (s + a1 - j * o1) * (s + a2))

H1 = H * (s + b1) / b1
G1 = H1 / s

g1 = G1.partfrac().inverse_laplace(causal=True).simplify()
h1 = H1.partfrac().inverse_laplace(causal=True).simplify()

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)').replace('/', ' / ')
    return s

print(topy(g1))

print(topy(h1))
