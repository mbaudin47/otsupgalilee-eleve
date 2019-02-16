#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
import openturns as ot
import otguibase

myStudy = otguibase.OTStudy('Study_CantileverBeam')

## Model
dist_E = ot.Beta(0.9, 3.5, 2.5e7, 5.0e7)
dist_F = ot.LogNormalMuSigma(30.e3, 9.e3, 15.e3).getDistribution()
dist_L = ot.Uniform(250., 260.)
dist_I = ot.Beta(2.5, 4., 310., 450.)

E = otguibase.Input('E', 3e7, dist_E, 'Young\'s modulus (Pa)')
F = otguibase.Input('F', 3e4, dist_F, 'Force applied (N)')
L = otguibase.Input('L', 250, dist_L, 'Length (m)')
I = otguibase.Input('I', 400, dist_I, 'Section modulus (m4)')
y = otguibase.Output('y', 'Vertical deviation (m)')

model = otguibase.SymbolicPhysicalModel('myPhysicalModel', [E, F, L, I], [y], ['F*L^3/(3*E*I)'])
myStudy.add(model)

# Create the Spearman correlation matrix of the input random vector
RS = ot.CorrelationMatrix(4)
RS[2,3] = -0.2
# Evaluate the correlation matrix of the Normal copula from RS
R = ot.NormalCopula.GetCorrelationFromSpearmanCorrelation(RS)
# Create the Normal copula parametrized by R
copula = ot.NormalCopula(R)
inputnames = ["E", "F", "L", "I"]
model.setCopula(inputnames,copula)

## script
script = myStudy.getPythonScript()
print(script)
exec(script)
