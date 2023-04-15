# LammpsANI
# This repository provides an example of lammps script for running trained ANI model
# The trained model parameters in "force-training-best.pt" by Torchani software
# The example provides the 1000 MD steps

# Requirements
1. Install https://github.com/gsjung0419/LammpsTorch
2. Install https://github.com/aiqm/torchani
3. MPI (MPICH or OPENMPI), with mpi4py


#Running single
python run.py

#Running mpi #2
mpirun -n 2 python run.py

#Example
1.Graphene

