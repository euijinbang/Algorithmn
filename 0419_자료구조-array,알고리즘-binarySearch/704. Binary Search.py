def search(nums, target):
    left = 0
    right = len(nums) - 1

    # < 아닌 <= 여야 길이가 1인 리스트 커버 가능
    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1

        if nums[mid] > target:
            right = mid - 1

    return -1

print(search([-1,0,3,5,9,12], 9))