'''
ID:   andy1li
LANG: PYTHON3
TASK: palsquare
'''

from string import digits, ascii_uppercase

def is_pal(x): return x == x[::-1]

def to_base(n, base, d=digits+ascii_uppercase):
    num = ''
    while n:
        num = d[n % base] + num
        n //= base
    return num

def solve():
    base = int(input())
    for i in range(1, 301):
        square = to_base(i*i, base)
        if is_pal(square):
            print_line(f'{to_base(i, base)} {square}')

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'palsquare'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()