#!/usr/bin/env python

file = open("input.txt")

data = []
for line in file:
    c1, c2 = line.strip().split("-")
    data.append([c1, c2])

file.close()

visited = []
count = 0
def next(src, dst, h):
    global count
    h += dst + ", "
    if src.islower() and not src in visited:
        visited.append(src)
    for p in data:
        if p[0] == dst:
            if p[1] in visited:
                continue
            if p[1] == 'end':
                #print(h + p[1])
                count += 1
                continue
            next(dst, p[1], h)
        elif p[1] == dst:
            if p[0] in visited:
                continue
            if p[0] == 'end':
                #print(h + p[0])
                count += 1
                continue
            next(dst, p[0], h)
    if src in visited:
        visited.pop()

for p in data:
    if p[0] == 'start':
        next(p[0], p[1], 'start, ')
    elif p[1] == 'start':
        next(p[1], p[0], 'start, ')

print()
print(count)
