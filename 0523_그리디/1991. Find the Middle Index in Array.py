class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        #sol1. sum, slicing
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

        #sol2. index, l and r sum  ==> 가장 빠름!!
        lsum, rsum = 0, sum(nums)
        for i in range(len(nums)):
            if lsum == rsum - nums[i]:
                return i
            lsum += nums[i]
            rsum -= nums[i]
        return -1

        #sol3. index, sum // 2
        lsum, rsum = 0, sum(nums)
        for i in range(len(nums)):
            if lsum * 2 == rsum - nums[i]:
                return i
            lsum += nums[i]
        return -1
