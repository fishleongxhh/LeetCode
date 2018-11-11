# !/bin/bash

sed -r 's#( +)#\n#g' words.txt | grep -v '^$' | sort | uniq -c | sort -r | awk -F" " '{print $NF" "$(NF-1)}'
