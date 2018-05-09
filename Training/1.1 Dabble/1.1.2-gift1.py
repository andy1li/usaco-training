from __future__  import print_function
from collections import OrderedDict

with open('gift1.in') as fin:
    n       = int(fin.readline())
    balance = OrderedDict([ (fin.readline().strip(), 0)
                             for _ in range(n) ])

    for _ in range(n):
        giver = fin.readline().strip()
        amount, num_receivers = map(int, fin.readline().split())

        receivers = (fin.readline().strip() for _ in range(num_receivers))
        for r in receivers:
            balance[giver] -= amount / num_receivers
            balance[r]     += amount / num_receivers

    for name, amount in balance.items():
        print(name, amount)