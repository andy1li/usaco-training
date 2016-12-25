from __future__  import print_function

def longest(s):
    res = 0; color = ''
    for x in s:
        if       color and x != 'w' and x != color: break
        elif not color and x != 'w'               : color = x
        res += 1
    return res

def solve(beads, i):
    beads = beads * 2
    a = ''.join(reversed(beads[:i])) 
    b = beads[i:]
    return longest(a) + longest(b)

with open('beads.in', 'r') as fin:
    n     = int(fin.readline())
    beads = fin.readline().strip()
    
    res   = max( solve(beads, i) for i in range(1, n * 2) )
    print(min(res, n))
