#!/bin/bash

# Trouve toute même frappe qui corresponde à plusieurs homophones dans les dictionnaires
# et réunis-les dans un fichier qui liste toutes les frappes dupliquées.
# De là, il devient possible d'isoler les homophones et les désambiguïser.

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

duplicatedKeys=() 

for ((i = 0;  i< ${#filesList[@]}; i++)); do
  filesToProcess=("${filesList[@]:($i+1)}")
  for ((j = 0;  j< ${#filesToProcess[@]}; j++)); do
    fileA="${filesList[$i]}"
    fileB="${filesToProcess[$j]}"

    duplicatedKeys+=( `grep -f <(grep -o ^\s*[^:]*: $fileA) $fileB` )
  done
done


dups=$(grep -o \s*[^:]*: <(for f in "${duplicatedKeys[@]}" ; do echo "$f" ; done))
echo "${dups[@]}"

outputKeys=()
for i in "${filesList[@]}" 
do
  fileA="${i}"
  outputKeys+=$(grep -Ff <(for f in "${dups[@]}" ; do echo "$f" ; done) $fileA)

done


echo "${outputKeys[@]}" | sort >> duplicatedKeys.json

