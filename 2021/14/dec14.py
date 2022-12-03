#!/usr/bin/env python

file = open("test.txt")
#file = open("input.txt")

template = ""
rules = []

nl = False
for line in file:
    if line == '\n':
        nl = True
        continue
    if not nl:
        template = line.strip()
    else:
        rules.append(line.strip().split(' -> '))

file.close()

def part1():
    polymer = template
    #print(polymer)
    steps = 40
    for s in range(steps):
        print(s, end='\r')
        p = ""
        for i in range(len(polymer)-1):
            pair = polymer[i] + polymer[i+1]
            #print(i, polymer, pair)
            for r in rules:
                if r[0] == pair:
                    p += pair[0] + r[1]
                    break
            #print(i, polymer, pair, p)
        polymer = p + pair[1]
        #print(polymer, len(polymer))
    print()
    chr = [0] * 26
    for c in polymer:
        i = ord(c) - ord('A')
        chr[i] += 1
    _min = 9e12
    _max = 0
    for c in chr:
        if c > 0:
            if c > _max:
                _max = c
            elif c < _min:
                _min = c
    print(_max - _min)
                




print("14 December 2021")
part1()
print()
