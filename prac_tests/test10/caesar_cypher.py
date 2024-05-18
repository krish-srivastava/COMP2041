#!/usr/bin/env python3

import sys

string = []
final_string = ""
cypher = int(sys.argv[1])

for lines in sys.stdin:
    string.append(lines)

for lines in string:
    for char in lines:
        if char.isalpha():
            if char.islower():
                base = ord('a')
                new = ((ord(char) - base + cypher) % 26 + base)
                final_string += chr(new)
            elif char.isupper(): 
                base = ord('A')
                new = ((ord(char) - base + cypher) % 26 + base)
                final_string += chr(new)
        else:
            final_string += char
    
print(final_string, end='')
