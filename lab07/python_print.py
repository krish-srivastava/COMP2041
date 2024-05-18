#!/usr/bin/env python3

import sys
import os
import subprocess

if len(sys.argv) < 2:
    print("Enter the correct amount of arguments for this file")
    sys.exit(1)

variable = str(sys.argv[1])

output_script = """#!/usr/bin/env python3

import sys

variable = {variable}
print(variable)
""".format(variable=repr(variable))

output_filename = os.path.join(os.getcwd(), "output_script.py")

print(output_script)

# subprocess.run(['python3', output_filename])