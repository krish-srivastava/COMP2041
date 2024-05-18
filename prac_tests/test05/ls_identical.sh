#!/bin/dash

first_path="$1"
second_path="$2"

for file in "$first_path"/*
do 
    if diff "$file" "$second_path" > /dev/null 2>&1
    then
        basename "$file"
    fi
done