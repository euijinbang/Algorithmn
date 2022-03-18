"""
반복문으로 풀면 시간초과 난다.
(1 ≤ B < A ≤ V ≤ 1,000,000,000)

O(1)로 풀어야...수학적 풀이
"""
import math

A, B, V = map(int, input().split())

k = (V - B) / (A - B)
print(int(k) if k == int(k) else int(k) + 1)  # 정수라면 그대로, 소수라면 1을 더한다.

# answer = math.ceil((V - A) / (A - B) + 1)


# 반복문(보다 간결)
# while height + A < V:
#     height += (A - B)
#     day += 1

# 내풀이
# height, day = 0, 1
# while height < V:
#     height += A
#     if height >= V:
#         break
#     height -= B
#
#     day += 1
# print(day)
