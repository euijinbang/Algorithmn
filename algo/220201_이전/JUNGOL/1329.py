N = int(input())

if N < 0 or N > 100 or N % 2 == 0:
    print("INPUT ERROR!")

else:
    for i in range(N):
        if i <= N//2:
            for j in range(i):
                print(" ", end="")
            for k in range(2*i+1):
                print("*", end="")
            print()

        else:
            for j in range(N-i-1):
                print(" ", end="")
            for k in range(2*(N-i)-1):
                print("*", end="")
            print()