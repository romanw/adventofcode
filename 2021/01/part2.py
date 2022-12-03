#!/usr/bin/env python

file = open("input.txt", "r")

line = []

for l in file:
  line.append(int(l))
  
count = 0

for i in range(len(line)-3):
  s1 = line[i] + line[i+1] + line[i+2]
  s2 = line[i+1] + line[i+2] + line[i+3]
  if s2 > s1:
    count += 1

file.close()

print(count)
