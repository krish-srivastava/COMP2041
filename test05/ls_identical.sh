#!/bin/dash

if [ $# -lt 2 ]
    then 
    echo Usage: "$0": Expects two arguments
    exit 1
else
    :
fi 


if [ -d "$1" ] && [ -d "$2" ] && [ "$(find "$1" -type f -print -quit)" ] && [ "$(find "$2" -type f -print -quit)" ]
then
    :
else

    exit 1
fi

result=0
for file in "$1"/*
do
    for file2 in "$2"/*
    do
        if [ "$(basename "$file")" = "$(basename "$file2")" ]
        then
            cmp "$file" "$file2" >/dev/null 2>&1
            result="$?"
            if [ "$result" -eq 0 ]
            then
                echo "$(basename "$file")"
            fi                
        fi
    done
done

exit 0