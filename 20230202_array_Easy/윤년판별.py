years = [1988, 1992, 1900, 2100, 2000, 2400]
# 윤 윤 평 평 윤 윤

year = int(input())

is_leap_year = None

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
