#!/bin/bash
#PBS -S /bin/bash
#PBS -l nodes=2:ppn=8
#PBS -N Cooperative Max-P
#PBS -o out
#PBS -e err
#PBS -A Jay
#PBS -l walltime=10:00:00
export OMP_NUM_THREADS=4
use openmpi-1.8.1
cd $PBS_O_WORKDIR
/packages/openmpi-1.8.1/bin/mpirun --map-by node -n 2 python hybrid_ifs.py
