"""
ID:   andy1li
LANG: PYTHON3
TASK: test
"""

def print_line(line): print(line); f_out.write( str(line) + '\n' )

task = 'test'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline

    a, b = map(int, input().split())
    print_line(a + b)