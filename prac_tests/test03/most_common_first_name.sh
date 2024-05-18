#! /bin/dash

grep -E "COMP2041|COMP9044" | cut -d "|" -f 2,3 | sort -k2 | uniq | cut -d "|" -f2 | cut -d "," -f 2 | cut -d ' ' -f 2 | uniq -c | sort -nr | head -n 1 | sed -E 's/[0-9]+//' | sed 's/^[[:space:]]*//'