#!/usr/bin/env python3

import sys
import re

listed_args = sys.argv[1:]
passed_args = []

for arg in listed_args:
    word = arg.lower()
    pattern = '[aeiou]{3}'
    match = re.search(pattern, word)
    if match:
        passed_args.append(arg)

completed_string = " ".join(passed_args)

print(completed_string)