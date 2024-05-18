#!/bin/dash

for image_file in "$@"; do
    last_modify_time=$(find . -name "$image_file" -printf "%t")
    mogrify -gravity south -pointsize 36 -draw "text 0,10 '$last_modify_time'" "$image_file" &&
    touch -d "$last_modify_time" "$image_file"
done