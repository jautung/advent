import sys

sys.path.append("..")

import copy
from collections import defaultdict
from helper import *

FILENAME = "19_dat.txt"
mapper = {}


def parse_rhs_item(item):
    if item.startswith('"') and item.endswith('"'):
        return item[1:-1]
    else:
        return int(item)


def parse_rule(rule):
    parts = rule.split(":")
    assert len(parts) == 2
    num, rhs = int(parts[0].strip()), parts[1].strip()
    options = rhs.split("|")
    # print(options)
    options = [
        [parse_rhs_item(x.strip()) for x in option.strip().split(" ")]
        for option in options
    ]
    return num, options


def main():
    data = readlines_split_by_newlines(FILENAME)
    rules = [parse_rule(rule) for rule in data[0]]
    rules_mapping = dict()
    for num, options in rules:
        rules_mapping[num] = options
    examples = data[1]

    results = dict()  # map from rule number to set of strings that match that rule
    expand_all(rules_mapping, results)

    # print(results[0])
    count = 0
    for example in examples:
        if example in results[0]:
            count += 1
    print(count)


def expand_all(rules_mapping, results, max_length=None):
    for num in rules_mapping:
        print("expanding all for", num)
        expand(num, rules_mapping, results, max_length)


def expand(num, rules_mapping, results, max_length=None, recursion_depth=0):
    print("expanding", num)
    if max_length is not None and recursion_depth > max_length:
        print("recursion depth", recursion_depth, "exceeds max length", max_length)
        return set()
    if num in results:
        print("already have results for", num)
        return results[num]
    options = rules_mapping[num]
    result = set()
    for option in options:
        print("option", option)
        build_for_option = set([""])
        for item in option:
            if isinstance(item, str):
                build_for_option = set(
                    [
                        s + item
                        for s in build_for_option
                        if max_length is None or len(s + item) <= max_length
                    ]
                )
            else:
                the_results = expand(
                    item, rules_mapping, results, max_length, recursion_depth + 1
                )
                build_for_option = set(
                    [
                        s1 + s2
                        for s1 in build_for_option
                        for s2 in the_results
                        if max_length is None or len(s1 + s2) <= max_length
                    ]
                )
        result.update(build_for_option)
    results[num] = result
    return result


def main2():
    data = readlines_split_by_newlines(FILENAME)
    rules = [parse_rule(rule) for rule in data[0]]
    rules_mapping = dict()
    for num, options in rules:
        rules_mapping[num] = options

    # updating rules_mapping for part 2 to have loops
    rules_mapping[8] = [[42], [42, 8]]
    rules_mapping[11] = [[42, 31], [42, 11, 31]]

    examples = data[1]

    max_length_of_examples = max(len(example) for example in examples)
    # print(max_length_of_examples)  # 96

    results = dict()  # map from rule number to set of strings that match that rule
    expand_all(rules_mapping, results, max_length_of_examples)
    print("done expanding all")

    # print(results[0])
    count = 0
    for example in examples:
        if example in results[0]:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
    main2()
