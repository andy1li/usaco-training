'''
ID:   andy1li
LANG: PYTHON3
TASK: barn1
'''

from itertools import groupby

def solve():
    m, s, c = map(int, input().split())
    stalls = ['0'] * s
    for _ in range(c): stalls[int(input())-1] = '1'

    stalls = ''.join(stalls).strip('0')
    gaps = (len(tuple(g)) for k, g in groupby(stalls) if k == '0')
    gaps = sorted(gaps, reverse=True)
    ans = len(stalls) - sum(gaps[:m-1])
    print_line(ans)

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'barn1'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()