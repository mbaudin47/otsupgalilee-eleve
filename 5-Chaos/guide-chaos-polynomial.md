# Guide du chaos polynomial avec OpenTURNS
Dans ce texte, j'énumère des méthodes permettant de tenter d'améliorer la qualité d'un polynôme du chaos créé avec OpenTURNS.

Ce guide est une tentative de fournir une méthode pour tenter d'être systématique dans l'exploration des paramètres du chaos polynomial. J'essaye de parcourir les paramètres du plus simple au plus complexe et de tenir compte de l'expérience pratique issue de mes études et du contact avec les utilisateurs.

## Du plus simple au plus complexe
Dans cette liste, j'énumère les paramètres du chaos polynomial qui sont susceptibles d'être modifiés. Cette expérience se fonde sur le fait que la méthode d'estimation par moindres carrés LARS fonctionne souvent très bien. Un point de départ acceptable peut être d'utiliser la fonction `ComputeSparseLeastSquaresChaos` dans [Exercice-chaos-cantilever-beam.ipynb](https://github.com/mbaudin47/otsupgalilee-eleve/blob/master/5-Chaos/Exercice-chaos-cantilever-beam.ipynb)
- Donner si possible la distribution du vecteur aléatoire $\boldsymbol{X}$ en entrée du métamodèle. Sinon, la classe `FunctionalChaosAlgorithm` tente d'inférer la loi à partir de l'échantillon d'entrée, ce qui peut être long et donner des résultats peu satisfaisants
- Tester des degrés croissants de 1, 2, 3, ... Commencer par un degré 2.
- Estimer les coefficients par régression 
- Avec la méthode LARS on peut réduire le nombre de coefficients grâce à la méthode de sélection de modèle. 
- Utiliser la règle d'énumération linéaire
- Estimer les coefficients par intégration
- Utiliser la règle d'énumération hyperbolique avec $0.5 \leq q \leq 1$ (isotrope). Utiliser une boucle sur $q \in \{0.5, 0.6, 0.7, 0.8, 0.9\}$ et conserver le meilleur. Cette règle permet de favoriser des degrés marginaux élevés, avec des interactions de degré faible. 
- Utiliser la règle d'énumération hyperbolique anisotropique. Diminuer les poids marginaux permet d'augmenter le degré marginal pour certaines variables, sans nécessairement les augmenter pour les autres. 

## Valider le chaos polynomial
Un des buts des méthodes suivantes est de vérifier que le nombre de coefficients estimés est compatible avec la taille du plan d'expériences. 

Les méthodes classiques de validation d'un métamodèle peuvent être employées :
- validation croisée : apprentissage, test, validation
- estimation du coefficient de prédictivité Q2 : par découpage apprentissage / test, par k-fold

Des méthodes spéficiques peuvent être utilisées pour valider un chaos polynomial :
- compter le nombre de coefficients du chaos polynomial avec la méthode ̀`FunctionalChaosResult.getCoefficients().getSize()`
- calculer le taux de creux, c'est à dire le complémentaire à 1 du pourcentage de coefficients sélectionnés parmi la base fonctionnelle complète. On peut utiliser la fonction `computeSparsityRate` dans [Exercice-chaos-poutre-sensibilite-degre.ipynb](https://github.com/mbaudin47/otsupgalilee-eleve/blob/master/5-Chaos/Exercice-chaos-poutre-sensibilite-degre.ipynb)
- observer la sensibilité du chaos au degré par l'intermédiaire du coefficient Q2 ([plot_chaos_beam_sensitivity_degree.html](https://openturns.github.io/openturns/latest/auto_meta_modeling/polynomial_chaos_metamodel/plot_chaos_beam_sensitivity_degree.html)). Tenir compte de la variabilité du Q2 dûe à l'échantillonnage. Pour le faire sur une fonction coûteuse, rééchantillonner aléatoirement une sous-partie de l'échantillon de test. 
- analyser les multi-indices impliqués avec la méthode `FunctionalChaosSobolIndices.summary()`. Si les degrés des multi-indices des coefficients ont une part de variance significative (par exemple, supérieure à 0.5) et si ces degrés sont proches du degré total utilisé dans l'apprentissage, augmenter le degré total pour laisser une marge à la méthode de sélection de modèle. 

## Améliorer la qualité du chaos polynomial
Pour améliorer la qualité du métamodèle, plusieurs options sont possibles.
- Mener une analyse de sensibilité. Cela permet de déterminer les variables influentes et leurs interactions.
- La taille du plan d'expériences pourrait être augmentée. C'est une option qui nécessite d'évaluer la fonction $g$ sur un plus grand nombre de points d'entrée, ce qui peut être coûteux.
- Le degré du polynôme pourrait être modifié. En effet, un polynôme de degré moins élevé est associé à un moins grand nombre de coefficients, qui sont plus faciles à estimer. Au contraire, il peut s'avérer que le modèle est très nonlinéaire, ce qui peut nécessiter un degré polynomial élevé.
- On peut changer de plan d'expériences et utiliser, par exemple, une séquence à faible discrépance ou un plan LHS. C'est une option qui nécessite d'évaluer la fonction $g$ sur des nouveaux points d'entrée, ce qui peut être coûteux.
- On pourrait changer la règle d'énumération par une règle qui favorise les coefficients associés aux degrés élevés, sans augmenter excessivement le nombre de coefficients, comme la règle hyperbolique par exemple.
- Diminuer la largeur de l'intervalle de définition du vecteur $\boldsymbol{X}$ en entrée : plus l'intervalle est petit, plus la fonction peut être proche de la linéarité. Il n'est pas toujours nécessaire d'utiliser un intervalle large, surtout au début d'une étude. 
- On peut changer la loi du vecteur aléatoire, grâce à une transformation appropriée. Il peut arriver que la transformation facilite l'apprentissage. Par exemple, on peut transformer les variables grâce à une transformation isoprobabiliste appropriée de telle sorte que le vecteur d'entrée soit gaussien, ce qui permet d'utiliser les polynômes d'Hermite. L'analyse de sensibilité par les indices de Sobol' n'est pas possible dans ce cas car l'analyse porte sur les variables transformées, et non pas les variables initiales. 
- On pourrait changer la base polynomiale orthogonale univariée, même si la famille polynomiale choisie n'est pas nécessairement celle du schéma de Askey. Par exemple, il se peut que la base orthogonale associée à la loi log-normale pose une difficulté (car la distribution log-normale n'est pas déterminée de manière unique par ses moments). On pourrait remplacer la famille de polynômes par la famille des polynômes de Laguerre, qui est également associée à des variables positives comme la loi log-normale. Il n'est pas nécessairement impropre de choisir des polynômes de Chebyshev à la place des polynômes de Legendre, puisque les deux polynômes sont sur l'intervalle $[-1, 1]$ et qu'ils sont orthogonaux. Si le but est d'avoir un métamodèle, on n'a pas nécessairement besoin d'une base orthogonale pour la mesure du vecteur aléatoire en entrée. L'analyse de sensibilité par les indices de Sobol' n'est pas possible dans ce cas. 

