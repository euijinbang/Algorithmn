"""
서로 다른 정수가 주어진다.
모든 순열을 구하라.
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def permute(nums):
    result = []

    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)

    return result


print(permute([1, 2, 3]))
