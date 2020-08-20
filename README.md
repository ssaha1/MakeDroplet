**MakeDroplet** is a Python package for converting a protein in bulk water structure into a protein in water droplet structure. 
It reads a .pdb file from GROMACS MD simulation output, define the radius of gyration of the protein and cut out a water layer sorrounding it. It outputs either .pdb or .xyz file with the transformed structure for further simulation, analysis or visualization.
 
## Requirements
 * **Python 3**
 * [numpy](https://numpy.org)
 * [pandas](https://pandas.pydata.org)
 
## Installation
``
`!pip install -i https://test.pypi.org/simple/MakeDroplet`

## Usage
```
usage: RunDroplet.py [-h] {XYZ,PDB} ...

positional arguments:
  {XYZ,PDB}
    XYZ       Make an XYZ structure of protein sorrounded by a water shell of
              given thickness
    PDB       Make an PDB file with structure of protein sorrounded by a water
              shell of given thickness

optional arguments:
  -h, --help  show this help message and exit

# Create the .xyz file
usage: RunDroplet.py XYZ [-h] [-i INFILE] [-o DOUT] [-s SHELL]

optional arguments:
  -h, --help  show this help message and exit
  -i INFILE   input data file
  -o DOUT     Output .xyz file
  -s SHELL    Thickness of the water layer surrounding the protein

# Create the .pdb file
usage: RunDroplet.py PDB [-h] [-i INFILE] [-o DOUT] [-s SHELL]

optional arguments:
  -h, --help  show this help message and exit
  -i INFILE   input data file
  -o DOUT     Output .pdb file
  -s SHELL    Thickness of the water layer surrounding the protein
```
  