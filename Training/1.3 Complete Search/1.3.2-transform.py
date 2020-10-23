'''
ID:   andy1li
LANG: PYTHON3
TASK: transform
'''

def reflect(square):
    return tuple(tuple(reversed(row)) for row in square)

def rotate(square, n):
    for _ in range(n):
        square = reflect(zip(*square))
    return square

def get_D4(square):
    D4 = {square: 6}
    for i in range(3): D4[rotate(reflect(square), i)] = 5
    D4[reflect(square)] = 4
    for i in [3, 2, 1]: D4[rotate(square, i)] = i
    return D4

def solve():
    n = int(input())
    square = tuple(tuple(input().strip()) for _ in range(n))
    target = tuple(tuple(input().strip()) for _ in range(n))

    D4 = get_D4(square)
    print_line(D4.get(target, 7))

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'transform'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()