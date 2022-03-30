import sys
sys.stdin = open("15969.txt")

n, lst = int(input()), list(map(int, input().split()))

print(max(lst) - min(lst))