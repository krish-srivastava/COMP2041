#!/bin/dash

snapshot_save=snapshot-save.sh
snapshot_load=snapshot-load.sh
count=$(find . -type d -regex '.*/\.snapshot\.[0-9]+' | wc -l)
dir_name=".snapshot.$count"
mkdir "$dir_name"
commit_path="$(realpath -e "$dir_name")"
for file in *
do
    if [ "$file" = "$snapshot_save" ] || [ "$file" = "$snapshot_load" ]; then
        :
    else
        src_path="$(realpath -e "$file")"
        cp "$src_path" "$commit_path"
    fi
done

echo "Creating snapshot $count"