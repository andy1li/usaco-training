'''
ID:   andy1li
LANG: PYTHON3
TASK: milk
'''

Ints  = lambda: [*map(int, input().split())]

def solve():
    demand, m = Ints()
    supply = (Ints() for _ in range(m))
    ans = 0
    for p, q in sorted(supply):
        amount = min(demand, q)
        ans += p * amount
        demand -= amount
        if demand <= 0: break
    print_line(ans)

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'milk'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()