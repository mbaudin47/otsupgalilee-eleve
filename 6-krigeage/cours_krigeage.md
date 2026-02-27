# Faire un métamodèle de krigeage

_Michaël Baudin, Mathieu Couplet_ (EDF R&D)

## Rappels méthodologiques

### Krigeage

On considère une fonction $g$ :

$$
y = g(\boldsymbol{x})
$$

pour tout $\boldsymbol{x} \in \mathcal{D}$, où $\mathcal{D} \subset \mathbb{R}^p$ est le domaine de définition de la fonction $g$, et $p$ est la dimension de l'espace d'entrée. Dans ce document, on considère que la sortie du code de calcul $y\in\mathbb{R}$ est scalaire. 

Le krigeage est une technique permettant de créer un métamodèle de la fonction $g$. Il est fondé sur les processus gaussiens et c'est pourquoi on nomme parfois cette technique *régression par processus gaussien*.

En d'autres termes, le krigeage consiste à modéliser $Z$ par un processus gaussien de moyenne $m$ et de covariance $k$ :

$$
Z(\boldsymbol{x}) = \operatorname{PG}\left(m(\boldsymbol{x}),k(\boldsymbol{x}, \boldsymbol{x}')\right)
$$

pour tout $\boldsymbol{x} \in \mathcal{D}$.

### Modèle de tendance

Pour définir la moyenne du processus gaussien, on fait le choix d'une base de fonctions 

$$
\boldsymbol{f} = (f_1,...,f_{d_f})
$$

où $d_f$ est le nombre de fonctions de base. 
Si les paramètres $\boldsymbol{\beta}\in\mathbb{R}^{d_f}$ sont connus, alors la moyenne est choisie sous la forme d'un modèle linéaire généralisé :

$$
\boldsymbol{m}(\boldsymbol{x}) = \boldsymbol{f}(\boldsymbol{x})^T \boldsymbol{\beta}
$$

_Remarque :_ on parle de *krigeage simple* lorsque la moyenne est supposée connue, de *krigeage ordinaire* lorsque la moyenne est inconnue mais supposée constante, sinon de *krigeage universel*. 

### Modèle de covariance

La fonction de covariance contrôle notamment la régularité du processus gaussien (continuité et différentiabilité de ses trajectoires ou en moyenne quadratique).

Pour définir la covariance du processus gaussien, on fait le choix d'une fonction de corrélation $r$ de la forme :

$$
k\left(\boldsymbol{x}, \boldsymbol{x}'\right) = \sigma^2 r\left(\boldsymbol{x} - \boldsymbol{x}', \boldsymbol{\theta}\right)
$$

où $\sigma^2$ est la variance du processus gaussien et $\boldsymbol{\theta} \in\mathbb{R}^p$.

### Régression par processus gaussien : principe

Dans la suite, nous considérons le krigeage associé à des observations $\boldsymbol{y}$ non bruitées.

Deux étapes peuvent être distinguées dans le krigeage :

* l'estimation des paramètres $\boldsymbol{\beta}$, $\sigma$ et $\boldsymbol{\theta}$;
* le conditionnement du processus par les données $\boldsymbol{y}$.

#### Étape (1) : estimation des (hyper)paramètres

Une approche rencontrée dans la littérature, appelée *bayesian kriging* ou *full bayesian kriging*, consiste à traiter les variables $\boldsymbol{\beta}$, $\sigma$ ou $\boldsymbol{\theta}$ comme des paramètres incertains que l'on associe à une distribution de probabilité a priori.
Dans OpenTURNS, ces variables sont simplement considérées comme des paramètres à estimer à partir de données censées provenir d'une même réalisation (de la même trajectoire) d'un processus gaussien. Cela est réalisé suivant le principe du maximum de vraisemblance.

La résolution de ce problème d'optimisation (le MV) peut poser des difficultés. Dans ce cas, on peut soit tenter de fournir à OpenTURNS des meilleures valeurs initiales, soit configurer la résolution du problème de manière plus fine en intervenant dans les objets de plus bas niveau.

#### Étape (2) : conditionnement

Nous nous limitons ci-dessous à une présentation du conditionnement (2) lorsque les paramètres $\boldsymbol{\beta}$, $\sigma$ et $\boldsymbol{\theta}$ sont connus (krigeage simple) et que l'on souhaite simplement
une prédiction en une unique point $\boldsymbol{x}\in\mathcal{D}$.

Faisons l'hypothèse que l'on connaît les valeurs de la fonction sur un plan d'expériences $\boldsymbol{x}^{(i)}$ pour $i=1,...,n$ où $n$ est le nombre de simulations. Pour chacune de ces entrées, on suppose que l'on connaît la valeur de la sortie scalaire $y^{(i)}$
pour $i=1,...,n$. On note $\boldsymbol{y} = (y_1, ..., y_n)^T$ le vecteur des sorties observées. 

Notons $F$ la matrice de conception associée aux fonctions de base :
$$
F = \left[ f_j\left(\boldsymbol{x}^{(i)}\right), \quad i=1,...,n, \quad j=1,...,d_f \right].
$$

Notons $R$ la matrice de correlation associée au noyau de corrélation :
$$
R = \left[ r\left(\boldsymbol{x}^{(i)}, \; \boldsymbol{x}^{(j)}, \; \boldsymbol{\theta}\right),\quad i,j=1,...,n \right].
$$

Considérons un nouveau point $\boldsymbol{x} \in \mathbb{R}^p$ correspondant à une sortie $y$ inconnue.
Notons $\boldsymbol{r}(\boldsymbol{x})$ le vecteur des corrélation entre le point $\boldsymbol{x}$ et les points du plan d'expériences :
$$
\boldsymbol{r}(\boldsymbol{x}) = \left[r\left(\boldsymbol{x}, \; \boldsymbol{x}^{(i)}, \; \boldsymbol{\theta}\right),\quad i=1,...,n \right]^T
$$

On peut démontrer que le vecteur aléatoire associé aux observations $\boldsymbol{Y}$ et la variable aléatoire $Y(\boldsymbol{x})$ sont liés par une loi normale :

$$
\begin{pmatrix}
\boldsymbol{Y} \\
Y(\boldsymbol{x})
\end{pmatrix}
= 
\mathcal{N}
\left(
\begin{pmatrix}
F \boldsymbol{\beta} \\
\boldsymbol{f(x)}^T \boldsymbol{\beta}
\end{pmatrix}
, \; 
\sigma^2 
\begin{pmatrix}
R & \boldsymbol{r}(\boldsymbol{x}) \\
\boldsymbol{r}(\boldsymbol{x})^T & 1 \\
\end{pmatrix}
\right).
$$

Le modèle prédictif est donné par loi de $Z(\boldsymbol{x})$ conditionnée par les observations connues du code :
$$
\widetilde{Y}(\boldsymbol{x}) = \left[ \boldsymbol{Y}(\boldsymbol{x}) \; 
| \; \boldsymbol{Y} = \boldsymbol{y}, \; 
\boldsymbol{\theta} = \boldsymbol{\theta}, \; 
\boldsymbol{\sigma} = \boldsymbol{\sigma} \right].
$$

On peut démontrer que $\widetilde{\boldsymbol{Y}}(\boldsymbol{x})$ est également une variable aléatoire gaussienne :
$$
\widetilde{Y}(\boldsymbol{x}) \sim \mathcal{N} \left( \mu_{\widetilde{Y}}(\boldsymbol{x}) ,  \; \sigma_{\widetilde{Y}}(\boldsymbol{x})^2 \right)
$$
où la moyenne $\mu_{\widetilde{Y}}(\boldsymbol{x})$ et la variance $\sigma_{\widetilde{Y}}(\boldsymbol{x})^2$ s'écrivent de manière explicite (voir la propriété de conditionnement des processus gaussiens dans le précédent _notebook_).

Les calculs liés au conditionnement n'impliquent que la résolution de systèmes d'équations linéaires. 
Néanmoins, si $n$ est grand (par exemple $n=10000$), alors la matrice de corrélation $R$ est de taille $n\times n$, ce qui peut poser des difficultés de performance, voire de mémoire. Pour résoudre ce problème, une alternative consiste à utiliser des techniques de compression de matrices, comme par exemple la technique des H-mat utilisée par OpenTURNS.

#### Remarque

Dans le cas du krigeage universel et d'une fonction de covariance à estimer, la définition de la fonction de covariance conditionnée est en fait modifiée pour tenir compte de l'incertitude sur $\boldsymbol{\beta}$.
