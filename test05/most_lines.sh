#!/bin/dash

if [ $# -lt 1 ]
    then 
    echo Usage: "$0": Expects three arguments
    exit 1
else
    :
fi 

max_lines=0
max_files=""

for file in "$@"
do 
    line_count=$(wc -l  < "$file")
    if [ "$line_count" -gt "$max_lines" ]
    then
        max_lines=$line_count
        max_files=$file
    else
        :
    fi
done

echo "$max_files"