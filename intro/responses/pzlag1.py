from lcapy import s, sympify, j

a = sympify('alpha')
tau = sympify('tau')

H = (s + 1 / tau) / (s + 1 / (a * tau)) / a

G = H / s

g = G.inverse_laplace(causal=True)
h = H.inverse_laplace(causal=True)

def topy(expr):

    s = str(expr)
    s = s.replace('**', '^').replace('_', '').replace('*', ' * ').replace('^', '**').replace('Heaviside(t)', '(t >= 0)').replace('/', ' / ')
    return s

print(topy(g))

print(topy(h))
