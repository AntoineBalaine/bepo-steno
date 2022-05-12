#!/bin/bash

# filtrer les lignes dupliquées d'un fichier à l'autre
# requiert de préalablement trier les dictionnaires avec trieur.sh

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
  filesToProcess=("${filesList[@]:($i+1)}")
  for ((j = 0;  j< ${#filesToProcess[@]}; j++)); do
    fileA="${filesList[$i]}"
    fileB="${filesToProcess[$j]}"
    echo $fileA
    echo $fileB
    echo
    comm -23 $fileB $fileA | sponge $fileB

  done
  
done


