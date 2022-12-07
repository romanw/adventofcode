#!/usr/bin/env python

file = open("input")

def norepeat(n):
    file.seek(0)
    q = []
    for line in file:
        i = 0
        while i < len(line):
            if line[i] == "\n":
                i += 1
                continue
            if len(q) >= n:
                d = 0
                for c in q:
                    if q.count(c) > 1:
                        d +=1
                if d == 0:
                    print(i)
                    return
                q.pop(0)
            q.append(line[i])
            i += 1
            
            
            

norepeat(4)
norepeat(14)

file.close()
