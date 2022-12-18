#!/usr/bin/env python

file = open("input")
#file = open("test")

def cpu():
    x = 1
    cycle = 0
    during = [20, 60, 100, 140, 180, 220]
    sum = 0

    for line in file:
        cmd = line.strip().split(" ")
        if cmd[0] == "addx":
            cycle += 1
            if cycle in during:
                sum += cycle * x
                #print("a1", cycle, x, sum)
            cycle += 1
            if cycle in during:
                sum += cycle * x
                #print("a2", cycle, x, sum)
            x += int(cmd[1])
        if cmd[0] == "noop":
            cycle += 1
            if cycle in during:
                sum += cycle * x
                #print("n", cycle, x, sum)
    print(sum)


def prt(c, x):
    c = c % 40
    if (c >= x) and (c <= x+2):
        print("#", end="")
    else:
        print(".", end="")
    if c == 0:
        print()


def crt():
    x = 1
    cycle = 0
    file.seek(0)
    for line in file:
        cmd = line.strip().split(" ")
        if cmd[0] == "addx":
            cycle += 1
            prt(cycle, x)
            cycle += 1
            prt(cycle, x)
            x += int(cmd[1])
        if cmd[0] == "noop":
            cycle += 1
            prt(cycle, x)


cpu()
crt()

file.close()
