#!/bin/bash

# SUBSTITUE LES FRAPPES DUPLIQUÉES 
# prend un fichier json contenant les frappes dupliquées des dictionnaires,
# ainsi qu'un dossier contenant les dictionnaires
# trouve les frappes dupliquées qui contiennent une substitution suivant le format 
# FRAPPEDUPLIQUÉE: MOT, FRAPPEDESUBSTITUTION: MOT
# trouve la paire «frappeDupliquée:mot» originelle dans les dictionnaires
# remplace-la par la substitution
# efface la ligne frappeDupliquée+substitution du fichier des dupliquées

duplicatedKeysFile=$1
dictionnaryDirectory=$2

if [ -z $1 ] || [ -z $2 ] ; then 
    echo "Usage: ./substitueur.sh duplicatedKeysFile dictionnaryDirectory"
    exit 1
fi
if [[ ! -f "$duplicatedKeysFile" ]] ; then
  echo "Duplicated keys file doesn't exist"
  exit 1
fi
if [ $(find "$dictionnaryDirectory" -name "$duplicatedKeysFile") ] ; then
  echo "Duplicated keys file cannot be in dictionnary directory"
  exit 1
fi
if [[ ! -d "$dictionnaryDirectory" ]] ; then
  echo "Dictionnaries folder doesn't exist"
  exit 1
fi

IFS=""
substitutionLines=($(grep ",\s*\"" $duplicatedKeysFile))

for line in "${substitutionLines[@]}" ; do
  IFS=',' 
  read -ra originalAndSubstitute <<< "$line"
  fileNames=($(grep -H -R "${originalAndSubstitute[0]}" $dictionnaryDirectory | cut -d: -f1))

  for i in "${fileNames[@]}"; do
    original=$(printf '%q\n' "${originalAndSubstitute[0]}")
    substitute=$(printf '%q\n' "${originalAndSubstitute[1]}")
    fullLine=$(printf '%q\n' "${line}" )
    sed "s/$original/$substitute/" $i | sponge $i
    sed "/$fullLine/d" $duplicatedKeysFile | sponge $duplicatedKeysFile

  done
done
