'''
ID:   andy1li
LANG: PYTHON3
TASK: beads
'''

from collections import deque

def collect(s, color = ''):
    for i, x in enumerate(s):
        if x == 'w': continue
        if not color: color = x
        elif x != color: break
    return i

def solve():
    n = int(input())
    beads = deque(input().strip())
    
    ans = 0
    for i in range(n):
        collected = collect(beads) + collect(reversed(beads))
        ans = max(ans, collected)
        beads.rotate()
    print_line(min(n, ans))

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'beads'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()