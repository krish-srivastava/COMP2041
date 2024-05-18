#!/bin/dash

# Error checking for amount of arguments
if [ "$#" -lt 1 ]
then 
    echo "Usage: $0 <filenames>" >&2
    exit 1
else 
    :
fi 

# Find the file in the working directory 
src_file="$(realpath -e "$1")" 2>/dev/null
file_name=$(basename "$src_file")

# Create the file for the src_file to be copied into
count=$(find . -type f \! -name "$file_name" -regex ".*/\.n\.txt\.[0-9]+$" -o -name "n.txt" | wc -l)
count=$((count - 1))
new_file=".$file_name.$count"
touch "$new_file"

# Find the path of the src_file
dest_file="$(realpath -e "$new_file")" 2>/dev/null

# Copy the src file into the destination path
cp "$src_file" "$dest_file"

echo Backup of "'$1'" saved as "'$new_file'"