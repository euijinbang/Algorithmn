"""
방문한 곳(셀프 넘버가 아닌 수)을 체크
"""

self_number = [True] * 100001


def generator(n):
    num_sum = n
    while n > 0:
        r = n % 10
        n = n // 10
        num_sum += r
    return num_sum


for i in range(1, 10000):
    self_number[generator(i)] = False

for i in range(1, 10000):
    if self_number[i]:
        print(i)
