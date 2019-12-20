#!/bin/sh

test_python_script()
{
  # test_python_script mypythonscript.py
  pythonscript=$1
  cp $pythonscript /tmp
  python /tmp/$pythonscript
}

test_ipython_notebook()
{
  # test_ipython_notebook mynotebook.ipynb
  ipythonnotebook=$1
  basefilename=$(basename -- "$ipythonnotebook")
  basefilename="${basefilename%.*}"
  nbfile="$basefilename.ipynb"
  pyfile="$basefilename.py"
  jupyter nbconvert --to python $nbfile
  mv $pyfile /tmp
  python /tmp/$pyfile
}

test_ipython_directory()
{
  FILES=*.ipynb
  for f in $FILES
  do
    echo "Processing $f file..."
    test_ipython_notebook $f
  done
}

set -xe

echo `Python interpreter`
echo `which python`
echo `OpenTURNS version`
python -c "import openturns; print(openturns.__version__); exit()"

# Run tests
cd ..
#
cd 0-Deroulement
test_ipython_directory
cd ..
#
cd 1-Intro-OT
test_ipython_directory
cd ..
#
cd 2-Quantification
test_ipython_directory
cd ..
#
cd 3-Propagation
test_ipython_directory
cd ..
#
cd 4-Sensibilite
test_ipython_directory
cd ..
#
cd 5-Chaos
test_ipython_directory
cd ..
#
cd 6-krigeage
test_ipython_directory
cd ..
#
cd 7-SALOME-OT
test_ipython_directory
cd ..
#
cd 8-Calage
test_ipython_directory
cd ..

