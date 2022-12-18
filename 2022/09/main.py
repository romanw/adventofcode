#!/usr/bin/env python

file = open("input")
#file = open("test2")

visited = []
count = 0

def moveTail(h, t, v):
    tx = t[0]
    ty = t[1]
    dx = abs(h[0] - t[0])
    dy = abs(h[1] - t[1])
    if dy == 0:
        # horizontal move
        while dx > 1:
            if h[0] > t[0]:
                tx += 1
            elif h[0] < t[0]:
                tx -= 1
            if not [tx, ty] in v:
                v.append([tx, ty])
            dx -= 1
    elif dx == 0:
        # vertical move
        while dy > 1:
            if h[1] > t[1]:
                ty += 1
            elif h[1] < t[1]:
                ty -= 1
            if not [tx, ty] in v:
                v.append([tx, ty])
            dy -= 1
    else:
        # diagonal
        if dx > 1:
            # horizontal
            if h[0] > t[0]:
                tx += 1
            elif h[0] < t[0]:
                tx -= 1
            if dy > 0:
                if h[1] > t[1]:
                    ty += 1
                elif h[1] < t[1]:
                    ty -= 1
                pass
            else:
                print("oops dy")
            if not [tx, ty] in v:
                v.append([tx, ty])
            pass
        elif dy > 1:
            # vertical
            if h[1] > t[1]:
                ty += 1
            elif h[1] < t[1]:
                ty -= 1
            if dx > 0:
                if h[0] > t[0]:
                    tx += 1
                elif h[0] < t[0]:
                    tx -= 1
                pass
            else:
                print("oops dx")
            if not [tx, ty] in v:
                v.append([tx, ty])
            pass
        else:
            #print("oops dx dy")
            #print(h, t)
            pass
    return [tx, ty]


def ropeBridge(knots):
    rope = [[0,0] for i in range(knots+1)]
    visited = [[] for i in range(knots+1)]
    file.seek(0)
    for line in file:
        motion = line.strip().split(" ")
        #print(motion)
        move = motion[0]
        steps = int(motion[1])
        while steps > 0:
            if move == "R":
                rope[0][0] += 1
            elif move == "L":
                rope[0][0] -= 1
            elif move == "U":
                rope[0][1] += 1
            elif move == "D":
                rope[0][1] -= 1
            #tx, ty = moveTail(hx, hy, tx, ty)
            for i in range(1, knots+1):
                rope[i] = moveTail(rope[i-1], rope[i], visited[i])
            #if not rope[i] in visited:
            #    visited.append(rope[i])
            steps -= 1
        #print(hx, hy, tx, ty)
    #print(visited)
    print(len(visited[i]) + 1)

ropeBridge(1)
ropeBridge(9)

file.close()
