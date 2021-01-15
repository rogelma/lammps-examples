#!/bin/bash
LANG=en_US
TEMPERATURES=$(seq 0.50 0.005 0.90)
RHOS=$(seq 0.30 0.01 0.50)
OMP_NUM_THREADS=2

python potential_generate_points.py

for rho in $RHOS
do
	for temp in $TEMPERATURES
	do
		mpirun -np 4 lammps -var temp $temp -var rho $rho < in.csw
	done
done

rm log.lammps
rm force.table

python process_densities.py

bash ~/dotfiles/bin/bin/notify "Job finished on $HOSTNAME"

