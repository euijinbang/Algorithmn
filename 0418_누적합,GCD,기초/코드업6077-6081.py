# n = 5
# total = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total += i
#
# print(total)


# while True:
#     num = input()
#     print(num)
#     if num == 'q':
#         break


# num = int(input())
# count, total = 1, 0
# while total < num:
#     total += count
#     count += 1
#
# print(count-1)


# n, m = 2, 3
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print((i, j))


n = 'B'
hexN = '0x'+'B'
intN = int(hexN, base=16)   # 16진수를 10진수로 변환하기
for i in range(1, 16):
    print('{0} * {1} = {2}'.format(n, hex(i)[2:].upper(), hex(intN * i)[2:].upper())) # 대문자 변환
