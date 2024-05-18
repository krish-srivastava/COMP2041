#!/bin/dash

sort -t'|' -k2 | cut -d '|' -f2 | uniq -c | sort -nr | grep -E "2 " | sed 's/^ *[0-9]\{1,\} //' | sort
