#!/usr/bin/env python

heightmap = []

file = open("input.txt")

for line in file:
    heightmap.append(list(line.strip()))

file.close()

for row in heightmap:
    row.insert(0, "o")
    row.append("o")

ooo = ["o"] * len(heightmap[0])
heightmap.insert(0, ooo)
heightmap.append(ooo)

risk = 0

row = 1
while row < len(heightmap) - 1:
    col = 1
    while col < len(heightmap[row]) - 1:
        count = 0
        for r in range(row -1, row + 2):
            for c in range(col - 1, col + 2):
                if r != row or c != col:
                    if heightmap[row][col] < heightmap[r][c]:
                        count += 1
        if count == 8:
            risk += int(heightmap[row][col]) + 1
        col += 1
    row += 1

print("risk = ", risk)
