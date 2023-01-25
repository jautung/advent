import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '4_dat.txt'
mapper = {}

def parse(dat):
    year = int(dat[1:5])
    month = int(dat[6:8])
    day = int(dat[9:11])
    hour = int(dat[12:14])
    mins = int(dat[15:17])
    rest = dat[19:]
    if 'Guard' in rest:
        action = int(rest.split()[1][1:])
    elif 'asleep' in rest:
        action = 'S'
    elif 'wakes' in rest:
        action = 'W'
    assert(hour == 0 or hour == 23)
    if hour == 0:
        return year,month,day,hour,mins,action
    if hour == 23:
        return year,month,day+1,0,mins-60,action

def main():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    data = sorted(data)
    # print_2d(data)

    better_logs = defaultdict(lambda: [])
    curr_guard = None
    curr_sleep_start = None
    for year,month,day,hour,mins,action in data:
        if isinstance(action, int):
            curr_guard = action
        elif action == 'S':
            assert(hour == 0)
            curr_sleep_start = (year,month,day,hour,mins)
        elif action == 'W':
            assert(hour == 0)
            assert(curr_guard)
            assert(curr_sleep_start)
            better_logs[curr_guard].append((curr_sleep_start, (year,month,day,hour,mins)))
            curr_sleep_start = None
    # print_2d(data)
    # for guard in better_logs:
    #     print(guard)
    #     print_2d(better_logs[guard])
    sleepy_times = [(asleep_time(better_logs[guard]), guard) for guard in better_logs]
    sleepy_times.sort(reverse=True)
    chosen_guard = sleepy_times[0][1]

    log_for_guard = better_logs[chosen_guard]
    best_minute = best_min_for_guard(log_for_guard)[1]
    # print(best_minute)

    print(chosen_guard*best_minute)

def best_min_for_guard(logs):
    counter = def_dict(0)
    for s, e in logs:
        s_year,s_month,s_day,s_hour,s_mins = s
        e_year,e_month,e_day,e_hour,e_mins = e
        assert(s_year == e_year)
        assert(s_month == e_month)
        assert(s_day == e_day)
        assert(s_hour == e_hour)
        for i in range(s_mins,e_mins):
            counter[i] += 1
    return sorted([(counter[i], i) for i in counter], reverse=True)[0]

def asleep_time(logs):
    total = 0
    for s, e in logs:
        s_year,s_month,s_day,s_hour,s_mins = s
        e_year,e_month,e_day,e_hour,e_mins = e
        assert(s_year == e_year)
        assert(s_month == e_month)
        assert(s_day == e_day)
        assert(s_hour == e_hour)
        total += (e_mins-s_mins)
    return total

def main2():
    data = readlines(FILENAME)
    data = [parse(dat) for dat in data]
    data = sorted(data)
    # print_2d(data)

    better_logs = defaultdict(lambda: [])
    curr_guard = None
    curr_sleep_start = None
    for year,month,day,hour,mins,action in data:
        if isinstance(action, int):
            curr_guard = action
        elif action == 'S':
            assert(hour == 0)
            curr_sleep_start = (year,month,day,hour,mins)
        elif action == 'W':
            assert(hour == 0)
            assert(curr_guard)
            assert(curr_sleep_start)
            better_logs[curr_guard].append((curr_sleep_start, (year,month,day,hour,mins)))
            curr_sleep_start = None
    # print_2d(data)
    # for guard in better_logs:
    #     print(guard)
    #     print_2d(better_logs[guard])
    # sleepy_times = [(asleep_time(better_logs[guard]), guard) for guard in better_logs]
    # sleepy_times.sort(reverse=True)
    # chosen_guard = sleepy_times[0][1]

    # log_for_guard = better_logs[chosen_guard]
    # best_minute = best_min_for_guard(log_for_guard)
    # # print(best_minute)

    # print(chosen_guard*best_minute)

    max_times = None
    best_guard = None
    best_min = None
    for guard in better_logs:
        times, best_minute = best_min_for_guard(better_logs[guard])
        if not max_times or times > max_times:
            max_times = times
            best_guard = guard
            best_min = best_minute
    print(best_guard*best_min)

if __name__ == '__main__':
    main()
    main2()
