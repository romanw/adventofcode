#!/usr/bin/env python

file = open("input.txt", "r")

hpos = 0
depth = 0
aim = 0

for line in file:
  command, amount = line.split()
  command = command.lower()
  amount = int(amount)
  if command == "down":
    aim += amount
  elif command == "up":
    aim -= amount
  elif command == "forward":
    hpos += amount
    depth += aim * amount
    
file.close()

print(hpos * depth)
