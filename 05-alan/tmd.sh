#!/bin/bash
LANG=en_US
TEMPERATURES=$(seq 0.15 0.05 0.50)
RHOS="0.100 0.103 0.105 0.107 0.110 0.113 0.115 0.117 0.120 0.123 0.125 0.127 0.130 0.132 0.134 0.136 0.138 0.140 0.142 0.144"
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
