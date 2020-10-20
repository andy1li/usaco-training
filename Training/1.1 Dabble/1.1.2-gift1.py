'''
ID:   andy1li
LANG: PYTHON3
TASK: gift1
'''

def solve():
    n = int(input())
    balance = { input(): 0 for _ in range(n) }

    for _ in range(n):
        giver = input()
        amount, num_receivers = map(int, input().split())

        for r in range(num_receivers):
            balance[giver]   -= amount // num_receivers
            balance[input()] += amount // num_receivers

    for name, amount in balance.items():
        print_line(f'{name.strip()} {amount}')

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'gift1'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()