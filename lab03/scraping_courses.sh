#!/bin/dash

case $# in
    2)
    YEAR=$1
    CODE=$2
    ;;
    *)
    echo "Usage: $0 <year> <course-prefix>" >& 2
    exit 1
esac


if [ "$YEAR" -ge 2019 ] 2> /dev/null && [ "$YEAR" -le 2022 ] 2> /dev/null; then
    :
else
    echo "$0: argument 1 must be an integer between 2019 and 2022" >& 2
    exit 1
fi


( curl -LS "https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:2021%20+unsw_psubject.studyLevel:undergraduate%20+unsw_psubje"
curl -LS "https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:2021%20+unsw_psubject.studyLevel:postgraduate%20+unsw_psubjec"
) |
jq -r '.["contentlets"][] | (.code + " " + .title|gsub("[\\n\\t]"; " "))' |
tr -s '[:blank:]' ' ' | # squeeze whitespace
sed -E 's/\s$//' | # remove trailing whitespace 
sort |
uniq

exit 0