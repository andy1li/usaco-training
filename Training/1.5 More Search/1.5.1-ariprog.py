'''
ID:   andy1li
LANG: PYTHON3
TASK: ariprog
'''

from itertools import product

def solve():
    N, M = int(input()), int(input())
    sq = (i*i for i in range(M+1))
    check = set(a + b for a, b in product(sq, repeat=2))
    n, bsq = len(check), sorted(check, reverse=True)
 
    ans = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            last, pen = bsq[i], bsq[j]
            step = last - pen
            first = last - step * (N-1)
            if first < 0: break
            if all(first + step*i in check for i in range(N-2)):
                ans.append((first, step)) 
    ans = sorted(ans, key=lambda pair: (pair[1], pair[0]))

    print_line(
        '\n'.join(f'{pair[0]} {pair[1]}' for pair in ans) 
        if ans else 
        'NONE'
    )

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'ariprog'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()