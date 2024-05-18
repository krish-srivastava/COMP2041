#!/bin/dash

for file in "$@"
do
    echo "$(wc -l "$file")" "$file"
done | sort -nr | cut -d " " -f3 | head -n 1