#!/usr/bin/env python

heightmap = []

file = open("input.txt")

for line in file:
    sl = list(line.strip())
    im = map(int, sl)
    heightmap.append(list(im))

file.close()

for row in heightmap:
    row.insert(0, 11)
    row.append(11)

oob = [11] * len(heightmap[0])
heightmap.insert(0, oob)
heightmap.append(oob)

visited = []

def basin(r, c):
    global visited
    visited.append([r, c])
    depth = 1
    # north
    n = heightmap[r-1][c]
    if n < 9:
        if not ([r-1, c] in visited):
            depth += basin(r-1, c)
    # south
    n = heightmap[r+1][c]
    if n < 9:
        if not ([r+1, c] in visited):
            depth += basin(r+1, c)
    # east
    n = heightmap[r][c+1]
    if n < 9:
        if not ([r, c+1] in visited):
            depth += basin(r, c+1)
    # west
    n = heightmap[r][c-1]
    if n < 9:
        if not ([r, c-1] in visited):
            depth += basin(r, c-1)
    return depth

risk = 0
basins = []

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
            risk += heightmap[row][col] + 1
            b = basin(row, col)
            basins.append(b)
        col += 1
    row += 1

print("risk = ", risk)

b = sorted(basins, reverse=True)
print(b[0] * b[1] * b[2])
