'''
ID:   andy1li
LANG: PYTHON3
TASK: milk2
'''

from itertools import groupby

def solve():
    time = ['0'] * 10**6
    for _ in range(int(input())):
        a, b = map(int, input().split())
        time[a:b] = ['1'] * (b-a)
   
    time = ''.join(time).strip('0') 
    groups = [(k, len(list(g))) for k, g in groupby(time)] 

    milking = idle = 0 
    for k, cnt in groups:
        if k == '1': milking = max(milking, cnt)
        if k == '0': idle = max(idle, cnt)
    print_line(f'{milking} {idle}')

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'milk2'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()