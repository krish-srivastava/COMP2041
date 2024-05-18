#!/bin/dash

grep -E "M$" $1 | cut -d'|' -f3 | cut -d',' -f1 | sort | uniq