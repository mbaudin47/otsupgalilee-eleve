#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import openturns as ot
import otguibase

myStudy = otguibase.OTStudy("Study_CantileverBeam")

## Model
distributionE = ot.Beta(0.9, 3.5, 2.5e7, 5.0e7)
distributionF = ot.LogNormalMuSigma(30.0e3, 9.0e3, 15.0e3).getDistribution()
distributionL = ot.Uniform(250.0, 260.0)
distributionI = ot.Beta(2.5, 4.0, 310.0, 450.0)

E = otguibase.Input("E", 3e7, distributionE, "Young's modulus (Pa)")
F = otguibase.Input("F", 3e4, distributionF, "Force applied (N)")
L = otguibase.Input("L", 250, distributionL, "Length (m)")
I = otguibase.Input("I", 400, distributionI, "Section modulus (m4)")
y = otguibase.Output("y", "Vertical deviation (m)")

model = otguibase.SymbolicPhysicalModel(
    "myPhysicalModel", [E, F, L, I], [y], ["F*L^3/(3*E*I)"]
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
