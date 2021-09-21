'''
ID:   andy1li
LANG: PYTHON3
TASK: milk3
'''

from itertools import permutations
# from sys import setrecursionlimit
# setrecursionlimit(10**9)

def solve():

    def nexts(state):
        for i, j in permutations(range(3), 2):
            pour = min(state[i], MAX[j]-state[j])
            nxt = list(state)
            nxt[i] -= pour; nxt[j] += pour
            yield tuple(nxt)

    def dfs(state):
        seen.add(state)
        for nxt in nexts(state):
            if nxt in seen: continue
            dfs(nxt)

    MAX = tuple(map(int, input().split()))
    seen = set(); dfs((0, 0, MAX[2]))
    ans = sorted(set(c for a, b, c in seen if not a))
    print_line(' '.join(map(str, ans)))
    
#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'milk3'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()