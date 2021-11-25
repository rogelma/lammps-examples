# Calculate changes in the temperature of maximum density

import numpy as np
from scipy.optimize import curve_fit, minimize

from data_extract import get_concentrations, get_pressures, get_temperatures, get_average

concentrations = get_concentrations()
pressures = ['0.003', '0.004', '0.005', '0.010', '0.015', '0.020']

def poly(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

for p in pressures:
    tmds = np.zeros_like(concentrations, dtype = 'float64')
    tmds_dev = np.zeros_like(concentrations, dtype = 'float64')
    for idx, x in enumerate(concentrations):
        temperatures = get_temperatures(x, p)
        temperatures_float = np.array(temperatures, dtype = 'float64')

        volume_mean = np.zeros_like(temperatures, dtype = 'float64')
        volume_dev = np.zeros_like(temperatures, dtype = 'float64')
        for idt, temp in enumerate(temperatures):
            volume_mean[idt], volume_dev[idt] = get_average(x, p, temp, 'volume')

        # Fit
        pars, cov = curve_fit(f = poly, xdata = temperatures_float, ydata = volume_mean, p0=[1, 1, 1, 1], bounds=(-np.inf, np.inf))

        a, b, c, d = pars
        t_min = np.min(temperatures_float)
        t_max = np.max(temperatures_float)
        t_tmd = minimize(poly, args=(a, b, c, d), x0 = 0.4, bounds = [[t_min, t_max]])['x'][0]
        p_tmd = poly(t_tmd, a, b, c, d)

        if (t_tmd > t_min) and (t_tmd < t_max):
            tmds[idx] = t_tmd
        else:
            tmds[idx] = -1

        # Fit error
        pars, cov = curve_fit(f = poly, xdata = temperatures_float, ydata = volume_mean + 5*volume_dev, p0=[1, 1, 1, 1], bounds=(-np.inf, np.inf))

        a, b, c, d = pars
        t_min = np.min(temperatures_float)
        t_max = np.max(temperatures_float)
        t_tmd = minimize(poly, args=(a, b, c, d), x0 = 0.4, bounds = [[t_min, t_max]])['x'][0]
        p_tmd = poly(t_tmd, a, b, c, d)

        if (t_tmd > t_min) and (t_tmd < t_max):
            tmds_dev[idx] = np.abs(tmds[idx] - t_tmd)
        else:
            tmds_dev[idx] = -1

    dtmds = tmds - tmds[0]
    dtmds_dev = tmds_dev - tmds_dev[0]

    concentrations_float = np.array(concentrations, dtype = 'float64')
    np.savetxt('results/tmds/dTMD_p{}.dat'.format(p), np.transpose([concentrations_float[tmds>0], dtmds[tmds>0], dtmds_dev[tmds>0]]))
    np.savetxt('results/tmds/TMD_p{}.dat'.format(p), np.transpose([concentrations_float[tmds>0], tmds[tmds>0], tmds_dev[tmds>0]]))
