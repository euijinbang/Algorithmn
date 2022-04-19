"""
remove negative prefix
sliding window
O(n)
https://www.youtube.com/watch?v=5WZl3MMT0Eg
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]    # 부분배열의 합과 비교하여 최댓값을 갱신
        curSum = 0

        for n in nums:
            if curSum < 0:  # 해당 수 앞까지의 총합이 음수면 0으로 초기화
                curSum = 0
            curSum += n
            maxSub = max(maxSub,curSum)

        return maxSub