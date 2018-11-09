from lcapy import s, sympify, j

alpha1 = sympify('alpha_1')
omega1 = sympify('omega_1')

alpha2 = sympify('alpha_2')

s1a = alpha1 + j * omega1
s1b = alpha1 - j * omega1
s2 = alpha2

H = 1 / ((s - s1a) * (s - s1b) * (s - s2))

h = H.inverse_laplace()
