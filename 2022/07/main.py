#!/usr/bin/env python

file = open("input")
#file = open("test1")

totaldiskspace = 70000000
minfreediskspace = 30000000

def diskspace():
    path = []
    ls = []
    sum1 = 0
    dirsize = 0
    lds = []
    for line in file:
        l = line.strip().split(" ")
        if l[0] == "$":
            # command
            if l[1] == "cd":
                if l[2] == "/":
                    path = []
                elif l[2] == "..":
                    lds.append(dirsize)
                    path.pop()
                    if dirsize <= 100000:
                        sum1 += dirsize
                    dirsize += ls.pop()
                else:
                    path.append(l[2])
                    ls.append(dirsize)
            elif l[1] == "ls":
                dirsize = 0
                pass
            pass
        elif l[0] == "dir":
            # directory
            pass
        elif l[0].isnumeric():
            # file size
            dirsize += int(l[0])
            pass
        else:
            print("oops!", l)

    print(sum1)

    while len(ls) > 0:
        dirsize += ls.pop()
    freespace = totaldiskspace - dirsize
    needed = minfreediskspace - freespace
    lds.sort()
    for ds in lds:
        if ds > needed:
            print(ds)
            break

diskspace()

file.close()
