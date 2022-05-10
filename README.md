# Sténo Bépo

[Installation](#installation) \
[Présentation](#présentation) \
[Cahier des charges](#cahier-des-charges) \
[La sténo Grandjean](#la-sténo-grandjean) \
[Adaptation au Bépo](#adaptation-au-bépo) \
[Désambiguer les homophones](#désambiguer-les-homophones) \
[Outillage](#outillage) \
[À venir](#à-venir) 

```
_________________________________________             
|  B|  É|  P|  O|   |   |  V|  D|  L|  J|             
|___|___|__p|__o|___|___|__*|___|___|__$|___           
| A | U | I | E |   | C | T | S | R | N |  M|         
|___|___|___|___|___|___|___|___|___|___|___|  
|   |  Y|  X|   |  K|  '|  Q|   |   |  F|               
|___|___|___|___|___|__n|__£|___|___|___|               
```

### Installation

Le présent projet n'en est qu'à ses débuts et n'est donc pas inclu dans la liste des plug-ins du gestionnaire de Plover. Il faudra l'installer manuellement.

## Versions compatibles

Assurez-vous d'utiliser Plover 4.x (dernière version) - les versions anterieures n'incluent pas les plugins.

## Instructions

* Invoquer la commande suivante depuis un terminal (cf [Invoke Plover from the command line](https://github.com/openstenoproject/plover/wiki/Invoke-Plover-from-the-command-line) pour plus de détails)

      ```
      plover -s plover_plugins install git+https://github.com/user/repo
      ```
      
      NB: `https://github.com/user/repo.git` ne fonctionnera pas; 
   
* Vous devriez voir un message indicant `Succesfully installed`, suivi d'un nombre de paquets, suivi du plugin.

* Re-démarrez Plover

### Présentation
##### Bépo sur Grandjean: un plugin de sténographie pour le clavier bépo.
Ce plug-in est une extension pour le [logiciel de sténo Plover](https://www.openstenoproject.org/plover/), avec un système de frappes basé sur la méthode Grandjean (méthode de sténo traditionelle en français).

Sa finalité est de fournir aux bépoïstes une technique d’écriture accélérée sur leur clavier de tous les jours - par opposition à une machine de sténo - sans les contraindre à apprendre une nouvelle disposition. 
En reposant sur une disposition déjà connue du bépoïste, le temps nécessaire à l’apprentissage de la sténo est fortement réduit.

Le plug-in tient sur deux piliers: le bépo modifié pour la sténo, et le dictionnaire. Pour ce dernier, j’ai modifié le dictionnaire open-source du plug-in [Plover-France](https://github.com/azizyemloul/plover-france), en l’adaptant un peu aux contraintes du bépo.

### Cahier des charges
- doit tenir sur un clavier ortholinéaire taille 40% (càd. [un planck](https://deskthority.net/wiki/Planck)),
- doit utiliser la disposition bépo d’origine au maximum, doit modifier la disposition le moins possible.
- doit avoir un moyen de désambiguiser les mots homophones autant que possible.
- doit avoir un moyen de désambiguiser les terminaisons des conjugaisons des verbes autant que possible.

### La sténo Grandjean
Cf. [ l'excellent article de Plover France ](https://github.com/azizyemloul/plover-france-dict#%C3%A0-propos-de-la-st%C3%A9notypie) sur le fonctionnement de la sténotypie Grandjean.

### Adaptation au Bépo
- touches Grandjean modifiées 
  1. «P*» est remplacé par «B»
  2. «ᴎ» s’annote «n». Le «N» sera traité comme début de syllabe, et «n» comme fin de syllabe
  3. «£» s’annote «l». Le «L» sera traité comme début de syllabe, et «l» comme fin de syllabe
- touches Bépo modifiées 

La sténo requiert d’avoir des consonnes dupliquées - les doublons servent à différencier les consonnes de début et de fin de syllabe ("sass", sténographié "SA$"). Installer des consonnes dupliquées sur le bépo impose de modifier la disposition d’origine. Cependant, chaque modification du bépo peut devenir une nouveauté gênante pour les bépoïstes.
Pour minimiser la gêne, la disposition actuelle suit les principes suivants:

- les lettres de début de syllabe doivent garder l’emplacement d’origine sur le bépo
- les doublons de fin de syllabe doivent être placés à des emplacements disponibles du bépo (càd. sur des touches qui ne sont pas utilisées par la méthode Grandjean).

J’ai porté une attention particulière à l’emplacement des lettres de fin de syllabe sur le clavier. Il en résulte quelques changements du bépo d’origine; ces changements sont des compromis et peuvent être appelés à changer à l’avenir - si l’on me prouve une disposition plus pratique, je serai ravi de l’intégrer dans le plug-in.
  1. «\$» se place sur «j» (frappe à l’annulaire droit)
  2. «ᴎ», devenu «n», se place sur «’» (frappe au pouce)
  3. «£», devenu «l», se place sur «q» (frappe au pouce ou index)
  4. «\*» se place sur «v» (frappe à l'index)

### Désambiguer les homophones
Parce que le français est une langue orthographique avant que phonétique, et que la sténo est une méthode phonétique avant qu’orthographique, toute transcription sténographique est vouée à souffrir des ambiguités phonétiques de la langue. C’est à dire qu’un même son peut correspondre à plusieurs mots: «ces», «ses», «c’est», «s’est», «sais», «sait»; et que ce son ne peut être sténographié que par une seule frappe: «SE». Cette spécificité du français défie toute méthode de transcription phonétique, et impose l’usage d’un moyen de désambiguiser les orthographies d’un même son. 

  Plusieurs méthodes de désambiguation sont utilisées par la sténo dans d’autres langues: 

    -ajout de frappes-préfixes 
    -ajout de frappes-suffixes

  Le présent projet fait cependant usage d’une touche «orthographie». Utilisée comme suffixe, ou placée dans la dernière syllabe d’un mot, elle converti les fins de syllabe en terminaisons orthographiques. Ainsi, «terminés» peut être frappé «TEl/MI/NÉE\$»: la touche d’orthographie «É» indique que le «\$» est en fait une terminaison en «s». On pourra ainsi conjuguer les homophones d’un verbe:

```
  «terminé»: «TEl/MI/NE» 
  «terminer»: «TEl/MI/NÉEl» ou «TEl/MI/NE/Él»
  «terminés»: «TEl/MI/NÉE\$» ou «TEl/MI/NÉE» ou «TEl/MI/NE/É» ou «TEl/MI/NE/É$»
  «terminai»: «TEl/MI/NÉEI» ou «TEl/MI/NE/ÉI»
  «terminais»: «TEl/MI/NÉEI\$» ou «TEl/MI/NEI$»
  «terminait»: «TEl/MI/NÉEID» ou «TEl/MI/NE/ÉID»
  «terminaient»: «TEl/MI/NÉEn» ou «TEl/MI/NÉEIn» ou «TEl/MI/NÉEInD» ou «TEl/MI/NE/Én» ou «TEl/MI/NE/ÉnD» 
```

   Cette touche ne couvre pas tous les cas d’ambiguités, mais pose un bon départ pour les conjuguaisons des verbes, et permet de distinguer le nombre des noms communs.


### Outillage
##### Plug-in
structure du plugin

  - le fichier sténo.py d’un côté, et 
  - le dico de l’autre.
##### Dictionnaire
Le dico doit être le plus catégorisé possible, par fichiers: 
  - **Verbes**: un fichier par groupe de verbes (1er groupe, 2e groupe, 3e groupe)
  - **Noms communs**: un fichier par genre/nombre (masculin/singulier, masculin/pluriel, féminin/singulier, féminin/pluriel)
  - **Adverbes**: un seul fichier (pour le moment)
  - **Chiffres**: un seul fichier
  - **Adjectifs**: un fichier par nombre
  - **Commandes**: un fichier contenant les commandes destinées à la manœuvre de Plover
##### Conjugueur
Un répositoire de scripts en typescript servant à: 
  conjuguer les verbes, 
  accorder les noms communs, 
  filtrer les dictionnaires du projet-parent [Plover-France](https://github.com/azizyemloul/plover-france-dict)
  adjoindre les frappes de désambiguisation, etc.


### À venir:
  Le présent projet n’est malheureusement pas encore utilisable au quotidien - son dictionnaire est encore trop incomplet. 
  Pour tout utilisateur intéressé à contribuer, les PR sont les bienvenues. 

##### Feuille de route:
- Inclure les verbes du premier et deuxième groupe manquants (la liste des frappes à monter est dans le répo «Conjugueur»)
- Inclure les conjuguaisons du troisième groupe (liste aussi présente dans le «Conjugueur»)
- Ajouter les frappes de désambiguisation partout où c’est nécessaire et nettoyer le dictionnaire
- Inclure d’autres touches de désambiguisation (parmi les hypothèses, «Ç» pour désambiguiser les «ses» et «ces»)


