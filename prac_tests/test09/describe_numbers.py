#!/usr/bin/env python3

import sys
import math

if len(sys.argv) < 1:
    print(f"Usage: {sys.argv[0]} <numbers>", file=sys.stderr)
    sys.exit(1)


def mode(list):
    mode = 0
    for num in list:
        if list.count(num) > list.count(mode):
            mode = num

    return mode

numbers = list(map(int, sys.argv[1:]))

print(f"mode={int(mode(numbers))}")
