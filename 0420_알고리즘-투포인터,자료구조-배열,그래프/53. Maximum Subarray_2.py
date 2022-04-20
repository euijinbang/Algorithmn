class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]  # 1개짜리 배열 주의
        curSum = 0

        for n in nums:
            # 이전까지의 총합을 먼저 확인
            if curSum < 0:
                curSum = 0

            # 그 다음에 n을 더한다. 두 순서가 바뀌면 안된다.
            curSum += n

            maxSub = max(maxSub, curSum)

        return maxSub