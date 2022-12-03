#!/usr/bin/env python

# target area: x=57..116, y=-198..-148
rx = range(57, 117)
ry = range(-198, -147)
lx = 116
ly = -198

# example target area: x=20..30, y=-10..-5
#rx = range(20, 31)
#ry = range(-10, -4)
#lx = 30
#ly = -10

pos = [0, 0]
vel = [6, 9]

def step():
    global pos, vel
    # The probe's x position increases by its x velocity.
    pos[0] += vel[0]
    # The probe's y position increases by its y velocity.
    pos[1] += vel[1]
    # Due to drag, the probe's x velocity changes by 1 toward the value 0;
    # that is, it decreases by 1 if it is greater than 0,
    # increases by 1 if it is less than 0, or does not change
    # if it is already 0.
    if vel[0] > 0:
        vel[0] -= 1
    elif vel[0] < 0:
        vel[0] += 1
    # Due to gravity, the probe's y velocity decreases by 1.
    vel[1] -= 1

def part1():
    global pos, vel
    for vx in range(10, 20):
        for vy in range(300):
            pos = [0, 0]
            vel = [vx, vy]
            gv = [vx, vy]
            maxy = 0
            le = False
            while True:
                step()
                if pos[0] > lx:
                    le = True
                    break
                if pos[1] < ly:
                    le = True
                    break
                if pos[1] > maxy:
                    maxy = pos[1]
                #print(pos, vel)
                if pos[0] in rx:
                    if pos[1] in ry:
                        break
            if not le:
                print(gv, maxy)

def part2():
    global pos, vel
    count = 0
    for vx in range(117):
        for vy in range(-198, 200):
            pos = [0, 0]
            vel = [vx, vy]
            gv = [vx, vy]
            while True:
                step()
                if pos[0] in rx and pos[1] in ry:
                    #print(gv)
                    count += 1
                    break
                if pos[0] > lx or pos[1] < ly:
                    break
    print(count)

part1()
part2()

