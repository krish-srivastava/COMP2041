#! /bin/dash

cut -d '|' -f 2,3 | sort -k1 | uniq | cut -d '|' -f 2 | cut -d ',' -f 2 | cut -d ' ' -f 2 | sort