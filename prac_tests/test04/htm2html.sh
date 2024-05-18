#! /bin/dash

for file in *
do
    new_name=$(echo "$file" | sed -E 's/.htm%/.html/')
    mv "$file" "$new_name" 2>/dev/null
done