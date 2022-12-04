#!/usr/bin/env python

file = open("input")

def CampCleanup():
    total1 = 0
    total2 = 0
    for line in file:
        elf = line.strip().split(",")
        sec1 = elf[0].split("-")
        sec2 = elf[1].split("-")
        # part 1 - one range within another
        if int(sec2[0]) >= int(sec1[0]) and int(sec2[1]) <= int(sec1[1]):
            total1 += 1
        elif int(sec1[0]) >= int(sec2[0]) and int(sec1[1]) <= int(sec2[1]):
            total1 += 1
        # part 2 - one range overlaps or is within another
        if int(sec2[0]) > int(sec1[1]):
            # no overlap
            pass
        elif int(sec2[1]) < int(sec1[0]):
            # no overlap
            pass
        else:
            total2 += 1
    print("part1:", total1)
    print("part2:", total2)

CampCleanup()

file.close()
