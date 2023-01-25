import sys 
sys.path.append('..')

import copy
from collections import defaultdict
from helper import *

FILENAME = '16_dat.txt'
mapper = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def main():
    data = readlines(FILENAME)
    data = data[0]
    data = ''.join([mapper[dat] for dat in data])
    # global GLOBAL_VERSION_NUMBER_SUM
    value, _, version_sum = parse_packet(data)
    print('final_version_sum', version_sum)
    print('final_value', value)

def parse_packet(data):
    version_bits = data[:3]
    version = bin_to_int(version_bits)
    typeid_bits = data[3:6]
    typeid = bin_to_int(typeid_bits)
    remaining_bits = data[6:]
    # print('version', version)
    # print('typeid' , typeid)
    # GLOBAL_VERSION_NUMBER_SUM += version
    if typeid == 4:
        # print('literal')
        bit_groups = [remaining_bits[i:i+5] for i in range(0, len(remaining_bits), 5)]
        full_bits = ''
        for bit_group in bit_groups:
            full_bits += bit_group[1:]
            if bit_group[0] == '0':
                break
        final_literal = bin_to_int(full_bits)
        print('literal', final_literal, (len(full_bits) // 4 * 5) + 6)
        return final_literal, (len(full_bits) // 4 * 5) + 6, version
    else:
    # elif typeid == 6 or typeid == 3:
        print('some operator')
        length_typeid_bits = data[6]
        length_typeid = bin_to_int(length_typeid_bits)
        if length_typeid == 0:
            # the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet
            total_length_bits = data[7:7+15]
            total_length = bin_to_int(total_length_bits)
            # print(total_length)
            read_length = 0
            packet_results = []
            sub_version_sum_total = 0
            while read_length < total_length:
                packet_result, length, sub_version_sum = parse_packet(data[7+15+read_length:])
                # print('subs', packet_result, length)
                read_length += length
                packet_results.append(packet_result)
                sub_version_sum_total += sub_version_sum
            print('full_subs', packet_results)
            return operate(packet_results, typeid), 7+15+read_length, sub_version_sum_total + version
        elif length_typeid == 1:
            # the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
            num_sub_packets_bits = data[7:7+11]
            num_sub_packets = bin_to_int(num_sub_packets_bits)
            # print('num_sub_packets', num_sub_packets)
            read_length = 0
            packet_results = []
            sub_version_sum_total = 0
            for i in range(num_sub_packets):
                packet_result, length, sub_version_sum = parse_packet(data[7+11+read_length:])
                # print('subs', packet_result, length)
                read_length += length
                packet_results.append(packet_result)
                sub_version_sum_total += sub_version_sum
            print('full_subs', packet_results)
            return operate(packet_results, typeid), 7+11+read_length, sub_version_sum_total + version

def operate(sub_packet_results, typeid):
    if typeid == 0:
        return sum(sub_packet_results)
    elif typeid == 1:
        return product(sub_packet_results)
    elif typeid == 2:
        return min(sub_packet_results)
    elif typeid == 3:
        return max(sub_packet_results)
    elif typeid == 5:
        return 1 if sub_packet_results[0] > sub_packet_results[1] else 0
    elif typeid == 6:
        return 1 if sub_packet_results[0] < sub_packet_results[1] else 0
    elif typeid == 7:
        return 1 if sub_packet_results[0] == sub_packet_results[1] else 0

# Time: 33:45

def main2():
    data = readlines(FILENAME)
    # data = [int(dat) for dat in data]
    # print(data)

# Time: 38:25

if __name__ == '__main__':
    main()
    main2()
