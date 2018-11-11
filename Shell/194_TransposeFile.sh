# !/bin/bash

awk -F" " '{if(NR==1) {for(i=1;i<=NF;i++) arr[i]=$i;} else {for(i=1;i<=NF;i++) arr[i]=arr[i]" "$i;}}END{arrlen=length(arr);for(i=1;i<=arrlen;i++) print arr[i]}' file2.txt
