#!/bin/dash

starting_number=0
ending_number=0

starting_number=$1
ending_number=$2

while [ "$starting_number" -lt "$ending_number" ]
do
    echo "$starting_number" >> "$3"
    starting_number=$((starting_number + 1))
done

echo "$starting_number" >> "$3"
