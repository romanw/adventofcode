#!/usr/bin/env python

file = open("input.txt", "r")

prev = int(file.readline())
count = 0

for line in file:
  curr = int(line)
  if curr > prev:
    count += 1
  prev = curr

file.close()

print(count)