## Un guide pour le chaos polynomial creux dans OpenTURNS
Voici les étapes principales et les objets pour créer un polynôme de chaos creux par régression.
* Créer un plan d'expériences (de type `Sample`) et évaluer les sorties de la fonction $g$
* Créer la base polynomiale multivariée avec la classe `OrthogonalProductPolynomialFactory`. 
  * La règle par défaut `StandardDistributionPolynomialFactory` sélectionne automatiquement la famille de polynômes en fonction de la distribution ou bien l'orthogonalise si elle n'existe pas. Si nécessaire, personnaliser la famille polynomiale univariée pour chaque marginale (par exemple, pour la variable log-normale). 
  * Si nécessaire, personnaliser la règle d'énumération avec `HyperbolicAnisotropicEnumerateFunction`.
* Choisir une méthode de sélection de modèle avec `LeastSquaresMetaModelSelectionFactory`. 
  * Par défaut, l'algorithme de sélection de modèle permettant de créer la hiérarchie de modèles du plus creux au moins creux est la méthode "Least Angle Regression Stepwise" (LARS). 
  * Par défaut, l'algorithme de choix du meilleur modèle dans la hiérarchie de modèles est la méthode `CorrectedLeaveOneOut`. Si nécessaire, choisir `KFold`. 
* Choisir une règle de calcul des coefficients du polynôme du chaos avec la classe `LeastSquaresStrategy`. Une alternative serait de calculer les coefficients par intégration avec `IntegrationStrategy`.
* Choisir une méthode de troncature pour déterminer combien de coefficients seront retenus dans l'exploration des modèles. La méthode de base est d'utiliser un nombre fixe avec `FixedStrategy`. L'alternative est la classe `SequentialStrategy` dont l'objectif est de conserver au plus un nombre donné de coefficients. 
* Mélangez les ingrédients; votre `FunctionalChaosAlgorithm` est prêt !
