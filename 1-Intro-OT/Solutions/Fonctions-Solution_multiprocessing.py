import openturns as ot
import math
import time
import sys
import numpy as np

def highDimensionSimulator(x):
    xPoint = ot.Point(x)
    dim_val = xPoint.getDimension()
    y0, y1 = 0.0, 1.0
    for i in range(dim_val):
        y0 += math.exp(x[i])
        y1 *= math.exp(x[i])
    return [y0, y1]

dim_h = 100
inputRV_h = ot.RandomVector(ot.Normal(dim_h))
sampleSize_h = 100

# Test Séquentiel
f_seq = ot.PythonFunction(dim_h, 2, highDimensionSimulator)
t0 = time.time()
ot.CompositeRandomVector(f_seq, inputRV_h).getSample(sampleSize_h)
print(f"Temps séquentiel : {time.time() - t0:.2f} s")

# Test Parallèle
if not sys.platform.startswith("win"):
    f_par = ot.PythonFunction(dim_h, 2, highDimensionSimulator, n_cpus=8)
    t0 = time.time()
    ot.CompositeRandomVector(f_par, inputRV_h).getSample(sampleSize_h)
    print(f"Temps parallèle : {time.time() - t0:.2f} s")
else:
    print("Parallélisation n_cpus ignorée (Windows).")