# ID:   andy1li
# PROG: haybales
# LANG: python 2.7

from __future__ import print_function
from bisect     import bisect_left

def solve(line):
    a, b = map(int, line.split())
    lo   = bisect_left(haybales, a)
    hi   = bisect_left(haybales, b)

    haybales.append(float('inf'))
    
    res  = hi - lo + (haybales[hi] == b)

    return str(res)+'\n'

PROG = 'haybales'
with open(PROG+'.in',  'r') as fin,\
     open(PROG+'.out', 'w') as fout:
    n, q     = map(int, fin.readline().split())
    haybales = sorted(map(int, fin.readline().split()))

    res = ''.join(solve(fin.readline()) for _ in range(q))

    #print(res)
    fout.write(res)

    



