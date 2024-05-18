#!/usr/bin/env python3

import sys

# Split the input into lines
# Split the lines into words 
# Split the words into letters
    # Count the amount of letters in the word using a dictionary
    # Check that the counts of each dictionary are unique or 1.

def helper(word):
    letters = {}
    for letter in word.lower():
        letters[letter] = letters.get(letter, 0) + 1
    return len(set(letters.values())) == 1 

for lines in sys.stdin:
    words = lines.split()
    processed_words = filter(helper, words)
    print(" ".join(processed_words))