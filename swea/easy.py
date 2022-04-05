# 55 44 33 22 11 0

arr = []

for i in range(6):
    arr.append(11 * (6 - i - 1))

print(arr)


# A B T A A A B A A 중복 제거, 알파벳 순서대로 출력 => A, B T

arr2 = ['A', 'B', 'T', 'A', 'A', 'A', 'B', 'A', 'A']

result = []
for i in range(len(arr)):
    val = arr2[i]
    if val not in result:
        result.append(val)

new_result = sorted(result, reverse=False)
print(new_result)


# 10 9 ..6 6 .. 10

def sol(n):
    if n < 6:
        return

    if n > 10:
        return

    print(n)
    sol(n-1)
    print(n)

sol(10)






