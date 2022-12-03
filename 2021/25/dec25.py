#!/usr/bin/env python

cucmap = []
file = open("input.txt", "r")
for line in file:
    cucmap.append(list(line.strip()))
file.close()

#for row in cucmap:
#    print(row)
h = len(cucmap)
w = len(cucmap[0])

def moveeast():
    moves = 0
    row = 0
    while row < h:
        col = 0
        cm = [cucmap[row][c] for c in range(w)]
        while col < w:
            if cm[col] == '.':
                pc = col - 1
                if pc < 0:
                    pc = w - 1
                if cm[pc] == '>':
                    cucmap[row][col] = '>'
                    cucmap[row][pc] = '.'
                    moves += 1
                    #col += 1
            col += 1
        row += 1
    return moves

def movesouth():
    moves = 0
    col = 0
    while col < w:
        row = 0
        rm = [cucmap[r][col] for r in range(h)]
        #print("rm = ", rm)
        while row < h:
            #print(row, col)
            if rm[row] == '.':
                pr = row - 1
                if pr < 0:
                    pr = h - 1
                if rm[pr] == 'v':
                    cucmap[row][col] = 'v'
                    cucmap[pr][col] = '.'
                    moves += 1
                    #row += 1
            row += 1
        col += 1
    return moves

def part1():
    steps = 1
    while True:
    #for i in range(60):
        me = moveeast()
        ms = movesouth()
        if me == 0 and ms == 0:
            break
        steps += 1

    print(steps)
    #for row in cucmap:
    #    print(row)

part1()



