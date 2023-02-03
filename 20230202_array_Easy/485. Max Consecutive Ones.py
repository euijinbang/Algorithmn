class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum_num = 0
        max_num = 0
        for i in range(len(nums)):
            sum_num += nums[i]
            if nums[i] == 0:
                sum_num = 0
            else:
                max_num = max(max_num, sum_num)

        return max_num
        