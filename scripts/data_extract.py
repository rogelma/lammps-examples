# Reads data from LAMMPS output files

import re
import numpy as np
from glob import glob
from scipy import stats

# Map quantity name to column in LAMMPS output file
column_map = {
    'volume': 3,
}

def extract_last_number_from_string(str):
    numbers = re.findall("\d+\.\d+", str)
    return numbers[-1]

def get_concentrations():
    folders = glob('log/concentrations/*')
    concentrations = [extract_last_number_from_string(str) for str in folders]
    sorted_concentrations = sorted(concentrations, key=float)
    return sorted_concentrations

def get_pressures(x):
    folders = glob('log/concentrations/{}/p/*'.format(x))
    pressures = [extract_last_number_from_string(str) for str in folders]
    sorted_pressures = sorted(pressures, key=float)
    return sorted_pressures

def get_temperatures(x, p):
    folders = glob('log/concentrations/{}/p/{}/temp/*'.format(x, p))
    temperatures = [extract_last_number_from_string(str) for str in folders]
    sorted_temperatures = sorted(temperatures, key=float)
    return sorted_temperatures

def get_average(x, p, t, key):
    filename = 'log/concentrations/{}/p/{}/temp/{}/averages.dat'.format(x, p, t)
    print(filename)
    log = np.loadtxt(filename)
    lammps_output_array = log[:, column_map[key]]
    mean = np.average(lammps_output_array)
    dev = stats.sem(lammps_output_array)
    return mean, dev