#!/usr/bin/env python

file = open("input")

def print_top_crates(stack):
    for i in range(9):
        print(stack[i].pop(), end="")
    print()

def part1():
    stack = [[], [], [], [], [], [], [], [], []]
    for line in file:
        if len(line) <= 1:
            continue
        if line[1] == "1":
            continue
        if line[0] == "m":
            procedure = line.strip().split(" ")
            num = int(procedure[1])
            frm = int(procedure[3])
            to = int(procedure[5])
            for i in range(num):
                crate = stack[frm-1].pop()
                stack[to-1].append(crate)
            continue
        for i in range(9):
            crate = line[i*4+1]
            if crate >= "A" and crate <= "Z":
                stack[i].insert(0, line[i*4+1])
    print_top_crates(stack)

def part2():
    file.seek(0)
    stack = [[], [], [], [], [], [], [], [], []]
    ts = []
    for line in file:
        if len(line) <= 1:
            continue
        if line[1] == "1":
            continue
        if line[0] == "m":
            procedure = line.strip().split(" ")
            num = int(procedure[1])
            frm = int(procedure[3])
            to = int(procedure[5])
            #breakpoint()
            for i in range(num):
                crate = stack[frm-1].pop()
                ts.append(crate)
            for i in range(num):
                crate = ts.pop()
                stack[to-1].append(crate)
            continue
        for i in range(9):
            crate = line[i*4+1]
            if crate >= "A" and crate <= "Z":
                stack[i].insert(0, line[i*4+1])
    print_top_crates(stack)

part1()
part2()


file.close()
