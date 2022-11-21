#!/bin/bash

jq 'keys' $1 | sed -e 's/\//",\n"/g' -e 's/^\s*//' | sort --unique | awk '!/[\[|\]]/' | sed -e '/[\\.]/d' -e '/,"/d' -e 's/"$/",/' -e 's/",/ß":"=space_or_split",/' -e 's/,$//' -e '1s/^/{\n/' -e 's/$/,/' | sort --unique | sed -e '$s/,$/\n}/' 
