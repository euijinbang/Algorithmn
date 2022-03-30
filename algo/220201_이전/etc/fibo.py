# a1, a2 = 1, 1
# n = 3
# print(a1)
# print(a2)
#
# while n <= 50:
#     a3 = a1 + a2
#     print(a3)
#     a1 = a2
#     a2 = a3
#     n += 1

# 피보나치 시작점이 1이고 이전 점을 0으로 가정
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous
    previous = current
    current = temp + previous
    i += 1


# pythonic
# while i <= 50:
#     print(current)
#     previous, current = current, current + previous