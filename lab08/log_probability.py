#!/usr/bin/env python3

import glob
import sys
import re
import math
from collections import Counter

passed_string = ' '.join(sys.argv[1:])
words = passed_string.split()
file_list = sorted(glob.glob("lyrics/*.txt"))
files_dict = {}

def count_words(word, file):
    pattern = r'\b' + word + r'\b'
    regex = re.compile(pattern, re.IGNORECASE)
    with open(file, 'r') as file2:
        file_contents = file2.read()
        result = re.findall(regex, file_contents)
    return len(result)


# Counts the total amount of words in the file.
total_words = {}
pattern = r'[a-zA-Z]+'
for file in file_list:
    with open(file, 'r') as file2:
        file_contents = file2.read()
        result = re.findall(pattern, file_contents)    
        result = [word for word in result if word.strip()]  
        total_words[file] = len(result)

# Counts the occurrence of each word in the file.
for file in file_list:
    files_dict[file] = Counter()
    with open(file, 'r') as file2:  
        file_contents = file2.read()
        for word in words:
            word_dict = Counter()
            occurrences = count_words(word, file) + 1
            # value = occurrences / total_words[file]
            word_dict[word] = occurrences / total_words[file]
            files_dict[file].update(word_dict)
    
# Print this out in the correct format
total_sum_words = {}
for file, word_counts in files_dict.items():
    total_sum = 0
    pattern = r'lyrics/(.*).txt'
    result = re.findall(pattern, file)
    result_with_spaces = re.sub('_', ' ', result[0])
    for word, count in word_counts.items():
        count_formatted = math.log(count)
        total_sum += count_formatted
        total_sum_words[file] = total_sum    
    print(f"{total_sum:10.5f} {result_with_spaces}")
