from sympy import symbols, lambdify, exp
import numpy as np

n_points = 1000
r = symbols('r', real=True)
#ur, delta, rr, a, ua, ra, deltaA = symbols('U_R Delta R_R a u_A, R_A, Delta_A')
#pot = pot = ur/(1+exp(delta*(r-rr)/a)) - ua*exp(-((r-ra)**2/(2*deltaA**2))) + (a/r)**(24)
pot = 2/(1+exp(15*(r-1.6))) - exp(-((r-2)**2)/(2*0.1)) + (1/r)**24 + 0.208876 -0.0673794*r
force = -pot.diff(r)

lamb_pot = lambdify(r, pot)
lamb_force = lambdify(r, force)

points = np.linspace(0.008, 3, n_points)
index = np.array(range(n_points))

f = open('force.table', 'w')

y1 = lamb_pot(points)
y2 = lamb_force(points)
f.write("AA\n")
f.write("N {} R 0.008 3.0\n\n".format(n_points))
for i in index:
    s = "{} {} {} {}\n".format(i+1, points[i], y1[i], y2[i])
    f.write(s)
f.write("\n")

f.close()
