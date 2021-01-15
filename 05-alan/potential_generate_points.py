from sympy import symbols, lambdify, exp
import numpy as np

n_points = 1000
r = symbols('r', real=True)
pot = 4*(r**(-12) - r**(-6)) + 5*exp(-(r-0.7)**2)
force = -pot.diff(r)

lamb_pot = lambdify(r, pot)
lamb_force = lambdify(r, force)

points = np.linspace(0.008, 5, n_points)
index = np.array(range(n_points))

f = open('force.table', 'w')

ua=1.0

y1 = lamb_pot(points)
y2 = lamb_force(points)
f.write("AA\n")
f.write("N {} R 0.008 5.0\n\n".format(n_points))
for i in index:
    s = "{} {} {} {}\n".format(i+1, points[i], y1[i], y2[i])
    f.write(s)
f.write("\n")

f.close()
