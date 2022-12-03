#!/usr/bin/env python

file = open("input")

def part1():
    mostCals = 0
    elf = 1
    sum = 0
    highCals = []
    for line in file:
        if line == "\n":
            if sum > mostCals:
                print(elf, sum)
                mostCals = sum
                highCals.append(sum)
            elf += 1
            sum = 0
        else:
            sum += int(line)
    return highCals

def part2(hc):
    print(sum(hc[-3:]))


hc = part1()
part2(hc)
