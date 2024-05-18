#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <number>", file=sys.stderr)
    sys.exit(1)

uniq = set()
count = 0
distinct = int(sys.argv[1])

for elem in sys.stdin:

    if elem not in uniq:
        elem = elem.lower()
        uniq.add(' '.join(elem.split()))

    count += 1
    
    if len(uniq) == distinct:
        print(f"{len(uniq)} distinct lines seen after {count} lines read.")
        sys.exit(0)

print(f"End of input reached after {count} lines read - {distinct} different lines not seen.")