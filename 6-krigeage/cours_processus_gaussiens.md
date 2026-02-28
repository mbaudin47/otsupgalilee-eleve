# Modèles de covariance et processus gaussien

_Michaël Baudin, Mathieu Couplet_ (EDF R&D)

## Processus gaussien (scalaire) et modèle de covariance

Le domaine sur lequel le processus prend ses valeurs est noté $\mathcal{D} \subset \mathbb{R}^p$. 

*Exemple* : dans le cas d'un processus stochastique temporel, le domaine considéré est un intervalle de dates : $\mathcal{D} \subset \mathbb{R}$, typiquement $\mathcal{D}=[x_{min},\: x_{max}]$ où $x_{min}$ et $x_{max}$ sont respectivement les dates initiale et finale considérées.

### Covariance

Pour toutes variables aléatoires réelles $Z$ et $Z'$, la covariance entre $Z$ et $Z'$ est définie par :

$$
\textrm{Cov}\left(Z,\:Z'\right) = \mathbb{E}\left[ \left(Z - \mathbb{E}(Z)\right) \left(Z' - \mathbb{E}\left(Z'\right)\right)\right].
$$

### Processus gaussien (scalaire)

Un processus stochastique réel $Z$ sur $\mathcal{D}$ est gaussien si, et seulement si, pour n'importe quel ensemble fini 

$$
\left\{\boldsymbol{x}^{(1)},\:\ldots,\boldsymbol{x}^{(k_x)}\right\}\in\mathcal{D},
$$

le vecteur aléatoire 

$$
\left(
\begin{array}{c}
Z\left(\boldsymbol{x}^{(1)} \right)\\
\vdots
\\Z\left(\boldsymbol{x}^{(k_x)}\right)
\end{array}
\right) 
\in\mathbb{R}^{k_x}
$$

est un vecteur gaussien. 

Un processus gaussien $Z(\boldsymbol{x})$ est caractérisé par 
* sa (fonction) moyenne $m(\boldsymbol{x})= \mathbb{E}[Z(\boldsymbol{x})]$ ;
* sa (fonction de) covariance $k(\boldsymbol{x},\:\boldsymbol{x}')= \textrm{Cov}(Z(\boldsymbol{x}),\:Z(\boldsymbol{x'}))$
pour tout $(\boldsymbol{x},\:\boldsymbol{x'})\in{\mathcal{D}}^2$.

La moyenne $m(\boldsymbol{x})$ d'un processus gaussien est souvent appelée *tendance* (en anglais : « *trend* »). 

Un processus gaussien de moyenne $m$ et de fonction de covariance $k$ est souvent noté (voir (Rasmussen, Williams, 2006), p.13, eq. 2.14):

$$
Z(x) \sim \operatorname{PG}\left(m(\boldsymbol{x}),\:k(\boldsymbol{x},\:\boldsymbol{x}')\right).
$$

### Quelques propriétés

#### Ajout d'une tendance

Si $Z(x) \sim \operatorname{PG}\left(m(\boldsymbol{x}),\:k(\boldsymbol{x},\:\boldsymbol{x}')\right)$ et $m':\mathcal{D}\rightarrow\mathbb{R}$, alors $Z(x)+m'(x) \sim \operatorname{PG}\left(m(\boldsymbol{x})+m'(\boldsymbol{x}),\:k(\boldsymbol{x},\:\boldsymbol{x}')\right)$. En particulier :
* si $Z(x) \sim \operatorname{PG}\left(m(\boldsymbol{x}),\:k(\boldsymbol{x},\:\boldsymbol{x}')\right)$, alors
$Z(x)-m(x) \sim \operatorname{PG}\left(0,\:k(\boldsymbol{x},\:\boldsymbol{x}')\right)$ ;
* si $Z(x) \sim \operatorname{PG}\left(0,\:k(\boldsymbol{x},\:\boldsymbol{x}')\right)$, alors
$Z(x)+m(x) \sim \operatorname{PG}\left(m(\boldsymbol{x}),\:k(\boldsymbol{x},\:\boldsymbol{x}')\right)$.

#### Conditionnement

Si :

$$
\left(\begin{array}{c}X_1\\X_2\end{array}\right)\sim\mathcal{N}\left(\left(\begin{array}{c}\mu_1\\\mu_2\end{array}\right),\:\left(\begin{array}{cc}K_{11}\:K_{12}\\K_{12}^T\:K_{22}\end{array}\right)\right),
$$

alors (voir (Rasmussen, Williams, 2006), p.16, eq. 2.19) :

$$
X_1 \: | \: X_2 = x_2 \sim\mathcal{N}\left(\mu_1 + K_{12}{K_{22}}^{-1}(x_2 - \mu_2),\:
K_{11} - K_{12}{K_{22}}^{-1}{K_{12}}^T\right).
$$

**Corollaire.** Un processus gaussien conditionné est un processus gaussien.


#### Propriété de la fonction de covariance

Une fonction $k\,:\mathcal{D}\times\mathcal{D}\rightarrow\mathbb{R}$ symétrique est dite définie positive si, et seulement si, pour tout $k_x\in\mathbb{N}^*$ et tout ensemble de $k_x$ points distincts :

$$
\left\{\boldsymbol{x}^{(1)},\:\ldots,\:\boldsymbol{x}^{(k_x)}\right\}\in\mathcal{D}
$$ 

alors

$$
\sum_{i,j=1}^{k_x} a_i\:a_j\:k\left(\boldsymbol{x}^{(i)},\boldsymbol{x}^{(j)}\right) \geq 0,
$$

pour tous $a_1,...,a_k\in\mathbb{R}$.

Une telle fonction est appelée *noyau* en théorie des espaces de Hilbert à noyau reproduisant (RKHS). Tout noyau peut être utilisé comme fonction de covariance (assure l'obtention de matrices de covariance semi-définies positives); réciproquement, toute fonction de covariance est un noyau.

### Modèle de covariance stationnaire

Un modèle de covariance *stationnaire* ne dépend que de la différence $\boldsymbol{x}- \boldsymbol{x'}$,
c'est-à-dire :

$$
k(\boldsymbol{x}, \boldsymbol{x'}) = k(\boldsymbol{x}- \boldsymbol{x'}),
$$

pour tous $\boldsymbol{x},\boldsymbol{x'}\in\mathcal{D}$.

Pour construire un métamodèle par krigeage, la fonction de covariance est généralement supposée stationnaire, ce qui n'apparaît pas une hypothèse très forte (si une manière d'introduire la métamodélisation par krigeage est de faire l'hypothèse que la fonction à métamodéliser est la réalisation d'un processus stochastique, ce n'est qu'une vue de l'esprit : on ne pourrait pas disposer d'autres réalisations de ce processus afin de tester sa stationnarité).
Si $k$ est une fonction de covariance stationnaire, alors

$$
\textrm{Var}(Z(\boldsymbol{x})) = \textrm{Cov}\left(Z(\boldsymbol{x}),\,Z(\boldsymbol{x})\right) = k(\boldsymbol{x},\,\boldsymbol{x}) = k(\boldsymbol{x}- \boldsymbol{x}) = k(\boldsymbol{0}),
$$

pour tout $\boldsymbol{x}\in\mathcal{D}$.
Autrement dit, si la fonction de covariance est stationnaire, la variance $k(\boldsymbol{0}) = \sigma^2$ en un point est constante sur tout le domaine $\mathcal{D}$. Il est alors possible de paramétrer la covariance du processus gaussien en paramétrant la fonction de corrélation $r$ :

$$
k(\boldsymbol{x},\,\boldsymbol{x}') = \sigma^2 r(\boldsymbol{x} - \boldsymbol{x}',\,\boldsymbol{\theta})
$$

où :
* $\sigma^2$ est la variance du processus gaussien ;
* et $\boldsymbol{\theta} \in\mathbb{R}^p$ les paramètres de la fonction de corrélation $r$.

Les paramètres $\sigma$ et $\boldsymbol{\theta}$ sont souvent nommés *hyperparamètres*. Avec certains modèles, faire varier certaines composantes de $\boldsymbol{\theta}$ a pour effet de changer la régularité du processus gaussien (continuité et différentiabilité des trajectoires ou en moyenne quadratique). 

## Exemple : le modèle exponentiel carré anisotrope

Le modèle exponentiel carré anisotrope est la fonction de covariance définie par :
$$
k \left( \boldsymbol{x}, \boldsymbol{x}' \right) 
= \sigma^2 \exp\left( -\frac{1}{2} \left\|\frac{\boldsymbol{x}-\boldsymbol{x}'}{\boldsymbol{\theta}}\right\|_2^2\right)
$$
pour tout $\boldsymbol{x}, \boldsymbol{x}' \in \mathcal{D}$ 
où la division entre le vecteur $\boldsymbol{x} - \boldsymbol{x}'$ au numérateur et le vecteur $\boldsymbol{\theta}$ au dénominateur est la division composante par composante :
$$
{\left(\frac{\boldsymbol{x} - \boldsymbol{x}'}{\boldsymbol{\theta}}\right)}_i
= \frac{x_i - x'_i}{\theta_i}
$$
pour $i=1,...,d$.

Si toutes les composantes du vecteur d'hyperparamètres $\boldsymbol{\theta}\in\mathbb{R}^d$ sont égales alors le modèle est *isotrope* : le comportement est le même dans chacune des $d$ dimensions/directions du domaine $\mathcal{D}$. Sinon le modèle est *anisotrope* : c'est le cas dans la classe `SquaredExponential`. 

La classe `SquaredExponential` permet de construire des modèles de covariances de ce type :
* le paramètre $\sigma\in\mathbb{R}$ est le paramètre d'amplitude,
* le paramètre $\boldsymbol{\theta}\in\mathbb{R}^d$ est le paramètre d'échelle.

