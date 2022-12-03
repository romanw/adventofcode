#!/usr/bin/env python

from bitstring import ConstBitStream

#stream = ConstBitStream(hex="9C0141080250320F1802104A08")

file = open("input.txt")
stream = ConstBitStream(hex=file.read())

vsum = 0

def process_type(ptype, values):
    res = 0
    # sum
    if ptype == 0:
        for v in values:
            res = res + v
    # product
    elif ptype == 1:
        res = values[0]
        for i in range(1, len(values)):
            res = res * values[i]
    # min
    elif ptype == 2:
        res = 1e99
        for v in values:
            if v < res:
                res = v
    # max
    elif ptype == 3:
        for v in values:
            if v > res:
                res = v
    # greater than
    elif ptype == 5:
        if values[0] > values[1]:
            res = 1
    # less than
    elif ptype == 6:
        if values[0] < values[1]:
            res = 1
    # equal to
    elif ptype == 7:
        if values[0] == values[1]:
            res = 1
    return res

def process_packet():
    global vsum
    bits_read = 0
    pversion = stream.read('uint:3')
    bits_read += 3
    ptype = stream.read('uint:3')
    bits_read += 3
    vsum += pversion
    num = 0
    if ptype == 4:
        while True:
            nlast = stream.read('uint:1')
            bits_read += 1
            num = num * 16 + stream.read('uint:4')
            bits_read += 4
            if nlast == 0:
                break
    else:
        lid = stream.read('uint:1')
        bits_read += 1
        n = 0
        nmax = 0
        nmin = 1e99
        if lid == 0:
            sblen = stream.read('uint:15')
            bits_read += 15
            values = []
            while sblen > 0:
                n, br = process_packet()
                sblen -= br
                bits_read += br
                values.append(n)
            num = process_type(ptype, values)
        else:
            sbnum = stream.read('uint:11')
            bits_read += 11
            values = []
            while sbnum > 0:
                n, br = process_packet()
                sbnum -= 1
                bits_read += br
                values.append(n)
            num = process_type(ptype, values)
    return num, bits_read
            

print("16 December 2021")
vsum = 0
n, br = process_packet()
print("part 1 sum of version numbers = {}".format(vsum))
print("part 2 evaluation = {}".format(n))
