import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '5_dat.txt'
mapper = {}

CACHE = dict()

def main():
    data = readlines_split_by_newlines(FILENAME)
    seeds = proc_s(data[0][0])
    maps = [proc_m(x) for x in data[1:]]
    # print(seeds)
    # print(maps)
    type_mapper = dict()
    for map in maps:
        key, val, aaa = map
        type_mapper[key] = (val, aaa)
    # print(type_mapper)
    xx = [full_convert_seed(s, type_mapper) for s in seeds]
    print(min(xx))

def full_convert_seed(s, type_mapper):
    return convert('seed', s, type_mapper)

def convert(typ, s, type_mapper):
    if typ == 'location':
        return s
    if typ not in CACHE:
        CACHE[typ] = dict()
    if s in CACHE[typ]:
        # print("HIT", s, typ)
        return CACHE[typ][s]
    val, aaa = type_mapper[typ]
    new_val = get_from(s, aaa)
    CACHE[typ][s] = convert(val, new_val, type_mapper)
    return CACHE[typ][s]

def get_from(s, aaa):
    for thing in aaa:
        dest_range_start, source_range_start, range_length = thing
        if source_range_start <= s and source_range_start + range_length > s:
            return dest_range_start - source_range_start + s
    return s

def proc_s(s):
    return [int(x.strip()) for x in s.split(':')[1].split()]

def proc_m(m):
    name = m[0]
    aa = name.split()[0].split('-')
    key = aa[0]
    val = aa[2]
    aaa = [[int(y.strip()) for y in x.split()] for x in m[1:]]
    # aaa is list of (dest_range_start, source_range_start, range_length)
    return (key, val, aaa)

def main2():
    data = readlines_split_by_newlines(FILENAME)
    seeds = proc_s(data[0][0])
    maps = [proc_m(x) for x in data[1:]]
    # print(seeds)
    # print(maps)
    type_mapper = dict()
    for map in maps:
        key, val, aaa = map
        type_mapper[key] = (val, aaa)
    # print(type_mapper)
    s_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    # print(s_ranges)
    coll = []
    for s_range in s_ranges:
        # all inclusive ranges easier
        start = s_range[0]
        end = s_range[0] + s_range[1] - 1
        a = range_full_convert_seed([start, end], type_mapper)
        # print(a)
        coll += a
        # exit(1)
        # for d in range(start, end + 1):
        #     print("REAL", d, full_convert_seed(d, type_mapper))
    # print()
    # for d in range(55, 55+13):
    #     print("REAL", d, full_convert_seed(d, type_mapper))
    print(min(flatten(coll)))
    # xx = [range_full_convert_seed(s, type_mapper) for s in seeds]
    # print(min(xx))
    

def range_full_convert_seed(s_range, type_mapper):
    # print(s_range)
    return range_convert('seed', [s_range], type_mapper)

def range_convert(typ, s_ranges, type_mapper):
    # print("range_convert", typ, s_ranges)
    if typ == 'location':
        return s_ranges
    new_typ, transformer_set = type_mapper[typ]
    new_ranges = range_get_from(s_ranges, transformer_set)
    return range_convert(new_typ, new_ranges, type_mapper)

def range_get_from(s_ranges, transformer_set):
    # if len(transformer_set) == 0:
    #     return s_ranges
    # print("range_get_from", s_ranges, transformer_set)
    final = []
    for s_range in s_ranges:
        final += transform_one(s_range, transformer_set)
    return final

def transform_one(s_range, transformer_set):
    # print("transform_one", s_range, transformer_set)
    current_start, current_end = s_range
    # if len(transformer_set) == 0:
    #     return s_range
    # dest_range_start, source_range_start, range_length = transformer_set[0]
    # source_range_end = source_range_start + range_length - 1
    # dest_range_end = dest_range_start + range_length - 1
    # new_ranges = []
    # if current_end < source_range_start:
    #     new_ranges = [s_range]
    # elif current_start > source_range_end:
    #     new_ranges = [s_range]
    # elif source_range_start <= current_start and current_end <= source_range_end:
    #     new_ranges_to_transform = [[current_start, current_end]]
    #     print("> A new_ranges_to_transform", new_ranges_to_transform)
    #     new_ranges = [transformmmmm(x, transformer_set[0]) for x in new_ranges_to_transform]
    # elif source_range_start <= current_start and current_start < source_range_end:
    #     new_ranges_to_transform = [[current_start, source_range_end], [source_range_end + 1, current_end]]
    #     print("> B new_ranges_to_transform", new_ranges_to_transform)
    #     new_ranges = [transformmmmm(x, transformer_set[0]) for x in new_ranges_to_transform]
    # elif source_range_start < current_end and current_end <= source_range_end:
    #     new_ranges_to_transform = [[current_start, source_range_start - 1], [source_range_start, current_end]]
    #     print("> C new_ranges_to_transform", new_ranges_to_transform)
    #     new_ranges = [transformmmmm(x, transformer_set[0]) for x in new_ranges_to_transform]
    # print("> new_ranges", new_ranges)
    keyframes = set()
    keyframes.add(current_start)
    keyframes.add(current_end)
    do_end = False
    do_start = False
    for t in transformer_set:
        dest_range_start, source_range_start, range_length = t
        source_range_end = source_range_start + range_length - 1
        dest_range_end = dest_range_start + range_length - 1
        if source_range_start == current_end:
            do_end = True
        if current_start == source_range_end:
            do_start = True
        if current_start < source_range_start and source_range_start <= current_end:
            keyframes.add(source_range_start - 1)
            keyframes.add(source_range_start)
        if current_start <= source_range_end and source_range_end < current_end:
            keyframes.add(source_range_end + 1)
            keyframes.add(source_range_end)
    # print("keyframes", keyframes)
    keyframes = sorted(list(keyframes))
    # print("keyframes", keyframes)
    if do_start:
        keyframes = [current_start] + keyframes
    if do_end:
        keyframes = keyframes + [current_end]
    # print("keyframes", keyframes)
    new_ranges_to_transform = [keyframes[i:i+2] for i in range(0, len(keyframes), 2)]
    # print("new_ranges_to_transform", new_ranges_to_transform)
    new_ranges = [transformmmmm(x, transformer_set) for x in new_ranges_to_transform]
    # print("new_ranges", new_ranges)
    # keyframes.append(current_end)
    return new_ranges
    # for thing in aaa:
    #     dest_range_start, source_range_start, range_length = thing
    #     if current_start + current_length < source_range_start:
    #         # =====
    #         # 
    #         # =====
            
    #     if source_range_start <= s and source_range_start + range_length > s:
    #         return dest_range_start - source_range_start + s

def transformmmmm(x, hmmm):
    # print("transformmmmm", x, hmmm)
    s = x[0]
    e = x[1]
    return [get_from(s, hmmm), get_from(e, hmmm)]

if __name__ == '__main__':
    main()
    main2()
