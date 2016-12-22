# ID:   andy1li
# PROG: moocast
# LANG: python 2.7

from __future__  import print_function
from collections import namedtuple

Cow = namedtuple('cow', ['x', 'y', 'power'])

def distance(a, b): return ( (a.x - b.x)**2 + (a.y - b.y)**2 ) ** .5

def can_reach(a, b):
    if   a == b                    : return False
    elif distance(a, b) <= a.power : return True
    else                           : return False

def reaches(i, cows):
    return set(j for j, cow in enumerate(cows)
                 if can_reach(cows[i], cows[j]))


def walk(graph, start, seen=set()): 
    res, queue = dict(), set() 
    res[start] = None
    queue.add(start)
    while queue:
        u = queue.pop()
        for v in graph[u].difference(res, seen): 
            queue.add(v)
            res[v] = u
    return res

def components(graph): 
    res, seen = [], set()
    for u in graph:
        if u in seen: continue
        component = walk(graph, u)
        seen.update(component)
        res.append(component)
    return res

with open('moocast.in',  'r') as fin,\
     open('moocast.out', 'w') as fout:
    n    = int(fin.readline())
    cows = [Cow(*map(int, fin.readline().split())) for _ in range(n)]
    cow_graph = {i: reaches(i, cows) for i, cow in enumerate(cows)}

    # print(cows)
    # print(cow_graph)
    # print(components(cow_graph))

    res = max(len(s) for s in components(cow_graph))
    print(res)
    #fout.write(str(res)+'\n')