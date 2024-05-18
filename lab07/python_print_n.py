#!/usr/bin/env python3

import sys
import os
import subprocess

variable = str(sys.argv[2])

output_script = """#!/usr/bin/env python3

import sys

variable = {variable}
print(variable)
""".format(variable=repr(variable))

output_filename = os.path.join(os.getcwd(), "output_script.py")

for i in range(1, int(sys.argv[1])):
    print(output_script)

# print the script
# pipe the script to python 