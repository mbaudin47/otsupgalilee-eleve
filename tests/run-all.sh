#!/bin/sh
#
# Example
# -------
# $ cd tests
# $ bash run-all.sh
#

set -xe

echo "Python interpreter"
echo `which python`
echo "OpenTURNS version"
python -c "import openturns; print(openturns.__version__); exit()"

# Run tests
cd ..

# Execute IPython Notebooks in all subdirectories
python tests/find-ipynb-files.py .

# Execute Python scripts in all subdirectories
python tests/find-py-files.py 0-Deroulement
python tests/find-py-files.py 1-Intro-OT
python tests/find-py-files.py 2-Quantification
python tests/find-py-files.py 3-Propagation
python tests/find-py-files.py 4-Sensibilite
python tests/find-py-files.py 5-Chaos
python tests/find-py-files.py 6-krigeage
python tests/find-py-files.py 8-Calage
python tests/find-py-files.py 9-Fiabilite
