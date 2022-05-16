# OpenTURNS cheat sheet

![](logo_OT-small.png)

This _OpenTURNS_ v1.17 cheat sheet provides a quick overview of all the programming interface. For full documentation, please read [the doc](http://openturns.github.io/openturns/master/contents.html). A beginner may be interested in the [Quick start guides](http://openturns.github.io/openturns/master/search.html?q=quick+start).

This cheat sheet follows the steps of the ABC method.

![The ABC method](MethodologieIncertitude-EN_arial.png)

## Step A : define the study

| **Purpose** |  **Class / Method** |
|---|---|
| Import _OpenTURNS_ | `import openturns as ot` |
| Vector | `ot.Point(dimension)` |
| Sample | `ot.Sample(size, dimension)` |
| Symbolic function | `ot.SymbolicFunction(["x0", "x1"], ["1 + x0 + x1"])` |
| Python function | `ot.PythonFunction(number_of_inputs, number_of_outputs, py_function)` |
| Manage history and cache | `ot.MemoizeFunction(g_function)` |
| Normal | `ot.Normal(mu, sigma)` |
| Uniform | `ot.Uniform(a, b)` |
| Multivariate distr., indep. copula | `ot.ComposedDistribution((dist_x0, dist_x1, dist_x2))` |
| Input random vector | `ot.RandomVector(input_distribution)` |
| Output random vector | `ot.CompositeRandomVector(g_function, input_random_vector)` |
| Generate observations | `randomVector.getSample(sample_size)` |
| Set the seed | `ot.RandomGenerator.SetSeed(1)` |
| Get sample size | `sample.getSize()` |
| Get sample dimension | `sample.getDimension()` |
| Sample mean | `sample.computeMean()` |
| Sample st. dev. | `sample.computeStandardDeviation()` |

## Step B : quantification of the sources of uncertainties

| **Purpose** |  **Class / Method** |
|---|---|
| Fit a Normal | `ot.NormalFactory().build(sample)` |
| Fit a Beta | `ot.BetaFactory().build(sample)` |
| Fit an histogram | `ot.HistogramFactory().build(sample)` |
| Fit a kernel density estimator | `ot.KernelSmoothing().build(sample)` |
| Draw QQ-plot | `ot.VisualTest.DrawQQplot(sample, distribution)` |
| Kolmogorov-Smirnov test (known parameters) | `ot.FittingTest.Kolmogorov(sample, distribution)` |
| Kolmogorov-Smirnov test (unknown parameters) | `ot.FittingTest.Lilliefors(sample, factory)` |
| BIC criteria | `ot.FittingTest.BIC(sample, distribution)` |

## Step C : push forward the uncertainties

| **Purpose** |  **Class / Method** |
|---|---|
| Taylor expansion | `ot.TaylorExpansionMoments(output_random_vector)` |
| Estimate mean | `ot.ExpectationSimulationAlgorithm(output_random_vector)` |
| Estimate P(Y > s) | `sample.computeEmpiricalCDF(s, True)` |
| Create the event (Y > s) | `ot.ThresholdEvent(output_random_vector, ot.Greater(), s)` |
| Create a Monte-Carlo experiment | `ot.MonteCarloExperiment()` |
| Estimate a probability | `ot.ProbabilitySimulationAlgorithm(myEvent, experiment)` |

## Step C' : sensitivity analysis

| **Purpose** |  **Class / Method** |
|---|---|
| Perform linear regression | `ot.LinearLeastSquares(input_sample, output_sample)` |
| Standardized regression coefficients | `ot.CorrelationAnalysis_SignedSRC(input_sample, output_sample)` |
| Draw indices | `ot.SobolIndicesAlgorithm.DrawCorrelationCoefficients(src_indices, input_names, "SRC coefficients")` |
| Estimate Sobol' indices given budget | `ot.SobolIndicesExperiment(distribution, sample_size)` |
| Estimate Sobol' indices | `ot.SaltelliSensitivityAlgorithm()` |

## Step B' : calibration

| **Purpose** |  **Class / Method** |
|---|---|
| Create the parametric model | `ot.ParametricFunction(g_function, calibrated_indices, theta_prior)` |
| Linear least squares | `ot.LinearLeastSquaresCalibration(parametric_g, input_sample, output_sample, theta_prior, "SVD")` |
| Non linear least squares | `ot.NonLinearLeastSquaresCalibration(parametric_g, input_sample, output_sample, theta_prior)`
| Linear gaussian | `ot.GaussianLinearCalibration(parametric_g, input_sample, output_sample, theta_prior, theta_sigma, output_covariance)` |
| Non linear gaussian | `ot.GaussianNonLinearCalibration(parametric_g, input_sample, output_sample, theta_prior, theta_sigma, output_covariance)`
| Bayesian calibration | `ot.RandomWalkMetropolisHastings(prior, conditional, model, input_sample, output_sample, initialState, proposal)` |

## Metamodel

| **Purpose** |  **Class / Method** |
|---|---|
| Squared exponential | `ot.SquaredExponential([1.0] * dimension, [1.0])` |
| Matern 5/2 covariance | `ot.MaternModel([1.0] * dimension, 2.5)` |
| Kriging | `ot.KrigingAlgorithm(input_sample, output_sample, covarianceModel, basis)` |
| Sample from kriging | `ot.KrigingRandomVector(result, input_sample)` |
| Conditioned gaussian process | `ot.ConditionedGaussianProcess(kriging_result, mesh)` |
| Multivariate basis | `ot.OrthogonalProductPolynomialFactory(distribution_collection)`
| Polynomial chaos (given data) | `ot.FunctionalChaosAlgorithm(input_sample, output_sample)`
| Polynomial chaos (given distribution) | `ot.FunctionalChaosAlgorithm(input_sample, output_sample, distribution, adaptive_strategy, projection_strategy)` |
| Sobol' indices from chaos | `ot.FunctionalChaosSobolIndices(functional_chaos_result)` |
| Sample from chaos | `ot.FunctionalChaosRandomVector(functional_chaos_result)` |
| Validation | `ot.MetaModelValidation(input_test, output_test, metamodel)` |

## Design of experiments

| **Purpose** |  **Class / Method** |
|---|---|
| Monte-Carlo | `ot.MonteCarloExperiment(distribution, sample_size)` |
| Latin Hypercube Sampling | `ot.LHSExperiment(distribution, sample_size)` |
| Optimized LHS | `ot.SimulatedAnnealingLHS(lhs_experiment, criteria, temperature_profile)` |
| Sobol' sequence | `ot.SobolSequence(dimension)` |
| Low discrepancy sequence | `ot.LowDiscrepancyExperiment(ld_sequence, distribution, samplesize, False)` |
| Import viewer | `import openturns.viewer as otv` |
| Plot DOE | `otv.PlotDesign(sample, bounds)` |

## Graphics

| **Purpose** |  **Class / Method** |
|---|---|
| Import viewer | `import openturns.viewer as otv` |
| Graph | `ot.Graph(title, x_title, y_title, show_axes_bool)` |
| Curve | `ot.Curve(sample_x, sample_y)` |
| Cloud | `ot.Cloud(sample_x, sample_y)` |
| Pairs | `ot.VisualTest.DrawPairs(sample)` |
| Pairs with distribution | `ot.VisualTest.DrawPairsMarginals(sample, distribution)` |
| Parallel coordinate | `VisualTest_DrawParallelCoordinates(input_sample, output_sample, min_value, max_value, color)` |
| Set colors | `graph.setColors(ot.Drawable().BuildDefaultPalette(number_of_graphs))` |
| Set size | `otv.View(graph, figure_kw={"figsize": (4.0, 3.0)})` |
| Move legend | `otv.View(graph, legend_kw={"bbox_to_anchor":(1.0, 1.0), "loc":"upper left"})`| 
| Save figure | `view.getFigure().savefig("filename.pdf", bbox_inches="tight")` |

## More resources

| **Resource** | **Link** |
|---|---|
| Forum | https://openturns.discourse.group |
| Chat | https://gitter.im/openturns/community |
| Modules | https://github.com/openturns/openturns/wiki/Modules |
| Install | http://openturns.github.io/openturns/master/install.html |
| Bugs | https://github.com/openturns/openturns/issues |
| Q&A | https://stackoverflow.com/questions/tagged/openturns |
| Events | https://github.com/openturns/openturns/wiki/OpenTURNS-events |
| Bibliography | https://github.com/openturns/openturns/wiki/Bibliography |
| Bib resources | [Bibtex file](https://github.com/mbaudin47/otsupgalilee-eleve/blob/master/Bibliography_OpenTURNS/bibliography_openturns.bib) |
| Presentations | https://github.com/openturns/presentation |

