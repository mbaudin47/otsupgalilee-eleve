# Notations
## Introduction
L'objectif de ce document est de formaliser un ensemble de notations cohérentes pour l'ensemble du cours.

## Vecteur aléatoire en entrée
Soit $p \in \mathbb{N}$ le nombre de composantes du vecteur d'entrée. Soit $\mathcal{X} \subset \mathbb{R}^p$ le support de $\boldsymbol{X}$. Soit $\boldsymbol{X} = (X_1,..., X_p)^T \in \mathcal{X}$ le vecteur aléatoire d’entrée.  On note $i\in\{1,...,p\}$ l'indice d'une composante du vecteur d'entrée $\boldsymbol{X}$. Pour tout $i=1,...,p$, on a donc $X_i\in\mathbb{R}$.

## Densité de probabilité du vecteur d'entrée
On note $f$ la densité de probabilité du vecteur aléatoire $\boldsymbol{X}$. Dans le contexte de l'inférence (c'est à dire de l'étape B), lorsqu'on considère un modèle probabiliste paramétrique, on peut chercher à estimer les paramètres du modèle s'ajustant au mieux à un échantillon donné de $\boldsymbol{X}$.

Soit $m \in \mathbb{N}$ le nombre de paramètres de la densité de probabilité $f$. Soit $\Theta \subset \mathbb{R}^m$ le sous-ensemble des paramètres. Alors $f(\boldsymbol{X}, \boldsymbol{\theta})$ est la densité de probabilité dont le vecteur de paramètres est $\boldsymbol{\theta} \in \Theta$.

## Variable aléatoire en sortie
On note $i\in\{1,...,p\}$ l'indice d'une composante du vecteur d'entrée $\boldsymbol{X}$. Pour tout $i=1,...,p$, on a donc $X_i\in\mathbb{R}$. On note $f$ la densité de probabilité du vecteur aléatoire $\boldsymbol{X}$.  Soit $g : \mathcal{X} \rightarrow \mathbb{R}$ une fonction. On considère la variable aléatoire :

$$
Y = g(\boldsymbol{X}).
$$

Nous allons estimer l'espérance de $Y$ :

$$
\mathbb{E}(Y) = \int_{\mathcal{X}} g(\boldsymbol{X}) f(\boldsymbol{X}) d\boldsymbol{X}.
$$

De plus, nous allons estimer la variance de $Y$ :

$$
\text{Var}(Y) = \mathbb{E}\left[(Y - \mathbb{E}(Y))^2\right].
$$

Pour un seuil $s \in \mathbb{R}$ fixé, on peut souhaiter la probabilité de dépasser le seuil $s$ :

$$
\mathbb{P}(Y > s) 
= \int_{\mathcal{X}} \mathbf{1}_{g(\mathbf{x}) > s} f(\mathbf{x}) d\mathbf{x}
$$

où $\mathbf{1}_{g(\mathbf{x}) > s}$ est la fonction indicatrice définie par :

$$
\begin{aligned}
\mathbf{1}_{g(\mathbf{x}) > s}(\mathbf{x})
= \left\{
\begin{array}{l}
1, \textrm{ si } g(\mathbf{x}) > s, \\
0, \textrm{ sinon}.
\end{array}
\right.
\end{aligned}
$$

## Echantillon Monte-Carlo simple
Soit $n\in\mathbb{N}$ un entier représentant la taille de l'échantillon. Soit:

$$
\left\lbrace \boldsymbol{X}^{(j)} \right\rbrace_{j=1,...,n}
$$

un échantillon i.i.d. du vecteur aléatoire $\boldsymbol{X}$. Par conséquent, la réalisation $x_i^{(j)}$ est la i-ème composante de la j-ème réalisation, pour $i=1,...,p$ et $j=1,...,n$. Le plan d'expériences $A$ associé est donc :

$$
A = 
\begin{pmatrix}
x_1^{(1)} & x_2^{(1)} & \cdots & x_p^{(1)} \\
x_1^{(2)} & x_2^{(2)} & \cdots & x_p^{(2)} \\
\vdots & \vdots & & \vdots \\
x_1^{(n)} & x_2^{(n)} & \cdots & x_p^{(n)}
\end{pmatrix}
$$

où chaque ligne représente une réalisation du vecteur aléatoire $\boldsymbol{X}$ et chaque colonne représente une composante. Soit :

$$
y^{(j)} = g\left(\boldsymbol{x}^{(j)}\right)
$$

pour $j=1,...,n$. L'estimateur Monte-Carlo de la moyenne empirique est :

$$
\bar{y} = \frac{1}{n} \sum_{j=1}^n y^{(j)}.
$$

## Modèle paramétrique
Dans certains cas, on suppose que la fonction $g$ est un modèle paramétrique dont on cherche à déterminer les paramètres. Il peut s'agir d'un contexte de calage de modèle (dans l'étape B') ou d'estimation des hyper-paramètres d'un méta-modèle (dans l'étape C). Soit $q \in \mathbb{N}$ le nombre de paramètres de la foncion $g$. Soit $\mathcal{B} \subset \mathbb{R}^q$ le sous-ensemble des paramètres. Pour tout $\boldsymbol{\beta} \in \mathcal{B}$, on considère la fonction $y = g(\boldsymbol{X}, \boldsymbol{\beta})$. 

## Réplications
Pour observer la variabilité d'un estimateur, on considère parfois des réplications d'une simulation de Monte-Carlo. Dans ce cas, le nombre de réplications est noté $r\in\mathbb{N}$ et chaque réplication porte l'indice $k=1,...,r$.
