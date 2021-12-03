#!/usr/bin/env python

import time
start_time = time.time()

file = open("input.txt", "r")

bitarray = [0] * 12

for line in file:
  i = 0
  for bit in line:
    if bit == "1":
      bitarray[i] += 1
    elif bit == "0":
      bitarray[i] -= 1
    i += 1
    
file.close()

gamma = ""
epsilon = ""

for i in range(12):
  if bitarray[i] > 0:
    gamma += "1"
    epsilon += "0"
  else:
    gamma += "0"
    epsilon += "1"

print(int(gamma,2) * int(epsilon,2))

print("--- runtime %s seconds ---" % (time.time() - start_time))
