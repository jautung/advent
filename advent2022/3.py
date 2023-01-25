import sys 
sys.path.append('..')
import helper

def main():
    data = helper.readlines('3_dat.txt')
    scores = []
    for dat in data:
        l = len(dat) // 2
        first = dat[:l]
        second = dat[l:]
        intersection = set(first).intersection(set(second))
        intersection = intersection.pop()
        if intersection.islower():
            score = ord(intersection) - 96
        else:
            score = ord(intersection) - 38
        scores.append(score)
    print(sum(scores))

def main2():
    data = helper.readlines('3_dat.txt')
    scores = []
    for i in range(len(data) // 3):
        a = data[3 * i]
        b = data[3 * i + 1]
        c = data[3 * i + 2]
        intersection = set(a).intersection(set(b)).intersection(set(c))
        intersection = intersection.pop()
        if intersection.islower():
            score = ord(intersection) - 96
        else:
            score = ord(intersection) - 38
        scores.append(score)
    print(sum(scores))

def main2_after():
    data = helper.readlines_partitioned('3_dat.txt', 3)
    scores = []
    for dat in data:
        intersection = set(dat[0]).intersection(set(dat[1])).intersection(set(dat[2]))
        intersection = intersection.pop()
        if intersection.islower():
            score = ord(intersection) - 96
        else:
            score = ord(intersection) - 38
        scores.append(score)
    print(sum(scores))        

if __name__ == '__main__':
    main()
    main2()
    main2_after()
