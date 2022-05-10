# Grandjean sur Bépo

### Qu'est-ce que c'est?
Une adaptation de la sténo Grandjean à la disposition de clavier bépo. Permet d'utiliser l'écriture accélérée en sténo à l'aide d'une disposition de dactylo. 

#### Un mot sur le bépo, pour contexte:
La disposition de clavier bépo a été inventée dans le but de substituer l'azerty comme standard utilisé pour la langue française. La disposition a été conçue sur la base d'une analyse de la fréquence d'utilisation des lettres dans la langue: les lettres les plus utilisées sont au centre du clavier, les moins utilisées sont à des emplacements périphériques, avec une distribution des consonnes vers la main droite et des voyelles vers la main gauche.
Le bépo rend aussi accessible des symboles nécessaires au français qui sont difficiles d'accès sur un azerty (quand était la dernière fois que vous avez volontairement tapé un "œ"?). Ne pas avoir certains symboles accessibles revient à contraindre les utilisateurs à faire des fautes en écrivant, ce qui est dommage et bête. 

### Un mot sur la sténo Grandjean, pour contexte aussi:
Le système Grandjean est une méthode de sténotypie inventée à l'origine pour le français, qui été étendue à l'usage de l'espagnol et (je crois aussi) à l'italien. Comme toutes les méthodes de sténotypie, elle dépend d'une machine équipée d'un clavier dont la disposition des lettres est conçue spécifiquement pour la sténo. 
La disposition permet d'écrire des mots abréviés en phonétique, donnant ainsi une vitesse d'écriture accélérée pouvant monter jusqu'à 300 mots par minute. 
Malgré la vitesse d'écriture, parce que la disposition d'un clavier de sténo est fondamentalement incompatible avec celle d'un clavier de dactylo (c.à.d d'un clavier traditionnel), le système Grandjean n'a pas pu connaître une large diffusion: la dactylo est infiniment plus facile à apprendre et infiniment plus flexible, quoiqu'au prix d'une vitesse de frappe ralentie (110 mots par minute max.) et d'une précision dégradée, et en plus le Grandjean implique la double punition de contraindre ses utilisateurs à apprendre et la sténo et la disposition du clavier dédié.

### Pour quoi faire?
À ma connaissance, il n'y a pas de disposition dactylographique qui soit compatible avec la sténo - cette implémentation sur le bépo est une première. 
Ceci implique que pour un utilisateur du bépo, il devient possible d'apprendre la sténo sans avoir à apprendre aussi la disposition de clavier Grandjean. Le «bépo-iste» bénéficie d'un apprentissage accéléré de la sténo car il a déjà la mémoire musculaire de l'emplacement des lettres sur le clavier. 
Parce que le bépo est une disposition dactylographique, elle peut être installée sur l'ordinateur et le smartphone (tous systèmes d'exploitations confondus) et peut être apprise et utilisée au jour le jour, hors d'un contexte d'entraînement spécifique.

Le deuxième avantage potentiel (et je dis bien potentiel) est que la sténo Grandjean a été implémentée dans plusieurs langues, ce qui signifie que le Grandjean sur bépo pourrait être adapté pour les autres langues latines. En ayant une disposition dactylographique dans plusieurs langues, on ouvre la porte à une diffusion plus large de la sténo. 
 
### Pour qui?
Les gens de lettres, la recherche, les gens du droit, les codeurs: toutes les professions qui requièrent l'usage de beaucoup de texte.

### Comment ça marche ? 
L'implémentation est un plugin pour le logiciel de sténo Plover. Les dictionnaires sont ceux du Grandjean-Français qu'Aziz Yamloul a rendu disponible sur le répo de plover-france il y a dix ans. On peut remercier les créateurs de Plover et M. Yamloul d'avoir généreusement rendu leurs travaux disponibles.
Pour toute requête ou demande de changement dans le système, créez une «issue» ou envoyez moi une pull-request.

### Désavantages et limitations? 
Il n'y a pas de solution technique sans une contrepartie technique:
- Apprendre la sténo est clairement un investissement en temps. J'apprends moi-même le Grandjean-sur-bépo en ce moment, et je mettrai cette page à jour pour indiquer la quantité de temps qu'il m'aura fallu pour atteindre 60 mots par minute - dès que j'y arriverai. Dans l'immédiat, j'estime que ça devrait prendre entre 20 et 40 heures de pratique pour un «bépo-iste» confirmé.
- Grandjean-sur-bépo est inutilisable hors du contexte de Plover. Pour s'en servir, il faut installer Plover. C'est comme ça. 
- Le français est une langue phonétiquement très ambigüe: nombres de mots et conjugaisons différents sont des homophones. Ceci pose problème pour la sténo qui est basée sur une transcription phonétique: à la transcription d'un manuscrit, des fautes de grammaires ou d'homophonie peuvent facilement se glisser dans le texte et fausser le sens de l'écrit sans que ce soit la faute de l'auteur ou du sténotypiste, simplement parce que le logiciel à interprété un homophone erroné. Je travaille actuellement à une solution pour ce problème.
- Parce que la sténo requiert de frapper plusieurs touches simultanément avec un seul doigt, il est recommandé d'utiliser un clavier adapté. Un clavier adapté, c'est un clavier ortholinéaire à touches plates, avec capacité NKRO (c.à.d pas de limites au nombre de touches simultanées). Dans les entrées de gamme (et sans avoir à s'investir dans le merveilleux monde des claviers mécaniques custom pour fous du gaming) un planck d'occasion et un jeu de 50 touches plates devrait être accessible en-dessous de 150 euros. 

### Pour aller plus loin:
Je ferai prochainement une mise à jour avec des instructions claires pour comprendre comment marche la sténo Grandjean. En attendant, vous pouvez vous diriger vers l'excellente présentation de M. Yamlloul sur les répos de plover-France: le premier, et le second.
