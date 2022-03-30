import sys
sys.stdin = open("2604.txt")

arr = list(input())
total = 10
for i in range(len(arr)-1):
    if arr[i+1] == arr[i]:
        total += 5
    else:
        total += 10

print(total)