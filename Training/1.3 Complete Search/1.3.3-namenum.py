'''
ID:   andy1li
LANG: PYTHON3
TASK: namenum
'''

from string import ascii_uppercase as U

def get_mapper():
    mapper = {}
    for i, x in enumerate(U[:16] + U[17:]):
        mapper[x] = str(i//3 + 2)
    mapper['Q'] = mapper['Z'] = ''
    return mapper

def solve():
    pattern = list(input().strip())
    to_num = get_mapper()

    def is_valid(name): 
        return pattern == [to_num[x] for x in name]

    names = open('dict.txt').read().split()
    valids = filter(is_valid, names)
    for name in (list(valids) or ['NONE']): 
        print_line(name)

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'namenum'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()