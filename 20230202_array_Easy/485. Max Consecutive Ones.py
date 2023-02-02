nums = [1, 0, 1, 1, 0, 1]

temp_sum, max_sum = 0, 0
for i in range(len(nums)):
    temp_sum += nums[i]
    if nums[i] == 1:
        max_sum = max(max_sum, temp_sum)
    else:
        temp_sum = 0

print(max_sum)

