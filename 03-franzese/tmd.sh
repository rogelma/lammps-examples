#!/bin/bash
LANG=en_US
TEMPERATURES=$(seq 0.30 0.005 1.00)
PRESSURES="0.20 0.25 0.30"

python potential_generate_points.py

for press in $PRESSURES
do
	for temp in $TEMPERATURES
	do
		mpirun -np 4 lammps -var temp $temp -var press $press < in.csw
	done
done

# Calculate averages
python process_data.py

# Generate plot
gnuplot RHOxT.gnupot
