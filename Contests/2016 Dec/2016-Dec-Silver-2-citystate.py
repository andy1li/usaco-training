# ID:   andy1li
# PROG: citystate
# LANG: python 2.7

from __future__  import print_function
from collections import Counter

with open('citystate.in',  'r') as fin,\
     open('citystate.out', 'w') as fout:
    n      = int(fin.readline())
    cities = (fin.readline().split() for _ in range(n))

    abbr_cnt = Counter(city[:2] + state 
                       for city, state in cities
                       if  city[:2] != state)
    # cnt = 0
    # for abbr in abbr_cnt:
    #     mirror_abbr = abbr[2:] + abbr[:2]
    #     if mirror_abbr in abbr_cnt: 
    #         cnt += abbr_cnt[abbr] * abbr_cnt[mirror_abbr]
    cnt = sum(abbr_cnt[abbr] * abbr_cnt[abbr[2:]+abbr[:2]]
              for abbr in abbr_cnt
              if  abbr[2:]+abbr[:2] in abbr_cnt)

    print(cnt/2)
    #fout.write(str(cnt/2)+'\n')
