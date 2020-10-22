'''
ID:   andy1li
LANG: PYTHON3
TASK: friday
'''

def is_leap(year): 
    return year%4==0 and (year%100 != 0 or year%400 == 0)

def days_in_month(year, month):
    length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return length[month] + (month == 1 and is_leap(year))

def solve():
    n = int(input())
    count = [0] * 7
    day_of_week = 0 # day of week: January 13, 1900 was a Saturday = 0 
    for year in range(1900, 1900+n):
        for month in range(12):
            count[day_of_week] += 1
            day_of_week += days_in_month(year, month)
            day_of_week %= 7

    print_line(' '.join(str(count[day]) for day in range(7)))

#------------------------------------------------------------------------------#

def print_line(line): print(line); f_out.write( f'{line}\n' )

task = 'friday'
with open(task+'.in') as f_in, open(task+'.out', 'w') as f_out:
    input = f_in.readline
    solve()

    