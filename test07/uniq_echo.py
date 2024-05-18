import sys

unique_args = []
seen = set()

for arg in sys.argv[1:]:
    if arg not in seen:
        unique_args.append(arg)
        seen.add(arg)

print(' '.join(unique_args))
