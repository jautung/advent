import sys 
sys.path.append('..')
import helper

def main():
    data = helper.readlines('1_dat.txt')
    cums = []
    cum = 0
    for dat in data:
        if dat == '':
            cums.append(cum)
            cum = 0
        else:
            cum += int(dat)
    print(max(cums))
    print(sum(sorted(cums)[-3:]))

if __name__ == '__main__':
    main()
