# PythonEnvs

Specifications (in the `requirements.txt` format) and code for modular creation of Python `conda` environments.

Packages are divided into groups, each having the corresponding directory with a `conda_reqs.txt`, `pip_reqs.txt`, or both requirements specification files.

The following groups are available:

 * `core`
 * `jupyter`
 * `opt`
 * `viz`
 * `ml-stats`
 * `vision`
 * `symbolic`
 * `desim`


`pe-install.py` utility manages installation of any of the available package groups, as well as all groups altogether.


Example of creating a `conda` environment and installation of groups `core`, `jupyter`, and `ml-stats`:

```
conda create -n myenv
source activate myenv
python pe-install.py core jupyter ml-stats
```

Example of creating a `conda` environment and installation of all the groups:

```
conda create -n myenv
source activate myenv
python pe-install.py all
```
