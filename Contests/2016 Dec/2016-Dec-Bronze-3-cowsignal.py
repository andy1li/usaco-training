# ID:   andy1li
# PROG: cowsignal
# LANG: python 2.7

from __future__ import print_function
from itertools  import chain

def ampifly(line, k):
    return [''.join(chain(c*k for c in line)) for _ in range(k)]

with open('cowsignal.in',  'r') as fin,\
     open('cowsignal.out', 'w') as fout:
    m, n, k = map(int, fin.readline().split())

    boards = [fin.readline().strip() for _ in range(m)]

    res = chain.from_iterable(ampifly(line, k) for line in boards)

    for line in res:
        #print(line)
        fout.write(line+'\n')