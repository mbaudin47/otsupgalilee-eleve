# -*- coding: utf-8 -*-
"""
Find Python script files in the directory, and subdirectories.

Examples
--------
$ python3 find-py-files.py <directoryname>
"""

import os


def findPythonScriptFiles(dirname, maximumNumberOfFiles=100):
    """
    Cherche la liste des fichiers .py dans le répertoire courant.
    """
    print("+ Searching in ", dirname, "...")
    nbfiles = 0
    for dirpath, dirnames, filenames in os.walk(dirname):
        for shortfilename in filenames:
            filename, fileExtension = os.path.splitext(shortfilename)
            if fileExtension == ".py":
                fullfile = os.path.join(dirpath, shortfilename)
                print("(%d) %-40s" % (nbfiles, fullfile))
                nbfiles = nbfiles + 1
                executePythonScript(fullfile)
                if nbfiles > maximumNumberOfFiles:
                    break
    print("Number of tested files:", nbfiles)
    return None


def executePythonScript(pythonFile):
    """
    Execute the given Python script file.
    This function fails if the execution fails.
    Generates a temporary script which is deleted afterwards.
    """
    print("+ Testing ", pythonFile)
    dirname = os.path.dirname(pythonFile)
    # 1. Got into the directory
    cwd = os.getcwd()
    os.chdir(dirname)
    basename = os.path.basename(pythonFile)
    # 2. Execute the notebook
    command = "python "
    command += '"' + basename + '"'
    print(command)
    returncode = os.system(command)
    if returncode != 0:
        raise ValueError("Wrong return code = %s" % (returncode))
    print("OK")
    # 4. Go back where we come from
    os.chdir(cwd)
    return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Number of arguments=%d" % (len(sys.argv)))
        print("Arguments=%s" % (sys.argv))
        raise Exception("find-py-files.py <directoryname>")

    dirname = sys.argv[1]
    print(f"dirname = {dirname}")
    print(f"CWD = {os.getcwd()}")
    findPythonScriptFiles(dirname)
