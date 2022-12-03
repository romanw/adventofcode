#!/usr/bin/env python

octo = []

file = open("input.txt")

for line in file:
    sl = list(line.strip())
    im = map(int, sl)
    octo.append(list(im))

file.close()

b = -1
for row in octo:
    row.insert(0, b)
    row.append(b)

oob = [b] * len(octo[0])
octo.insert(0, oob)
octo.append(oob)

def flash(rw, cl):
    octo[rw][cl] += 1
    for r in range(rw - 1, rw + 2):
        for c in range(cl - 1, cl + 2):
            if r == rw and c == cl:
                continue
            if octo[r][c] >= 0:
                octo[r][c] += 1
            if octo[r][c] == 10:
                flash(r, c)

def step1():
    row = 1
    while row < len(octo) - 1:
        col = 1
        while col < len(octo[row]) - 1:
            octo[row][col] += 1
            if octo[row][col] == 10:
                flash(row, col)
            col += 1
        row += 1

def step2():
    flashes = 0
    for r in range(len(octo)):
        for c in range(len(octo[r])):
            if octo[r][c] > 9:
                octo[r][c] = 0
                flashes += 1
    return flashes

steps = 100
flashes = 0
for step in range(steps):
    step1()
    flashes += step2()

print(flashes)
