#!/bin/dash

sort -t'|' -k2 | cut -d '|' -f2,3 | sort | uniq | cut -d '|' -f2 | cut -d ',' -f2 | cut -d ' ' -f2 | sort

# cut -d '|' -f3 | sort 

# | uniq | cut -d ',' -f2 | cut -d ' ' -f2 | sort
