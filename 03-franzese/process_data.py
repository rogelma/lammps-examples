#!/usr/bin/python

import numpy as np

# Read LAMMPS output logs
# Calculates the average density for each temperature

temperatures = np.arange(0.30, 1.0, 0.005).round(3)
pressures = [0.20, 0.25, 0.30]

for press in pressures:
    processed_values = open('RHOxT_press_{0:.2f}.dat'.format(press), 'w')
    for temp in temperatures:
        log = np.loadtxt('log/lammps_press_{0:.2f}_temp_{1:.3f}.log'.format(press, temp), skiprows = 119, max_rows=10)
        s = "{}\t{}\n".format(temp, np.average(log[:, 3]))
        processed_values.write(s)
    processed_values.close()
