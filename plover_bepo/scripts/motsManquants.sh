#!/bin/bash

readarray -t myArray < "$1"

echo "$2"

for item in "${myArray[@]}"; do
if rg -Fq "$item" "${@:2}"; then
:
else
echo "$item" >> verbesManquants.txt
fi;

done
