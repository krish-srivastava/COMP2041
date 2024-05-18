#!/usr/bin/env dash

# Error checking, double check the length of the arguments is less than 2

if [ "$#" -lt 2 ]
then
    echo "Usage: $0 <number of lines> <string>" >&2
    exit 1
fi

if ! [ "$1" -eq "$1" ] 2> /dev/null
then
    echo ""$0": argument 1 must be a non-negative integer" >&2
    exit 1    
fi

if [ "$#" -gt 2 ]
then
    echo "Usage: $0 <number of lines> <string>" >&2
    exit 1
fi

if [ "$1" -lt 0 ]
then
    echo ""$0": argument 1 must be a non-negative integer" >&2
    exit 1
fi

max="$1"
string="$2"

i=1
while [ "$i" -le "$max" ]
do
    echo "$string"
    i=$((i + 1))
done