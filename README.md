# LammpsANI

Reference: Jung, Gang Seob, Hoon Joo Myung, and Stephan Irle. "Artificial Neural Network Potentials for Mechanics and Fracture Dynamics of Two-Dimensional Crystals." Machine Learning: Science and Technology (2023)

0. Intro

 -. Python script and lammps input for running trained ANI model

 -. The trained model parameters in "force-training-best.pt" by Torchani software

 -. The example provides the 1000 MD steps

1. Requirements

 -. Install https://github.com/gsjung0419/LammpsTorch
 
 -. Install https://github.com/aiqm/torchani
 
 -. MPI (MPICH or OPENMPI), with mpi4py

2. Running 

 -. python run.py

 -. mpirun -n 2 python run.py (#CPU=2)


Please report any bug/commetns to jungg@ornl.gov or gs4phone@gmail.com
