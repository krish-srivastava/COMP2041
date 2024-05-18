#!/bin/dash

sort -t'|' -k2 | cut -d '|' -f2,3 | sort | uniq | cut -d '|' -f2 | cut -d ',' -f2 | cut -d ' ' -f2 | sort | uniq -c | sort -nr | head -n1 | sed 's/^ *[0-9]\{1,\} //'