import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *
import re

FILENAME = '3_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    running = 0
    for dat in data:
        pat = re.compile("mul\((\d+),(\d+)\)")
        match = pat.findall(dat)
        # print(match)
        # print(sum([int(a[0]) * int(a[1]) for a in match]))
        running += sum([int(a[0]) * int(a[1]) for a in match])
    print(running)

def main2():
    data = readlines(FILENAME)
    enabled = True
    running = 0
    for dat in data:
        mul_pat = re.compile("mul\((\d+),(\d+)\)")
        # mul_pat = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
        do_pat = re.compile("do\(\)")
        dont_pat = re.compile("don't\(\)")

        startpos = 0
        # enabled = True
        for_row = 0
        while True:
            mul_match = mul_pat.search(dat, startpos)
            do_match = do_pat.search(dat, startpos)
            dont_match = dont_pat.search(dat, startpos)

            earliest_i = None
            if mul_match is not None:
                maybe_i = mul_match.start()
                if earliest_i is None or maybe_i < earliest_i:
                    earliest_i = maybe_i
                    typ = "mul"
                    mat = mul_match
            if do_match is not None:
                maybe_i = do_match.start()
                if earliest_i is None or maybe_i < earliest_i:
                    earliest_i = maybe_i
                    typ = "do"
                    mat = do_match
            if dont_match is not None:
                maybe_i = dont_match.start()
                if earliest_i is None or maybe_i < earliest_i:
                    earliest_i = maybe_i
                    typ = "dont"
                    mat = dont_match
            if earliest_i is None:
                break
            # print(typ)
            # print(mat)
            # print(mat.end())
            if typ == "mul":
                if enabled:
                    # print(int(mat.group(1)), int(mat.group(2)))
                    for_row += int(mat.group(1)) * int(mat.group(2))
            elif typ == "do":
                enabled = True
            elif typ == "dont":
                enabled = False
            startpos = mat.end()

        # print(do_match)
        # print(dont_match)
        # running += sum([int(a[0]) * int(a[1]) for a in match])
        # print(for_row)
        running += for_row
    print(running)

# def copied():
#     data = readlines(FILENAME)
#     mul = r"mul\((\d{1,3}),(\d{1,3})\)"
#     running = 0
#     for dat in data:
#         clean = "".join(
#             [segment[segment.find("do()") :] for segment in ("do()" + dat).split("don't()")]
#         )
#         running += sum(int(pair[0]) * int(pair[1]) for pair in re.findall(mul, clean))
#     print(running)

# def copied2():
#     total1 = total2 = 0
#     enabled = True
#     data = readlines(FILENAME)

#     for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
#         if do or dont:
#             enabled = bool(do)
#         else:
#             x = int(a) * int(b)
#             total1 += x
#             total2 += x * enabled

#     print(total1, total2)

if __name__ == '__main__':
    main()
    main2()
    # copied()
    # copied2()
