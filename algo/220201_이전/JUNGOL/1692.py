import sys
sys.stdin = open("input.txt")

a = int(input())
b = int(input())

# n진수 각 자릿수 구하기
n = 10
ans3 = a * (b // (n ** 0) % n)
ans4 = a * (b // (n ** 1) % n)
ans5 = a * (b // (n ** 2) % n)

ans6 = a * b

print(ans3)
print(ans4)
print(ans5)
print(ans6)