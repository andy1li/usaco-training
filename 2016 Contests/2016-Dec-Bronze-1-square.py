# ID:   andy1li
# PROG: square
# LANG: python 2.7

from __future__  import print_function
from collections import namedtuple

Rect = namedtuple('rect', ['x1', 'y1', 'x2', 'y2'])

def solve(rect1, rect2):
    min_x1 = min(rect1.x1, rect2.x1)
    min_y1 = min(rect1.y1, rect2.y1)
    max_x2 = max(rect1.x2, rect2.x2)
    max_y2 = max(rect1.y2, rect2.y2)
    
    return max(max_x2 - min_x1, max_y2 - min_y1) ** 2

with open('square.in',  'r') as fin,\
     open('square.out', 'w') as fout:
    rect1 = Rect(*map(int, fin.readline().split())) 
    rect2 = Rect(*map(int, fin.readline().split()))

    res = solve(rect1, rect2)
    fout.write(str(res))

    

    