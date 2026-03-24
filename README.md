 # Stadium Access Simulation
 
## Running
To run the simulation, make sure you have anaconda installed, then open up a terminal and run
`conda env create -f environment.yml`
in the root of the source directory. You must adjust the `prefix:` variable at the bottom of `environment.yml`
to suit your own user directory, and the location where you would like to have the environment installed.

To run without anaconda, you must ensure that the packages in `environment.yml` are installed in
your current python environment.

Once the dependencies are met, simply run `main.py` from your IDE, or run `python -m main` from the terminal.
Again making sure you are in the root of the source directory.

## Configuration
To configure the simulation you can adjust the variables in `configuration.py` to suit your scenario.
Most parameters will be adjustable using that file, however the distribution functions are located in `functions.py` and
will require a bit more knowledge of python and the numpy library to alter successfully.