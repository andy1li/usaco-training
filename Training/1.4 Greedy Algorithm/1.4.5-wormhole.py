'''
ID:   andy1li
LANG: PYTHON3
TASK: wormhole
'''

from collections import defaultdict

def n_parings():
    n = int(input())
    pairing = ['_'] * n
    def pairings():
        try: i = next(i for i in range(n) if pairing[i] == '_')
        except StopIteration: yield pairing; return

        for j in range(i+1, n): 
            if pairing[j] == '_':
                pairing[i], pairing[j] = j, i
                yield from pairings()
                pairing[i] = pairing[j] = '_'

    return n, pairings

def get_nexts(n):
    nexts, rows = [None] * n, defaultdict(dict)
    for i in range(n):
        x, y = map(int, input().split())
        rows[y][i] = x

    for row in rows.values():
        if len(row) == 1: continue
        row = sorted(row, key=row.get)
        for a, b in zip(row, row[1:]): nexts[a] = b
    # print(nexts)  
    return nexts

def detect_cycle(nexts, pairing):
    # print(pairing)
    n = len(nexts)
    for i in range(n):
        try: 
            for _ in range(n): i = nexts[pairing[i]]
        except TypeError: continue # None for nexts: no cycle
        return True
    return False

def solve():
    n, pairings = n_parings()
    nexts = get_nexts(n)
    ans = sum(detect_cycle(nexts, p) for p in pairings())
    print_line(ans)

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'wormhole'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()