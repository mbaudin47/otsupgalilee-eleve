#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import openturns as ot
import otguibase

myStudy = otguibase.OTStudy("Study_CantileverBeam")

## Model
distributionE = ot.Beta(0.9, 3.5, 65.0e9, 75.0e9)
distributionF = ot.LogNormalMuSigma(300.0, 30.0, 0.0).getDistribution()
distributionL = ot.Uniform(2.50, 2.60)
distributionI = ot.Beta(2.5, 4.0, 1.3e-7, 1.7e-7)

E = otguibase.Input("E", 70.0e9, distributionE, "Young's modulus (Pa)")
F = otguibase.Input("F", 300.0, distributionF, "Force applied (N)")
L = otguibase.Input("L", 2.55, distributionL, "Length (m)")
I = otguibase.Input("I", 1.5e-7, distributionI, "Section modulus (m4)")
y = otguibase.Output("y", "Vertical deviation (m)")

model = otguibase.SymbolicPhysicalModel(
    "myPhysicalModel", [E, F, L, I], [y], ["F * L^3 / (3 * E * I)"]
)
myStudy.add(model)

# Create the Spearman correlation matrix of the input random vector
RS = ot.CorrelationMatrix(4)
RS[2, 3] = -0.2
# Evaluate the correlation matrix of the Normal copula from RS
R = ot.NormalCopula.GetCorrelationFromSpearmanCorrelation(RS)
# Create the Normal copula parametrized by R
copula = ot.NormalCopula(R)
inputnames = ["E", "F", "L", "I"]
model.setCopula(inputnames, copula)

## script
script = myStudy.getPythonScript()
print(script)
exec(script)
