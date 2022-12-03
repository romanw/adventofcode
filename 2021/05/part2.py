#!/usr/bin/env python

import time
start_time = time.time()

grid_size = 1000
grid = [[0] * grid_size for i in range(grid_size)]

file = open("input.txt", "r")

for line in file:
    line = line.split("->")
    x1, y1 = line[0].strip().split(",")
    x2, y2 = line[1].strip().split(",")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    if x1 == x2:
        step = 1
        if y2 < y1:
            step = -1
        for i in range(y1, y2 + step, step):
            grid[i][x1] += 1
    elif y1 == y2:
        step = 1
        if x2 < x1:
            step = -1
        for i in range(x1, x2 + step, step):
            grid[y1][i] += 1
    else:
        if abs(x2-x1) == abs(y2-y1):
            xstep = 1
            ystep = 1
            if x2 < x1:
                xstep = -1
            if y2 < y1:
                ystep = -1
            x = x1
            y = y1
            for i in range(abs(x2-x1)+1):
                grid[y][x] += 1
                x += xstep
                y += ystep

    
file.close()

count = 0
for x in range(grid_size):
    for y in  range(grid_size):
        if grid[x][y] > 1:
            count += 1

print(count)

print("--- runtime %s seconds ---" % (time.time() - start_time))
