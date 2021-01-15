#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

temperatures = np.arange(0.15, 0.4, 0.05)
densities = [0.100, 0.105, 0.110, 0.115, 0.120, 0.125, 0.130, 0.134, 0.140, 0.144]

fig, ax = plt.subplots()
ax.set_xlabel('$T^{*}$')
ax.set_ylabel('$P^{*}$')

for rho in densities:
    # processed_values = open('PxT_rho_{0:.2f}.dat'.format(rho), 'w')
    pressures = []
    for temp in temperatures:
        log = np.loadtxt('log/rho/{0:.3f}/temp_{1:.2f}.profile'.format(rho, temp))
        # s = "{}\t{}\n".format(temp, np.average(log[:, 1]))
        # processed_values.write(s)
        pressures.append(np.average(log[:, 1]))
    # processed_values.close()
    ax.plot(temperatures, pressures, label = 'rho = {0:.3f}'.format(rho))

plt.legend(loc='best', frameon=False)
fig.savefig('PxT.png')
