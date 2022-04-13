nums = [2, 7, 11, 15]
target = 9
result = []
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        temp = nums[i] + nums[j]
        if temp == target:
            result.append(i)
            result.append(j)

print(result)