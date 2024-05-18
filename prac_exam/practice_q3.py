#!/usr/bin/env python3

import sys

file = sys.argv[1]

with open(file, "r") as filename:
    lines = filename.readlines()

male_names = []

for line in lines:
    fields = line.strip().split('|')
    if fields[-1] == 'M':
        name_parts = fields[2].split(',')[0].strip()
        male_names.append(name_parts)

male_names = sorted(set(male_names))

for male_name in male_names:
    print(male_name)