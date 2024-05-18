#!/usr/bin/env python3

import re
import sys

lines = sys.stdin.readlines()

def round_decimal(match):
    return str(int(round(float(match.group()), 1)))

input_text = "".join(lines)

rounded_text = re.sub(r'\b\d+(\.\d+)?\b', round_decimal, input_text)

print(rounded_text)
