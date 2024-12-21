import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '21_dat.txt'
mapper = {}

def main():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

    BOARD_NUMERIC = {
        ( 0,0): "A",
        (-1,0): "0",
        (-2,1): "1",
        (-1,1): "2",
        ( 0,1): "3",
        (-2,2): "4",
        (-1,2): "5",
        ( 0,2): "6",
        (-2,3): "7",
        (-1,3): "8",
        ( 0,3): "9",
    }

    BOARD_DIREC = {
        ( 0, 0): "A",
        (-1, 0): "^",
        (-2,-1): "<",
        (-1,-1): "v",
        ( 0,-1): ">",
    }

    def a_pos(board):
        for b in board:
            if board[b] == "A":
                return b

    def get_pos_for(to_output, board):
        for b in board:
            if board[b] == to_output:
                return b

    def reduce_seq(moves, board):
        # if moves is None:
        #     return None
        output = ""
        curr = a_pos(board)
        for m in moves:
            if m == "^":
                curr = add_tup(curr, (0,1))
                if curr not in board:
                    return None
            elif m == "<":
                curr = add_tup(curr, (-1,0))
                if curr not in board:
                    return None
            elif m == "v":
                curr = add_tup(curr, (0,-1))
                if curr not in board:
                    return None
            elif m == ">":
                curr = add_tup(curr, (1,0))
                if curr not in board:
                    return None
            elif m == "A":
                output += board[curr]
        return output

    # TEST_1 = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    # TEST_2 = "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"
    # TEST_3 = "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
    # TEST_4 = "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"
    # TEST_5 = "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"

    # print(reduce_seq(reduce_seq(reduce_seq(TEST_1, BOARD_DIREC), BOARD_DIREC), BOARD_NUMERIC))
    # print(reduce_seq(reduce_seq(reduce_seq(TEST_2, BOARD_DIREC), BOARD_DIREC), BOARD_NUMERIC))
    # print(reduce_seq(reduce_seq(reduce_seq(TEST_3, BOARD_DIREC), BOARD_DIREC), BOARD_NUMERIC))
    # print(reduce_seq(reduce_seq(reduce_seq(TEST_4, BOARD_DIREC), BOARD_DIREC), BOARD_NUMERIC))
    # print(reduce_seq(reduce_seq(reduce_seq(TEST_5, BOARD_DIREC), BOARD_DIREC), BOARD_NUMERIC))

    # print(TEST_1)
    # a = reduce_seq(TEST_1, BOARD_DIREC)
    # print(a)
    # b = reduce_seq(a, BOARD_DIREC)
    # print(b)
    # c = reduce_seq(b, BOARD_NUMERIC)
    # print(c)

    # print(reduce_seq("<A^A>^^AvvvA", BOARD_NUMERIC))    
    # print(reduce_seq("<A^A^>^AvvvA", BOARD_NUMERIC))    
    # print(reduce_seq("<A^A^^>AvvvA", BOARD_NUMERIC))    
    # print(reduce_seq(reduce_seq("v<<A>>^A<A>AvA<^AA>A<vAAA>^A", BOARD_DIREC), BOARD_NUMERIC))
    # print(reduce_seq(reduce_seq(reduce_seq("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A", BOARD_DIREC), BOARD_DIREC), BOARD_NUMERIC))

    def complete_func_for(x, ignore_stupid=False):
        # print('complete_func_for', x)
        # reduce_seq(reduce_seq(reduce_seq(x, BOARD_DIREC), BOARD_DIREC), BOARD_NUMERIC)
        a = reduce_seq(x, BOARD_DIREC)
        if a is None or (not ignore_stupid and is_stupid_candidate(a)):
            return None
        b = reduce_seq(a, BOARD_DIREC)
        if b is None or (not ignore_stupid and is_stupid_candidate(b)):
            return None
        c = reduce_seq(b, BOARD_NUMERIC)
        if c is None or (not ignore_stupid and is_stupid_candidate(c)):
            return None
        return c

    def is_stupid_candidate(c):
        for subseq_l in range(2, len(c)+1, 2):
            for start_i in range(0, len(c)):
                subseq = c[start_i:start_i+subseq_l]
                k = Counter()
                for s in subseq:
                    k[s] += 1
                if k["A"] == 0 and k["<"] == k[">"] and k["^"] == k["v"]:
                    return True
        return False
        # if "<>" in c:
        #     return True
        # if "><" in c:
        #     return True
        # if "^v" in c:
        #     return True
        # if "v^" in c:
        #     return True
        # return False

    def get_next_candidates(curr_candidate):
        basic = [curr_candidate + n for n in ["<", ">", "v", "^", "A"]]
        return [k for k in basic if not is_stupid_candidate(k)]

    def shortest_for(pattern):
        # this is a really strange really warped form of bfs i think???
        candidates = [""]
        while len(candidates) > 0:
            curr_candidate = candidates.pop(0)
            # print(curr_candidate, len(curr_candidate), len(candidates))
            # we can probably heuristic here but doing this for now
            next_candidates = get_next_candidates(curr_candidate)
            # next_candidates = [curr_candidate + n for n in ["<", ">", "v", "^", "A"]]
            # print(next_candidates)
            for next_candidate in next_candidates:
                result = complete_func_for(next_candidate)
                if result is None:
                    continue
                elif not pattern.startswith(result):
                    continue
                elif result == pattern:
                    return next_candidate
                candidates.append(next_candidate)
        # return 0

    # for p in data:
    #     print(p, shortest_for(p))
    # print(shortest_for(data[0]))
    # print(shortest_for("0")) # "<vA<AA>>^AvAA<^A>A"
    # print(shortest_for("1")) # "<v<A>>^A<vA<A>>^AAvAA<^A>A"
    # print(shortest_for("2")) # "<vA<AA>>^AvA<^A>AvA^A"
    # print(shortest_for("3")) # "<v<A>>^AvA^A"
    # print(shortest_for("4")) # "<v<A>>^AA<vA<A>>^AAvAA<^A>A"
    # print(shortest_for("5")) # "<vA<AA>>^AvA<^A>AAvA^A""
    # print(shortest_for("6")) # "<v<A>>^AAvA^A"
    # print(shortest_for("7"))
    # print(shortest_for("8"))
    # print(shortest_for("9"))
    # print(shortest_for("33"))
    # print(complete_func_for(""))

    # hard pivot...
    # each 'state' consists of (already printed string, position of robot 1, robot 2, robot 3)
    # maybe we can dp the shit out of this?
    # so there are basically 5 * 5 * 11 'ending states'
    # we can 'find the shortest sequence that will generate each state'
    # or NONE if no possible sequence will generate this state

    # seqs = dict()
    # already_in_stack = set()
    # seqs[("", a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC))] = "" # this is the starting 'base case'
    def find_it(state, depth=0):
        print(' '*depth, 'start', state)
        if state in seqs:
            return seqs[state]
        already_in_stack.add(state)
        # ok nvm this `already_in_stack` is terrible, because just because an unknown state is in limbo
        # doesn't mean that it is definitely worse
        # we need to do some bottom up dp probably, instead of doing this
        # also every digit print is independent, no? at the point of printing
        # 
        # last operation will always be "A" on both pos1 and pos2, and the last digit for pos3
        # but yea, that's an optimization, this is not even working...
        outp, pos1, pos2, pos3 = state
        possible_final_solutions = []
        def store_possible_solution(result):
            possible_final_solutions.append(result)
            # seqs[(outp, pos1, pos2, pos3)] = result
            # print('end', (outp, pos1, pos2, pos3), result)
            # return result
        # how can we get into this state with one move??
        # we can ONLY affect outp if pos1 is on A, pos2 is on A, pos3 is on the first char of outp
        #   - then, me hitting 'A' will cascade down
        if len(outp) > 0 and BOARD_NUMERIC[pos3] == outp[-1] and BOARD_DIREC[pos2] == "A" and BOARD_DIREC[pos1] == "A":
            potential_previous_state = (outp[:-1], pos1, pos2, pos3)
            if potential_previous_state not in already_in_stack:
                potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                if potential_previous_solution is not None:
                    store_possible_solution(potential_previous_solution + "A")
        # there's no other way to 'generate an output'
        # all other 'previous states' will have the full outp, and are just with different combinations of pos's

        # how can we affect pos3?
        # ONLY if pos2 is a direction, and pos1 is on "A"
        if BOARD_DIREC[pos1] == "A":
            if BOARD_DIREC[pos2] == "^":
                # previous state was with pos3 one square lower, and I hit "A""
                maybe_prev_pos3 = add_tup(pos3, (0, -1))
                if maybe_prev_pos3 in BOARD_NUMERIC:
                    potential_previous_state = (outp, pos1, pos2, maybe_prev_pos3)
                    if potential_previous_state not in already_in_stack:
                        potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                        if potential_previous_solution is not None:
                            store_possible_solution(potential_previous_solution + "A")
            elif BOARD_DIREC[pos2] == "<":
                maybe_prev_pos3 = add_tup(pos3, (1, 0))
                if maybe_prev_pos3 in BOARD_NUMERIC:
                    potential_previous_state = (outp, pos1, pos2, maybe_prev_pos3)
                    if potential_previous_state not in already_in_stack:
                        potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                        if potential_previous_solution is not None:
                            store_possible_solution(potential_previous_solution + "A")
            elif BOARD_DIREC[pos2] == "v":
                maybe_prev_pos3 = add_tup(pos3, (0, 1))
                if maybe_prev_pos3 in BOARD_NUMERIC:
                    potential_previous_state = (outp, pos1, pos2, maybe_prev_pos3)
                    if potential_previous_state not in already_in_stack:
                        potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                        if potential_previous_solution is not None:
                            store_possible_solution(potential_previous_solution + "A")
            elif BOARD_DIREC[pos2] == ">":
                maybe_prev_pos3 = add_tup(pos3, (-1, 0))
                if maybe_prev_pos3 in BOARD_NUMERIC:
                    potential_previous_state = (outp, pos1, pos2, maybe_prev_pos3)
                    if potential_previous_state not in already_in_stack:
                        potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                        if potential_previous_solution is not None:
                            store_possible_solution(potential_previous_solution + "A")

        # at this point, outp is not being affected and pos3 cannot possibly be affected
        # all moves are within affecting pos1 and pos2
        # how can we affect pos2?
        #  - pos1 MUST be already on a direction
        #  - and I just hit "A" to make pos1 tap that direction
        if BOARD_DIREC[pos1] == "^":
            maybe_prev_pos2 = add_tup(pos2, (0, -1))
            if maybe_prev_pos2 in BOARD_DIREC:
                potential_previous_state = (outp, pos1, maybe_prev_pos2, pos3)
                if potential_previous_state not in already_in_stack:
                    potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                    if potential_previous_solution is not None:
                        store_possible_solution(potential_previous_solution + "A")
        elif BOARD_DIREC[pos1] == "<":
            maybe_prev_pos2 = add_tup(pos2, (1, 0))
            if maybe_prev_pos2 in BOARD_DIREC:
                potential_previous_state = (outp, pos1, maybe_prev_pos2, pos3)
                if potential_previous_state not in already_in_stack:
                    potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                    if potential_previous_solution is not None:
                        store_possible_solution(potential_previous_solution + "A")
        elif BOARD_DIREC[pos1] == "v":
            maybe_prev_pos2 = add_tup(pos2, (0, 1))
            if maybe_prev_pos2 in BOARD_DIREC:
                potential_previous_state = (outp, pos1, maybe_prev_pos2, pos3)
                if potential_previous_state not in already_in_stack:
                    potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                    if potential_previous_solution is not None:
                        store_possible_solution(potential_previous_solution + "A")
        elif BOARD_DIREC[pos1] == ">":
            maybe_prev_pos2 = add_tup(pos2, (-1, 0))
            if maybe_prev_pos2 in BOARD_DIREC:
                potential_previous_state = (outp, pos1, maybe_prev_pos2, pos3)
                if potential_previous_state not in already_in_stack:
                    potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                    if potential_previous_solution is not None:
                        store_possible_solution(potential_previous_solution + "A")

        # simple moves to move pos1
        maybe_prev_pos1 = add_tup(pos1, (0, -1))
        if maybe_prev_pos1 in BOARD_DIREC:
            potential_previous_state = (outp, maybe_prev_pos1, pos2, pos3)
            if potential_previous_state not in already_in_stack:
                potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                if potential_previous_solution is not None:
                    store_possible_solution(potential_previous_solution + "^")
        maybe_prev_pos1 = add_tup(pos1, (1, 0))
        if maybe_prev_pos1 in BOARD_DIREC:
            potential_previous_state = (outp, maybe_prev_pos1, pos2, pos3)
            if potential_previous_state not in already_in_stack:
                potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                if potential_previous_solution is not None:
                    store_possible_solution(potential_previous_solution + "<")
        maybe_prev_pos1 = add_tup(pos1, (0, 1))
        if maybe_prev_pos1 in BOARD_DIREC:
            potential_previous_state = (outp, maybe_prev_pos1, pos2, pos3)
            if potential_previous_state not in already_in_stack:
                potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                if potential_previous_solution is not None:
                    store_possible_solution(potential_previous_solution + "v")
        maybe_prev_pos1 = add_tup(pos1, (-1, 0))
        if maybe_prev_pos1 in BOARD_DIREC:
            potential_previous_state = (outp, maybe_prev_pos1, pos2, pos3)
            if potential_previous_state not in already_in_stack:
                potential_previous_solution = find_it(potential_previous_state, depth=depth+1)
                if potential_previous_solution is not None:
                    store_possible_solution(potential_previous_solution + ">")

        # assert False
        if len(possible_final_solutions) == 0:
            print(' '*depth, 'end', (outp, pos1, pos2, pos3), None)
            return None
        result = sorted(possible_final_solutions, key=lambda x: len(x))[0]
        seqs[(outp, pos1, pos2, pos3)] = result
        print(' '*depth, 'end', (outp, pos1, pos2, pos3), possible_final_solutions, result)
        return result

    # # x = find_it(("3", a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC)))
    # # print(x) # "v<A<AA>^>vA<^Av>^AvA^Av<A<AA>^>vA<^Av>^AAvA<A<AA>^>vA^AAAvA<^Av<A>A^A>vA^"

    # # print(complete_func_for("v<A<AA>^>vA<^Av>^AvA^Av<A<AA>^>vA<^Av>^AAvA<A<AA>^>vA^AAAvA<^Av<A>A^A>vA^", ignore_stupid=True))
    # # print(complete_func_for("v<A<AA>^>vA", ignore_stupid=True))
    # # a = reduce_seq("<v<A>>^AvA^A", BOARD_DIREC) # <v<A>>^AvA^A
    # # print(a) # <A>A
    # # b = reduce_seq(a, BOARD_DIREC)
    # # print(b) # ^A
    # # c = reduce_seq(b, BOARD_NUMERIC)
    # # print(c) # 3

    # # print(complete_func_for(""))
    # # print(complete_func_for(""))
    # # print(complete_func_for(""))
    # # print(complete_func_for(""))
    # # print(complete_func_for(""))


    # to_find = "3"

    # # last operation will always be "A" on both pos1 and pos2, and the last digit for pos3
    # # but yea, that's an optimization, this is not even working...

    # # ideal = find_it((to_find, (0,0), (0,0), (0,1)))
    # # print(ideal)
    # # print(ideal, complete_func_for(ideal, ignore_stupid=True), complete_func_for(ideal, ignore_stupid=False))

    # # already_in_stack = set()
    # ideal = find_it(("", (-1,-1), (-1,0), (0,0)))
    # # print(ideal)
    # print(ideal, complete_func_for(ideal, ignore_stupid=True), complete_func_for(ideal, ignore_stupid=False))

    # # cands = []
    # # for pot_pos1 in BOARD_DIREC:
    # #     for pot_pos2 in BOARD_DIREC:
    # #         for pot_pos3 in BOARD_NUMERIC:
    # #             cands.append(find_it((to_find, pot_pos1, pot_pos2, pot_pos3)))
    # # # print_2d(cands)
    # # # for c in cands:
    # # #     if c is None:
    # # #         continue
    # # #     print(c, complete_func_for(c, ignore_stupid=True))
    # # # print_2d(cands)
    # # cands = [c for c in cands if c is not None]
    # # sorted_cands = sorted(cands, key=lambda x: len(x))
    # # # print_2d(sorted_cands)
    # # for c in sorted_cands:
    # #     if c is None:
    # #         continue
    # #     print(c, complete_func_for(c, ignore_stupid=True), complete_func_for(c, ignore_stupid=False))
    # # # print(sorted_cands[0], len(sorted_cands[0]))
    # brute = shortest_for(to_find)
    # print(brute, complete_func_for(brute, ignore_stupid=True), complete_func_for(brute, ignore_stupid=False))

    def translated(m):
        if m == "^":
            return (0,1)
        elif m == "<":
            return (-1,0)
        elif m == "v":
            return (0,-1)
        elif m == ">":
            return (1,0)
        assert False





    # ok ok time to hard pivot again...
    # shortest input needed to output a SINGLE CHAR, given an initial STATE (pos1, pos2, pos3)
    def shortest(to_output, state):
        # results = dict()
        target_state = (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), get_pos_for(to_output, BOARD_NUMERIC))
        queue = [(state, "")]
        in_queue = set()
        in_queue.add(state)
        while len(queue) > 0:
            curr_state, curr_candidate = queue.pop(0)
            # print(curr_state, curr_candidate)
            curr_pos1, curr_pos2, curr_pos3 = curr_state
            for d in ['<', '>', '^', 'v']:
                maybe_pos1 = add_tup(curr_pos1, translated(d))
                if maybe_pos1 in BOARD_DIREC:
                    next_state = (maybe_pos1, curr_pos2, curr_pos3)                        
                    if next_state == target_state:
                        return curr_candidate + d
                    if next_state not in in_queue:
                        queue.append((next_state, curr_candidate + d))
                        in_queue.add(next_state)
            # hit 'A'
            robot1_hit = BOARD_DIREC[curr_pos1]
            if robot1_hit in ['<', '>', '^', 'v']:
                maybe_pos2 = add_tup(curr_pos2, translated(robot1_hit))
                if maybe_pos2 in BOARD_DIREC:
                    next_state = (curr_pos1, maybe_pos2, curr_pos3)
                    if next_state == target_state:
                        return curr_candidate + 'A'
                    if next_state not in in_queue:
                        queue.append((next_state, curr_candidate + 'A'))
                        in_queue.add(next_state)
            else:
                assert robot1_hit == 'A'
                robot2_hit = BOARD_DIREC[curr_pos2]
                if robot2_hit in ['<', '>', '^', 'v']:
                    maybe_pos3 = add_tup(curr_pos3, translated(robot2_hit))
                    if maybe_pos3 in BOARD_NUMERIC:
                        next_state = (curr_pos1, curr_pos2, maybe_pos3)
                        if next_state == target_state:
                            return curr_candidate + 'A'
                        if next_state not in in_queue:
                            queue.append((next_state, curr_candidate + 'A'))
                            in_queue.add(next_state)
                else:
                    assert robot2_hit == 'A'
                    # we never want to do this unless pos3 is already aligned, so no point searching this space
                    # and the check for pos3 already being aligned is already above
                    continue
        assert False
        # for pot_pos1 in BOARD_DIREC:
        #     for pot_pos2 in BOARD_DIREC:
        #         for pot_pos3 in BOARD_NUMERIC:
        #             results[(pot_pos1, pot_pos2, pot_pos3)] = None
        # results[state] = ""

    # print(shortest('0', (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC))))
    # print(shortest('1', (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC))))
    # print(shortest('2', (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC))))
    # print(shortest('3', (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC))))
    # print(shortest('4', (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC))))
    # print(shortest('5', (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC))))
    # print(shortest_for("0")) # "<vA<AA>>^AvAA<^A>A"
    # print(shortest_for("1")) # "<v<A>>^A<vA<A>>^AAvAA<^A>A"
    # print(shortest_for("2")) # "<vA<AA>>^AvA<^A>AvA^A"
    # print(shortest_for("3")) # "<v<A>>^AvA^A"
    # print(shortest_for("4")) # "<v<A>>^AA<vA<A>>^AAvAA<^A>A"
    # print(shortest_for("5")) # "<vA<AA>>^AvA<^A>AAvA^A""
    # print(shortest_for("6")) # "<v<A>>^AAvA^A"

    def solve_for_final_final(thing):
        overall = ''
        for index, t in enumerate(thing):
            if index == 0:
                overall += shortest(t, (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), a_pos(BOARD_NUMERIC))) + 'A'
            else:
                overall += shortest(t, (a_pos(BOARD_DIREC), a_pos(BOARD_DIREC), get_pos_for(thing[index-1], BOARD_NUMERIC))) + 'A'
        return overall

    # print(solve_for_final_final('029A'), len(solve_for_final_final('029A')), len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"))
    # print(solve_for_final_final('980A'), len(solve_for_final_final('980A')), len("<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"))
    # print(solve_for_final_final('179A'), len(solve_for_final_final('179A')), len("<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))
    # print(solve_for_final_final('456A'), len(solve_for_final_final('456A')), len("<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"))
    # print(solve_for_final_final('379A'), len(solve_for_final_final('379A')), len("<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"))

    # print(complete_func_for(solve_for_final_final('029A'), ignore_stupid=True))
    # print(complete_func_for(solve_for_final_final('980A'), ignore_stupid=True))
    # print(complete_func_for(solve_for_final_final('179A'), ignore_stupid=True))
    # print(complete_func_for(solve_for_final_final('456A'), ignore_stupid=True))
    # print(complete_func_for(solve_for_final_final('379A'), ignore_stupid=True))

    the_real_return_value = 0
    for d in data:
        numeric_part = int(d.split('A')[0].strip())
        seq = solve_for_final_final(d)
        the_real_return_value += numeric_part * len(seq)
    print(the_real_return_value)



