# Guide du krigeage avec OpenTURNS
Dans ce texte, j'énumère des méthodes permettant de tenter d'améliorer la qualité d'un métamodèle de krigeage avec OpenTURNS.

Ce guide est une tentative de fournir une méthode pour tenter d'être systématique dans l'exploration des paramètres du chaos polynomial. J'essaye de parcourir les paramètres du plus simple au plus complexe et de tenir compte de l'expérience pratique issue de mes études et du contact avec les utilisateurs.

## Du plus simple au plus complexe
Dans cette liste, j'énumère les paramètres du krigeage qui sont susceptibles d'être modifiés. Un point de départ acceptable peut être d'utiliser l'exemple [de la poutre encastrée](https://openturns.github.io/openturns/latest/auto_meta_modeling/kriging_metamodel/plot_kriging_hyperparameters_optimization.html) dans lequel on montre comment configurer le problème d'optimisation.
- Configurer les bornes de l'algorithme d'optimisation pour faciliter le travail de la librairie d'optimisation. 
- Initialiser correctement les paramètres du modèle de covariance avant de créer l'instance de la classe `GaussianProcessFitter`. Cela permet d'initialiser l'algorithme de krigeage avec des paramètres plus appropriés. 
- Dessiner la fonction de vraisemblance : est-elle plate ? l'optimum est-il sur les bords de l'intervalle ?
- Utiliser une tendance plus appropriée : tester une constante, un modèle linéaire, un modèle quadratique, un polynôme du chaos.
- Augmenter la taille de l'échantillon d'apprentissage. 

Référence
- [Normalization of the input sample in KrigingAlgorithm in OT1.16](https://openturns.discourse.group/t/normalization-of-the-input-sample-in-krigingalgorithm-in-ot1-16/101)

## Mettre à l'échelle le plan d'expériences d'apprentissage ?
Une alternative consiste à mettre à l'échelle l'échantillon d'apprentissage avant l'appel au krigeage. Par exemple, considérer des variables $\boldsymbol{z} \in [-1, 1]^d$ plutôt que la variable physique $\boldsymbol{x} \in \mathbb{R}^d$. C'est parce que la mise à l'échelle des variable facilite le travail de maximisation de la vraisemblance et la recherche des longueurs de corrélation optimales. Dans ce cas, le métamodèle est le composition de la mise à l'échelle et du krigeage, ce qui complique un peu le code source. 

