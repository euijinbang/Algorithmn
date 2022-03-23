import sys
sys.stdin = open("input.txt")

a = int(input())
b = int(input())
c = int(input())

num = a * b * c

result = {}
# 딕셔너리 생성
for i in range(10):
    result[i] = 0

# 해당 숫자를 key로 하는 딕셔너리의 value 추가
for n in str(num):
    result[int(n)] += 1

for ans in result.values():
    print(ans)
