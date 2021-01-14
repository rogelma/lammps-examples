#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

temperatures = np.arange(0.5, 0.9, 0.02)
densities = [0.175, 0.18, 0.185, 0.19, 0.2, 0.21, 0.215, 0.22]

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
