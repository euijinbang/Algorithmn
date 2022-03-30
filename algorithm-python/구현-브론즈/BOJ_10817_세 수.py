
nums = list(map(int, input().split()))

# sort 정렬 후 인덱스가 1인 데이터를 출력

nums_sorted = sorted(nums)
print(nums_sorted[1])


# 더 빠른 코드
"""
A, B, C = map(int, input().split())
result = sorted([A, B, C])
print(result[1])
"""