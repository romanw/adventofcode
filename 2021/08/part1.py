#!/usr/bin/env python

# 0 = abcefg
# 1 = cf    *
# 2 = acdeg
# 3 = acdfg
# 4 = bcdf  *
# 5 = abdfg
# 6 = abdefg
# 7 = acf   *
# 8 = abcdefg   *
# 9 = abcdfg

file = open("input.txt")

count = 0
for line in file:
    patterns, output = line.split("|")
    values = output.strip().split()
    for value in values:
        l = len(value)
        if l == 2 or l == 4 or l == 3 or l == 7:
            count += 1

file.close()

print(count)
