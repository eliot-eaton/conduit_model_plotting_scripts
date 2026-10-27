# Conduit Model — Figure Reproduction Scripts

## Overview

This repository contains Python/Jupyter notebooks, numerical model outputs, and supporting files used to generate figures for the study:

**Linking Dome-Feeding Conduit Flow to Near-Field Ground Deformation**

Eliot Eaton¹, Jurgen Neuberg¹, Susanna Ebmeier¹

The primary purpose of this repository is to provide access to the plotting scripts and supporting data used in the study, allowing readers to inspect the results and recreate the figures presented in the accompanying publication.

The repository includes results from numerical models developed using COMSOL Multiphysics, together with Python notebooks for processing model outputs and generating figures.

## Repository structure

### `py/` — Python plotting notebooks

Contains Jupyter notebooks (`.ipynb`) used to process numerical model outputs and recreate figures.

The notebooks are grouped according to the physical processes and model configurations examined:

- `1_basic_conduit_loading_model/` — Basic conduit loading and ground deformation.
- `2_Xc_growth_during_ascent/` — Effects of crystal growth during magma ascent.
- `3_outgassing_model/` — Outgassing model comparisons.
- `4_Slip_at_conduit_walls/` — Effects of slip at the conduit walls.
- `5_20m3s/` — Summary plots for simulations examining a magma discharge rate of 20 m³/s.

The file `py/plotting_library.py` contains shared functions for reading and processing COMSOL model outputs.

### `data/` — Numerical model output data

Contains data exported from the COMSOL models, primarily as text files (`.txt`), used by the Python plotting notebooks.

### `mph/` — COMSOL model files

Contains selected COMSOL Multiphysics model files (`.mph`) associated with the numerical analyses.

Compatible COMSOL software is required to open and execute these models.

### `output_plots/` — Generated figures

Contains exported figures produced using the Python plotting notebooks.

## Reproducing figures

1. Download or clone this repository.
2. Install Python and Jupyter Notebook or JupyterLab.
3. Install the required Python packages:
   - NumPy
   - pandas
   - Matplotlib
   - cmcrameri
4. Open the relevant Jupyter notebook in the `py/` directory.
5. Check that the input file paths reference the appropriate files in `data/`.
6. Run the notebook cells to reproduce the figures.

Some notebooks may require adjustments to file paths or access to additional model outputs.

## Software

Numerical modelling was carried out using COMSOL Multiphysics.

Post-processing and figure generation were performed using Python and Jupyter notebooks.

Software versions and dependencies will be documented for the archived release.

## Associated publication

Eaton, E., Neuberg, J., & Ebmeier, S. ([Year]).

**Linking Dome-Feeding Conduit Flow to Near-Field Ground Deformation.**

*[Journal and DOI to be added upon publication.]*

## Citation

If using the scripts or datasets, please cite the associated scientific publication and the archived repository.

A permanent DOI will be provided through Zenodo.

## License

License information will be added prior to the archived release.
