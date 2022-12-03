#!/usr/bin/env python

file = open("input")

def result1(a, b):
    hs1 = ord(a) - ord("A") + 1
    hs2 = ord(b) - ord("X") + 1
    outcome = 0
    if hs2 == hs1:
        outcome = 3
    elif (hs2 == 1 and hs1 == 3) or (hs2 == 2 and hs1 == 1) or (hs2 == 3 and hs1 == 2):
        outcome = 6
    return hs2 + outcome

def toWin(a):
    hs = a + 1
    if hs > 3:
        hs -= 3
    return hs

def toLose(a):
    hs = a - 1
    if hs < 1:
        hs += 3
    return hs
    
def result2(a, b):
    res = 0
    hs1 = ord(a) - ord("A") + 1
    outcome = ord(b) - ord("X") + 1
    if outcome == 1:
        res = toLose(hs1)
    if outcome == 2:
        res = hs1 + 3
    if outcome == 3:
        res = toWin(hs1) + 6
    return res
    

def scores():
    totalScore1 = 0
    totalScore2 = 0
    for line in file:
        hs = line.strip().split()
        totalScore1 += result1(hs[0], hs[1])
        totalScore2 += result2(hs[0], hs[1])
    print(totalScore1, totalScore2)


scores()
