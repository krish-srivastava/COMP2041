#!/bin/dash

if [ "$#" -lt 2 ] || [ "$#" -gt 2 ];
    then
    echo "Usage: ""$0"" <number of lines> <string>"
    exit 1
fi

if ! [ "$1" -eq "$1" ] 2> /dev/null || [ "$1" -lt 0 ]
    then
    echo "$0": argument 1 must be a non-negative integer
    exit 1
else
    number=0
    if [ "$1" -eq 1 ]
        then
        echo "$2"
        exit 0
    fi    
    while [ "$number" -lt "$1" ]
    do
        echo "$2"
        number=$((number + 1))
    done
fi