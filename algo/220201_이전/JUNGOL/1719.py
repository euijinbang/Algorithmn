import sys
sys.stdin = open("input.txt")
n, m = map(int,input().split())

if n < 0 or n > 100 or m < 1 or m > 4:
    print("INPUT ERROR!")

else:
    if m == 1:
        for i in range(n):
            if i <= n//2:
                for j in range(i+1):
                    print("*", end="")
                print()
            else:
                for k in range(n-i, 0, -1):
                    print("*", end="")
                print()

    elif m == 2:
        for i in range(n):
            if i <= n//2:
                for j in range(n//2-i, -1, -1):
                    print(" ", end="")
                for k in range(i+1):
                    print("*", end="")
                print()
            else:
                for j in range(i-n//2+1):
                    print(" ", end="")
                for k in range(n-i, 0, -1):
                    print("*", end="")
                print()

    elif m == 3:
        for i in range(n):
            if i <= n//2:
                for j in range(i):
                    print(" ", end="")
                for k in range(n, 2*i, -1):
                    print("*", end="")
                print()

            else:
                for j in range(n-i-1, 0, -1):
                    print(" ", end="")
                for k in range(2*(i-n//2)+1):
                    print("*", end="")
                print()

    else:
        for i in range(n):
            if i <= n//2:
                for j in range(1, i+1):
                    print(" ", end="")
                for k in range(n//2+1, i, -1):
                    print("*", end="")
                print()
            else:
                for j in range(1, n//2+1):
                    print(" ", end="")
                for k in range(n//2-1, i):
                    print("*", end="")
                print()