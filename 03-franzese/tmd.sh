#!/bin/bash
LANG=en_US
TEMPERATURES=$(seq 0.50 0.02 0.90)
RHOS="0.175 0.180 0.185 0.190 0.200 0.210 0.215 0.220"
OMP_NUM_THREADS=2

python3 potential_generate_points.py

for rho in $RHOS
do
	for temp in $TEMPERATURES
	do
		mpirun -np 4 lammps -var temp $temp -var rho $rho < in.csw
	done
done

rm log.lammps
rm force.table

python3 process_densities.py