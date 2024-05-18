#!/bin/dash

for htm_file in *.htm
    do
    html_file=$(echo "$htm_file" | sed -E -- 's/.htm$/.html/')
    if [ -e "$html_file" ]; then 
        echo "$html_file" exists
        exit 1
    else 
        mv "$htm_file" "$html_file"
    fi 
done