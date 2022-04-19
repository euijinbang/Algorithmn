# nums = [1, 2, 3, 4]
nums = [-1, -2, -3, -4, 1, 2, 3, 4]

n = len(nums)
nums.sort()
print(nums)

# 가장 큰 마지막 세 수, 또는 가장 작은 처음 두 수와 맨 마지막 수
print(max(nums[n-1]*nums[n-2]*nums[n-3], nums[n-1]*nums[0]*nums[1]))