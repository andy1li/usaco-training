'''
ID:   andy1li
LANG: PYTHON3
TASK: combo
'''

from itertools import product
Ints = lambda: [*map(int, input().split())]

def solve():
    def close(key):
        mod = lambda x: str((x-1) % n + 1)
        for error in product(range(-2, 3), repeat=3):
            yield tuple( mod(key[i]+error[i]) for i in range(3) )

    n = int(input())
    closes = set(close(Ints())) | set(close(Ints()))
    print_line(len(closes))

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'combo'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()