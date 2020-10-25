'''
ID:   andy1li
LANG: PYTHON3
TASK: dualpal
'''

from itertools import count
from string import digits, ascii_uppercase

def is_pal(x): return x == x[::-1]

def to_base(n, base, d=digits+ascii_uppercase):
    num = ''
    while n:
        num = d[n % base] + num
        n //= base
    return num

def solve():
    n, s = map(int, input().split())
    for i in count(s+1):
        if not n: break
        pals = ( b
            for b in range(2, 11)
            if is_pal(to_base(i, b))
        )
        if len(set(pals)) > 1:
            n -= 1
            print_line(i)

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'dualpal'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()