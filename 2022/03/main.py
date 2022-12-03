#!/usr/bin/env python

#file = open("test1")
file = open("input")

def toPriority(c):
    p = 0
    if ord(c) >= ord("a"):
        p = ord(c) - ord("a") + 1
    elif ord(c) >= ord("A"):
        p = ord(c) - ord("A") + 27
    return p

def part1():
    sum = 0
    for line in file:
        s = line.strip()
        m = len(s) // 2
        c1 = s[:m]
        c2 = s[m:]
        b = ""
        for c in c1:
            if c in c2:
                b += c
        sum += toPriority(b[0])
    print(sum)

def part2():
    file.seek(0)
    g = ["", "", ""]
    c = 0
    sum = 0
    for line in file:
        g[c] = line.strip()
        c += 1
        if c >= 3:
            c = 0
            for i in g[0]:
                if (i in g[1]) and (i in g[2]):
                    sum += toPriority(i)
                    break
    print(sum)

part1()
part2()
