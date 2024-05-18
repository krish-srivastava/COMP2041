#!/bin/dash

cut -d '|' -f 2| sort | uniq -c | sort -nr | grep -E "2 " | sed -E s'/2//' | sed -E s'/[[:space:]]*//' | sort