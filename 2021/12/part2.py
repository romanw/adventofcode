#!/usr/bin/env python

file = open("input.txt")

data = []
caves = []
for line in file:
    c1, c2 = line.strip().split("-")
    data.append([c1, c2])
    if not c1 in caves:
        if c1 != 'start' and c1 != 'end' and c1.islower():
            caves.append(c1)
    if not c2 in caves:
        if c2 != 'start' and c2 != 'end' and c2.islower():
            caves.append(c2)

file.close()

visited = []
count = 0
paths = []

def visits(cave):
    v = 0
    if cave in visited:
        for c in visited:
            if c == cave:
                v += 1
    return v
        
def next(src, dst, h, twice):
    global count
    global ci
    h += dst + ", "
    if src.islower():
        visited.append(src)
    for p in data:
        if p[0] == dst:
            if visits(p[1]) > int(p[1] == twice):
                continue
            if p[1] == 'end':
                path = h + p[1]
                if not path in paths:
                    paths.append(path)
                    count += 1
                continue
            next(dst, p[1], h, twice)
        elif p[1] == dst:
            if visits(p[0]) > int(p[0] == twice):
                continue
            if p[0] == 'end':
                path = h + p[0]
                if not path in paths:
                    paths.append(path)
                    count += 1
                continue
            next(dst, p[0], h, twice)
    if src in visited:
        visited.pop()

for p in data:
    for cave in caves:
        if p[0] == 'start':
            next(p[0], p[1], 'start, ', cave)
        elif p[1] == 'start':
            next(p[1], p[0], 'start, ', cave)

print()
print(count)
