#!/bin/dash

if [ -z "$1" ]; then
    echo "Usage: $0 <course_prefix>"
    exit 1
fi 

course_data=$(curl --location --silent "http://www.timetable.unsw.edu.au/2023/COMPKENS.html")

first_arg="$1"
course_list=$(echo "$course_data" | grep "Kensington Campus" | grep "$1" | grep -E '<a href="[A-Z]*[0-9]*.html">[A-Za-z ]*</a>' | sort -u)

# Check if any courses were found with the given prefix
if [ -z "$course_list" ]; then
    echo "No courses found for prefix '$1' in $current_year on Kensington Campus."
else
    # Sort the course list by course code (lowest to highest)
    sorted_course_list=$(echo "$course_list" | sort -t'>' -k2,2 -k1,1 | sed 's/^.*">\(.*\)<\/a>$/\1/')
    echo "$sorted_course_list"
fi