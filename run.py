#Generated by GS JUNG@ORNL. jungg@ornl.gov gs4phone@gmail.com

import os
from lammps import lammps
import torch
import torchani

#os.system("rm geo*.xyz ss*.dat sd.dat")
lmp=lammps()
lmp.file("md.in")

