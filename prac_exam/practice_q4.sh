#!/usr/bin/dash

years=$(grep -E "$1" | cut -d'|' -f2 | sort | uniq)

if [ -z "$years" ]
then 
    echo "No award matching" >&2
    exit 1
fi

start=$(echo "$years" | head -n1)
end=$(echo "$years" | tail -n1)

for year in $(seq "$start" "$end")
do
    if !( echo "$years" | grep -q "$year" )
    then
        echo "$year"

    fi
done