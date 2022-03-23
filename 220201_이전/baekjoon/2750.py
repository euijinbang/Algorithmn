import sys
sys.stdin = open("2750.txt")

n = int(input())

def bubblesort(n, arr):
    for i in range(n-1, 0, -1):  # 인덱스 n-1부터 1까지
        for j in range(0, i):    # 인덱스 0부터 i-1까지
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = list()
for _ in range(n):
    arr.append(int(input()))

result = bubblesort(n, arr)
for i in range(n):
    print(result[i])