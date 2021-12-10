#!/usr/bin/env python

file = open("input.txt")

ob = "([{<"
cb = ")]}>"
pt = [ 3, 57, 1197, 25137 ]

points = 0
scores = []
for line in file:
    stack = []
    count = 0
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
        count += 1
        if count == len(line):
            score = 0
            while len(stack) > 0:
                s = stack.pop()
                score = score * 5
                score += s + 1
            scores.append(score)

file.close()

print(points)
s = sorted(scores)
m = int(len(s)/2)
print(s[m])
