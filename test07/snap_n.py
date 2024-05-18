#!/usr/bin/env python3

import sys

snap_amount = int(sys.argv[1])
user_input_list = []
count = 0

a = []
for line in sys.stdin:
    line = line.strip().lower()
    a.append(line)
    if len(a) >= snap_amount:
            count = 1
            for i in range(len(a)):
                if a[i] == a[i - 1]:
                    count += 1
                    if count == snap_amount:
                        print("Snap:", a[i])
                        sys.exit()