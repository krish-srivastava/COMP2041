#!/usr/bin/env python3

import sys

vowels = set('aeiouAEIOU')
lst = []

for arg in sys.argv[1:]:
    word = list(arg)
    count = 0
    for letter in word:
        if letter in vowels:
            count = count + 1
            if count == 3:
                lst.append("".join(word))
        else:
            count = 0

result_string = " ".join(lst)
print(result_string)
