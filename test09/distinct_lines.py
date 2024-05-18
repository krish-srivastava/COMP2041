#!/usr/bin/env python3

import sys

value = True
amount_of_lines = int(sys.argv[1])
string_list = []
count = 0

try:
    while (value == True):
        count = count + 1
        input_str = input().split()
        input_str = ' '.join(input_str)
        input_str = input_str.strip()
        input_str = input_str.lower()
        string_list.append(input_str)
        string_set = set(string_list)
        if (len(string_set) == amount_of_lines):
            print(str(amount_of_lines)+" distinct lines seen after "+str(count)+" lines read.")
            value = False
except:
    print("End of input reached after "+str(count-1)+" lines read - "+str(amount_of_lines)+" different lines not seen.")
