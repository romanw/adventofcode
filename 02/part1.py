#!/usr/bin/env python

file = open("input.txt", "r")

hpos = 0
depth = 0

for line in file:
  command, amount = line.split()
  command = command.lower()
  amount = int(amount)
  if command == "down":
    depth += amount
  elif command == "up":
    depth -= amount
  elif command == "forward":
    hpos += amount
    
file.close()

print(hpos * depth)
