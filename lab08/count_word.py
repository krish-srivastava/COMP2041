#!/usr/bin/env python3
import sys
import re

pattern = r'\b' + sys.argv[1] + r'\b'
regex = re.compile(pattern, re.IGNORECASE)

input_text = sys.stdin.read()
result = re.findall(regex, input_text)
print(str(sys.argv[1]) + " occurred " + str(len(result)) + " times")
