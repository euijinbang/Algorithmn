class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        numSet = set()
        result,  max_result = 0, 0

        for r in range(len(nums)):
            while nums[r] in numSet:
                numSet.remove(nums[l])
                result -= nums[l]
                l += 1

            numSet.add(nums[r])
            result += nums[r]

            if result > max_result:
                max_result = result

        return max_result