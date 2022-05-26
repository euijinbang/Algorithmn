class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #         d = collections.defaultdict(int)
        #         for n in nums:
        #             if d[n] == 0: d[n] = nums.count(n)
        #             if d[n] > len(nums)//2: return n


        #         # Counter
        #         counts = collections.Counter(nums)
        #         return max(counts.keys(), key=counts.get)

        # Divide and Conquer
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]