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

src_path=$(find . -type d -regex ".*/\.snapshot\.$1")
commit_path="$(pwd)"

cd "$src_path" || return

for file in *
do
    src_path="$(realpath -e "$file")"
    cp "$src_path" "$commit_path"
done

echo "Restoring snapshot $1"