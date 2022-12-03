#!/usr/bin/env python

import time
start_time = time.time()

file = open("input.txt", "r")

oxygen = []
oxygen0 = []
oxygen1 = []
co2 = []
co20 = []
co21 = []

for line in file:
  oxygen.append(line.strip())
  co2.append(line.strip())
    
file.close()

for i in range(12):
  oxygen0.clear()
  oxygen1.clear()
  co20.clear()
  co21.clear()

  if len(oxygen) > 1:
    for j in oxygen:
      if j[i] == "0":
        oxygen0.append(j)
      elif j[i] == "1":
        oxygen1.append(j)
    if len(oxygen1) >= len(oxygen0):
      oxygen = list(oxygen1)
    else:
      oxygen = list(oxygen0)

  if len(co2) > 1:
    for j in co2:
      if j[i] == "0":
        co20.append(j)
      elif j[i] == "1":
        co21.append(j)
    if len(co21) >= len(co20):
      if len(co20) > 0:
        co2 = list(co20)
      else:
        co2 = list(co21)
    else:
      if len(co21) > 0:
        co2 = list(co21)
      else:
        co2 = list(co20)

print(int(oxygen[0], 2) * int(co2[0], 2))

print("--- runtime %s seconds ---" % (time.time() - start_time))