def main2():
    data = readlines(FILENAME)

    BOARD_NUMERIC = {
        ( 0,0): "A",
        (-1,0): "0",
        (-2,1): "1",
        (-1,1): "2",
        ( 0,1): "3",
        (-2,2): "4",
        (-1,2): "5",
        ( 0,2): "6",
        (-2,3): "7",
        (-1,3): "8",
        ( 0,3): "9",
    }

    BOARD_DIREC = {
        ( 0, 0): "A",
        (-1, 0): "^",
        (-2,-1): "<",
        (-1,-1): "v",
        ( 0,-1): ">",
    }

    def a_pos(board):
        for b in board:
            if board[b] == "A":
                return b

    def get_pos_for(to_output, board):
        for b in board:
            if board[b] == to_output:
                return b

    def translated(m):
        if m == "^":
            return (0,1)
        elif m == "<":
            return (-1,0)
        elif m == "v":
            return (0,-1)
        elif m == ">":
            return (1,0)
        assert False

    def tuple_replacing(tup, index, new_val):
        l = list(tup)
        l[index] = new_val
        return tuple(l)

    # LAYERS = 2
    # LAYERS = 8
    # LAYERS = 25

    # wheeee now state is a 26-tuple
    # the first 25 are DIREC positions, the last one is the NUMERIC
    #   ....  yea  of course why did i even believe this would work... 5^25 is huge, and even 5^8 is giving up on me... :///
    def shortest(to_output, last, LAYERS):
        state = tuple([a_pos(BOARD_DIREC)] * LAYERS + [last])
        # print(to_output, state)
        target_state = tuple([a_pos(BOARD_DIREC)] * LAYERS + [get_pos_for(to_output, BOARD_NUMERIC)])
        queue = [(state, "")]
        in_queue = set()
        in_queue.add(state)
        while len(queue) > 0:
            curr_state, curr_candidate = queue.pop(0)
            # print(curr_state)
            # curr_state is now a 26-tuple :)
            for d in ['<', '>', '^', 'v']:
                maybe_pos0 = add_tup(curr_state[0], translated(d))
                board = BOARD_NUMERIC if 0 == LAYERS else BOARD_DIREC
                if maybe_pos0 in board:
                    next_state = tuple_replacing(curr_state, 0, maybe_pos0)
                    if next_state == target_state:
                        return curr_candidate + d
                    if next_state not in in_queue:
                        queue.append((next_state, curr_candidate + d))
                        in_queue.add(next_state)

            # hit 'A' in all of these cases, the only question is how far it propagated... and 'what happened'
            new_candidate = curr_candidate + 'A'
            # did_a_move = False
            tapping_robot_index = 0
            while tapping_robot_index <= LAYERS-1:
                hit_spot = BOARD_DIREC[curr_state[tapping_robot_index]]
                if hit_spot == 'A':
                    tapping_robot_index += 1
                    continue
                assert hit_spot in ['<', '>', '^', 'v']
                # did_a_move = True
                tapped_robot_index = tapping_robot_index+1
                maybe_new_pos = add_tup(curr_state[tapped_robot_index], translated(hit_spot))
                board = BOARD_NUMERIC if tapped_robot_index == LAYERS else BOARD_DIREC
                if maybe_new_pos in board:
                    next_state = tuple_replacing(curr_state, tapped_robot_index, maybe_new_pos)
                    if next_state == target_state:
                        return new_candidate
                    if next_state not in in_queue:
                        queue.append((next_state, new_candidate))
                        in_queue.add(next_state)
                break

            # nothing else to do after breaking out of the loop I don't think
            # we never want to do this unless pos3 is already aligned, so no point searching this space
            # and the check for pos3 already being aligned is already above
        assert False

    # I BET there is some kind of mathy exponential pattern against layers such that
    # we don't even need to sequence out everything... let's test that..

    t = '3'
    for layer in range(10):
        # print(layer)
        ans = shortest(t, a_pos(BOARD_NUMERIC), LAYERS=layer) + 'A'
        # print(layer, len(ans), ans)
        print(layer, len(ans))

    # 0 2 <A
    # 1 8 <v<A>>^A
    # 2 18 <vA<AA>>^AvAA<^A>A
    # 3 46 <v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A
    # 4 108 <vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A
    # 5 274 <v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^AA<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<v<A>^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A
    # 6 674 <vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>AA<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<v<A>^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>AA<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>A
    # 7 1686 <v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^AA<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<vA<AA>>^AvA^A<A>vA^A<vA>^A<A>A<v<A>>^AvA^A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^AA<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<v<A>^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>AA<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<vA<AA>>^AvA^A<A>vA^A<vA>^A<A>A<v<A>>^AvA^A<vA<AA>>^AvAA<^A>A<vA>^A<A>AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^AA<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<v<A>^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A
    # 8 4188 <vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>AA<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<v<A>^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>AA<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<v<A>^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>AA<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>AA<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<vA<AA>>^AvA^A<A>vA^A<vA>^A<A>A<v<A>>^AvA^A<vA<AA>>^AvAA<^A>A<vA>^A<A>AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^AA<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<v<A>^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^AA<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<vA<AA>>^AvA^A<A>vA^A<vA>^A<A>A<v<A>>^AvA^A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^AA<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>AA<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>AA<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<v<A>^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^A<A>A<v<A>>^A<vA>A^A<A>A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^A<v<A>>^AvA^A<v<A>A>^A<A>vA^A<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<v<A>A>^A<v<A>>^AAvAA<^A>A<vA>^AA<v<A>^A>AvA^A<vA<AA>>^AvA^A<A>vA^A<vA>^A<A>A<v<A>>^AvA^A<vA<AA>>^AvAA<^A>A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<vA<AA>>^AvAA<^A>AA<vA>^AA<v<A>^A>AvA^A<v<A>A>^A<A>vA^AA<vA<AA>>^AvA<^A>AvA^A<vA>^A<A>A<vA<AA>>^AvA^A<A>vA^A<v<A>>^A<vA>A^A<A>A<vA<AA>>^AvAA<^A>A<vA>^A<A>A

    # def solve_for_final_final(thing):
    #     overall = ''
    #     for index, t in enumerate(thing):
    #         # print(index, t)
    #         if index == 0:
    #             overall += shortest(t, a_pos(BOARD_NUMERIC), LAYERS=2) + 'A'
    #         else:
    #             overall += shortest(t, get_pos_for(thing[index-1], BOARD_NUMERIC), LAYERS=2) + 'A'
    #     return overall

    # the_real_return_value = 0
    # for d in data:
    #     numeric_part = int(d.split('A')[0].strip())
    #     seq = solve_for_final_final(d)
    #     the_real_return_value += numeric_part * len(seq)
    # print(the_real_return_value)

if __name__ == '__main__':
    # sys.setrecursionlimit(100)
    main()
    main2()
