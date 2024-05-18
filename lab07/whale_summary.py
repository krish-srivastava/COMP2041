#!/usr/bin/env python3
import re
import sys

# Check if a filename argument is provided
if len(sys.argv) < 2:
    print("Please provide a filename as a command line argument.")
    sys.exit(1)

filenames = sys.argv[1:]

# Read the file and extract the column of interest
columns = []
for filename in filenames:
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split()
            if line:
                columns.append(line)

# Combine everything after the second column, as thats the name of the animal
for i in range(len(columns)):
    combined_value = ' '.join(columns[i][2:])
    combined_value = combined_value.lower()
    combined_value = re.sub(r's$', '', combined_value)
    columns[i] = [columns[i][0], columns[i][1], combined_value]

sorted_columns = sorted(columns, key=lambda x: x[2])

# Create a key of all the different animals and put them into a list
animal_type = []
for sublist in sorted_columns:
    animal = sublist[2]
    animal_type.append(animal)

animal_type = list(set(animal_type))
animal_type = sorted(animal_type)

# Create a list of animals which are substrings of each other and put them into a list
edge_cases = []
for i in range(len(animal_type)):
    for j in range(i+1, len(animal_type)):
        if animal_type[i] in animal_type[j] or animal_type[j] in animal_type[i]:
            edge_cases.append(animal_type[i])

# print(edge_cases)   

# Create a dictionary to count the amount of occurrences of pods
pod_count = {}
for sublist in sorted_columns:
    animal = sublist[2]
    if animal in pod_count:
        pod_count[animal] = pod_count[animal] + 1
    else:
        pod_count[animal] = 1

# Create a dictionary to count the amount of occurrences of the animals
animal_count = {}
bottlenose_count = 0
for animal_key in animal_type:
    animal_count[animal_key] = 0
    for sublist in sorted_columns:
        animal_number = sublist[2]
        pattern = r"^" + re.escape(animal_key) + r"$"
        if re.search(pattern, animal_number):
            animal_count[animal_key] = animal_count[animal_key] + int(sublist[1])

for i in animal_type:
    pod_value = pod_count[i]
    animal_value = animal_count[i]
    output = i + " observations: " + str(pod_value) + " pods, " + str(animal_value) + " individuals"
    print(output)