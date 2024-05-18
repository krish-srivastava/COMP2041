#!/bin/dash

if [ $# -lt 2 ]
    then 
    echo Usage: $0: Expects two arguments
    exit 1
else
    :
fi 

number=1
while test $number -le "$1"
do
    file_name="hello$number"
    content="hello $2"
    echo "$content" > "$file_name.txt"
    number=$((number + 1))
done
exit 0