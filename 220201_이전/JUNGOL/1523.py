import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())

if n < 0 or n > 100 or m < 1 or m > 3:
    print('INPUT ERROR!')

else:
    if m == 1:
        for i in range(1, n+1):
            for j in range(i):
                print('*', end='')
            print()

    elif m == 2:
        for i in range(n, 0, -1):
            for j in range(i):
                print('*', end='')
            print()

    elif m == 3:
        for i in range(1, n+1):
            for j in range(n-i, -1, -1):
                print(' ', end='')
            for k in range(2*i-1):
                print('*', end='')
            print()