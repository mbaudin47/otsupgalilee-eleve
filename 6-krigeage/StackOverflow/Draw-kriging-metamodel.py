#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://stackoverflow.com/questions/68925585/how-to-get-better-kriging-result-graphs-in-openturns
https://openturns.discourse.group/t/normalization-of-the-input-sample-in-krigingalgorithm-in-ot1-16/101
"""

# %%
import openturns as ot
import openturns.experimental as otexp


# %%
dimension = 2  # dimension of your input (x,y)
distribution = ot.JointDistribution([ot.Uniform(-10.0, 50.0)] * dimension)
inputdata = distribution.getSample(100)

g = ot.SymbolicFunction(["x", "y"], ["30 + 3.0 * sin(x / 10.0) * (y / 10.0) ^ 2"])

outputdata = g(inputdata)


# %%
basis = ot.ConstantBasisFactory(dimension).build()
covarianceModel = ot.SphericalModel(dimension)
covarianceModel.setScale(inputdata.getMax())  # Trick A
fitter = otexp.GaussianProcessFitter(inputdata, outputdata, covarianceModel, basis)
# Trick B, v2
x_range = inputdata.getMax() - inputdata.getMin()
scale_max_factor = 2.0  # Must be > 1, tune this to match your problem
scale_min_factor = 0.1  # Must be < 1, tune this to match your problem
maximum_scale_bounds = scale_max_factor * x_range
minimum_scale_bounds = scale_min_factor * x_range
scaleOptimizationBounds = ot.Interval(minimum_scale_bounds, maximum_scale_bounds)
fitter.setOptimizationBounds(scaleOptimizationBounds)
fitter.run()
gpr = otexp.GaussianProcessRegression(fitter.getResult())
gpr.run()
gpr_result = gpr.getResult()
metamodel = gpr_result.getMetaModel()
metamodel.setInputDescription(["x", "y"])
metamodel.setOutputDescription(["z"])

# %%
lower = [-10.0] * 2  # lower bound of the 2D window
upper = [50.0] * 2  # upper bound of the 2D window
graph = metamodel.draw(lower, upper)
graph.setBoundingBox(ot.Interval(lower, upper))
graph.add(ot.Cloud(inputdata))  # overlay a scatter plot of the observation points
graph.setTitle("Kriging metamodel")

# A View object allows us to interact with the underlying matplotlib figure
from openturns.viewer import View

view = View(graph, legend_kw={"bbox_to_anchor": (1, 1), "loc": "upper left"})
view.getFigure().tight_layout()
