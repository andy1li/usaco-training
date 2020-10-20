"""
ID:   andy1li
LANG: PYTHON3
TASK: ride 
"""

from functools import reduce
from operator  import mul

def get_ord(x): 
    return (ord(x) - ord('A') + 1) % 47

def get_hash(name):
    ords = map(get_ord, name)
    return reduce(mul, ords) % 47

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'ride'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline

    comet = input().strip()
    group = input().strip()
    matched = get_hash(comet) == get_hash(group)
    print_line("GO" if matched else "STAY")