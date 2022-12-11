#!/usr/bin/env python

file = open("input")
#file = open("test")

copse = []

def visibleLeft(r, c):
    visible = True
    count = 0
    col = c-1
    while col >= 0:
        if int(copse[r][col]) >= int(copse[r][c]):
            visible = False
            count += 1
            break
        col -= 1
        count += 1
    return [visible, count]

def visibleRight(r, c):
    visible = True
    count = 0
    col = c+1
    while col < len(copse[0]):
        if int(copse[r][col]) >= int(copse[r][c]):
            visible = False
            count += 1
            break
        col += 1
        count += 1
    return [visible, count]

def visibleUp(r, c):
    visible = True
    count = 0
    row = r-1
    while row >= 0:
        if int(copse[row][c]) >= int(copse[r][c]):
            visible = False
            count += 1
            break
        row -= 1
        count += 1
    return [visible, count]

def visibleDown(r, c):
    visible = True
    count = 0
    row = r+1
    while row < len(copse):
        if int(copse[row][c]) >= int(copse[r][c]):
            visible = False
            count += 1
            break
        row += 1
        count += 1
    return [visible, count]

def countVisible(g):
    h = len(g)
    w = len(g[0])
    count = 0
    row = 0
    while row < h:
        col = 0
        while col < w:
            if g[row][col] > 0:
                count += 1
            col += 1
        row += 1
    return count

def bestView(v):
    h = len(v)
    w = len(v[0])
    view = 0
    row = 0
    while row < h:
        col = 0
        while col < w:
            if v[row][col] > view:
                view = v[row][col]
            col += 1
        row += 1
    return view


def treeHouse():
    for line in file:
        copse.append(line.strip())
    file.close()
    h = len(copse)
    w = len(copse[0])
    grid = [[0 for i in range(w)] for j in range(h)]
    view = [[1 for i in range(w)] for j in range(h)]
    visible = 0
    row = 1
    while row < h-1:
        col = 1
        while col < w-1:
            v = visibleLeft(row, col)
            if v[0]:
                grid[row][col] += 1
            if v[1] > 0:
                view[row][col] *= v[1]
            v = visibleRight(row, col)
            if v[0]:
                grid[row][col] += 1
            if v[1] > 0:
                view[row][col] *= v[1]
            v = visibleUp(row, col)
            if v[0]:
                grid[row][col] += 1
            if v[1] > 0:
                view[row][col] *= v[1]
            v = visibleDown(row, col)
            if v[0]:
                grid[row][col] += 1
            if v[1] > 0:
                view[row][col] *= v[1]
            col += 1
        row += 1
    cnt = countVisible(grid)
    print(cnt + h*2 + w*2 - 4)
    print(bestView(view))

treeHouse()
