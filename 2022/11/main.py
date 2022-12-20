#!/usr/bin/env python

import re
import math

file = open("input")
#file = open("test")

items = [[] for i in range(8)]
op = [[] for i in range(8)]
test = [[] for i in range(8)]
iftrue = [[] for i in range(8)]
iffalse = [[] for i in range(8)]
inspected = [0 for i in range(8)]
supermod = 1

def processFile():
    global supermod
    monkey = 0
    monkeys = 0
    file.seek(0)
    for line in file:
        if line == "\n":
            continue
        l = line.strip().split(":")
        if "Monkey" in l[0]:
            m = l[0].split(" ")
            monkey = int(re.sub("[^0-9]", "", m[1]))
            monkeys += 1
        elif "Starting" in l[0]:
            si = l[1].strip().split(", ")
            for i in si:
                items[monkey].append(int(i))
        elif "Operation" in l[0]:
            o = l[1].strip().split(" ")
            op[monkey] = [o[3], o[4]]
        elif "Test" in l[0]:
            tst = l[1].strip().split(" ")
            test[monkey] = int(tst[2])
            supermod *= test[monkey]
        elif "true" in l[0]:
            t = l[1].strip().split(" ")
            iftrue[monkey] = int(t[3])
        elif "false" in l[0]:
            f = l[1].strip().split(" ")
            iffalse[monkey] = int(f[3])
        else:
            print(f"oops {l = }")
    return monkeys

def doRound(monkeys, part):
    for monkey in range(monkeys):
        for item in items[monkey]:
            worry = 0
            opval = 0
            if op[monkey][1] == "old":
                opval = item
            else:
                opval = int(op[monkey][1])
            if op[monkey][0] == "*":
                worry = item * opval
            elif op[monkey][0] == "+":
                worry = item + opval
            if part == 1:
                worry = math.floor(worry / 3)
            if part == 2:
                worry %= supermod
            if worry % test[monkey] == 0:
                items[iftrue[monkey]].append(worry)
            else:
                items[iffalse[monkey]].append(worry)
            inspected[monkey] += 1
        items[monkey].clear()


def part1():
    for r in range(20):
        doRound(monkeys, 1)

def part2():
    for r in range(10000):
        doRound(monkeys, 2)



monkeys = processFile()

#part1()
part2()

inspected.sort(reverse=True)
print(inspected[0] * inspected[1])

file.close()
