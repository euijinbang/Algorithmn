class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        missing num = full total - sum of nums
        O(1)
        """
        n = len(nums)
        full = n * (n+1) // 2
        target = full - sum(nums)
        return target