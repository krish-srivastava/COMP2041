#!/usr/bin/env python3

import sys

src_file = sys.argv[1]
dest_file = sys.argv[2]

line_list = []

with open(src_file, "r") as filename:
    lines = filename.readlines()

    for line in lines:
        line_list.append(line)

with open(dest_file, "w") as filename2:
    line_list = reversed(line_list)

    for i in line_list:
        filename2.write(str(i))
