#!/bin/dash

start_amount=1
end_amount="$1"
string_name="$2"

while [ "$start_amount" -le "$end_amount" ]
do
    echo "hello $string_name" > "hello$start_amount.txt"
    start_amount=$((start_amount + 1))
done