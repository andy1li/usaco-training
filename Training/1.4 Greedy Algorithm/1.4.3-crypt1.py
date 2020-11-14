'''
ID:   andy1li
LANG: PYTHON3
TASK: crypt1
'''

from itertools import product as p

def solve():
    def check(three_two):
        three, two = [int(''.join(t)) for t in three_two] 
        fst = str(three * (two %10))
        snd = str(three * (two//10))
        product = str(three * two)

        return (
            len(fst) == len(snd) == 3 and len(product) == 4
        and all(set(x).issubset(A) for x in [fst, snd, product])
        )
        
    _, A = int(input()), set(input().split())
    ans = sum(map(check, p(p(A, repeat=3), p(A, repeat=2))))
    print_line(ans)

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'crypt1'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()