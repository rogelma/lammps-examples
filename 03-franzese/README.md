# Franzese potential

This code finds the temperature of maximum density (TMD) for the [potential proposed by Franzese](https://doi.org/10.1016/j.molliq.2007.08.021) and [Alan](https://doi.org/10.1063/1.2830706). By default, it calculates the reduced density X reduced temperature curves for fixed reduced pressures 0.20, 0.25, 0.30.

To run this simulation, [LAMMPS](https://lammps.sandia.gov/) is required. Potential generation and average calculation are performed using [Sympy](https://www.sympy.org/) and [Numpy](https://numpy.org/).

Run with
```
bash tmd.sh
```
