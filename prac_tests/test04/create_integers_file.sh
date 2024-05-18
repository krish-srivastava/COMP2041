#! /bin/dash

start="$1"
max="$2"
filename="$3"

i="$start"
while [ "$i" -le "$max" ]
do
    echo "$i" >> "$filename"
    i=$((i + 1))
done