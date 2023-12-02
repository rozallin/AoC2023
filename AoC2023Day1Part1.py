#Advent of Code 2023 Day 1 Part 1

import re

try:
    with open('input.txt') as file:
        lines = file.read().split('\n')
        result = sum(int(digits[0]) + int(digits[-1]) for line in lines if (digits := re.findall(r'[0-9]', line)))
except FileNotFoundError:
    print("File not found.")
    # Handle the error as needed
except PermissionError:
    print("Permission error.")
    # Handle the error as needed
