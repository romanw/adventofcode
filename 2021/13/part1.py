#!/usr/bin/env python

file = open("input.txt")

x = []
y = []
folds = []
pc = True
for line in file:
    if line == '\n':
        pc = False
        continue
    if pc:
        xc, yc = line.strip().split(',')
        x.append(int(xc))
        y.append(int(yc))
    else:
        fold = line.strip().split(' ')
        folds.append(fold[2].split('='))

file.close()

cols = max(x) + 1
rows = max(y) + 1
paper = [[0] * cols for i in range(rows)]
for c in range(len(x)):
    col = x[c]
    row = y[c]
    paper[row][col] = 1

fcount = 0
for f in folds:
    if fcount > 0:
        break
    fl = int(f[1])
    if f[0] == 'x':
        # fold on col
        for fcol in range(fl+1, cols):
            for row in range(rows):
                col = fl + (fl - fcol)
                paper[row][col] += paper[row][fcol]
        cols = fl
    else:
        # fold on row
        for frow in range(fl+1, rows):
            for col in range(cols):
                row = fl + (fl - frow)
                paper[row][col] += paper[frow][col]
        rows = fl
    count = 0
    for r in range(rows):
        for c in range(cols):
            if paper[r][c] > 0:
                count += 1
    print(count)
    fcount += 1



