#!/usr/bin/env python3

import sys
import re

pattern = r'[a-zA-Z]+'

input_text = sys.stdin.read()
result = re.findall(pattern, input_text)    
result = [word for word in result if word.strip()]
print(str(len(result)) + " words")