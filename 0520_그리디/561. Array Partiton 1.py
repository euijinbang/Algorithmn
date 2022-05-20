class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)//2):
            result += nums[2*i]
        return result

        #### one-line
        return sum(sorted(nums)[::2])
