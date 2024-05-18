#!/usr/bin/env python3

import sys
from collections import Counter

def count_duplicates(iterable):
    counter = Counter(numbers_list)
    most_common = counter.most_common(1)
    
    if most_common:
        return most_common[0][0]
    else:
        return None

def find_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        median = sorted_numbers[length // 2]
    else:
        middle1 = sorted_numbers[length // 2 - 1]
        middle2 = sorted_numbers[length // 2]
        median = (middle1 + middle2) / 2

    return median

def convert_float_to_int_if_possible(number):
    if number % 1 == 0:  # Check if the decimal part is zero
        return int(number)
    else:
        return number

count = len(sys.argv) - 1
numbers_list = list()

for arg in sys.argv[1:]:
    number = int(arg)
    numbers_list.append(number)

unique_numbers = set(numbers_list)
unique = len(unique_numbers)

minimum = numbers_list[0]
for number in numbers_list:
    if number < minimum:
        minimum = number

maximum = numbers_list[0]
for number in numbers_list:
    if number > maximum:
        maximum = number

sum = 0
mean = 0
for number in numbers_list:
    sum += number
mean = sum / count

mean = convert_float_to_int_if_possible(mean)

mode = 0
if (unique == len(numbers_list)):
    mode = numbers_list[0]
else:
    mode = count_duplicates(numbers_list)

product = 1
for number in numbers_list:
    product *= number

median = find_median(numbers_list)

print("count="+str(count))
print("unique="+str(unique))
print("minimum="+str(minimum))
print("maximum="+str(maximum))
print("mean="+str(mean))
print("median="+str(median))
print("mode="+str(mode))
print("sum="+str(sum))
print("product="+str(product))