# Sténo Bépo

[Installation](#installation) \
[Présentation](#présentation) \
[Cahier des charges](#cahier-des-charges) \
[La sténo Grandjean](#la-sténo-grandjean-vs-bépo-sténo) \
[Adaptation au Bépo](#adaptation-au-bépo) \
[Disposition](#disposition-et-lettres-à-double-usage) \
[Ordre sténo de bépo-sténo](#ordre-sténo-de-bépo-sténo) \
[Touches «É» et «È»: Désambiguïser les homophones](#touches-é-et-è) \
[Touche H](#touche-h) \
[Touche espace](#touche-espace) \
[Touche B](#touche-b) \
[Outillage](#outillage) \
[À venir](#à-venir) 

```
_________________________________________
|  B|  É|  P|  O|  È|  ^|  *|  D|  L|  $|
|___|___|___|___|___|___|__v|___|___|__j|___
| A | U | I | E |  ,|  C| T | S | R | N |  M|
|___|___|___|___|___|___|___|___|___|___|___|
|  À|  Y|  Y|  .|  K|  n|  l|  H|  H|  F|
|___|___|__x|___|___|__'|__q|__g|___|___|
```

### Installation

Le présent projet n'en est qu'à ses débuts et n'est donc pas inclu dans la liste des plug-ins du gestionnaire de Plover. Il faudra l'installer manuellement.

## Versions compatibles

Assurez-vous d'utiliser Plover 4.x (dernière version) - les versions antérieures n'incluent pas les plugins.

## Instructions

* Invoquer la commande suivante depuis un terminal (cf [Invoke Plover from the command line](https://github.com/openstenoproject/plover/wiki/Invoke-Plover-from-the-command-line) pour plus de détails)
```bash
plover -s plover_plugins install git+https://github.com/AntoineBalaine/bepo-steno
```

**MacOS:**
```bash
/Applications/Plover.app/Contents/MacOS/Plover -s plover_plugins install git+https://github.com/AntoineBalaine/bepo-steno
```
NB: MacOS requiert d'autoriser plover dans `préférences système > sécurité > confidentialité > accessibilité`

**Linux:**
```bash
plover.AppImage -s plover_plugins install git+https://github.com/AntoineBalaine/bepo-steno
```
**Windows** (non-testé)

`.\plover_console.exe -s plover_plugins install git+https://github.com/AntoineBalaine/bepo-steno`

      NB: `https://github.com/user/repo.git` ne fonctionnera pas; 

* Vous devriez voir un message indiquant `Succesfully installed`, suivi d'un nombre de paquets, suivi du plugin.

* Re-démarrez Plover

* Allez dans `Configure`, puis `System` et sélectionnez `French Bépo`

* Dans le cas où l'installation ne fonctionne pas, 
    1. Si le plugin ne descend pas, vous pouvez faire une installation locale en clonant ce repo, et en invoquant la même commande avec l'emplacement du dosser sur votre ordinateur: 
    `plover -s plover_plugins install emplacementUtilisateur/bepo-steno`
    3. Si le clavier ne connecte pas sur MacOS, dé-autorisez et ré-autorisez plover dans les préférences de sécurité sus-indiquées. 
    2. Si les dictionnaires ne chargent pas, clonez ce repo, et importez les manuellement depuis la fenêtre principale de plover (en bas de fenêtre, bouton vert "+").

### Présentation
##### Bépo sur Grandjean: un plugin de sténographie pour le clavier bépo.
Ce plug-in est une extension pour le [logiciel de sténo Plover](https://www.openstenoproject.org/plover/), avec un système de frappes basé sur la méthode Grandjean (méthode de sténo traditionelle en français). Son dictionnaire adapte la méthode Grandjean à la disposition de [clavier Bépo](https://bepo.fr/wiki/Accueil). 
La disposition Bépo est une alternative au clavier traditionnel Azerty, qui a été conçue spécifiquement pour les besoins du français.

La finalité du plug-in est de fournir aux bépoïstes une technique d’écriture accélérée sur leur clavier de tous les jours - par opposition à une machine de sténo - sans les contraindre à apprendre une nouvelle disposition. 
En reposant sur une disposition déjà connue du bépoïste, le temps nécessaire à l’apprentissage de la sténo est fortement réduit.

Le plug-in tient sur deux piliers: le bépo modifié pour la sténo, et le dictionnaire. Pour ce dernier, j’ai modifié le dictionnaire open-source du plug-in [Plover-France](https://github.com/azizyemloul/plover-france), en l’adaptant un peu aux contraintes du bépo.

### Cahier des charges
- doit tenir sur un clavier ortholinéaire taille 40% (càd. [un planck](https://deskthority.net/wiki/Planck)),
- doit utiliser la disposition bépo d’origine au maximum, doit modifier la disposition le moins possible.
- doit avoir un moyen de désambiguïser les mots homophones autant que possible.
- doit avoir un moyen de désambiguïser les terminaisons des conjugaisons des verbes autant que possible.

### La sténo Grandjean vs bépo-sténo
Cf. [ l'excellent article de Plover France ](https://github.com/azizyemloul/plover-france-dict#%C3%A0-propos-de-la-st%C3%A9notypie) sur le fonctionnement de la sténotypie Grandjean. Lisez-le bien, sans quoi rien de ce qui suis ne fera sens.

### Adaptation au Bépo
- touches Grandjean modifiées 
  1. «ᴎ» s’annote «n». Le «N» sera traité comme début de syllabe, et «n» comme fin de syllabe
  3. «£» s’annote «l». Le «L» sera traité comme début de syllabe, et «l» comme fin de syllabe
- touches Bépo modifiées 
  1. «\$» se place sur «j» (frappe à l’annulaire droit)
  2. «ᴎ», devenu «n», se place sur «’» (frappe au pouce)
  3. «£», devenu «l», se place sur «q» (frappe au pouce ou index)
  4. «\*» se place sur «v» (frappe à l'index)

La sténo requiert d’avoir des consonnes dupliquées (touches «K» et «c» par ex., qui font référence au même son). Ces doublons servent à différencier les consonnes de début et de fin de syllabe ("sass", sténographié "SA$"). Installer des consonnes dupliquées sur le bépo impose de modifier la disposition d’origine. Cependant, chaque modification du bépo peut devenir une nouveauté gênante pour les bépoïstes.
Pour minimiser la gêne, la disposition actuelle suit les principes suivants:

- les lettres de début de syllabe doivent garder l’emplacement d’origine sur le bépo
- les doublons de fin de syllabe doivent être placés à des emplacements disponibles du bépo (càd. sur des touches qui ne sont pas utilisées par la méthode Grandjean).

J’ai porté une attention particulière à l’emplacement des lettres de fin de syllabe sur le clavier. Il en résulte quelques changements du bépo d’origine; ces changements sont des compromis et peuvent être appelés à changer à l’avenir - si l’on me prouve une disposition plus pratique, je serai ravi de l’intégrer dans le plug-in.

### Disposition et lettres à double usage

La sténo Grandjean contient nombre de lettres de terminaison à double usage:
- «\$» est utilisée pour indiquer les fins de mots en «s», «z», «f», «v»
- «n» est utilisée pour les fins en «n» et «m»
- «l» est utilisée pour les fins en «l» et «r»
- «d» est utilisée pour les fins en «d», «t», «p», «b»
- «c» est utilisée pour les fins en «c» et pour les «e» silencieux

Ce qui cause beaucoup d'ambiguïtés dans l'interprétation des frappes sténo. Pour résoudre ce problème et minimiser les doubles et quadruples usages de certaines lettres, sténo bépo utilise de nouvelles lettres.

### Ordre sténo de bépo-sténo

`S K P M T F * R N L Y H O ^ E È A À U I l É n $ B D C <espace> . ,`

Bépo-sténo introduit plusieurs nouvelles lettres par rapport à la méthode Grandjean, pour adresser plusieurs nécessités de l'usage quotidien.
Les modifications sont les suivantes:
- **«H»**: indique les apostrophes,  et permet de cycler parmi la liste d'homophones de la frappe précédente lorsqu'il est frappé seul.
- **«È»**: indique les sons «é» orthographiés «ai»
- **«É»**: est la touche orthographie. Elle indique que la dernière consonne du mot est une consonne silencieuse d'orthographie (ex: «met», frappé `«MÉED»` - le `«D»` de fin est silencieux). Si aucune consonne de fin n'est frappée, le mot sera mit au pluriel par défaut.
- **«B»**: indique les terminaisons en «b» et «p», ainsi que d'autres terminaisons lorsque combinée avec d'autres consonnes de fin de syllabe.
- **espace**: sert à insérer des espaces, mais pas seulement: inclu dans une syllabe, il acquiert des capacités spéciales (cf plus bas).
- **«.»** et **«,»**:  indiquent… «.» et «,», et peuvent être utilisées comme suffixes dans une syllabe: «son», frappée `SOn`, pourra être frappée `SOn.`, ce qui produira «son.». Cela permet d'éviter d'avoir à faire une frappe séparée pour la ponctuation.

Dans l'ordre des lettres de sténo bépo, S K P M T F * R N L et Y restent à leur emplacement d'origine: comme frappes de consonnes d'attaque.

### Touches É et È 
#### Désambiguïser les homophones
Parce que le français est une langue orthographique avant que phonétique, et que la sténo est une méthode phonétique avant qu’orthographique, toute transcription sténographique est vouée à souffrir des ambiguïtés phonétiques de la langue. C’est à dire qu’un même son peut correspondre à plusieurs mots: «ces», «ses», «c’est», «s’est», «sais», «sait»; et que ce son ne peut être sténographié que par une seule frappe: «SE». Cette spécificité du français défie toute méthode de transcription phonétique, et impose l’usage d’un moyen de désambiguïser les orthographies d’un même son. 

  Le présent projet fait usage d’une touche «orthographie», la «É». Placée dans la dernière syllabe d’un mot, elle converti la fin de syllabe en terminaison orthographique. Plusieurs règles s'appliquent:
  1. si le mot n'a pas de consonne de fin, le mot est mis au pluriel par défaut. `TEl/MI/NÉE` donne «terminés»
  2. si le mot a une consonne de fin, la consonne est silencieuse. `MÉED` donne «met». 
  3. si la consonne de fin de mot est «\$»,  alors la terminaison se transforme en «-ez». `TEl/MI/NÉE\$` donne «terminez». NB: cette règle n'est malheureusement pas implémentée de manière très rigoureuse dans le dictionnaire, il se peut qu'il y ait des erreurs lorsque vous emploierez cette règle.
  4. si la consonne de fin est un «c», soit la frappe sténo est traduite en un mot finissant en «C» et mit au pluriel: `STUÉc` donnera «stucs», soit elle est traduite en un mot féminin pluriel: `MUÉC` sera traduite «mues».
  
La touche «É» n'est cependant pas suffisante pour venir à bout de tous les cas d'ambiguïtés, particulièrement pour la conjugaison des verbes au passé. «terminai» se frappe jusqu'ici pareil que «terminé». l'ambiguïté entre la terminaison en *«ai»* et la terminaison en *«É»* est présente dans toutes les conjugaisons au passé du français, et requiert donc une solution spéciale: la touche «È». 

La touche `È` indique le son «é» orthographié «ai». Elle est utilisable pour les verbes comme pour les noms communs, avec une différence d'usage entre les deux: 
1. pour les noms communs, «É» suit l'usage normal: `LÈ` = «lait», `LÈÉD` = «laid», `LÈD` = «laide», etc.
2. pour les verbes, `«È»` considère que toutes les consonnes de fin de frappe sont silencieuses - la touche orthographie n'a pas besoin d'être utilisée. `MAn/YÈ$` = «mangeais», `MAn/YÈD` = «mangeait», `MAn/YÈn` = «mangeaient», etc. Seule la terminaison en «-ez» requiert l'usage de la touche orthographie: `MAn/YÈÉ$` = «mangez».


### Touche H 
#### Apostrophes et homophones
- la touche «H» a deux usages:  
1. Placée entre les consonnes d'attaque et les voyelles de milieu de syllabe, sert à indiquer les apostrophes: quand on frappe dans une même syllabe une consonne d'attaque, le H et une voyelle, sténo-bépo divisera la syllabe à l'emplacement de la frappe «H». Ex: `LHAn` sera transcrit «l'an», `KHOn` sera transcrit «qu'on». Plover divisera les deux mots en deux frappes. **À noter impérativement** que pour bénéficier de cette fonctionnalité, vous devrez installer le plug-in [plover-split-at-apostrophe](https://github.com/AntoineBalaine/plover-split-at-apostrophe). Pour ce faire, suivez les mêmes étapes que pour l'installation de sténo-bépo, mais en substituant l'adresse par celle de plover-split-at-apostrophe:

```bash
plover -s plover_plugins install git+https://github.com/AntoineBalaine/plover-split-at-apostrophe
```
2. Frappée seule, la touche «H» permet de substituer le mot précédent par un autre homophone (même son) du dictionnaire. Ainsi, frapper `KA/NAl` est traduit en «canal», puis en «canard» lorsqu'on frappe le `H`. Pour accéder à «canard», il faudra donc frapper `KA/NAl/H`. À noter qu'il est possible de frapper la touche H plusieurs fois d'affilée pour cycler toute la liste des homophones d'une même frappe. Idem que pour les apostrophes, vous devrez impérativement installer le plug-in correspondant: [plover_cycle_homophones](https://github.com/AntoineBalaine/plover_cycle_homophones) avec la commande:
```bash
plover -s plover_plugins install git+https://github.com/AntoineBalaine/plover_cycle_homophones
```

### Touche espace 
#### Diviser la frappe précédente

Avec plus de 300 mille mots dans le dictionnaire, il est inévitable que plover en confonde certains, et que certaines frappes qu'on veut avoir sur des mots séparés s'agrègent pour former des résultats indésirables. `KI/F*A/S*` est traduit «kiva z», alors qu'on pourrait vouloir écrire «qui vase». Une fonctionnalité du plug-in [plover_cycle_homophones](https://github.com/AntoineBalaine/plover_cycle_homophones) permet de diviser/désagréger la frappe précédente: `*<espace>` permet de diviser la frappe précédente et `<espace>` frappé dans syllabe permet de diviser les deux dernières frappes et tout en ajoutant la nouvelle syllabe.

### Touche B 
#### Terminaisons spéciales
La touche `B` permet d'écrire les syllabes terminant en «p», «b», «bl», et quelques «pl». `KAR/TAB` = « cartable»

Les terminaisons en «-tre» ou «-dre» peuvent être ob tenues en combinant `B` et `D`: «montre» peut s'annoter `MOnBD`. Autre exemple: `FOUBD` = «foudre».
Les terminaisons en «-che» peuvent être annotées avec `DC` (ex. `MAnDC` = «manche»), comme c'était déjà le cas dans le dictionnaire de Plover France. En ajoutant un `B` avant le `DC`, le «-che» devient «-ge»: `A/LU/MABDC` = «allumage»

### Outillage
##### Plug-in
structure du plugin

  - le fichier sténo.py d’un côté, et 
  - le dico de l’autre. Beaucoup de petits détails et de conventions du dictionnaire ne sont pas documentées ici.
##### Dictionnaire
Le dico cherche à être le plus catégorisé possible, par fichiers: 
  - **Verbes**: un fichier par groupe de verbes (1er groupe, 2e groupe, 3e groupe)
  - **Noms communs**: un fichier par genre/nombre (masculin/singulier, masculin/pluriel, féminin/singulier, féminin/pluriel)
  - **Adverbes**: un seul fichier (pour le moment)
  - **Chiffres**: un seul fichier
  - **Adjectifs**: un fichier par nombre
  - **Commandes**: un fichier contenant les commandes destinées à la manœuvre de Plover

Ce n'est malheureusement pas toujours possible, et les 300 mille mots du dictionnaire sont truffés de petites erreurs que je rectifie au fil du temps.

##### Conjugueur
Un [répositoire de scripts](https://github.com/AntoineBalaine/bepo-steno-conjugueur) en typescript servant à: 
  conjuguer les verbes, 
  accorder les noms communs, 
  filtrer les dictionnaires du projet-parent [Plover-France](https://github.com/azizyemloul/plover-france-dict)
  adjoindre les frappes de désambiguïsation, etc.


### À venir:
  Le présent projet ne fait aucune promesse quant à la moindre fonctionnalité ou dommages à votre santé mentale en tentant de l'utiliser. Je m'en sers moi-même régulièrement et garde des sentiments mitigés à son sujet. Bépo-sténo n'est pas une bonne option pour être votre méthode de saisie principale, seulement une méthode secondaire pour de la rédaction. Il n'est pas capable de saisir à la vitesse de la parole,  Et il n'est sans doute pas capable de dépasser 150 mots par minute dans le meilleur des cas. Bépo-sténo  n'est même pas une vraie méthode de sténo, c'est plutôt un vélotype. Là où il brille, là où il est bonde s'en servir, c'est pour accélérer une partie de rédaction un peu ennuyeuse. Je dirais aussi que comparé à la sténo anglaise, il est beaucoup plus facile à apprendre. Curieux de comparer? Essayez donc [mon plug-in pour le bépo en anglais](https://github.com/AntoineBalaine/bepo-steno-english)

  Dans ce qu'il *faudrait* faire pour le réparer, et que je ne ferai sans doute jamais:

  1. Avoir un programme conjugueur dans `system.py` pour remplacer tous les verbes conjugués du dictionnaire. Cela permettrait de réduire drastiquement la taille du dictionnaire et de réduire les erreurs.
  2. Corriger toutes les erreurs dans les frappes.
  3. Supprimer tous les mots rares ou inutiles du dictionnaire.
  4. convertir tous les «en» pour qu'il soient annotés `«EN»` plutôt que le `«AN»` actuel   

  Pour tout utilisateur intéressé à contribuer, les PR sont les bienvenues. 

##### Feuille de route:
- [x] Inclure les verbes du premier et deuxième groupe manquants (la liste des frappes à monter est dans le répo «[Conjugueur](https://github.com/AntoineBalaine/bepo-steno-conjugueur)»)
- [x] Inclure les conjuguaisons du troisième groupe (liste aussi présente dans le «Conjugueur»)
- [x] Ajouter les frappes de désambiguïsation partout où c’est nécessaire et nettoyer le dictionnaire
- [x] Inclure d’autres touches de désambiguïsation (parmi les hypothèses, «Ç» pour désambiguïser les «ses» et «ces»)

