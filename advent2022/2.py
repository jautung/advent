import sys 
sys.path.append('..')
import helper

mapper = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}

mapper2 = {
    ('X', 'Rock'): 'Scissors',
    ('X', 'Paper'): 'Rock',
    ('X', 'Scissors'): 'Paper',
    ('Y', 'Rock'): 'Rock',
    ('Y', 'Paper'): 'Paper',
    ('Y', 'Scissors'): 'Scissors',
    ('Z', 'Rock'): 'Paper',
    ('Z', 'Paper'): 'Scissors',
    ('Z', 'Scissors'): 'Rock',
}

scorer = {
    ('Rock', 'Rock'): 3 + 1,
    ('Rock', 'Paper'): 6 + 2,
    ('Rock', 'Scissors'): 0 + 3,
    ('Paper', 'Rock'): 0 + 1,
    ('Paper', 'Paper'): 3 + 2,
    ('Paper', 'Scissors'): 6 + 3,
    ('Scissors', 'Rock'): 6 + 1,
    ('Scissors', 'Paper'): 0 + 2,
    ('Scissors', 'Scissors'): 3 + 3,
}

def main():
    data = helper.readlines_split_each_line('2_dat.txt')
    # data = helper.readlines_split_each_line('2_dat_mini.txt')
    # data = [(mapper[a[0]], mapper[a[1]]) for a in data]
    data = [(mapper[a[0]], mapper2[(a[1], mapper[a[0]])]) for a in data]
    scores = [scorer[dat] for dat in data]
    # print(scores)
    print(sum(scores))

if __name__ == '__main__':
    main()
