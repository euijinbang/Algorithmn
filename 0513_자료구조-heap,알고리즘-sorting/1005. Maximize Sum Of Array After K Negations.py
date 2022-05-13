from heapq import heapify, heappop, heappush
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # min 우선순위 큐로 가장 작은 수부터 나열하고 앞에서부터
        # 하나씩 꺼내 negate 하고 다시 넣는다.(k번 반복)
        heapify(nums)
        while k:
            heappush(nums, -heappop(nums))
            k -= 1
        return sum(nums)
