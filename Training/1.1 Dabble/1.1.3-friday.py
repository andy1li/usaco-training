from __future__  import print_function

def is_leap(year): return year%4==0 and (year%100 != 0 or year%400 == 0)

def days_in_month(year, month):
    if   month == 2            : return 28 + is_leap(year)
    elif month in [4, 6, 9, 11]: return 30
    else                       : return 31

with open('friday.in') as fin:
    n  = int(fin.readline())

    thirteenths = [0] * 7
    day_of_week  = 0 # day of week: January 13, 1900 was a Saturday = 0 
    for year in range(1900, 1900+n):
        for month in range(1, 13):
            thirteenths[day_of_week] += 1
            day_of_week = (day_of_week + days_in_month(year, month)) % 7

    print(*(thirteenths[day] for day in range(7)))
