#!/usr/bin/env python3

import sys

input_file = sys.argv[1]

if input_file == "/dev/null":
    sys.exit(1)

with open(input_file, "r") as file:
    lines = file.readlines()

    num_of_lines = len(lines)

    if num_of_lines % 2 == 1:
        goal_line = num_of_lines // 2
        print(lines[goal_line], end="")
    else:
        first_num_goal_line = (num_of_lines // 2) - 1
        second_num_goal_line = (num_of_lines // 2)
        print(lines[first_num_goal_line], end="")
        print(lines[second_num_goal_line], end="")

