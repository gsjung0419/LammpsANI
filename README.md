# LMPANI

Reference: Gang Seob Jung, Hunjoo Myung, and Stephan Irle. "Artificial Neural Network Potentials for Mechanics and Fracture Dynamics of Two-Dimensional Crystals." Machine Learning: Science and Technology (2023)

0. Intro

 -. Python script and lammps input for running trained ANI model

 -. The trained model parameters in "force-training-best.pt" by Torchani software

 -. The example provides the 1000 MD steps

1. Requirements

 -. Install https://github.com/gsjung0419/LMPTorch
 
 -. For the current legacy workflow, install https://github.com/gsjung0419/torchani_gs branch `v`
 
 -. MPI (MPICH or OPENMPI), with mpi4py

2. Running 

 -. python run.py

 -. mpirun -n 2 python run.py (#CPU=2)


3. Current LAMMPS 2025 status

Current repository folder: `LMPANI`.

This example was smoke-tested with the shared LAMMPS stack documented in:

```text
/Users/gsjung/ModelingAgent/lmp_packages/installation.md
```

Validated local stack:

```text
LAMMPS: 22 Jul 2025
LAMMPS packages: DFTBP, COLVARS, PYTHON, KSPACE, MOLECULE,
                 EXTRA-FIX, EXTRA-MOLECULE, EXTRA-PAIR
LMPTorch: gsjung0419/LMPTorch commit 760037a
TorchANI: gsjung0419/torchani_gs branch v, installed as 2.2.0+gs0
Python: lammps 2025.7.22, mpi4py 4.1.1, torch 2.11.0
```

The current `model.py` and `animpi.py` use legacy TorchANI APIs such as
`torchani.neurochem.Constants` and `nn._atomic_energies`. Official TorchANI
2.7/2.8 does not provide the same legacy API surface, so use `torchani_gs@v`
for this workflow until the model/callback code is ported.

Install the tested TorchANI fork:

```bash
pip install "git+ssh://git@github.com/gsjung0419/torchani_gs.git@v"
```

Short LAMMPS smoke test used locally:

```lammps
read_data Benchmark_Size/10nm_10nm.data
thermo 1
run 1
```

The reduced `run 1` test completed with both 1 MPI rank and 4 MPI ranks. The
4-rank command used the LAMMPS MPI launcher from the `lmp` environment:

```bash
export PYTHONPATH=/path/to/LMPANI
export KMP_DUPLICATE_LIB_OK=TRUE
export OMP_NUM_THREADS=1

mpirun -np 4 lmp -in input.in
```

On Linux, avoid `KMP_DUPLICATE_LIB_OK` unless a duplicate OpenMP runtime issue
is actually observed. Prefer a consistent compiler/MPI/OpenMP stack.

Please report any bug/commetns to jungg@ornl.gov or gs4phone@gmail.com
