#!/usr/bin/env python

file = open("input.txt")

ob = "([{<"
cb = ")]}>"
pt = [ 3, 57, 1197, 25137 ]

points = 0
for line in file:
    stack = []
    for c in line:
        i = ob.find(c)
        if i >= 0:
            stack.append(i)
        else:
            i = cb.find(c)
            if i >= 0:
                s = stack.pop()
                if i != s:
                    points += pt[i]
                    #print("Expected " + cb[s] + ", but found " + cb[i] + " instead.")
                    break
                

file.close()

print(points)
