'''
ID:   andy1li
LANG: PYTHON3
TASK: skidesign
'''

from collections import defaultdict

class Plan():
    def __init__(self, hills, decreased=None, increased=None):
        self.hills = hills
        self.max = max(hills)
        self.min = min(hills)
        n = len(hills)
        self.decreased = decreased or [0] * n
        self.increased = increased or [0] * n
        self.level = defaultdict(set)
        for i, h in enumerate(hills):
            self.level[h].add(i)
        
    def ok(self): 
        return self.max - self.min <= 17

    def cost(self): 
        return (
            sum(x*x for x in self.decreased) 
        +   sum(x*x for x in self.increased)
        )

    def decrease(self):
        hills = self.hills.copy()
        decreased = self.decreased.copy()
        for i in self.level[self.max]:
            hills[i] -= 1
            decreased[i] += 1
        return Plan(hills, decreased, self.increased)

    def increase(self):
        hills = self.hills.copy()
        increased = self.increased.copy()
        for i in self.level[self.min]:
            hills[i] += 1
            increased[i] += 1
        return Plan(hills, self.decreased, increased)

    def step(self):
        dec = self.decrease()
        inc = self.increase()
        return dec if dec.cost() < inc.cost() else inc

def solve():
    n = int(input())
    hills = [int(input()) for _ in range(n)]
    plan = Plan(hills)
    while not plan.ok(): 
        plan = plan.step()
    print_line(plan.cost())

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'skidesign'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()