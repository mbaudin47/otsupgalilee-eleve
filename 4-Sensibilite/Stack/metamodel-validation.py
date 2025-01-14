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
dist_E = ot.Beta(0.9, 2.2, 2.8e7, 4.8e7)
dist_E.setDescription(["E"])
F_para = ot.LogNormalMuSigma(3.0e4, 9.0e3, 15.0e3)  # in N
dist_F = ot.ParametrizedDistribution(F_para)
dist_F.setDescription(["F"])
dist_L = ot.Uniform(250.0, 260.0)  # in cm
dist_L.setDescription(["L"])
dist_I = ot.Beta(2.5, 1.5, 310.0, 450.0)  # in cm^4
dist_I.setDescription(["I"])

X = ot.JointDistribution([dist_E, dist_F, dist_L, dist_I])

g = ot.SymbolicFunction(["E", "F", "L", "I"], ["F* L^3 /  (3 * E * I)"])
g.setOutputDescription(["Y (cm)"])

# %%
# Pour pouvoir exploiter au mieux les simulations, nous équipons
# la fonction d'un méchanisme d'historique.
g = ot.MemoizeFunction(g)


# %%
# Enfin, nous définissons le vecteur aléatoire de sortie.

XRV = ot.RandomVector(X)
Y = ot.CompositeRandomVector(g, XRV)
Y.setDescription(["Y (cm)"])

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
