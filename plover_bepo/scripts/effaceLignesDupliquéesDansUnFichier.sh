#!/bin/bash

# Dans un fichier, efface toute ligne qui apparaît plus d'une fois

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
 awk '!seen[$0]++' "${filesList[$i]}" | sponge "${filesList[$i]}"
done


