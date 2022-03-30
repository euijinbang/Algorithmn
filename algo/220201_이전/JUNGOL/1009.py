import sys
sys.stdin = open("input.txt")

while True:
    n = int(input())
    if n == 0:
        break

    # 역수 = 10씩 곱하고 일의 자리(나머지)를 더함
    num = 0
    # 각 자리수의 합 = 10으로 나눈 나머지
    total = 0
    while n > 0:
        num = (num * 10) + (n % 10)
        total += n % 10
        n = n // 10

    print(num, total)

