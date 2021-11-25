#!/usr/bin/python3

import numpy as np

from data_extract import get_concentrations, get_pressures, get_temperatures, get_average

concentrations = get_concentrations()

for x in concentrations:
    pressures = get_pressures(x)
    for idp, p in enumerate(pressures):
        temperatures = get_temperatures(x, p)
        temperatures_float = np.array(temperatures, dtype = 'float64')
        
        volume_mean = np.zeros_like(temperatures, dtype = 'float64')
        volume_dev = np.zeros_like(temperatures, dtype = 'float64')

        for idt, temp in enumerate(temperatures):
            volume_mean[idt], volume_dev[idt] = get_average(x, p, temp, 'volume')

        np.savetxt('results/phase_diagram/VxT_x{}_p{}.dat'.format(x, p), np.transpose([temperatures_float, volume_mean, volume_dev]))
