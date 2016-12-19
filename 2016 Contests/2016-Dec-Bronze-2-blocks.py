# ID:   andy1li
# PROG: blocks
# LANG: python 2.7

from __future__  import print_function
from collections import Counter, namedtuple
from operator    import add
from string      import ascii_lowercase

def max_cnt(board):
    f = Counter(board.front)
    b = Counter(board.back)

    for k in set(f.keys()+b.keys()):
        f[k] = max(f.get(k, 0), b.get(k, 0))
    
    return f


Board = namedtuple('Board', ['front', 'back'])

with open('blocks.in',  'r') as fin,\
     open('blocks.out', 'w') as fout:
    n = int(fin.readline())
    boards = [Board(*fin.readline().split()) for _ in range(n)]

    res = reduce(add, (max_cnt(b) for b in boards))

    for letter in ascii_lowercase:
        fout.write(str(res.get(letter, 0)) + '\n')
        #print(res.get(letter, 0))