#!/usr/bin/env python3

import glob
import sys
import re

def word_total(file):
    pattern = r'\b' + sys.argv[1] + r'\b'
    with open(file, 'r') as file2:  
        file_contents = file2.read()      
        regex = re.compile(pattern, re.IGNORECASE)
        result = re.findall(regex, file_contents)    

    return len(result)

def total(file):
    pattern = r'[a-zA-Z]+'
    with open(file, 'r') as file2:       
        file_contents = file2.read() 
        result = re.findall(pattern, file_contents)    
        result = [word for word in result if word.strip()]
        return len(result)

total_dict = {}
word_dict = {}

file_list = sorted(glob.glob("lyrics/*.txt"))

for file in file_list:
    total_dict[file] = total(file)
    word_dict[file] = word_total(file)
    var3 = word_dict[file]/total_dict[file]
    pattern = r'lyrics/(.*).txt'
    result = re.findall(pattern, file)
    result_with_spaces = re.sub('_', ' ', result[0])
    print(f"{word_dict[file]:4}/{total_dict[file]:6} = {var3:.9f} {result_with_spaces}")
