#!/usr/bin/env python

# 0 = abcefg    012456      6
# 1 = cf        25      *  >2<
# 2 = acdeg     02346       5
# 3 = acdfg     02356       5
# 4 = bcdf      1235    *  >4<
# 5 = abdfg     01356       5
# 6 = abdefg    013456      6
# 7 = acf       025     *  >3<
# 8 = abcdefg   0123456 *  >7<
# 9 = abcdfg    012356      6

file = open("input.txt")

count = 0
for line in file:
    patterns, output = line.split("|")
    pttrns = patterns.strip().split()
    pttrns.sort(key = len)
    ss = list("0000000")
    for pattern in pttrns:
        pttrn = sorted(pattern)
        l = len(pttrn)
        if l == 2:
            ss[2] = list(pttrn[0]+ pttrn[1])
            ss[5] = list(pttrn[0]+ pttrn[1])
        elif l == 3:
            ss[0] = []
            for c in pttrn:
                if c != ss[2][0] and c != ss[2][1]:
                    ss[0].append(c)
                    break
        elif l == 4:
            ss[1] = []
            ss[3] = []
            for c in pttrn:
                if c != ss[2][0] and c != ss[2][1]:
                    ss[1].append(c)
                    ss[3].append(c)
        elif l == 7:
            ss[4] = []
            ss[6] = []
            for c in pttrn:
                if c != ss[0][0]:
                    if c != ss[1][0] and c != ss[1][1]:
                        if c != ss[2][0] and c != ss[2][1]:
                            ss[4].append(c)
                            ss[6].append(c)
    values = output.strip().split()
    value = ""
    for entry in values:
        el = sorted(entry)
        l = len(el)
        if l == 2:
            value += "1"
        elif l == 3:
            value += "7"
        elif l == 4:
            value += "4"
        elif l == 7:
            value += "8"
        elif l == 5:
            if ss[2][0] in el and ss[2][1] in el:
                value += "3"
            elif ss[1][0] in el and ss[1][1] in el:
                value += "5"
            elif ss[4][0] in el and ss[4][1] in el:
                value += "2"
            else:
                value += "?"
        elif l == 6:
            if ss[2][0] in el and ss[2][1] in el:
                if ss[1][0] in el and ss[1][1] in el:
                    value += "9"
                else:
                    value += "0"
            else:
                value += "6"
        else:
            value += "?"
    count += int(value)

file.close()

print(count)
