import sys 
sys.path.append('..')
import helper

def main():
    data = helper.readlines_split_each_line('2_dat.txt')
    data = [(dat[0], int(dat[1])) for dat in data]
    x = 0
    y = 0
    for dat in data:
        if dat[0] == 'forward':
            x += dat[1]
        elif dat[0] == 'down':
            y += dat[1]
        elif dat[0] == 'up':
            y -= dat[1]
    print(x*y)

def main2():
    data = helper.readlines_split_each_line('2_dat.txt')
    data = [(dat[0], int(dat[1])) for dat in data]
    a = 0
    x = 0
    y = 0
    for dat in data:
        if dat[0] == 'forward':
            x += dat[1]
            y += a * dat[1]
        elif dat[0] == 'down':
            a += dat[1]
        elif dat[0] == 'up':
            a -= dat[1]
    print(x*y)

if __name__ == '__main__':
    main()
    main2()
