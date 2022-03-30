import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
m = int(input())


# m의 약수와 배수의 합을 arr에서 찾아서 출력

yak = []
bae = []
for num in arr:
    if m % num == 0:
        yak.append(num)

    if num % m == 0:
        bae.append(num)

print(sum(yak))
print(sum(bae))
