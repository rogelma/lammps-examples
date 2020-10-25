from sympy import symbols, lambdify, exp
import numpy as np

n_points = 1000
a, b, c, w, r = symbols('a b c w r', real=True)

#pot = 1/exp((r-b)/w) + a/(1+exp((r-c)/w))
#pot = 4*(pow(1/r, 12)- pow(1/r, 6))
pot = 2/(1+exp(15*(r-1.6))) - exp(-((r-2)**2/(2*0.1))) + (1/r)**(24) + (0.208876) + (-0.0673794)*r
der_pot = -pot.diff(r)

lamb_pot = lambdify(r, pot)
lamb_der_pot = lambdify(r, der_pot)

points = np.linspace(0.008, 3, n_points)
index = np.array(range(n_points))

f = open('force.table', 'w')

y1 = lamb_pot(points)
y2 = lamb_der_pot(points)
f.write("AA\n")
f.write("N {} R 0.008 3.0\n\n".format(n_points))
for i in index:
    s = "{} {} {} {}\n".format(i+1, points[i], y1[i], y2[i])
    f.write(s)
f.write("\n")

f.close()
