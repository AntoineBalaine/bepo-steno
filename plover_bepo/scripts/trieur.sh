#!/bin/bash

# Trie les lignes d'un fichier
# Étape nécessaire et préalable à comparer les dictionnaires
# et retirer toutes les lignes qui apparaissent plus d'une fois 
# entre plusieurs fichiers

filesList=(
"../dictionaries/verbesPremierGroupe.json"
"../dictionaries/verbesDeuxièmeGroupe.json"
"../dictionaries/SténoTroisièmeGroupe.json"
"../dictionaries/nomsFémininsPluriels.json"
"../dictionaries/nomsFémininsSinguliers.json"
"../dictionaries/nomsMasculinsPluriels.json"
"../dictionaries/nomsMasculinsSinguliers.json"
"../dictionaries/adjectifsSinguliersFéminins(filtrésPartiellement).json"
"../dictionaries/adjectifsPluriels.json"
"../dictionaries/adjectifsSinguliers.json"
"../dictionaries/prépositions.json"
"../dictionaries/PloverFrance_07_French_User.json"
"../dictionaries/PloverFrance_03_French_Adverbes.json"
"../dictionaries/PloverFrance_02_French_Chiffres.json"
"../dictionaries/PloverFrance_01_French_SION.json"
)

for ((i = 0;  i< ${#filesList[@]}; i++)); do
 echo "${filesList[$i]}"
 sort "${filesList[$i]}" | sponge "${filesList[$i]}"
done


