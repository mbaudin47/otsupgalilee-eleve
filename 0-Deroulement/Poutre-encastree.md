## Déviation verticale d'une poutre encastrée

Nous considérons une poutre encastrée définie par son module de Young $E$, sa longueur $L$ et son moment d'inertie $I$. Une extrémité est encastrée dans un mur et nous appliquons une charge $F$ à l'autre extrémité de la poutre, ce qui entraîne une déviation verticale $Y$, également nommée « flèche » en mécanique.

Nous analysons la déviation verticale produite par un enfant sur un plongeoir. Nous considérons un enfant dont le poids génère une force approximativement égale à 300 N (c'est-à-dire environ 30 kg). En raison des incertitudes sur le poids de la personne, nous considérons que la force est une variable aléatoire. La longueur du plongeoir est comprise entre 2,5 m et 2,6 m. Le module de Young est incertain et compris entre 65 et 75 GPa (c'est-à-dire entre $65 \times 10^9$ et $75 \times 10^9$ Pascals), ce qui correspond à de la fibre de verre, un matériau souvent utilisé pour les plongeoirs. Les incertitudes liées à la production du matériau sont prises en compte dans le module de Young et le moment d'inertie du plongeoir.

<img src="poutre.png" width="200">

**Figure 1.** Déviation verticale $Y$ de la poutre encastrée de longueur $L$.

## Entrées

- $E$ : Module de Young (en Pa),
- $F$ : Charge (en N),
- $L$ : Longueur de la poutre (en m),
- $I$ : Moment d'inertie (en $\mathrm{m}^4$).

| Variable | Distribution                                                                      |
| -------- | --------------------------------------------------------------------------------- |
| E        | Beta(alpha = 0.9, beta = 3.5, a = $65 \times 10^9$, $b = 75 \times 10^9$)         |
| F        | Lognormal($\mu_F=300 $, $\sigma_F=30$, $\gamma$=0)                                   |
| L        | Uniform(min=2.5, max= 2.6)                                                        |
| I        | Beta(alpha = 2.5, beta = 4.0, a = $1.3 \times 10^{-7}$, b = $1.7 \times 10^{-7}$) |

**Tableau 1.** Lois marginales des variables $E$, $F$, $L$ et $I$.

Dans le tableau précédent, $\mu_F = \mathbb{E}[F]$ et $\sigma_F = \sqrt{\operatorname{Var}(F)}$ désignent la moyenne et l'écart-type de $F$. Les variables d'entrée sont supposées indépendantes.

**Remarque.** La variable $F$ est de loi Log-Normale. Il serait possible de paramétrer cette variable aléatoire en spécifiant la moyenne et l'écart-type de la variable gaussienne sous-jacente. Ce n'est toutefois pas ce qui est réalisé ici : nous spécifions la moyenne et l'écart-type de la variable $F$ elle-même. C'est la raison pour laquelle nous utiliserons par la suite la classe `LogNormalMuSigma`.

**Remarque.** Les paramètres de forme de la loi Beta ($\alpha=0.9$ et $\beta=3.5$) modélisent une asymétrie marquée vers la borne inférieure, représentative d'un biais de fabrication tendant vers la spécification minimale du matériau. 

## Sortie d'intérêt

Le déplacement vertical à l'extrémité libre de la poutre encastrée est :
$$
Y  = \dfrac{F\, L^3}{3 \, E \, I}.
$$
