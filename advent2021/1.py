import sys 
sys.path.append('..')
import helper

def main():
    data = helper.readlines('1_dat.txt')
    data = [int(dat) for dat in data]
    # data = [data[i]+data[i+1]+data[i+2] for i in range(len(data)-2)]
    prev = None
    count = 0
    for dat in data:
        if prev and dat > prev:
            count += 1
        prev = dat
    print(count)

def main2():
    data = helper.readlines('1_dat.txt')
    data = [int(dat) for dat in data]
    # data = [data[i]+data[i+1]+data[i+2] for i in range(len(data)-2)]
    print(sum([data[i] > data[i-1] for i in range(1, len(data))]))

def main3():
    data = helper.readlines_sliding('1_dat.txt', 3)
    data = [sum([int(dat2) for dat2 in dat]) for dat in data]
    print(sum([data[i] > data[i-1] for i in range(1, len(data))]))

if __name__ == '__main__':
    main()
    main2()
    main3()
