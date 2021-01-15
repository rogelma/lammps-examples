#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, minimize

temperatures = np.arange(0.50, 0.90, 0.005)
densities = np.arange(0.30, 0.451, 0.01)

def poly(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

fig, ax = plt.subplots()
ax.set_xlabel('$T^{*}$')
ax.set_ylabel('$P^{*}$')

tmds = []
tmds_pressures = []
for rho in densities:
    #processed_values = open('PxT_rho_{0:.3f}.dat'.format(rho), 'w')
    pressures = []
    for temp in temperatures:
        log = np.loadtxt('log/rho/{0:.2f}/temp_{1:.3f}.profile'.format(rho, temp))
        #s = "{}\t{}\n".format(temp, np.average(log[:, 1]))
        #processed_values.write(s)
        pressures.append(np.average(log[:, 1]))

    #processed_values.close()
    ax.plot(temperatures, pressures, label = 'rho = {0:.2f}'.format(rho))

    pars, cov = curve_fit(f=poly, xdata=temperatures, ydata=pressures, p0=[1, 1, 1, 1], bounds=(-np.inf, np.inf))
    ## Plot fitted density curve
    #ax.plot(temperatures, poly(temperatures, *pars), linestyle='--', linewidth=2, color='black')

    # Find pressure minima
    a, b, c, d = pars
    t_min = minimize(poly, args=(a, b, c, d), x0 = 0.7, bounds = [[0.5, 0.90]])['x'][0]
    p_min = poly(t_min, a, b, c, d)
    
    # Ignore if minima is the range start
    if (t_min != 0.5):
        tmds.append(t_min)
        tmds_pressures.append(p_min)

# Plot TMD's
ax.plot(tmds, tmds_pressures, color='black')

plt.legend(loc='best', frameon=False)
fig.savefig('PxT.png')

