#!/usr/bin/env python
# coding: utf-8

# Analyse de sensibilité globale par regression - application au cas
# de la déviation verticale de la poutre
#

# # Model definition

# %%
import openturns as ot
import openturns.viewer as otv


# %%
distributionE = ot.Beta(0.9, 3.5, 65.0e9, 75.0e9)
distributionE.setDescription(["E"])
parametersF = ot.LogNormalMuSigma(300.0, 30.0, 0.0)  # Paramétrage par les moments
distributionF = ot.ParametrizedDistribution(parametersF)
distributionF.setDescription(["F"])
distributionL = ot.Uniform(2.50, 2.60)  # in m
distributionL.setDescription(["L"])
distributionI = ot.Beta(2.5, 4.0, 1.3e-7, 1.7e-7)  # in m^4
distributionI.setDescription(["I"])

X = ot.JointDistribution([distributionE, distributionF, distributionL, distributionI])

g = ot.SymbolicFunction(["E", "F", "L", "I"], ["F* L^3 /  (3 * E * I)"])
g.setOutputDescription(["Y (m)"])

# %%
# Pour pouvoir exploiter au mieux les simulations, nous équipons
# la fonction d'un mécanisme d'historique.
g = ot.MemoizeFunction(g)


# %%
# Enfin, nous définissons le vecteur aléatoire de sortie.

XRV = ot.RandomVector(X)
Y = ot.CompositeRandomVector(g, XRV)
Y.setDescription(["Y (m)"])

# %%
# ## Régression linéaire avec LinearLeastSquares

n = 1000
sampleX = X.getSample(n)
sampleY = g(sampleX)

myLeastSquares = ot.LinearLeastSquares(sampleX, sampleY)
myLeastSquares.run()
responseSurface = myLeastSquares.getMetaModel()

val = ot.MetaModelValidation(sampleY, responseSurface(sampleX))

graph = val.drawValidation()
view = otv.View(graph)
