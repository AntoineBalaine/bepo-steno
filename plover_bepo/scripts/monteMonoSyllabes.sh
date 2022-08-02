#!/bin/bash

echo "{
$(rg "^[^/]*:" "$1"  | sed 's/":/ß":/' | sed 's/",/{^ ^}",/')
}" > "monosyllabes.json"

